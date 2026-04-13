#!/usr/bin/env python3
"""
md_to_dbml.py — Convert a Mandarin data model .md (classDiagram) to DBML.

Parsing strategy
----------------
The script selects the first ```mermaid classDiagram block in the source file
and parses class definitions (``class ENTITY { +type col [PK|FK|UK|NN] }``).

Attribute format (classDiagram):
  ``+type colname [PK] [FK] [UK] [NN]``  — leading visibility marker stripped

Relationship format (classDiagram):
  ``EntityA "cardA" --> "cardB" EntityB : label``
  Cardinality strings: "1", "0..1", "0..*", "1..*"

FK resolution (in order)
  1. Direct  : pk_index[T] == fk_col
  2. Suffix  : strip ``_geraadpleegd`` / ``_werkbron``, retry direct
  3. Label   : relationship label slug contained in fk_col
  4. Entity  : target entity name slug contained in fk_col
  5. Single  : entity has exactly one outgoing FK relationship

FK nullability is derived from cardinality: if the "one" side has cardinality
"0..1", the FK is nullable.

Usage
-----
    python scripts/md_to_dbml.py path/to/model.md
"""

from __future__ import annotations

import re
import argparse
from dataclasses import dataclass
from pathlib import Path


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class Column:
    name: str
    raw_type: str        # mermaid type: string, text, boolean, datetime, …
    keywords: list[str]  # subset of {PK, FK, UK}
    note: str            # stripped of outer quotes


@dataclass
class Relationship:
    entity1: str
    card1: str   # cardinality near entity1, e.g. "||", "}o", "|o"
    card2: str   # cardinality near entity2, e.g. "o{", "||", "|{"
    entity2: str
    label: str


# ---------------------------------------------------------------------------
# Type mapping
# ---------------------------------------------------------------------------

TYPE_MAP: dict[str, str] = {
    "string":   "varchar",
    "text":     "text",
    "boolean":  "boolean",
    "datetime": "timestamp",
    "int":      "int",
    "integer":  "int",
    "float":    "decimal",
    "date":     "date",
}


def dbml_type(raw: str) -> str:
    return TYPE_MAP.get(raw.lower(), "varchar")


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

# erDiagram cardinality symbols
_CARD_RE = r"[|}{o]+"
_ENT_RE  = r"[A-Z_][A-Z0-9_]*"

_COL_RE  = re.compile(r"^(\w+)\s+(\w+)(.*)")
_REL_RE  = re.compile(
    rf"^({_ENT_RE})\s+({_CARD_RE})--({_CARD_RE})\s+({_ENT_RE})"
    rf"(?:\s*:\s*\"([^\"]*)\")?"
)
_ENT_OPEN_RE   = re.compile(rf"^({_ENT_RE})\s*{{")           # erDiagram entity
_CLASS_OPEN_RE = re.compile(rf"^class\s+({_ENT_RE})\s*{{")   # classDiagram entity

# classDiagram relationship: EntityA "cardA" --> "cardB" EntityB : label
_CLASS_REL_RE = re.compile(
    rf'^\s*({_ENT_RE})\s+"([^"]+)"\s+--[->]+\s+"([^"]+)"\s+({_ENT_RE})'
    rf'(?:\s*:\s*(.+))?'
)

# classDiagram cardinality string → erDiagram-compatible card symbol
# (keeps _outgoing_rels / _fk_nullable logic intact)
_CLASS_CARD_LEFT: dict[str, str] = {
    "1":    "||",
    "0..1": "|o",
    "0..*": "}o",
    "1..*": "}|",
}
_CLASS_CARD_RIGHT: dict[str, str] = {
    "1":    "||",
    "0..1": "o|",
    "0..*": "o{",
    "1..*": "|{",
}


def _parse_column(raw: str) -> Column | None:
    """Parse one attribute line.

    Handles three formats:
    - erDiagram    : ``type colname [PK] [FK] [UK] ["note"]``
    - classDiagram : ``+type colname [PK|FK|UK|NN|PK_FK]``  (leading +/-/#/~ stripped)
    - classDiagram : ``+colname: type «PK» «FK»``  (name:type with «» modifiers)
    """
    stripped = raw.strip().lstrip("+-#~").strip()

    # Format: ``colname: type «PK» «FK»``
    colon_m = re.match(r'^(\w+)\s*:\s*(\w+)(.*)', stripped)
    if colon_m:
        name     = colon_m.group(1)
        raw_type = colon_m.group(2)
        rest     = colon_m.group(3)
        # Extract «PK», «FK», «UK» modifiers
        kw_raw = re.findall(r'«(PK_FK|PK|FK|UK|NN)»', rest)
        tokens: list[str] = []
        for t in kw_raw:
            if t == "PK_FK":
                tokens += ["PK", "FK"]
            else:
                tokens.append(t)
        keywords = [kw for kw in tokens if kw in ("PK", "FK", "UK")]
        note = "NN" if "NN" in tokens else ""
        return Column(name=name, raw_type=raw_type, keywords=keywords, note=note)

    # Format: ``type colname [PK] [FK] [UK] ["note"]`` or ``+type colname [MODIFIERS]``
    m = _COL_RE.match(stripped)
    if not m:
        return None
    raw_type = m.group(1)
    name     = m.group(2)
    rest     = m.group(3).strip()

    note = ""
    nm = re.search(r'"([^"]*)"$', rest)
    if nm:
        note = nm.group(1)
        rest = rest[: nm.start()].strip()

    # Expand combined modifier PK_FK
    tokens = []
    for t in rest.split():
        if t == "PK_FK":
            tokens += ["PK", "FK"]
        else:
            tokens.append(t)

    keywords = [kw for kw in tokens if kw in ("PK", "FK", "UK")]

    if "NN" in tokens and not note:
        note = "NN"

    return Column(name=name, raw_type=raw_type, keywords=keywords, note=note)


def _parse_class_relationship(raw: str) -> Relationship | None:
    """Parse a classDiagram relationship line.

    Input:  ``VALUE_STREAM "1" --> "0..*" VALUE_STREAM_FASE : heeft``
    Returns a Relationship with card1/card2 converted to erDiagram symbols
    so the existing FK-resolution logic remains valid.
    """
    m = _CLASS_REL_RE.match(raw.strip())
    if not m:
        return None
    card1 = _CLASS_CARD_LEFT.get(m.group(2), "||")
    card2 = _CLASS_CARD_RIGHT.get(m.group(3), "||")
    return Relationship(
        entity1=m.group(1), card1=card1,
        card2=card2,         entity2=m.group(4),
        label=(m.group(5) or "").strip(),
    )


def _parse_relationship(raw: str) -> Relationship | None:
    m = _REL_RE.match(raw.strip())
    if not m:
        return None
    return Relationship(
        entity1=m.group(1), card1=m.group(2),
        card2=m.group(3),   entity2=m.group(4),
        label=m.group(5) or "",
    )


# ---------------------------------------------------------------------------
# Block extraction
# ---------------------------------------------------------------------------

def _extract_mermaid_blocks(md_text: str) -> list[str]:
    """Return content of every ```mermaid … ``` block in the file."""
    return [m.group(1) for m in re.finditer(r"```mermaid\s*\n(.*?)```", md_text, re.DOTALL)]


def _parse_lines(
    lines: list[str],
    entities: dict[str, list[Column]],
    relationships: list[Relationship],
) -> None:
    """
    Parse classDiagram entities and relationships from a list of text lines.
    Mutates ``entities`` and ``relationships`` in place.

    Priority: classDiagram entities (``class ENTITY {``) are parsed.
    erDiagram entities (``ENTITY {``) are skipped.
    """
    current: str | None = None

    for raw_line in lines:
        line = raw_line.strip()
        if not line or line.startswith("%"):
            continue
        if line in ("erDiagram", "classDiagram") or re.match(r"^direction\s", line):
            continue

        if line == "}":
            current = None
            continue

        # classDiagram entity open: class ENTITY {
        cm = _CLASS_OPEN_RE.match(line)
        if cm:
            current = cm.group(1)
            entities[current] = []
            continue

        # classDiagram attribute: +type name [MODIFIERS]
        if line.startswith(("+", "-", "#", "~")) and current is not None:
            col = _parse_column(line)
            if col:
                entities[current].append(col)
            continue

        # classDiagram relationship: EntityA "card" --> "card" EntityB : label
        class_rel = _parse_class_relationship(line)
        if class_rel:
            relationships.append(class_rel)
            continue

        # erDiagram entity open → skip (not the target format)
        mo = _ENT_OPEN_RE.match(line)
        if mo:
            current = "__skip__"
            continue

        if current in (None, "__skip__"):
            # erDiagram relationship (fallback for mixed blocks)
            rel = _parse_relationship(line)
            if rel:
                relationships.append(rel)


def parse_md(md_text: str) -> tuple[dict[str, list[Column]], list[Relationship]]:
    """
    Return (entities, relationships) from a Mandarin .md file.

    Strategy
    --------
    1. Select the first ```mermaid block that contains ``classDiagram``.
    2. If none found, fall back to any mermaid block (erDiagram support).
    3. If still nothing, scan the full file line-by-line.
    """
    entities: dict[str, list[Column]] = {}
    relationships: list[Relationship] = []

    all_blocks = _extract_mermaid_blocks(md_text)

    # Prefer classDiagram blocks
    class_blocks = [b for b in all_blocks if "classDiagram" in b]
    target_blocks = class_blocks or all_blocks

    for block in target_blocks:
        _parse_lines(block.splitlines(), entities, relationships)

    # Fallback: full-file scan
    if not entities:
        _parse_lines(md_text.splitlines(), entities, relationships)

    return entities, relationships


# ---------------------------------------------------------------------------
# Enum extraction
# ---------------------------------------------------------------------------

def extract_enums(entities: dict[str, list[Column]]) -> dict[str, list[str]]:
    """
    Extract enums from columns whose note contains ``|``-separated values.
    Uses the column name as the enum name.
    Skips:
    - notes containing ``...`` (incomplete domain)
    - boolean columns (TRUE|FALSE is not an enum)
    """
    enums: dict[str, list[str]] = {}
    seen: set[str] = set()

    for cols in entities.values():
        for col in cols:
            if col.raw_type.lower() == "boolean":
                continue
            if "|" not in col.note or "..." in col.note:
                continue
            values = [v.strip() for v in col.note.split("|") if v.strip()]
            if len(values) < 2 or col.name in seen:
                continue
            seen.add(col.name)
            enums[col.name] = values

    return enums


# ---------------------------------------------------------------------------
# FK resolution
# ---------------------------------------------------------------------------

_FK_SUFFIXES = ("_geraadpleegd", "_werkbron")

# These specific FK columns form a circular pair — their refs go in separate Ref blocks.
_CIRCULAR_FKS = frozenset([
    ("ARTEFACT",       "herkomstcode"),
    ("HERKOMST_KETEN", "initierend_artefact"),
])


def _build_pk_index(entities: dict[str, list[Column]]) -> dict[str, str]:
    """Return ``{entity_name: pk_column_name}``."""
    idx = {}
    for entity, cols in entities.items():
        for col in cols:
            if "PK" in col.keywords:
                idx[entity] = col.name
                break
    return idx


def _outgoing_rels(entity: str, relationships: list[Relationship]) -> list[Relationship]:
    """
    Return relationships where ``entity`` holds the FK (many / dependent side).
    Normalised so entity1 is always the FK-holding entity.
    """
    result = []
    for rel in relationships:
        if rel.entity1 == entity and rel.card1.startswith("}"):
            result.append(rel)
        elif rel.entity2 == entity and rel.card2.startswith("}"):
            result.append(Relationship(
                entity1=rel.entity2, card1=rel.card2,
                card2=rel.card1,     entity2=rel.entity1,
                label=rel.label,
            ))
    return result


def _resolve_fk(
    entity: str,
    fk_col: str,
    relationships: list[Relationship],
    pk_index: dict[str, str],
) -> str | None:
    """
    Return ``"TABLE.col"`` for a FK column, or ``None`` if unresolvable.
    """
    # 1. Direct name match
    for tbl, pk in pk_index.items():
        if pk == fk_col:
            return f"{tbl}.{pk}"

    # 2. Suffix stripping (e.g. execution_id_geraadpleegd → execution_id)
    stripped = fk_col
    for sfx in _FK_SUFFIXES:
        if fk_col.endswith(sfx):
            stripped = fk_col[: -len(sfx)]
            break
    if stripped != fk_col:
        for tbl, pk in pk_index.items():
            if pk == stripped:
                return f"{tbl}.{pk}"

    # 3 & 4. Relationship-based
    outgoing = _outgoing_rels(entity, relationships)
    slug = fk_col.lower().replace("_", "")

    for rel in outgoing:
        tgt = rel.entity2
        pk = pk_index.get(tgt)
        if not pk:
            continue
        label_slug = rel.label.lower().replace(" ", "").replace("-", "_").replace("_", "")
        tgt_slug   = tgt.lower().replace("_", "")
        # label match
        if label_slug and label_slug in slug:
            return f"{tgt}.{pk}"
        # PK name contained in FK col
        if pk.lower().replace("_", "") in slug:
            return f"{tgt}.{pk}"
        # entity name contained in FK col
        if tgt_slug in slug:
            return f"{tgt}.{pk}"

    # 5. Single outgoing relationship
    if len(outgoing) == 1:
        tgt = outgoing[0].entity2
        pk = pk_index.get(tgt)
        if pk:
            return f"{tgt}.{pk}"

    # 6. Last resort: any entity name (slug) appears inside the FK column name
    fk_slug = fk_col.lower().replace("_", "")
    for tbl, pk in pk_index.items():
        tbl_slug = tbl.lower().replace("_", "")
        if len(tbl_slug) >= 4 and tbl_slug in fk_slug:
            return f"{tbl}.{pk}"

    return None


def _fk_nullable(
    entity: str,
    target_entity: str,
    relationships: list[Relationship],
) -> bool:
    """
    Return True if the FK from ``entity`` to ``target_entity`` is nullable.
    Nullable when the "one" side cardinality starts with ``o`` (zero-or-one).
    """
    for rel in relationships:
        if rel.entity1 == entity and rel.entity2 == target_entity and rel.card1.startswith("}"):
            return rel.card2.startswith("o")
        if rel.entity2 == entity and rel.entity1 == target_entity and rel.card2.startswith("}"):
            return rel.card1.startswith("o")
    return False


# ---------------------------------------------------------------------------
# DBML column rendering
# ---------------------------------------------------------------------------

def _infer_nullable(col: Column) -> bool:
    """Heuristic nullability for non-PK, non-FK, non-UK columns without explicit NN/null note."""
    name = col.name.lower()
    note = col.note

    # Explicit markers take priority (handled by caller, but guard here too)
    if note == "NN":
        return False
    if note.lower() == "null":
        return True

    # Denormalised/optional markers in note
    if "[denorm]" in note:
        return True

    # By type
    if col.raw_type.lower() == "datetime":
        return False          # timestamps are always present
    if col.raw_type.lower() == "boolean":
        return False          # booleans are always present
    if col.raw_type.lower() == "text":
        return True           # long-text fields default to nullable

    # inhoud_* fields: nullable unless note="NN"
    if name.startswith("inhoud_"):
        return True

    # Optional audit/digest fields
    if name.startswith("digest_"):
        return True

    # Complete domain list (enum-like, no '...'): required categorical
    if "|" in note and "..." not in note:
        return False

    # Name / label fields are typically required
    if name.endswith("_naam"):
        return False

    # Default: NOT NULL for remaining string fields
    return False


def _col_to_dbml(
    col: Column,
    entity: str,
    relationships: list[Relationship],
    pk_index: dict[str, str],
    enums: dict[str, list[str]],
) -> str:
    """Return one DBML column line (with inline attributes)."""
    # DBML type (use enum name when applicable)
    dtype = col.name if col.name in enums else dbml_type(col.raw_type)

    # Padding for alignment
    pad = " " * max(28 - len(col.name), 1)
    line = f"  {col.name}{pad}{dtype}"

    attrs: list[str] = []

    is_pk = "PK" in col.keywords
    is_fk = "FK" in col.keywords
    is_uk = "UK" in col.keywords

    if is_pk:
        attrs.append("pk")
    if is_uk:
        attrs.append("unique")

    # Nullability
    if is_pk:
        pass  # pk implies not null in DBML
    elif col.note == "NN":
        attrs.append("not null")
    elif col.note.lower() == "null":
        attrs.append("null")
    elif is_fk:
        # derive from cardinality for FK; explicit note overrides
        ref = _resolve_fk(entity, col.name, relationships, pk_index)
        target = ref.split(".")[0] if ref else None
        nullable = _fk_nullable(entity, target, relationships) if target else False
        attrs.append("null" if nullable else "not null")
    else:
        attrs.append("null" if _infer_nullable(col) else "not null")

    # FK ref (skip circular pair columns — handled in separate Ref blocks)
    if is_fk and (entity, col.name) not in _CIRCULAR_FKS:
        ref = _resolve_fk(entity, col.name, relationships, pk_index)
        if ref:
            attrs.append(f"ref: > {ref}")
        else:
            attrs.append(f"note: 'FK — target unresolved for {col.name}'")

    # Inline note (skip NN/null markers and pure enum notes)
    note = col.note
    if note and note not in ("NN", "null") and "|" not in note:
        attrs.append(f"note: '{note.replace(chr(39), chr(92) + chr(39))}'")
    elif "|" in note and "..." in note:
        # partial domain hint — keep as note
        attrs.append(f"note: '{note.replace(chr(39), chr(92) + chr(39))}'")

    if attrs:
        line += f" [{', '.join(attrs)}]"

    return line


# ---------------------------------------------------------------------------
# DBML builder
# ---------------------------------------------------------------------------

def _extract_version(md_text: str) -> str:
    for pattern in [r"^versie:\s*(.+)$", r"\*\*Versie\*\*:\s*(.+)"]:
        m = re.search(pattern, md_text, re.MULTILINE)
        if m:
            return m.group(1).strip()
    return "unknown"


def build_dbml(
    entities: dict[str, list[Column]],
    relationships: list[Relationship],
    source_path: Path,
    version: str,
) -> str:
    pk_index = _build_pk_index(entities)
    enums    = extract_enums(entities)

    lines: list[str] = []

    # ── Header ────────────────────────────────────────────────────────────
    sep = "=" * 58
    lines += [
        f"// {sep}",
        f"// Source : {source_path.name}",
        f"// Versie : {version}",
        f"// Gegenereerd door: scripts/md_to_dbml.py",
        f"// {sep}",
        "",
    ]

    # ── Enums ─────────────────────────────────────────────────────────────
    if enums:
        lines += ["// ─── ENUMS " + "─" * 50, ""]
        for name, values in enums.items():
            lines.append(f"Enum {name} {{")
            for v in values:
                lines.append(f'  "{v}"' if "-" in v else f"  {v}")
            lines += ["}", ""]

    # ── Tables ────────────────────────────────────────────────────────────
    lines += ["// ─── TABELLEN " + "─" * 47, ""]

    for entity, cols in entities.items():
        lines.append(f"Table {entity} {{")
        for col in cols:
            lines.append(_col_to_dbml(col, entity, relationships, pk_index, enums))
        lines += ["}", ""]

    # ── Circular / deferred Ref blocks ────────────────────────────────────
    circular_refs: list[str] = []
    for (circ_entity, circ_col) in _CIRCULAR_FKS:
        if circ_entity not in entities:
            continue
        ref = _resolve_fk(circ_entity, circ_col, relationships, pk_index)
        if ref:
            circular_refs.append(f"Ref: {circ_entity}.{circ_col} > {ref}")

    if circular_refs:
        lines += ["// ─── CIRCULAIRE REFS (deferred) " + "─" * 29, ""]
        lines += circular_refs
        lines.append("")

    # ── Implied-relationship Ref blocks ──────────────────────────────────
    # Relationships where the FK-holding entity has no FK column that resolves
    # to the parent entity — emit a standalone Ref using the parent PK name as
    # the inferred FK column name (e.g. VALUE_STREAM_FASE.value_stream_code).
    covered_pairs: set[tuple[str, str]] = set()
    for _ent, _cols in entities.items():
        for _col in _cols:
            if "FK" not in _col.keywords:
                continue
            if (_ent, _col.name) in _CIRCULAR_FKS:
                continue
            _ref = _resolve_fk(_ent, _col.name, relationships, pk_index)
            if _ref:
                covered_pairs.add((_ent, _ref.split(".")[0]))
    for _circ_ent, _circ_col in _CIRCULAR_FKS:
        if _circ_ent not in entities:
            continue
        _ref = _resolve_fk(_circ_ent, _circ_col, relationships, pk_index)
        if _ref:
            covered_pairs.add((_circ_ent, _ref.split(".")[0]))

    implied_refs: list[str] = []
    seen_implied: set[tuple[str, str]] = set()
    for rel in relationships:
        # card1 starts with "}" → entity1 is the many/FK side
        # card2 ends   with "{" → entity2 is the many/FK side
        candidates: list[tuple[str, str]] = []
        if rel.card1.startswith("}"):
            candidates.append((rel.entity1, rel.entity2))
        if rel.card2.endswith("{"):
            candidates.append((rel.entity2, rel.entity1))
        for fk_entity, pk_entity in candidates:
            if fk_entity not in entities or pk_entity not in entities:
                continue
            if (fk_entity, pk_entity) in covered_pairs:
                continue
            if (fk_entity, pk_entity) in seen_implied:
                continue
            # Only emit when the entity has NO FK columns at all — entities
            # that already have FK columns (even unresolved ones) own their
            # relationship declarations.
            if any("FK" in c.keywords for c in entities[fk_entity]):
                continue
            pk_col = pk_index.get(pk_entity)
            if not pk_col:
                continue
            seen_implied.add((fk_entity, pk_entity))
            implied_refs.append(f"Ref: {fk_entity}.{pk_col} > {pk_entity}.{pk_col}")

    if implied_refs:
        lines += ["// ─── IMPLICIETE RELATIES (geen FK-kolom in entiteitsdefinitie) " + "─" * 10, ""]
        lines += implied_refs
        lines.append("")

    # ── Unresolved FK summary ─────────────────────────────────────────────
    unresolved: list[str] = []
    for entity, cols in entities.items():
        for col in cols:
            if "FK" not in col.keywords:
                continue
            if (entity, col.name) in _CIRCULAR_FKS:
                continue
            ref = _resolve_fk(entity, col.name, relationships, pk_index)
            if not ref:
                unresolved.append(f"//   {entity}.{col.name}")

    if unresolved:
        lines += ["// ─── NIET-OPGELOSTE FKs (handmatig aanvullen) " + "─" * 14, ""]
        lines += unresolved
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Converteer een Mandarin .md classDiagram naar DBML"
    )
    parser.add_argument(
        "source",
        help="Pad naar het .md invoerbestand met een mermaid classDiagram-blok",
    )
    args = parser.parse_args()

    src = Path(args.source)
    dst = src.with_suffix(".dbml")

    if not src.exists():
        parser.error(f"Invoerbestand niet gevonden: {src}")

    text    = src.read_text(encoding="utf-8")
    version = _extract_version(text)
    entities, relationships = parse_md(text)

    if not entities:
        parser.error(f"Geen classDiagram-entiteiten gevonden in: {src}")

    print(f"Gelezen: {len(entities)} entiteiten, {len(relationships)} relaties", flush=True)
    for e, cols in entities.items():
        fks = sum(1 for c in cols if "FK" in c.keywords)
        print(f"  {e}: {len(cols)} kolommen ({fks} FK)", flush=True)

    dbml = build_dbml(entities, relationships, src, version)

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(dbml, encoding="utf-8")
    print(f"\nDBML geschreven naar: {dst}", flush=True)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
erd_to_class.py — Genereert een TDM markdown-bestand op basis van een LDM.

Leest het mermaid-blok (erDiagram of classDiagram) uit een LDM-bestand,
parseet de entiteitdefinitietabellen (§4) voor kolombeschrijvingen, en
schrijft een volledig TDM .md-bestand met classDiagram en entiteitstabellen.

Gebruik
-------
    python scripts/erd_to_class.py grondslagen/aeo/aeo.datamodel/ldm-mandarin.md
    python scripts/erd_to_class.py <ldm.md> --output <tdm.md>
"""

from __future__ import annotations

import re
import sys
import argparse
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class Column:
    name: str
    raw_type: str
    keywords: list[str]    # PK, FK, UK (structural)
    required: bool = False # NN


@dataclass
class Relationship:
    entity1: str
    card1: str   # classDiagram cardinality string e.g. "1", "0..*"
    card2: str
    entity2: str
    label: str


# ---------------------------------------------------------------------------
# Cardinality maps: erDiagram symbols → classDiagram strings
# ---------------------------------------------------------------------------

_LEFT_CARD  = {"||": "1",    "|o": "0..1", "}o": "0..*", "}|": "1..*"}
_RIGHT_CARD = {"||": "1",    "o|": "0..1", "o{": "0..*", "|{": "1..*"}

# ---------------------------------------------------------------------------
# Regex
# ---------------------------------------------------------------------------

_CARD_RE      = r"[|}{o]+"
_ENT_RE       = r"[A-Z_][A-Z0-9_]*"

_ERD_REL_RE   = re.compile(
    rf"^\s*({_ENT_RE})\s+({_CARD_RE})--({_CARD_RE})\s+({_ENT_RE})"
    rf'(?:\s*:\s*"([^"]*)")?'
)
_CLASS_REL_RE = re.compile(
    rf'^\s*({_ENT_RE})\s+"([^"]+)"\s+--[->]+\s+"([^"]+)"\s+({_ENT_RE})'
    rf'(?:\s*:\s*(.+))?'
)
_ERD_OPEN_RE  = re.compile(rf"^\s*({_ENT_RE})\s*{{")
_CLASS_OPEN_RE = re.compile(rf"^\s*class\s+({_ENT_RE})\s*{{")

_ERD_COL_RE   = re.compile(r"^(\w+)\s+(\w+)(.*)")      # type name rest
_CLASS_COL_RE = re.compile(r"^[+\-#~]?(\w+)\s+(\w+)(.*)") # [vis]type name rest


# ---------------------------------------------------------------------------
# Column parsers
# ---------------------------------------------------------------------------

def _parse_erd_col(raw: str) -> Column | None:
    """Parse erDiagram column: ``type name [PK] [FK] ["NN"]``"""
    m = _ERD_COL_RE.match(raw.strip())
    if not m:
        return None
    raw_type, name, rest = m.group(1), m.group(2), m.group(3).strip()

    note = ""
    nm = re.search(r'"([^"]*)"', rest)
    if nm:
        note = nm.group(1)
        rest = rest[:nm.start()].strip()

    tokens = rest.split()
    keywords: list[str] = []
    for t in tokens:
        if t == "PK_FK":
            keywords += ["PK", "FK"]
        elif t in ("PK", "FK", "UK"):
            keywords.append(t)

    required = "NN" in tokens or note == "NN"
    return Column(name=name, raw_type=raw_type, keywords=keywords, required=required)


def _parse_class_col(raw: str) -> Column | None:
    """Parse classDiagram column: ``+type name [PK] [FK] [UK] [NN]``"""
    stripped = raw.strip().lstrip("+-#~").strip()
    m = _CLASS_COL_RE.match(stripped)
    if not m:
        return None
    raw_type, name, rest = m.group(1), m.group(2), m.group(3).strip()

    tokens = rest.split()
    keywords: list[str] = []
    for t in tokens:
        if t == "PK_FK":
            keywords += ["PK", "FK"]
        elif t in ("PK", "FK", "UK"):
            keywords.append(t)

    required = "NN" in tokens
    return Column(name=name, raw_type=raw_type, keywords=keywords, required=required)


# ---------------------------------------------------------------------------
# Diagram extraction and parsing
# ---------------------------------------------------------------------------

def _mermaid_blocks(text: str) -> list[str]:
    return [m.group(1) for m in re.finditer(r"```mermaid\s*\n(.*?)```", text, re.DOTALL)]


def parse_diagram(
    md_text: str,
) -> tuple[dict[str, list[Column]], list[Relationship], str]:
    """
    Parse entities and relationships from the first classDigram or erDiagram block.
    Returns (entities, relationships, diagram_type).
    """
    entities: dict[str, list[Column]] = {}
    relationships: list[Relationship] = []

    blocks = _mermaid_blocks(md_text)
    class_blocks = [b for b in blocks if "classDiagram" in b]
    erd_blocks   = [b for b in blocks if "erDiagram" in b]

    block = None
    is_erd = False
    if class_blocks:
        block = class_blocks[0]
    elif erd_blocks:
        block = erd_blocks[0]
        is_erd = True
    else:
        block = md_text  # full-file fallback

    current: str | None = None

    for raw_line in block.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("%"):
            continue
        if line in ("erDiagram", "classDiagram") or re.match(r"^direction\s", line):
            continue
        if line == "}":
            current = None
            continue

        if is_erd:
            mo = _ERD_OPEN_RE.match(line)
            if mo and not _CLASS_OPEN_RE.match(line):
                current = mo.group(1)
                entities[current] = []
                continue
        else:
            cm = _CLASS_OPEN_RE.match(line)
            if cm:
                current = cm.group(1)
                entities[current] = []
                continue

        if current is not None:
            col = _parse_erd_col(line) if is_erd else _parse_class_col(line)
            if col:
                entities[current].append(col)
            continue

        # Relationships
        if is_erd:
            rm = _ERD_REL_RE.match(line)
            if rm:
                c1 = _LEFT_CARD.get(rm.group(2), rm.group(2))
                c2 = _RIGHT_CARD.get(rm.group(3), rm.group(3))
                relationships.append(Relationship(
                    rm.group(1), c1, c2, rm.group(4), rm.group(5) or ""
                ))
        else:
            rm = _CLASS_REL_RE.match(line)
            if rm:
                relationships.append(Relationship(
                    rm.group(1), rm.group(2), rm.group(3),
                    rm.group(4), (rm.group(5) or "").strip()
                ))

    return entities, relationships, "erDiagram" if is_erd else "classDiagram"


# ---------------------------------------------------------------------------
# Parse entity descriptions from markdown tables (§4 in LDM)
# ---------------------------------------------------------------------------

def parse_descriptions(md_text: str) -> dict[str, dict[str, str]]:
    """
    Parse column descriptions from markdown entity tables.
    Supports 4-column (TDM) and 5-column (LDM with NN column) formats.
    Returns {entity_name: {col_name: description}}.
    """
    result: dict[str, dict[str, str]] = {}
    section_re = re.compile(rf"^#+\s+[\d.]+\s+({_ENT_RE})\b", re.MULTILINE)
    # 5-col: | `name` | type | key | NN | desc |
    row5 = re.compile(r"^\|\s*`(\w+)`\s*\|[^|]*\|[^|]*\|[^|]*\|\s*([^|]+?)\s*\|")
    # 4-col: | `name` | type | key | desc |
    row4 = re.compile(r"^\|\s*`(\w+)`\s*\|[^|]*\|[^|]*\|\s*([^|]+?)\s*\|")

    for sec_m in section_re.finditer(md_text):
        entity = sec_m.group(1)
        start  = sec_m.end()
        nxt    = section_re.search(md_text, start)
        chunk  = md_text[start: nxt.start() if nxt else len(md_text)]

        descs: dict[str, str] = {}
        for line in chunk.splitlines():
            m = row5.match(line) or row4.match(line)
            if m:
                col_name = m.group(1)
                desc     = re.sub(r"`([^`]+)`", r"\1", m.group(2)).strip()
                if desc and desc not in ("—", "-", ""):
                    descs[col_name] = desc
        if descs:
            result[entity] = descs

    return result


# ---------------------------------------------------------------------------
# classDiagram generation (TDM style: +name: type «PK»)
# ---------------------------------------------------------------------------

def _fmt_modifiers(col: Column) -> str:
    """Return «PK» «FK» «UK» string for a column."""
    mods = col.keywords[:]  # PK, FK, UK
    return " ".join(f"«{k}»" for k in mods)


def _diagram_col(col: Column) -> str:
    mods = _fmt_modifiers(col)
    if mods:
        return f"        +{col.name}: {col.raw_type} {mods}"
    return f"        +{col.name}: {col.raw_type}"


def build_class_diagram(
    entities: dict[str, list[Column]],
    relationships: list[Relationship],
    title: str = "",
) -> str:
    BAR = "═" * 55
    lines = ["```mermaid", "classDiagram", "    direction TB", ""]
    if title:
        lines += [f"    %% {BAR}", f"    %% {title}", f"    %% {BAR}", ""]

    for entity, cols in entities.items():
        lines.append(f"    class {entity} {{")
        for col in cols:
            lines.append(_diagram_col(col))
        lines += ["    }", ""]

    if relationships:
        lines += [f"    %% {BAR}", "    %% RELATIES", f"    %% {BAR}", ""]
        for r in relationships:
            line = f'    {r.entity1} "{r.card1}" --> "{r.card2}" {r.entity2}'
            if r.label:
                line += f" : {r.label}"
            lines.append(line)

    lines.append("```")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Entity definition table generation (TDM style)
# ---------------------------------------------------------------------------

def _sleutel(col: Column) -> str:
    parts = list(col.keywords)
    return ", ".join(parts) if parts else ""


def build_entity_table(
    cols: list[Column],
    descriptions: dict[str, str],
) -> str:
    rows = [
        "| Attribuut | Type | Sleutel | NN | Beschrijving |",
        "|-----------|------|---------|----|----|",
    ]
    for col in cols:
        nn   = "✓" if col.required or "PK" in col.keywords else ""
        desc = descriptions.get(col.name, "")
        rows.append(f"| `{col.name}` | {col.raw_type} | {_sleutel(col)} | {nn} | {desc} |")
    return "\n".join(rows)


# ---------------------------------------------------------------------------
# Metadata extraction
# ---------------------------------------------------------------------------

def _extract_meta(md_text: str, src: Path) -> dict[str, str]:
    meta = {
        "versie": "1.0",
        "naam":   src.stem,
        "datum":  str(date.today()),
        "bron":   src.name,
    }
    fm = re.match(r"^---\s*\n(.*?)\n---", md_text, re.DOTALL)
    if fm:
        for key in ("versie", "naam"):
            m = re.search(rf"^{key}:\s*(.+)$", fm.group(1), re.MULTILINE)
            if m:
                meta[key] = m.group(1).strip()
    else:
        m = re.search(r"\*\*Versie\*\*:\s*(.+)", md_text)
        if m:
            meta["versie"] = m.group(1).strip()

    # Strip "Logisch Data Model — " prefix from name
    meta["naam"] = re.sub(r"(?i)logisch\s+data\s+model\s*[—\-]\s*", "", meta["naam"]).strip() or meta["naam"]
    return meta


# ---------------------------------------------------------------------------
# TDM document builder
# ---------------------------------------------------------------------------

def build_tdm(
    entities: dict[str, list[Column]],
    relationships: list[Relationship],
    descriptions: dict[str, dict[str, str]],
    meta: dict[str, str],
) -> str:
    naam    = meta["naam"]
    versie  = meta["versie"]
    datum   = meta["datum"]
    bron    = meta["bron"]

    lines: list[str] = []

    # YAML frontmatter
    lines += [
        "---",
        "type: target-model",
        f"naam: Target Data Model — {naam}",
        f"versie: {versie}",
        f"bron: {bron}",
        f"datum: {datum}",
        "status: gegenereerd",
        "---",
        "",
    ]

    # Title block
    lines += [
        f"# Target Data Model — {naam}",
        "",
        f"**Status**: Afgeleid van LDM  ",
        f"**Versie**: {versie}  ",
        f"**Datum**: {datum}  ",
        f"**Bron**: `{bron}`",
        "",
        "---",
        "",
    ]

    # §1
    lines += [
        "## 1. Inleiding",
        "",
        f"Dit document is automatisch afgeleid van het Logisch Data Model (`{bron}`) "
        f"via `scripts/erd_to_class.py`. Het bevat {len(entities)} entiteiten.",
        "",
        "---",
        "",
    ]

    # §2 Visueel Model
    lines += [
        "## 2. Visueel Model",
        "",
        build_class_diagram(entities, relationships, f"TARGET DATA MODEL: {naam}"),
        "",
        "---",
        "",
    ]

    # §3 Entiteitdefinities
    lines += ["## 3. Entiteitdefinities", ""]
    for idx, (entity, cols) in enumerate(entities.items(), start=1):
        lines += [
            f"### 3.{idx} {entity}",
            "",
            build_entity_table(cols, descriptions.get(entity, {})),
            "",
            "---",
            "",
        ]

    # Wijzigingslog
    lines += [
        "## Wijzigingslog",
        "",
        "| Datum | Versie | Wijziging | Auteur |",
        "|-------|--------|-----------|--------|",
        f"| {datum} | {versie} | Gegenereerd vanuit `{bron}` via `erd_to_class.py` | script |",
        "",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _configure_utf8() -> None:
    import io
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    else:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def main() -> None:
    _configure_utf8()
    parser = argparse.ArgumentParser(
        description="Genereer een TDM markdown-bestand op basis van een LDM."
    )
    parser.add_argument(
        "source",
        help="Pad naar het LDM markdown-bestand",
    )
    parser.add_argument(
        "--output", default=None,
        help="Uitvoerpad voor het TDM-bestand "
             "(default: <bronmap>/tdm-<bronnaam>.md)",
    )
    args = parser.parse_args()

    src = Path(args.source)
    if not src.exists():
        print(f"Fout: bestand niet gevonden: {src}", file=sys.stderr)
        sys.exit(1)

    if args.output:
        dst = Path(args.output)
    else:
        stem = re.sub(r"(?i)^ldm[-_]?", "", src.stem) or src.stem
        dst  = src.parent / f"tdm-{stem}.md"

    text = src.read_text(encoding="utf-8")

    entities, relationships, diag_type = parse_diagram(text)
    if not entities:
        print(f"Fout: geen entiteiten gevonden in: {src}", file=sys.stderr)
        sys.exit(1)

    descriptions = parse_descriptions(text)
    meta         = _extract_meta(text, src)

    print(f"Gelezen: {len(entities)} entiteiten, {len(relationships)} relaties ({diag_type})")
    for e, cols in entities.items():
        d = len(descriptions.get(e, {}))
        print(f"  {e}: {len(cols)} kolommen, {d} beschrijvingen")

    tdm = build_tdm(entities, relationships, descriptions, meta)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(tdm, encoding="utf-8")
    print(f"\nTDM geschreven naar: {dst}")


if __name__ == "__main__":
    main()


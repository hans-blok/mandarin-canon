#!/usr/bin/env python3
"""
Grondslagen Digest Tool — Voeg YAML frontmatter met digest toe aan grondslagen.

Standardiseert YAML frontmatter voor alle documenten in grondslagen/ met:
  - type, naam, versie, value-stream (optioneel), digest, status

Subcommands:
  init    — Voeg/update YAML frontmatter voor alle grondslagen
  verify  — Controleer digests van alle grondslagen
  update  — Update digest van specifiek bestand

Conform: doctrine-traceability-digest (concept v0.1.0)
         mandarin-ecosysteem-ordeningsconcepten.md (artefacttoestand)
"""
import argparse
import hashlib
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple


# ==============================================================================
# CONSTANTEN
# ==============================================================================

# Mapping van bestandspad-patronen naar type
TYPE_PATTERNS = {
    r"constitutie\.md$": "constitutie",
    r"doctrine-.*\.md$": "doctrine",
    r".*concepten.*\.md$": "concepten",
    r".*kaderdefinitie.*\.md$": "kaderdefinitie",
    r"checklist.*\.md$": "checklist",
    r"value-streams.*\.md$": "value-stream",
    r"workspace-doctrine\.md$": "doctrine",
}

# Value stream mapping op basis van pad
VS_PATTERNS = {
    r"/aeo/": "AEO",
    r"/fnd/": "FND",
    r"\\aeo\\": "AEO",
    r"\\fnd\\": "FND",
}


# ==============================================================================
# CORE FUNCTIES (hergebruik van artefact_digest.py logica)
# ==============================================================================

def get_grondslagen_root() -> Path:
    """Bepaal de grondslagen root (workspace/grondslagen)."""
    script_dir = Path(__file__).resolve().parent
    workspace = script_dir.parent
    grondslagen = workspace / "grondslagen"
    if grondslagen.exists():
        return grondslagen
    cwd_grondslagen = Path.cwd() / "grondslagen"
    if cwd_grondslagen.exists():
        return cwd_grondslagen
    print("ERROR: grondslagen/ folder niet gevonden.")
    sys.exit(1)


def split_frontmatter(content: str) -> Tuple[Optional[str], str]:
    """Splits bestandsinhoud in frontmatter en body.

    Returns:
        (frontmatter_text, body) — frontmatter_text is None als er geen YAML frontmatter is.
    """
    if not content.startswith("---"):
        return None, content

    end_match = re.search(r"\n---\s*\n", content[3:])
    if not end_match:
        return None, content

    end_pos = 3 + end_match.end()
    fm_text = content[3:3 + end_match.start()].strip()
    body = content[end_pos:]
    return fm_text, body


def compute_digest(body: str) -> str:
    """Bereken 4-karakter MD5 digest van de body content."""
    return hashlib.md5(body.encode("utf-8")).hexdigest()[:4]


def parse_frontmatter_fields(fm_text: str) -> Dict[str, str]:
    """Parse YAML frontmatter naar een simpele key-value dict."""
    fields = {}
    for line in fm_text.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        match = re.match(r"^([a-zA-Z_][a-zA-Z0-9_-]*)\s*:\s*(.*)", line)
        if match:
            key = match.group(1)
            value = match.group(2).strip()
            if (value.startswith('"') and value.endswith('"')) or \
               (value.startswith("'") and value.endswith("'")):
                value = value[1:-1]
            fields[key] = value
    return fields


def set_frontmatter_field(fm_text: str, key: str, value: str) -> str:
    """Stel een veld in de frontmatter in (update of voeg toe)."""
    lines = fm_text.split("\n")
    updated = False
    for i, line in enumerate(lines):
        if re.match(rf"^{re.escape(key)}\s*:", line):
            lines[i] = f"{key}: {value}"
            updated = True
            break
    if not updated:
        lines.append(f"{key}: {value}")
    return "\n".join(lines)


def reconstruct_file(fm_text: str, body: str) -> str:
    """Reconstrueer bestandsinhoud uit frontmatter en body."""
    return f"---\n{fm_text}\n---\n{body}"


# ==============================================================================
# GRONDSLAGEN-SPECIFIEKE FUNCTIES
# ==============================================================================

def infer_type(file_path: Path) -> str:
    """Leid document type af uit bestandsnaam."""
    name = file_path.name
    path_str = str(file_path)
    
    for pattern, doc_type in TYPE_PATTERNS.items():
        if re.search(pattern, name, re.IGNORECASE):
            return doc_type
    
    # Fallback
    return "grondslag"


def infer_value_stream(file_path: Path) -> Optional[str]:
    """Leid value stream af uit bestandspad."""
    path_str = str(file_path)
    
    for pattern, vs in VS_PATTERNS.items():
        if re.search(pattern, path_str, re.IGNORECASE):
            return vs
    
    return None


def extract_naam_from_body(body: str) -> str:
    """Extract naam uit eerste H1 heading in body."""
    match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    if match:
        naam = match.group(1).strip()
        # Verwijder markdown formatting
        naam = re.sub(r"\*\*(.+?)\*\*", r"\1", naam)
        return naam
    return "Onbekend"


def extract_markdown_metadata(body: str) -> Dict[str, str]:
    """Extract metadata uit Markdown-style headers (**Versie**: 1.0.0)."""
    metadata = {}
    
    # Zoek naar **Key**: Value of **Key:** Value patronen
    patterns = [
        (r"\*\*Versie?\*\*:?\s*(\S+)", "versie"),
        (r"\*\*Version\*\*:?\s*(\S+)", "versie"),
        (r"\*\*Status\*\*:?\s*(\w+)", "status_old"),
        (r"\*\*Doctrine-ID\*\*:?\s*`?([^`\s]+)`?", "doctrine-id"),
        (r"\*\*Value Stream\*\*:?\s*(.+?)(?:\s{2,}|\n|$)", "value-stream-naam"),
        (r"\*\*Type\*\*:?\s*(.+?)(?:\s{2,}|\n|$)", "type_old"),
        (r"\*\*Datum\*\*:?\s*(\S+)", "datum"),
        (r"\*\*Last Updated\*\*:?\s*(\S+)", "datum"),
        (r"\*\*Owner\*\*:?\s*(.+?)(?:\s{2,}|\n|$)", "eigenaar"),
        (r"\*\*Eigenaar\*\*:?\s*(.+?)(?:\s{2,}|\n|$)", "eigenaar"),
    ]
    
    for pattern, key in patterns:
        match = re.search(pattern, body)
        if match:
            metadata[key] = match.group(1).strip()
    
    return metadata


def remove_markdown_metadata_block(body: str) -> str:
    """Verwijder het Markdown-style metadata blok uit de body.
    
    Zoekt naar een blok dat begint direct na de titel en eindigt voor ---
    """
    # Zoek naar het patroon: titel, lege regel, metadata regels, ---, rest
    # We willen de metadata regels verwijderen maar de --- en rest behouden
    
    lines = body.split("\n")
    new_lines = []
    in_metadata_block = False
    found_title = False
    metadata_ended = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Check of dit de titel is
        if not found_title and stripped.startswith("#"):
            found_title = True
            new_lines.append(line)
            continue
        
        # Na de titel, check voor metadata regels
        if found_title and not metadata_ended:
            # Lege regel na titel -> start metadata blok
            if not in_metadata_block and stripped == "":
                in_metadata_block = True
                new_lines.append(line)
                continue
            
            # In metadata blok
            if in_metadata_block:
                # --- markeert einde van metadata blok
                if stripped == "---":
                    metadata_ended = True
                    new_lines.append(line)
                    continue
                
                # Metadata regel (begint met **)
                if stripped.startswith("**") and "**:" in stripped:
                    # Skip deze regel (verwijder metadata)
                    continue
                
                # Andere content -> einde metadata blok
                if stripped and not stripped.startswith("**"):
                    metadata_ended = True
        
        new_lines.append(line)
    
    return "\n".join(new_lines)


def create_standard_frontmatter(
    file_path: Path,
    body: str,
    existing_fm: Optional[Dict[str, str]] = None
) -> str:
    """Creëer gestandaardiseerde YAML frontmatter."""
    
    # Basis metadata infereren
    doc_type = infer_type(file_path)
    value_stream = infer_value_stream(file_path)
    naam = extract_naam_from_body(body)
    
    # Bestaande metadata uit Markdown-style extraheren
    md_metadata = extract_markdown_metadata(body)
    
    # Prioriteit: bestaande YAML > Markdown metadata > default
    fields = {}
    
    # Type
    fields["type"] = doc_type
    
    # Naam
    fields["naam"] = naam
    
    # Versie
    if existing_fm and existing_fm.get("versie"):
        fields["versie"] = existing_fm["versie"]
    elif md_metadata.get("versie"):
        fields["versie"] = md_metadata["versie"]
    else:
        fields["versie"] = "1.0.0"
    
    # Value stream (alleen als relevant)
    if value_stream:
        fields["value-stream"] = value_stream
    elif existing_fm and existing_fm.get("value-stream"):
        fields["value-stream"] = existing_fm["value-stream"]
    
    # Digest wordt later toegevoegd
    # Status wordt later toegevoegd
    
    # Bouw frontmatter string
    fm_lines = []
    for key in ["type", "naam", "versie", "value-stream"]:
        if key in fields:
            fm_lines.append(f"{key}: {fields[key]}")
    
    return "\n".join(fm_lines)


# ==============================================================================
# DISCOVER
# ==============================================================================

def discover_grondslagen(grondslagen_root: Path) -> List[Path]:
    """Vind alle markdown bestanden in grondslagen/."""
    results = []
    for file_path in sorted(grondslagen_root.rglob("*.md")):
        # Skip readme en andere niet-grondslag bestanden
        if file_path.name.lower() == "readme.md":
            continue
        results.append(file_path)
    return results


# ==============================================================================
# SUBCOMMANDS
# ==============================================================================

def cmd_init(grondslagen_root: Path, dry_run: bool = False) -> int:
    """Initialiseer/update YAML frontmatter voor alle grondslagen."""
    files = discover_grondslagen(grondslagen_root)

    print("=" * 70)
    print("GRONDSLAGEN DIGEST — INIT")
    print(f"Scope: {grondslagen_root}")
    print(f"Gevonden: {len(files)} bestanden")
    if dry_run:
        print("[DRY-RUN]")
    print("=" * 70)
    print()

    updated = 0
    created = 0
    errors = 0

    for file_path in files:
        try:
            rel_path = file_path.relative_to(grondslagen_root)
        except ValueError:
            rel_path = file_path.name

        try:
            content = file_path.read_text(encoding="utf-8")
            fm_text, body = split_frontmatter(content)
            
            existing_fm = None
            body_for_digest = body
            
            if fm_text is not None:
                # Bestaande YAML frontmatter - voeg digest toe
                existing_fm = parse_frontmatter_fields(fm_text)
                
                # Check of digest al bestaat
                if "digest" in existing_fm:
                    stored_digest = existing_fm["digest"]
                    actual_digest = compute_digest(body)
                    if stored_digest == actual_digest:
                        print(f"  [SKIP] {rel_path} (digest actueel)")
                        continue
                
                # Voeg digest en status toe aan bestaande frontmatter
                digest = compute_digest(body)
                fm_text = set_frontmatter_field(fm_text, "digest", digest)
                fm_text = set_frontmatter_field(fm_text, "status", "vers")
                
                tag = "[UPD]"
                updated += 1
            else:
                # Geen YAML frontmatter - maak nieuwe aan
                # Verwijder Markdown-style metadata uit body
                clean_body = remove_markdown_metadata_block(body)
                body_for_digest = clean_body
                
                # Creëer nieuwe frontmatter
                fm_text = create_standard_frontmatter(file_path, body, None)
                
                # Bereken digest en voeg toe
                digest = compute_digest(clean_body)
                fm_text = set_frontmatter_field(fm_text, "digest", digest)
                fm_text = set_frontmatter_field(fm_text, "status", "vers")
                
                # Update body (zonder Markdown metadata)
                body = clean_body
                
                tag = "[NEW]"
                created += 1

            print(f"  {tag} {rel_path}  digest={digest}")

            if not dry_run:
                new_content = reconstruct_file(fm_text, body)
                file_path.write_text(new_content, encoding="utf-8")

        except Exception as e:
            print(f"  [ERR] {rel_path}: {e}")
            import traceback
            traceback.print_exc()
            errors += 1

    print()
    print("-" * 70)
    print(f"Resultaat:")
    print(f"  Nieuw aangemaakt: {created}")
    print(f"  Bijgewerkt:       {updated}")
    print(f"  Fouten:           {errors}")
    print(f"  Totaal:           {len(files)}")
    print("-" * 70)

    return 1 if errors > 0 else 0


def cmd_verify(grondslagen_root: Path, verbose: bool = False) -> int:
    """Verifieer digests voor alle grondslagen."""
    files = discover_grondslagen(grondslagen_root)

    print("=" * 70)
    print("GRONDSLAGEN DIGEST — VERIFY")
    print(f"Scope: {grondslagen_root}")
    print(f"Gevonden: {len(files)} bestanden")
    print("=" * 70)
    print()

    vers_count = 0
    mismatch_count = 0
    no_digest_count = 0
    no_fm_count = 0
    errors = 0

    mismatches = []

    for file_path in files:
        try:
            rel_path = file_path.relative_to(grondslagen_root)
        except ValueError:
            rel_path = file_path.name

        try:
            content = file_path.read_text(encoding="utf-8")
            fm_text, body = split_frontmatter(content)

            if fm_text is None:
                no_fm_count += 1
                print(f"  [GEEN FM] {rel_path}")
                continue

            fields = parse_frontmatter_fields(fm_text)
            stored_digest = fields.get("digest")

            if not stored_digest:
                no_digest_count += 1
                print(f"  [GEEN DIGEST] {rel_path}")
                continue

            actual_digest = compute_digest(body)
            status = fields.get("status", "?")

            if stored_digest == actual_digest:
                vers_count += 1
                if verbose:
                    print(f"  [VERS]  {rel_path}  digest={actual_digest}  status={status}")
            else:
                mismatch_count += 1
                mismatches.append((rel_path, stored_digest, actual_digest, status))
                print(f"  [MISMATCH] {rel_path}  opgeslagen={stored_digest}  actueel={actual_digest}  status={status}")

        except Exception as e:
            print(f"  [ERR] {rel_path}: {e}")
            errors += 1

    print()
    print("-" * 70)
    print(f"Resultaat:")
    print(f"  Vers:          {vers_count}")
    print(f"  Mismatch:      {mismatch_count}")
    print(f"  Geen digest:   {no_digest_count}")
    print(f"  Geen FM:       {no_fm_count}")
    print(f"  Fouten:        {errors}")
    print(f"  Totaal:        {len(files)}")
    print("-" * 70)

    return 0 if mismatch_count == 0 and no_fm_count == 0 and no_digest_count == 0 else 1


def cmd_update(grondslagen_root: Path, file_pattern: str, status: Optional[str] = None) -> int:
    """Update digest voor specifiek bestand of markeer als muf/rot."""
    files = discover_grondslagen(grondslagen_root)
    
    # Filter op patroon
    matching = [f for f in files if file_pattern in str(f)]
    
    if not matching:
        print(f"ERROR: Geen bestanden gevonden die matchen met '{file_pattern}'")
        return 1
    
    for file_path in matching:
        try:
            rel_path = file_path.relative_to(grondslagen_root)
        except ValueError:
            rel_path = file_path.name
        
        content = file_path.read_text(encoding="utf-8")
        fm_text, body = split_frontmatter(content)
        
        if fm_text is None:
            print(f"  [ERR] {rel_path}: geen frontmatter")
            continue
        
        if status:
            # Markeer als muf/rot zonder digest update
            fm_text = set_frontmatter_field(fm_text, "status", status)
            print(f"  [STATUS] {rel_path} → {status}")
        else:
            # Update digest en zet status op vers
            digest = compute_digest(body)
            fm_text = set_frontmatter_field(fm_text, "digest", digest)
            fm_text = set_frontmatter_field(fm_text, "status", "vers")
            print(f"  [UPD] {rel_path}  digest={digest}")
        
        new_content = reconstruct_file(fm_text, body)
        file_path.write_text(new_content, encoding="utf-8")
    
    return 0


# ==============================================================================
# MAIN
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Grondslagen Digest Tool — Beheer YAML frontmatter voor grondslagen"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # init
    init_parser = subparsers.add_parser("init", help="Initialiseer frontmatter voor alle grondslagen")
    init_parser.add_argument("--dry-run", action="store_true", help="Toon wijzigingen zonder te schrijven")

    # verify
    verify_parser = subparsers.add_parser("verify", help="Verifieer digests")
    verify_parser.add_argument("--verbose", "-v", action="store_true", help="Toon ook correcte bestanden")

    # update
    update_parser = subparsers.add_parser("update", help="Update digest of status voor specifiek bestand")
    update_parser.add_argument("file", help="Bestandsnaam of patroon")
    update_parser.add_argument("--status", choices=["vers", "muf", "rot"], help="Markeer als status zonder digest update")

    args = parser.parse_args()
    grondslagen_root = get_grondslagen_root()

    if args.command == "init":
        return cmd_init(grondslagen_root, args.dry_run)
    elif args.command == "verify":
        return cmd_verify(grondslagen_root, args.verbose)
    elif args.command == "update":
        return cmd_update(grondslagen_root, args.file, args.status)


if __name__ == "__main__":
    sys.exit(main())

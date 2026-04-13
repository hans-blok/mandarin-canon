"""
dbml_to_graphml.py — Converts tdm_mandarin.dbml to yEd-compatible GraphML.

Usage:
    python scripts/dbml_to_graphml.py
    python scripts/dbml_to_graphml.py --input path/to/file.dbml --output path/to/file.graphml

Output: grondslagen/aeo/aeo.datamodel/tdm_mandarin.graphml

Why the old version failed in yEd:
    Generic GraphML data keys (d_label, d_columns, …) are invisible to yEd's
    renderer. yEd only draws a node when it finds a <data yfiles.type="nodegraphics">
    block containing <y:ShapeNode> (or similar). Without it, yEd shows small default
    yellow squares with no content or labels.

Why this version works:
    Every node contains <data key="d_nodegraphics"><y:ShapeNode> with geometry,
    fill, border, a multiline label, and a shape type. Every edge contains
    <data key="d_edgegraphics"><y:PolyLineEdge> with line style, arrows, and an
    edge label. yEd reads these yFiles blocks to produce a fully rendered diagram.

yEd validation checklist after opening the file:
    1. File opens without errors
    2. Nodes are visible rectangles with multiline table labels
    3. Edges are visible directed arrows
    4. Edge labels are visible (may need View > Edge Labels to be enabled)
    5. Layout > Hierarchical produces a readable top-down diagram
    6. Labels resize correctly after Edit > Select All + Tools > Fit Node to Label
"""

import re
import argparse
import xml.etree.ElementTree as ET
from pathlib import Path


GRAPHML_NS = "http://graphml.graphdrawing.org/graphml"
Y_NS       = "http://www.yworks.com/xml/graphml"
XML_NS     = "http://www.w3.org/XML/1998/namespace"

# Node layout constants
NODE_WIDTH  = 290
LINE_HEIGHT = 14
HEADER_PAD  = 10   # extra px for the table-name header line
V_PADDING   = 12   # total vertical padding (top + bottom)
GRID_COLS   = 5
GRID_X_GAP  = 360
GRID_Y_GAP  = 320

# Visual theme
FILL_COLOR   = "#DDEEFF"
BORDER_COLOR = "#336699"
FONT_FAMILY  = "Courier New"
FONT_SIZE    = "11"


def gn(tag: str) -> str:
    return f"{{{GRAPHML_NS}}}{tag}"


def yn(tag: str) -> str:
    return f"{{{Y_NS}}}{tag}"


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def parse_dbml(text: str) -> tuple[dict, list]:
    """Return (tables, refs).

    tables: { table_name: [{"name": str, "type": str, "pk": bool, "fk": bool,
                             "uk": bool, "not_null": bool, "note": str}] }
    refs:   [{"from_table": str, "from_col": str, "op": str,
               "to_table": str, "to_col": str}]
    """
    tables: dict[str, list[dict]] = {}
    refs: list[dict] = []

    table_pattern = re.compile(r'Table\s+(\w+)\s*\{([^}]*)\}', re.DOTALL)
    col_pattern = re.compile(
        r'^\s*(\w+)\s+([\w()]+)((?:\s*\[[^\]]*\])*)',
        re.MULTILINE
    )

    for m in table_pattern.finditer(text):
        table_name = m.group(1)
        body = m.group(2)
        columns = []

        for col_m in col_pattern.finditer(body):
            col_name = col_m.group(1)
            col_type = col_m.group(2)
            attrs_raw = col_m.group(3)

            if col_name.lower() in ("indexes",):
                continue

            attrs = attrs_raw.lower()
            is_pk = bool(re.search(r'\bpk\b', attrs))
            is_uk = bool(re.search(r'\bunique\b', attrs))
            is_nn = is_pk or bool(re.search(r'\bnot null\b', attrs))
            is_fk = bool(re.search(r'\bref\s*:', attrs))

            note_m = re.search(r"note:\s*'([^']*)'", attrs_raw, re.IGNORECASE)
            note = note_m.group(1) if note_m else ""

            ref_m = re.search(
                r'ref\s*:\s*([<>]{1,2})\s*([\w]+)\.([\w]+)',
                attrs_raw, re.IGNORECASE
            )
            if ref_m:
                refs.append({
                    "from_table": table_name,
                    "from_col":   col_name,
                    "op":         ref_m.group(1),
                    "to_table":   ref_m.group(2),
                    "to_col":     ref_m.group(3),
                })

            columns.append({
                "name":     col_name,
                "type":     col_type,
                "pk":       is_pk,
                "fk":       is_fk,
                "uk":       is_uk,
                "not_null": is_nn,
                "note":     note,
            })

        tables[table_name] = columns

    standalone_ref = re.compile(
        r'^Ref\s*:\s*([\w]+)\.([\w]+)\s*([<>]{1,2})\s*([\w]+)\.([\w]+)',
        re.MULTILINE
    )
    for m in standalone_ref.finditer(text):
        refs.append({
            "from_table": m.group(1),
            "from_col":   m.group(2),
            "op":         m.group(3),
            "to_table":   m.group(4),
            "to_col":     m.group(5),
        })

    return tables, refs


# ---------------------------------------------------------------------------
# Label and layout helpers
# ---------------------------------------------------------------------------

def format_col_line(c: dict) -> str:
    flags = []
    if c["pk"]:                          flags.append("PK")
    if c["uk"]:                          flags.append("UK")
    if c["fk"]:                          flags.append("FK")
    if c["not_null"] and not c["pk"]:    flags.append("NN")
    suffix = f"  [{', '.join(flags)}]" if flags else ""
    return f"{c['name']}: {c['type']}{suffix}"


def node_label(table_name: str, columns: list) -> str:
    sep = "\u2500" * 34   # ──────────────────────────────────
    lines = [table_name, sep] + [format_col_line(c) for c in columns]
    return "\n".join(lines)


def node_height(columns: list) -> int:
    n_lines = 2 + len(columns)   # header + separator + columns
    return V_PADDING + HEADER_PAD + n_lines * LINE_HEIGHT


def grid_pos(idx: int) -> tuple[int, int]:
    col = idx % GRID_COLS
    row = idx // GRID_COLS
    return col * GRID_X_GAP, row * GRID_Y_GAP


# ---------------------------------------------------------------------------
# GraphML builder
# ---------------------------------------------------------------------------

def build_graphml(tables: dict, refs: list) -> ET.Element:
    ET.register_namespace("",    GRAPHML_NS)
    ET.register_namespace("y",   Y_NS)

    root = ET.Element(gn("graphml"))

    # ── Key declarations ────────────────────────────────────────────────────

    def sem_key(id_: str, for_: str, name: str) -> None:
        k = ET.SubElement(root, gn("key"))
        k.set("id", id_); k.set("for", for_)
        k.set("attr.name", name); k.set("attr.type", "string")

    sem_key("d_label",       "node", "label")
    sem_key("d_columns",     "node", "columns")
    sem_key("d_pk",          "node", "primary_keys")
    sem_key("d_fk",          "node", "foreign_keys")
    sem_key("d_e_label",     "edge", "label")
    sem_key("d_cardinality", "edge", "cardinality")

    # yFiles graphics keys — these are what yEd actually renders
    k_node = ET.SubElement(root, gn("key"))
    k_node.set("id", "d_nodegraphics")
    k_node.set("for", "node")
    k_node.set("yfiles.type", "nodegraphics")

    k_edge = ET.SubElement(root, gn("key"))
    k_edge.set("id", "d_edgegraphics")
    k_edge.set("for", "edge")
    k_edge.set("yfiles.type", "edgegraphics")

    graph = ET.SubElement(root, gn("graph"))
    graph.set("id", "G")
    graph.set("edgedefault", "directed")

    def data(parent: ET.Element, key_id: str, text: str | None = None) -> ET.Element:
        d = ET.SubElement(parent, gn("data"))
        d.set("key", key_id)
        if text is not None:
            d.text = text
        return d

    # ── Nodes ───────────────────────────────────────────────────────────────

    for idx, (table_name, columns) in enumerate(tables.items()):
        node = ET.SubElement(graph, gn("node"))
        node.set("id", table_name)

        # Semantic metadata (kept for interoperability)
        col_lines, pk_cols, fk_cols = [], [], []
        for c in columns:
            col_lines.append(format_col_line(c))
            if c["pk"]: pk_cols.append(c["name"])
            if c["fk"]: fk_cols.append(c["name"])

        data(node, "d_label",   table_name)
        data(node, "d_columns", "\n".join(col_lines))
        data(node, "d_pk",      ", ".join(pk_cols))
        data(node, "d_fk",      ", ".join(fk_cols))

        # yEd graphics — the part yEd actually renders
        x, y = grid_pos(idx)
        h = node_height(columns)
        label_text = node_label(table_name, columns)

        d_ng  = data(node, "d_nodegraphics")
        snode = ET.SubElement(d_ng, yn("ShapeNode"))

        geom = ET.SubElement(snode, yn("Geometry"))
        geom.set("height", str(h))
        geom.set("width",  str(NODE_WIDTH))
        geom.set("x",      str(x))
        geom.set("y",      str(y))

        fill = ET.SubElement(snode, yn("Fill"))
        fill.set("color",       FILL_COLOR)
        fill.set("transparent", "false")

        border = ET.SubElement(snode, yn("BorderStyle"))
        border.set("color", BORDER_COLOR)
        border.set("type",  "line")
        border.set("width", "1.5")

        lbl = ET.SubElement(snode, yn("NodeLabel"))
        lbl.set("alignment",      "left")
        lbl.set("fontFamily",     FONT_FAMILY)
        lbl.set("fontSize",       FONT_SIZE)
        lbl.set("autoSizePolicy", "content")
        lbl.set(f"{{{XML_NS}}}space", "preserve")
        lbl.text = label_text

        ET.SubElement(snode, yn("Shape")).set("type", "rectangle")

    # ── Edges ───────────────────────────────────────────────────────────────

    edge_seen: set[tuple] = set()

    for i, ref in enumerate(refs):
        from_t, to_t = ref["from_table"], ref["to_table"]
        if from_t not in tables or to_t not in tables:
            continue
        key_t = (from_t, ref["from_col"], to_t, ref["to_col"])
        if key_t in edge_seen:
            continue
        edge_seen.add(key_t)

        edge = ET.SubElement(graph, gn("edge"))
        edge.set("id",     f"e{i}")
        edge.set("source", from_t)
        edge.set("target", to_t)

        card    = {">": "many-to-one", "<": "one-to-many", "<>": "many-to-many"}.get(ref["op"], ref["op"])
        lbl_txt = f"{ref['from_col']} \u2192 {ref['to_col']}"

        data(edge, "d_e_label",     lbl_txt)
        data(edge, "d_cardinality", card)

        # yEd edge graphics
        d_eg = data(edge, "d_edgegraphics")
        ple  = ET.SubElement(d_eg, yn("PolyLineEdge"))

        ls = ET.SubElement(ple, yn("LineStyle"))
        ls.set("color", BORDER_COLOR)
        ls.set("type",  "line")
        ls.set("width", "1.0")

        arrows = ET.SubElement(ple, yn("Arrows"))
        arrows.set("source", "none")
        arrows.set("target", "standard")

        el = ET.SubElement(ple, yn("EdgeLabel"))
        el.set("alignment", "center")
        el.set("fontSize",  "10")
        el.text = lbl_txt

        ET.SubElement(ple, yn("BendStyle")).set("smoothed", "false")

    return root


# ---------------------------------------------------------------------------
# Serialization
# ---------------------------------------------------------------------------

def serialize(root: ET.Element) -> str:
    """Serialize to XML string.

    Uses ET.indent (Python 3.9+) for readable output without disturbing
    text content inside NodeLabel / EdgeLabel elements.
    Falls back to compact output on older Python.
    """
    try:
        ET.indent(root, space="  ")
    except AttributeError:
        pass   # Python < 3.9: output is compact but valid
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root, encoding="unicode")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Converteer een .dbml bestand naar yEd-compatibel GraphML"
    )
    parser.add_argument(
        "source",
        help="Pad naar het .dbml invoerbestand",
    )
    args = parser.parse_args()

    src = Path(args.source)
    dst = src.with_suffix(".graphml")

    if not src.exists():
        parser.error(f"Invoerbestand niet gevonden: {src}")

    text = src.read_text(encoding="utf-8")
    tables, refs = parse_dbml(text)

    if not tables:
        parser.error(f"Geen tabellen gevonden in: {src}")

    print(f"Gelezen: {len(tables)} tabellen, {len(refs)} referenties", flush=True)
    for t in tables:
        print(f"  {t}: {len(tables[t])} kolommen", flush=True)

    root    = build_graphml(tables, refs)
    xml_str = serialize(root)

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(xml_str, encoding="utf-8")
    print(f"\nGraphML geschreven naar: {dst}", flush=True)


if __name__ == "__main__":
    main()


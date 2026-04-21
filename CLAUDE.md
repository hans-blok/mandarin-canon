# CLAUDE.md — mandarin-canon

## Over deze workspace

**mandarin-canon** is de centrale governance-workspace voor het Mandarin agent-ecosysteem. Zij staat *boven* de value streams — zij is zelf geen value stream.

Inhoud: constitutie, doctrines, kaderdefinities, domeinconcepten, ontologie, rulespeak, templates en agent-contracts.

Taal: **Nederlands, B1-niveau**. Geen synoniemen voor canonieke termen. Geen informele schrijfstijl.

---

## Drielagenstructuur

De grondslagen zijn verdeeld over drie lagen met strikt gescheiden verantwoordelijkheden:

| Laag | Map | Inhoud | Runner-toegang |
|---|---|---|---|
| **1 — Normatief** | `grondslagen/.normatief/` | Constitutie, doctrines, bronafleiding — mensleesbaar | Nee |
| **2 — Formeel** | `grondslagen/.formeel/` | `ontologie.ttl` — machine-readable, uitsluitend voor verificatie | Nee |
| **3 — Bronnen** | `grondslagen/.bronnen/` | `ontologie.compact.md`, `graph/`, `rules/` — broninjectie | **Ja** |

**De runner kent uitsluitend Laag 3 als kennisbron.** Laag 1 en Laag 2 zijn verboden als directe runner-input.

---

## Mapstructuur

```
grondslagen/
├── .normatief/          # Laag 1: constitutie, doctrine.*.md, bronafleiding
├── .formeel/            # Laag 2: ontologie.ttl
├── .bronnen/            # Laag 3: ontologie.compact.md, graph/, rules/
│   └── rules/           # Gestructureerde rulespeak (YAML)
│       └── rules.manifest.json
├── aeo/                 # Value-stream AEO (doctrines, datamodellen)
├── fnd/                 # Value-stream FND
├── kaderdefinities/     # Kaderdefinities (TOGAF e.d.)
├── sleutelset/          # Artefacttype-matrix per value stream fase
├── concepten/           # Domeinconcepten (≠ .normatief)
├── conceptuele-grondslagen.md
├── mandarin-domeinconcepten.md
├── mandarin-ecosysteem-ordeningsconcepten.md
└── bronselectiebeleid.json

.github/agents/          # Agent-contracts (*.agent.md)
.github/prompts/         # Prompt-bestanden (*.prompt.md)
artefacten/canon-curator/ # Curator-rapporten (publicatie-*.md)
templates/               # YAML-headertemplate, doctrine-template, etc.
scripts/                 # grondslagen_digest.py, fetch_ecosysteem_coordinator.py
```

---

## Rulespeak (Laag 3)

Rulespeak-bestanden in `grondslagen/.bronnen/rules/` zijn **YAML**, niet markdown.

Regelmodel:
```yaml
- id: BRH-001              # Domeinprefix + volgnummer (onveranderlijk na publicatie)
  type: verplichting       # verplichting | verbod | permissie
  entiteit: [agent]        # agent | runner | auteur | curator | all
  actie: werken-op-expliciete-bronnen   # kebab-case actie-id
  tekst: >                 # Natuurlijke RuleSpeak-zin (leesbaar)
    Elke agent MOET uitsluitend werken op basis van expliciet aangeleverde bronnen.
  conditie: null           # null of gestructureerde expressie {veld, operator, waarde}
  value_stream: [all]
  fase: [all]
  status: actief
  doctrine_ref: "doctrine.bronhouding-en-exploratie.md#§4.2"
```

Domeinprefixen: `BRH` bronhouding · `TRC` traceability · `HND` handoff · `RTR` retrieval · `TPL` templategebruik · `CMN` common.

Manifest: `grondslagen/.bronnen/rules/rules.manifest.json` — runner laadt uitsluitend bestanden die overeenkomen met actieve `value_stream` en `fase`.

---

## YAML-headers

Elk canoniek artefact heeft een YAML-frontmatter. Zie `templates/yaml-header.template.md` voor de exacte structuur per entiteitstype:

| Bestandspatroon | Entiteit | Verplichte velden |
|---|---|---|
| `*.charter.md` | AGENT | `agent-id`, `value-stream-fase`, `bronhouding` |
| `*.agent.md` | INTENT | `intent-id`, `agent-id`, `artefact-type-id` |
| concept, rapport, datamodel | ARTEFACT | `artefact-id`, `herkomstcode`, `herkomstpositie`, `execution-id` |
| `*.template.md` | TEMPLATE | `template-id`, `template-naam` |
| `*.prompt.md` | EXECUTION | `execution-id`, `execution-code` |
| `hf-*.md` | HANDOFF | `handoff-id`, `van-execution` |

Digest: altijd 4-char hex. Status: `vers` | `muf` | `rot` (via `scripts/grondslagen_digest.py`).

---

## Naamgevingsconventies

- Doctrines: `doctrine.{onderwerp}.md` (dot-notatie)
- Rulespeak: `rules.{onderwerp}.yaml`
- Agent-contracts: `{agent}.{intent}.agent.md`
- Handoff-bestanden: `hf-JJMM.NNNN.handoff.md`
- Herkomstcodes: `JJMM.XXXX` (alfanumeriek, case-sensitive)
- Execution-code: `exec-JJMM.XXXX` (altijd `exec-` prefix)
- Handoff-id: `hf-JJMM.NNNN` (altijd `hf-` prefix, maandelijks oplopend)

---

## Agents in deze workspace

| Agent | Contract | Rol |
|---|---|---|
| **canon-curator** | `.github/agents/canon-curator.valideer-laagconsistentie.agent.md` | Bewaakt consistentie tussen Laag 1, 2 en 3 |
| **ecosysteem-coordinator** | `.github/agents/ecosysteem-coordinator.*.agent.md` | Assembleert bronpakket en tasks.json |

Curator-rapporten naar `artefacten/canon-curator/publicatie-laagconsistentie-{YYYYMMDD-HHMMSS}.md`.

---

## Veelgebruikte scripts

```bash
# Digest-beheer (status vers/muf/rot)
python scripts/grondslagen_digest.py verify
python scripts/grondslagen_digest.py update

# Ecosysteem-coordinator ophalen
python scripts/fetch_ecosysteem_coordinator.py

# Datamodel converteren
python scripts/md_to_dbml.py
python scripts/dbml_to_graphml.py
```

---

## Leesvolgorde voor agents

Agents die in deze workspace opereren lezen in deze volgorde:

1. `grondslagen/conceptuele-grondslagen.md` — fundamentele taal
2. `grondslagen/.normatief/constitutie.md` — hoogste gezagsbron
3. `beleid-mandarin-canon.md` — workspace-scope en grenzen
4. Relevante doctrines uit `grondslagen/.normatief/doctrine.*.md`

Buiten scope voor agents in deze workspace: individuele agent-charters, applicatiecode, project-specifieke afspraken.

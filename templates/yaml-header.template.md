---
template-id: "002"
template-naam: YAML Header Template — Mandarin Artefacten
artefact-type-id: ""
agent-id: ""
versie: 1.0.0
status: vers
digest: tbd0
---
# YAML Header Template — Mandarin Artefacten

Elke artefact-header bestaat uit drie secties: **IDENTIFICATIE · RELATIES · META-DATA**.  
Alle niet-`inhoud`-attributen uit het datamodel staan in de header. De `inhoud`-attributen vormen de body van het bestand.

---

## Routering: welk bestandstype → welke entiteit → welk template

| Bestandspatroon                   | Entiteit  | Sectie |
|-----------------------------------|-----------|--------|
| `*.charter.md`                    | AGENT     | §1     |
| `*agent-boundary*.md`             | AGENT     | §1     |
| `*.agent.md` (contract)           | INTENT    | §2     |
| Logisch datamodel, Gherkin, SQL,  | ARTEFACT  | §3     |
| concept, rapport, validatierapport|           |        |
| `*.template.md`                   | TEMPLATE  | §4     |
| `*.prompt.md`                     | EXECUTION | §5     |
| `hf-*.md` / handoff               | HANDOFF   | §6     |

---

## §1 — AGENT
*Bestanden: charter, boundary*

```yaml
---
# IDENTIFICATIE
agent-id: ""           # PK: vs.versie.naam  (bijv. aeo.02.agent-ontwerper)

# RELATIES
value-stream-fase: ""  # FK → VALUE_STREAM_FASE  (bijv. aeo.02)
bronhouding: ""        # input-gebonden | canon-gebonden | externe-bron-gebonden | exploratief

# META-DATA
versie: ""             # semver  (bijv. 1.0.0)
status: ""             # vers | concept | gearchiveerd
digest: ""             # 4-char hash
---
```

---

## §2 — INTENT
*Bestanden: contract, `.agent.md`*

```yaml
---
# IDENTIFICATIE
intent-id: ""          # PK: agent_id.intent  (bijv. agent-ontwerper.definieer-agent-charter)

# RELATIES
agent-id: ""           # FK → AGENT
artefact-type-id: ""   # FK → ARTEFACT_TYPE  (output-type van deze intent)

# META-DATA
versie: ""
status: ""             # vers | concept | gearchiveerd
digest: ""             # 4-char hash
---
```

---

## §3 — ARTEFACT
*Bestanden: logisch datamodel, Gherkin requirements, PostgreSQL functie, concept, rapport*

```yaml
---
# IDENTIFICATIE
artefact-id: ""        # PK: art-JJMM.XXXX
artefact-type-id: ""   # FK → ARTEFACT_TYPE  (NNN)

# RELATIES
herkomstcode: ""       # FK → HERKOMST_KETEN  (JJMM.XXXX)
herkomstpositie: ""    # initierend | voortbouwend
gegenereerd-door: ""   # FK → AGENT  (agent-id)
intent-id: ""          # FK → INTENT  (producerende intent)
execution-id: ""       # FK → EXECUTION  (exec-JJMM.XXXX)

# META-DATA
versie: ""
status: ""             # vers | concept | gearchiveerd
digest: ""             # 4-char hash
---
```

---

## §4 — TEMPLATE
*Bestanden: `.template.md`*

> TEMPLATE-entiteit heeft geen FK-velden in het datamodel — ARTEFACT_TYPE wijst naar TEMPLATE, niet andersom. De koppeling wordt daarom gedenormaliseerd opgenomen.

```yaml
---
# IDENTIFICATIE
template-id: ""        # PK: NNN
template-naam: ""      # naam van het template

# RELATIES
artefact-type-id: ""   # ARTEFACT_TYPE die dit template gebruikt (1:1, denorm)
agent-id: ""           # producerende agent (context)

# META-DATA
versie: ""
status: ""             # vers | concept | gearchiveerd
digest: ""             # 4-char hash
---
```

---

## §5 — EXECUTION
*Bestanden: `.prompt.md`*

```yaml
---
# IDENTIFICATIE
execution-id: ""           # PK: JJMM.XXXX
execution-code: ""         # UK: exec-JJMM.XXXX

# RELATIES
agent-id: ""               # FK → AGENT
intent-id: ""              # FK → INTENT
orchestratie-run-id: ""    # FK → ORCHESTRATIE_RUN  (optioneel)
bronhouding: ""            # input-gebonden | canon-gebonden | externe-bron-gebonden | exploratief
modus: ""                  # handmatig | tool-ondersteund

# META-DATA
execution-digest: ""       # hash
timestamp: ""              # ISO 8601
status: ""
---
```

---

## §6 — HANDOFF
*Bestanden: handoff*

```yaml
---
# IDENTIFICATIE
handoff-id: ""         # PK: hf-JJMM.NNNN

# RELATIES
van-execution: ""      # FK → EXECUTION  (exec-JJMM.XXXX)
naar-agent: ""         # FK → AGENT  (optioneel)
van-agent: ""          # denorm (agent-id)
artefact-id: ""        # denorm (art-JJMM.XXXX)
value-stream-fase: ""  # denorm (bijv. aeo.02)
human-in-the-loop: ""  # true | false

# META-DATA
timestamp: ""          # ISO 8601
status: ""
digest: ""             # 4-char hash
---
```

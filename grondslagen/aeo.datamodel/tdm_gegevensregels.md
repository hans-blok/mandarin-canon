---
type: gegevensregels
naam: TDM Gegevensregels — Mandarin Sleutelset
versie: 1.2.0
digest: tbd0
status: vers
---
# TDM Gegevensregels — Mandarin Sleutelset

---

## Herkomstverantwoording

Dit document is afgeleid van `tdm_mandarin.md` (versie 1.1, definitief ontwerp) en de volgende normatieve bronnen:

**Geraadpleegde bronnen**:
- `tdm_mandarin.md` — leidend datamodel (versie 1.1, gelezen op 2026-04-12)
- `doctrine-traceability.md` — §2.1–2.4, §3.2, §6.2–6.5, §7.2 (versie 1.5.0, gelezen op 2026-04-12)
- `doctrine-handoff.md` — §2.2–2.4, §7.2–7.3 (versie 1.2.0, gelezen op 2026-04-12)
- `mandarin-ecosysteem-ordeningsconcepten.md` — Bronhouding-as (versie 1.9.0, gelezen op 2026-04-12)
- `workspace-doctrine.md` — §5.2 (versie 1.6.0, gelezen op 2026-04-12)

**Doel**: Formele, gestructureerde vastlegging van alle gegevensregels (business rules) die impliciet in de grondslagen zijn opgenomen maar nog niet als samenhangende set beschikbaar waren.

---

## 1. Inleiding

Deze gegevensregels zijn het normatieve complement op het Target Data Model (`tdm_mandarin.md`). Waar het TDM de structuur vastlegt (entiteiten, attributen, relaties), leggen deze regels de **geldigheidseisen aan de gegevenswaarden** vast.

Elke regel heeft:
- Een uniek **regelidentificator** (BR-NNN)
- Een **beschrijving** van de regel
- Het betrokken **TDM-attribuut of -entiteit**
- De **brondocumentverwijzing**

---

## 2. Gegevensregels

### 2.1 Herkomstcode

| # | Regel | Attribuut | Bron |
|---|-------|-----------|------|
| BR-001 | `herkomstcode` heeft formaat `JJMM.XXXX`: JJ = jaar (2 cijfers), MM = maand (01–12), XXXX = 4-char alfanumeriek (0–9, a–z, A–Z), case-sensitive | `HERKOMST_KETEN.herkomstcode` | doctrine-traceability §2.2 |
| BR-002 | Een initierend artefact genereert een nieuwe herkomstcode; een voortbouwend artefact erft de herkomstcode van het initierende artefact in dezelfde keten | `ARTEFACT.herkomstpositie` | doctrine-traceability §3.2 |
| BR-003 | Alleen de **runner** genereert herkomstcodes; agents genereren ze nooit | `HERKOMST_KETEN.herkomstcode` | doctrine-traceability §2.4 |
| BR-004 | De herkomstcode is onveranderlijk na generatie | `HERKOMST_KETEN.herkomstcode` | doctrine-traceability §2.1 |
| BR-022 | Hash-invoer voor herkomstcode: `timestamp_iso + agent_id + artefact_type_naam` → MD5 → base62 → truncate(4) | `HERKOMST_KETEN.herkomstcode` | doctrine-traceability §2.3, TDM §3.6 |

---

### 2.2 Herkomstpositie

| # | Regel | Attribuut | Bron |
|---|-------|-----------|------|
| BR-018 | `herkomstpositie` heeft exact één van twee waarden: `initierend` of `voortbouwend` | `ARTEFACT.herkomstpositie` | TDM §3.7 |

---

### 2.3 Execution-identiteit

| # | Regel | Attribuut | Bron |
|---|-------|-----------|------|
| BR-005 | `execution_code` wordt afgeleid als `exec-` + `execution_id`; de prefix `exec-` is onveranderlijk onderdeel van de externe identiteit | `EXECUTION.execution_code` | TDM §7.3 |
| BR-020 | `modus` heeft exact één van twee waarden: `handmatig` of `tool-ondersteund` | `EXECUTION.modus` | TDM §3.9, doctrine-traceability §6.5 |
| BR-027 | Een execution-trace-bestand is alleen geldig als `execution_id` én `execution_digest` exact verwijzen naar één bestaand execution-bestand | `EXECUTION.execution_id`, `EXECUTION.execution_digest` | doctrine-traceability §7.2 |
| BR-024 | De execution-bundel-mapnaam gebruikt altijd de `exec-` prefix: `exec-JJMM.XXXX.agent.intent` — nooit de kale `execution_id` | `EXECUTION.execution_code` | workspace-doctrine §5.2, doctrine-traceability §6.4 |

---

### 2.4 Handoff-identiteit

| # | Regel | Attribuut | Bron |
|---|-------|-----------|------|
| BR-006 | `handoff_id` heeft formaat `hf-JJMM.NNNN`: `hf-` prefix, JJ = jaar (2 cijfers), MM = maand (01–12), NNNN = 4-cijferig volgnummer (0001–9999) | `HANDOFF.handoff_id` | doctrine-handoff §2.2 |
| BR-007 | Het handoff-volgnummer loopt per kalendermaand oplopend en herstart bij `0001` elke nieuwe maand; een eenmaal uitgegeven nummer wordt nooit hergebruikt | `HANDOFF.handoff_id` | doctrine-handoff §2.3 |
| BR-008 | Alleen de **runner** genereert `handoff_id`; agents genereren ze nooit | `HANDOFF.handoff_id` | doctrine-handoff §2.4 |
| BR-009 | Als `human_in_the_loop = TRUE` dan is `naar_agent` leeg (NULL) | `HANDOFF.naar_agent`, `HANDOFF.human_in_the_loop` | TDM §3.12 |
| BR-025 | Een handoff-bestand is onveranderlijk na uitgifte; correcties vereisen een nieuw handoff-bestand met een nieuwe `handoff_id` | `HANDOFF.handoff_id` | doctrine-handoff §7.3 |
| BR-026 | Handoff-bestanden mogen niet retroactief worden aangemaakt voor overdrachten die al hebben plaatsgevonden zonder vastlegging | `HANDOFF.handoff_id` | doctrine-handoff §7.2 |

---

### 2.5 Artefact-identiteit

| # | Regel | Attribuut | Bron |
|---|-------|-----------|------|
| BR-010 | `artefact_id` heeft formaat `art-JJMM.XXXX` | `ARTEFACT.artefact_id` | TDM §3.7, §5 |

---

### 2.6 Orchestratie-identiteit

| # | Regel | Attribuut | Bron |
|---|-------|-----------|------|
| BR-011 | `orchestratie_run_id` heeft formaat `run-JJMM.XXXX` | `ORCHESTRATIE_RUN.orchestratie_run_id` | TDM §3.13, §5 |
| BR-021 | `status` (ORCHESTRATIE_RUN) heeft exact één van drie waarden: `running`, `completed`, `failed` | `ORCHESTRATIE_RUN.status` | TDM §3.13 |

---

### 2.7 Value stream en fase

| # | Regel | Attribuut | Bron |
|---|-------|-----------|------|
| BR-012 | `value_stream_fase_code` heeft formaat `<value_stream_code>.<fase_nr>`, waarbij `fase_nr` een nul-gepaddeerd 2-cijferig getal is (bijv. `sfw.01`, `fnd.02`) | `VALUE_STREAM_FASE.value_stream_fase_code` | TDM §3.2 |

---

### 2.8 Agent- en intent-identiteit

| # | Regel | Attribuut | Bron |
|---|-------|-----------|------|
| BR-013 | `agent_id` heeft formaat `<value_stream_code>.<versie>.<naam>` | `AGENT.agent_id` | TDM §3.3 |
| BR-014 | `intent_id` is een compound key met formaat `<agent_id>.<intent>` | `INTENT.intent_id` | TDM §3.4 |

---

### 2.9 Artefact-type, template en parametersleutels

| # | Regel | Attribuut | Bron |
|---|-------|-----------|------|
| BR-029 | `artefact_type_id` is een betekenisloos 3-cijferig nummer zonder prefix | `ARTEFACT_TYPE.artefact_type_id` | TDM §3.6, §5 |
| BR-030 | `artefact_functie` heeft exact één van zes waarden: `normerend`, `structurerend`, `vastleggend`, `realiserend`, `evaluerend` of `beschrijvend` | `ARTEFACT_TYPE.artefact_functie` | TDM §3.6 |
| BR-031 | `beschrijvings_modus` is ALLEEN gevuld wanneer `artefact_functie = 'beschrijvend'`; in alle andere gevallen is het veld leeg (NULL) | `ARTEFACT_TYPE.beschrijvings_modus` | TDM §3.6 |
| BR-032 | `beschrijvings_modus` heeft, wanneer gevuld, exact één van twee waarden: `verkennend` of `verantwoordend` | `ARTEFACT_TYPE.beschrijvings_modus` | TDM §3.6 |
| BR-015 | `template_id` is een betekenisloos 3-cijferig nummer zonder prefix | `TEMPLATE.template_id` | TDM §3.6a, §5 |
| BR-016 | `parameter_id` is een betekenisloos 4-cijferig nummer zonder prefix | `INVOER_PARAMETER.parameter_id` | TDM §3.5 |

---

### 2.10 Bronsleutels

| # | Regel | Attribuut | Bron |
|---|-------|-----------|------|
| BR-017 | `kaderbron_id` is een betekenisloos 8-cijferig nummer zonder prefix | `KADERBRON.kaderbron_id` | TDM §3.10, §5 |
| BR-019 | `werkbron_id` is een betekenisloos 8-cijferig nummer zonder prefix | `WERKBRON.werkbron_id` | TDM §3.11, §5 |
| BR-023 | KADERBRON verwijst naar canonieke (normatieve) artefacten (doctrines, constitutie); WERKBRON verwijst naar output-artefacten van eerdere executions | `KADERBRON`, `WERKBRON` | TDM §3.10–3.11 |

---

### 2.11 Bronhouding

| # | Regel | Attribuut | Bron |
|---|-------|-----------|------|
| BR-028 | `bronhouding` heeft exact één van vijf waarden: `input-gebonden`, `canon-gebonden`, `workspace-gebonden`, `extern-gebonden`, `exploratief` | `EXECUTION.bronhouding`, `AGENT.bronhouding` | mandarin-ecosysteem-ordeningsconcepten §Bronhouding |

---

### 2.12 Inhoud-velden

Inhoud-velden zijn vrije tekstvelden met prefix `inhoud_`. Ze bevatten substantiële tekstinhoud (charter, contract, prompt, definitie) en zijn daarmee te onderscheiden van structurele sleutelvelden in YAML-headers.

| # | Regel | Attribuut | Bron |
|---|-------|-----------|------|
| BR-033 | `AGENT.inhoud_charter` is verplicht (NOT NULL): elk geregistreerd agent heeft een charter | `AGENT.inhoud_charter` | TDM §3.3 |
| BR-034 | `INTENT.inhoud_contract` is verplicht (NOT NULL): elke intent heeft een contract met pre/postcondities en gedragsregels | `INTENT.inhoud_contract` | TDM §3.4 |
| BR-035 | `EXECUTION.inhoud_prompt_instructions` is verplicht (NOT NULL): de gebruikte prompt wordt altijd vastgelegd als onderdeel van het execution-record | `EXECUTION.inhoud_prompt_instructions` | TDM §3.9 |
| BR-036 | `TEMPLATE.inhoud_body` is verplicht (NOT NULL): een template zonder body heeft geen functie | `TEMPLATE.inhoud_body` | TDM §3.6a |
| BR-037 | Inhoud-velden met prefix `inhoud_` zijn vrije tekstvelden; ze bevatten geen sleutelwaarden en zijn niet onderhevig aan formaatconstraints | alle `inhoud_*` attributen | TDM §2 |

---

## 3. Overzicht per TDM-entiteit

| Entiteit | Gegevensregels |
|----------|----------------|
| HERKOMST_KETEN | BR-001, BR-003, BR-004, BR-022 |
| ARTEFACT | BR-002, BR-010, BR-018 |
| ARTEFACT_TYPE | BR-029, BR-030, BR-031, BR-032 |
| TEMPLATE | BR-015, BR-036 |
| EXECUTION | BR-005, BR-020, BR-024, BR-027, BR-028, BR-035 |
| HANDOFF | BR-006, BR-007, BR-008, BR-009, BR-025, BR-026 |
| ORCHESTRATIE_RUN | BR-011, BR-021 |
| VALUE_STREAM_FASE | BR-012 |
| AGENT | BR-013, BR-028, BR-033 |
| INTENT | BR-014, BR-034 |
| INVOER_PARAMETER | BR-016 |
| KADERBRON | BR-017, BR-023 |
| WERKBRON | BR-019, BR-023 |

---

## Wijzigingslog

| Datum | Versie | Wijziging | Auteur |
|-------|--------|-----------|--------|
| 2026-04-12 | 1.1.0 | Toegevoegd: BR-029 t/m BR-032 voor ARTEFACT_TYPE (artefact_functie, beschrijvings_modus); BR-015 verwijst naar §3.6a; BR-022 gebruikt artefact_type_naam; entiteitoverzicht bijgewerkt | Hans Blok |
| 2026-04-12 | 1.2.0 | Toegevoegd: §2.12 Inhoud-velden met BR-033 t/m BR-037; entiteitoverzicht bijgewerkt voor TEMPLATE, EXECUTION, AGENT, INTENT | Hans Blok |
| 2026-04-12 | 1.0.0 | Initiële versie: 28 gegevensregels geëxtraheerd uit TDM en grondslagen | Hans Blok |

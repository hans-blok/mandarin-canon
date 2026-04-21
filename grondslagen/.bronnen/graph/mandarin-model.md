---
artefact-id: ""
artefact-type-id: ""
herkomstcode: ""
herkomstpositie: "initierend"
gegenereerd-door: ""
intent-id: ""
execution-id: ""
versie: 1.0.0
status: vers
digest: tbd0
---
# Mandarin Ecosystem - Neo4j Graph Model

**Sources (closed source stance)**:
- `ldm-mandarin.md` v1.4.0 - authoritative data model (15 entities, 3NF, Barker method)
- `mandarin-domeinconcepten.md` v2.13.0 - canonical concept definitions
- `mandarin-ecosysteem-ordeningsconcepten.md` v1.9.0 - four orthogonal axes
- `doctrine-traceability.md` v1.6.0 - provenance code, execution identity, YAML header
- `doctrine-handoff.md` v1.2.0 - handoff format, escalation
- `mandarin-value-streams-en-fasen.md` v1.8.0 - value streams and phases
- `doctrine-agent-charter-normering.md` v2.4.0 - agent identity and charter principles
- `doctrine-bronhouding-en-exploratie.md` v1.0.0 - source regime axes

---

## 1. Core Concepts and Derived Graph Structure

### 1.1 Canonical Concepts to Neo4j Labels

| LDM entity | Neo4j label | Explanation |
|---|---|---|
| `AGENT` | `MandarinAgent` | Prefix to avoid collision with Neo4j-internal `Agent` |
| `VALUE_STREAM` | `ValueStream` | Adopted directly |
| `VALUE_STREAM_FASE` | `ValueStreamFase` | Adopted directly |
| `INTENT` | `Intent` | Adopted directly |
| `INVOER_PARAMETER` | `InvoerParameter` | Adopted directly |
| `ORCHESTRATIE_RUN` | `OrchestratieRun` | Adopted directly |
| `EXECUTION` | `Execution` | Adopted directly |
| `ARTEFACT` | `MandarinArtefact` | Prefix to avoid collision with graph-internal `Artefact` |
| `ARTEFACT_TYPE` | `ArtefactType` | Adopted directly |
| `BESCHRIJVEND_ARTEFACT_TYPE` | `BeschrijvendArtefactType` | Additional label on the `ArtefactType` node (multi-label approach) |
| `TEMPLATE` | `Template` | Adopted directly |
| `HERKOMST_KETEN` | `HerkomstKeten` | Adopted directly |
| `KADERBRON` | `KaderBron` | Canonical LDM name retained |
| `WERKBRON` | `WerkBron` | Canonical LDM name retained |
| `HANDOFF` | `Handoff` | Adopted directly |
| *(not in LDM)* | `Bronregime` | Domain concept (source-stance doctrine); modeled in LDM as an attribute on AGENT and EXECUTION |
| *(not in LDM)* | `Workspace` | Domain concept (workspace doctrine); not modeled in LDM |

### 1.2 Canonical Relationships to Neo4j Relationship Types

| LDM relationship (functional name) | Neo4j relationship type | Direction |
|---|---|---|
| VALUE_STREAM **omvat** VALUE_STREAM_FASE | `OMVAT` | `(ValueStream)→(ValueStreamFase)` |
| VALUE_STREAM_FASE **huisvest** AGENT | `HUISVEST` | `(ValueStreamFase)→(MandarinAgent)` |
| ARTEFACT_TYPE **heeft subtype** BESCHRIJVEND_ARTEFACT_TYPE | `HEEFT_SUBTYPE` | `(ArtefactType)→(BeschrijvendArtefactType)` |
| ARTEFACT_TYPE **gebruikt** TEMPLATE | `GEBRUIKT` | `(ArtefactType)→(Template)` |
| AGENT **definieert** INTENT | `DEFINIEERT` | `(MandarinAgent)→(Intent)` |
| INTENT **vereist** INVOER_PARAMETER | `VEREIST` | `(Intent)→(InvoerParameter)` |
| INTENT **produceert type** ARTEFACT_TYPE | `PRODUCEERT_TYPE` | `(Intent)→(ArtefactType)` |
| ORCHESTRATIE_RUN **orkestreert** EXECUTION | `ORKESTREERT` | `(OrchestratieRun)→(Execution)` |
| EXECUTION **uitgevoerd door** AGENT | `UITGEVOERD_DOOR` | `(Execution)→(MandarinAgent)` |
| EXECUTION **voert uit** INTENT | `VOERT_UIT` | `(Execution)→(Intent)` |
| EXECUTION **produceert** ARTEFACT | `PRODUCEERT` | `(Execution)→(MandarinArtefact)` |
| EXECUTION **raadpleegt als kader** KADERBRON | `RAADPLEEGT_ALS_KADER` | `(Execution)→(KaderBron)` |
| EXECUTION **raadpleegt als werk** WERKBRON | `RAADPLEEGT_ALS_WERK` | `(Execution)→(WerkBron)` |
| ARTEFACT **is van type** ARTEFACT_TYPE | `IS_VAN_TYPE` | `(MandarinArtefact)→(ArtefactType)` |
| ARTEFACT **gegenereerd door** AGENT | `GEGENEREERD_DOOR` | `(MandarinArtefact)→(MandarinAgent)` |
| ARTEFACT **behoort tot** HERKOMST_KETEN | `BEHOORT_TOT` | `(MandarinArtefact)→(HerkomstKeten)` |
| HERKOMST_KETEN **gestart door** ARTEFACT *(deferred)* | `GESTART_DOOR` | `(HerkomstKeten)→(MandarinArtefact)` |
| KADERBRON **verwijst naar** ARTEFACT | `VERWIJST_NAAR` | `(KaderBron)→(MandarinArtefact)` |
| WERKBRON **verwijst naar** ARTEFACT | `VERWIJST_NAAR` | `(WerkBron)→(MandarinArtefact)` |
| WERKBRON **ontstaan in** EXECUTION | `ONTSTAAN_IN` | `(WerkBron)→(Execution)` |
| HANDOFF **vloeit voort uit** EXECUTION | `VLOEIT_VOORT_UIT` | `(Handoff)→(Execution)` |
| HANDOFF **adresseert** AGENT | `ADRESSEERT` | `(Handoff)→(MandarinAgent)` |
| *(extensie)* AGENT/EXECUTION **valt onder** BRONREGIME | `VALT_ONDER` | `(MandarinAgent|Execution)→(Bronregime)` |

---

## 2. Properties Per Label

### `MandarinAgent`
| Property | Type | Source | Explanation |
|---|---|---|---|
| `agentId` | String | PK | Formaat: `vs.versie.naam` (bijv. `aeo.02.agent-ontwerper`) |
| `agentNaam` | String | NN | Readable name |
| `versie` | String | NN | Semver |
| `bronhouding` | String | NN | `input-gebonden` \| `canon-gebonden` \| `externe-bron-gebonden` \| `exploratief` |
| `inhoudCharter` | String | NN | Full charter text |

### `ValueStream`
| Property | Type | Source |
|---|---|---|
| `waardestroomCode` | String | PK |
| `waardestroomNaam` | String | NN |
| `inhoudBeschrijving` | String | opt |

### `ValueStreamFase`
| Eigenschap | Type | Bron |
|---|---|---|
| `faseCode` | String | PK | Format: `vs.NN` (for example `aeo.02`) |
| `waardestroomNaam` | String | NN |
| `inhoudBeschrijving` | String | opt |

### `Intent`
| Eigenschap | Type | Bron |
|---|---|---|
| `intentId` | String | PK | Formaat: `agent_id.intent` |
| `intentNaam` | String | NN |
| `inhoudContract` | String | NN |

### `Execution`
| Eigenschap | Type | Bron |
|---|---|---|
| `executieId` | String | PK | Format: `JJMM.XXXX` |
| `executieCode` | String | UK | Format: `exec-JJMM.XXXX` |
| `executieDigest` | String | NN |
| `bronhouding` | String | NN | Stored derivation (N7 in LDM) |
| `modus` | String | NN | `handmatig` \| `tool-ondersteund` |
| `tijdstip` | DateTime | NN | ISO 8601 |
| `inhoudPromptInstructies` | String | NN |

### `MandarinArtefact`
| Eigenschap | Type | Bron |
|---|---|---|
| `artefactId` | String | PK | Formaat: `art-JJMM.XXXX` |
| `herkomstpositie` | String | NN | `initierend` \| `voortbouwend` |
| `executieId` | String | UK | FK+UK (uitzondering Barker — N8 in LDM) |
| `tijdstip` | DateTime | NN |
| `inhoudTekst` | String | opt |

### `ArtefactType`
| Eigenschap | Type | Bron |
|---|---|---|
| `artefactTypeId` | String | PK | Format: `NNN` |
| `artefactTypeNaam` | String | NN |
| `artefactFunctie` | String | NN | `vastleggend` \| `structurerend` \| `registrerend` \| `beschrijvend` \| `sturend` \| `informatief` |
| `inhoudBeschrijving` | String | opt |

### `BeschrijvendArtefactType`
> Multi-label node: the same node receives both `ArtefactType` and `BeschrijvendArtefactType`. The subtype relationship is also retained as a `HEEFT_SUBTYPE` edge for querying.

| Eigenschap | Type | Bron |
|---|---|---|
| `beschrijvingsModus` | String | NN | `verkennend` \| `verantwoordend` |

### `Template`
| Eigenschap | Type | Bron |
|---|---|---|
| `templateId` | String | PK |
| `templateNaam` | String | NN |
| `inhoudTekst` | String | NN |

### `HerkomstKeten`
| Eigenschap | Type | Bron |
|---|---|---|
| `herkomstCode` | String | PK | Format: `JJMM.XXXX` |
| `oorsprong Tijdstip` | DateTime | NN |

### `KaderBron`
| Eigenschap | Type | Bron |
|---|---|---|
| `kaderBronId` | String | PK |
| `headerDigest` | String | opt |
| `werkelijkeDigest` | String | opt |

### `WerkBron`
| Eigenschap | Type | Bron |
|---|---|---|
| `werkBronId` | String | PK |
| `headerDigest` | String | opt |
| `werkelijkeDigest` | String | opt |

### `Handoff`
| Eigenschap | Type | Bron |
|---|---|---|
| `handoffId` | String | PK | Format: `hf-JJMM.NNNN` |
| `menselijkeInterventie` | Boolean | NN | `true` = escalation |
| `tijdstip` | DateTime | NN |
| `inhoudBoodschap` | String | opt |

### `Bronregime` *(extension node - not in LDM)*
| Eigenschap | Type | Bron |
|---|---|---|
| `regimeId` | String | PK | `input-gebonden` \| `canon-gebonden` \| `externe-bron-gebonden` \| `exploratief` |
| `beschrijving` | String | opt |

### `Workspace` *(extension node - not in LDM)*
| Eigenschap | Type | Bron |
|---|---|---|
| `workspaceId` | String | PK |
| `workspaceNaam` | String | opt |

---

## 3. Design Choices and Rationale

### K1 - Prefixing `Mandarin` on AGENT and ARTEFACT
Neo4j has no built-in `Agent` concept, but in an AI context a naming collision is likely. `MandarinAgent` and `MandarinArtefact` make the domain origin explicit and avoid ambiguity in query writing.

### K2 - Multi-label for BESCHRIJVEND_ARTEFACT_TYPE
The LDM models this as a separate subtype entity (N5, subtype-supertype relationship). In Neo4j, a separate node is also valid, but a multi-label approach (`ArtefactType` + `BeschrijvendArtefactType`) is more compact and preserves direct queryability through the supertype label. The `HEEFT_SUBTYPE` relationship is retained alongside the multi-label for backward compatibility.

### K3 - KADERBRON and WERKBRON as Separate Labels
The LDM distinguishes KADERBRON and WERKBRON as separate entities. This distinction is preserved as separate labels, not merged into one `Bron` label. Reason: the two types have a different relationship structure (`WERKBRON` has an additional `ONTSTAAN_IN` relationship to `EXECUTION`).

### K4 - Bronregime as an Extension Node
`bronhouding` is an attribute on AGENT and EXECUTION in the LDM. In the graph model, it is also included as a separate `Bronregime` node so that all agents and executions with the same regime can be queried through one `VALT_ONDER` relationship. This reflects the domain-driven structure in `doctrine-bronhouding-en-exploratie.md`.

### K5 - Workspace as an Extension Node
`Workspace` is a canonical domain concept (see `mandarin-domeinconcepten.md`) but is not included as an entity in the LDM. It is added as an extension node for the graph model because workspace context is relevant when querying execution context.

### K6 - Deferred Constraint HERKOMST_KETEN to ARTEFACT
The circular relationship (N6 in the LDM) is included as a `GESTART_DOOR` relationship. Its deferred nature is documented as the relationship property `deferred: true`. Neo4j does not provide declarative deferred constraints; the creation order (INSERT HERKOMST_KETEN -> INSERT ARTEFACT -> SET relationship) is an application responsibility.

### K7 - Relationship Property `deferred` on GESTART_DOOR
See K6. The `GESTART_DOOR` relationship receives the property `deferred: true` to make the implementation constraint explicit in the graph data.

---

## 4. Open Points

| No. | Point | Impact |
|---|---|---|
| OP-01 | `INVOER_PARAMETER` nodes are not included in the seed data. Their structure is defined in the schema. | Low |
| OP-02 | `ORCHESTRATIE_RUN` is included in schema and seed, but the link to a working orchestration mechanism is out of scope. | Low |
| OP-03 | `Workspace` nodes do not have a formal PK convention in the canon. Proposed format: `ws-<name>`. | Medium |
| OP-04 | The `inhoud*` attributes (charter, contract, prompt instructions) are large text fields. Consider separate text nodes or external storage when scaling up. | Low |
| OP-05 | The link `MandarinAgent` -> `Workspace` through VALUE_STREAM_FASE is implicit (AGENT.waardestroomfasecode -> FASE -> WORKSPACE). A direct relationship is missing; adding it requires extension of the LDM. | Medium |

---

## 5. Version History

| Date | Version | Change |
|---|---|---|
| 2026-04-13 | 1.0.0 | Initial version: concept-to-label mapping, relationship-type mapping, properties per label, K1-K7 design choices, OP-01-OP-05 | Hans Blok |

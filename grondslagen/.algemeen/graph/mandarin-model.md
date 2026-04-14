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
# Mandarin Ecosysteem — Neo4j Grafmodel

**Bronnen (gesloten bronhouding)**:
- `ldm-mandarin.md` v1.4.0 — gezaghebbend datamodel (15 entiteiten, 3NF, Barker-methode)
- `mandarin-domeinconcepten.md` v2.13.0 — canonieke conceptdefinities
- `mandarin-ecosysteem-ordeningsconcepten.md` v1.9.0 — vier orthogonale assen
- `doctrine-traceability.md` v1.6.0 — herkomstcode, execution-identiteit, YAML-header
- `doctrine-handoff.md` v1.2.0 — handoff-formaat, escalatie
- `mandarin-value-streams-en-fasen.md` v1.8.0 — value streams en fasen
- `doctrine-agent-charter-normering.md` v2.4.0 — agentidentiteit en charter-principes
- `doctrine-bronhouding-en-exploratie.md` v1.0.0 — bronregime-assen

---

## 1. Kernconcepten en afgeleide grafstructuur

### 1.1 Canonieke concepten → Neo4j-labels

| LDM-entiteit | Neo4j-label | Toelichting |
|---|---|---|
| `AGENT` | `MandarinAgent` | Prefix om botsing met Neo4j-intern `Agent` te vermijden |
| `VALUE_STREAM` | `ValueStream` | Direct overgenomen |
| `VALUE_STREAM_FASE` | `ValueStreamFase` | Direct overgenomen |
| `INTENT` | `Intent` | Direct overgenomen |
| `INVOER_PARAMETER` | `InvoerParameter` | Direct overgenomen |
| `ORCHESTRATIE_RUN` | `OrchestratieRun` | Direct overgenomen |
| `EXECUTION` | `Execution` | Direct overgenomen |
| `ARTEFACT` | `MandarinArtefact` | Prefix om botsing met graph-intern `Artefact` te vermijden |
| `ARTEFACT_TYPE` | `ArtefactType` | Direct overgenomen |
| `BESCHRIJVEND_ARTEFACT_TYPE` | `BeschrijvendArtefactType` | Aanvullend label op `ArtefactType`-node (multi-label aanpak) |
| `TEMPLATE` | `Template` | Direct overgenomen |
| `HERKOMST_KETEN` | `HerkomstKeten` | Direct overgenomen |
| `KADERBRON` | `KaderBron` | Canonieke naam uit LDM behouden |
| `WERKBRON` | `WerkBron` | Canonieke naam uit LDM behouden |
| `HANDOFF` | `Handoff` | Direct overgenomen |
| *(niet in LDM)* | `Bronregime` | Domeinconcept (bronhouding-doctrine); in LDM als attribuut op AGENT en EXECUTION |
| *(niet in LDM)* | `Workspace` | Domeinconcept (workspace-doctrine); niet gemodelleerd in LDM |

### 1.2 Canonieke relaties → Neo4j-relatietypes

| LDM-relatie (functionele naam) | Neo4j-relatietype | Richting |
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

## 2. Eigenschappen per label

### `MandarinAgent`
| Eigenschap | Type | Bron | Toelichting |
|---|---|---|---|
| `agentId` | String | PK | Formaat: `vs.versie.naam` (bijv. `aeo.02.agent-ontwerper`) |
| `agentNaam` | String | NN | Leesbare naam |
| `versie` | String | NN | Semver |
| `bronhouding` | String | NN | `input-gebonden` \| `canon-gebonden` \| `externe-bron-gebonden` \| `exploratief` |
| `inhoudCharter` | String | NN | Volledige charter-tekst |

### `ValueStream`
| Eigenschap | Type | Bron |
|---|---|---|
| `waardestroomCode` | String | PK |
| `waardestroomNaam` | String | NN |
| `inhoudBeschrijving` | String | opt |

### `ValueStreamFase`
| Eigenschap | Type | Bron |
|---|---|---|
| `faseCode` | String | PK | Formaat: `vs.NN` (bijv. `aeo.02`) |
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
| `executieId` | String | PK | Formaat: `JJMM.XXXX` |
| `executieCode` | String | UK | Formaat: `exec-JJMM.XXXX` |
| `executieDigest` | String | NN |
| `bronhouding` | String | NN | Bewaarde afleiding (N7 in LDM) |
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
| `artefactTypeId` | String | PK | Formaat: `NNN` |
| `artefactTypeNaam` | String | NN |
| `artefactFunctie` | String | NN | `vastleggend` \| `structurerend` \| `registrerend` \| `beschrijvend` \| `sturend` \| `informatief` |
| `inhoudBeschrijving` | String | opt |

### `BeschrijvendArtefactType`
> Multi-label node: dezelfde node krijgt zowel `ArtefactType` als `BeschrijvendArtefactType`. De subtype-relatie wordt ook als `HEEFT_SUBTYPE`-edge bewaard voor querying.

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
| `herkomstCode` | String | PK | Formaat: `JJMM.XXXX` |
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
| `handoffId` | String | PK | Formaat: `hf-JJMM.NNNN` |
| `menselijkeInterventie` | Boolean | NN | `true` = escalatie |
| `tijdstip` | DateTime | NN |
| `inhoudBoodschap` | String | opt |

### `Bronregime` *(extensienode — niet in LDM)*
| Eigenschap | Type | Bron |
|---|---|---|
| `regimeId` | String | PK | `input-gebonden` \| `canon-gebonden` \| `externe-bron-gebonden` \| `exploratief` |
| `beschrijving` | String | opt |

### `Workspace` *(extensienode — niet in LDM)*
| Eigenschap | Type | Bron |
|---|---|---|
| `workspaceId` | String | PK |
| `workspaceNaam` | String | opt |

---

## 3. Ontwerp-keuzes en motivatie

### K1 — Prefixen `Mandarin` op AGENT en ARTEFACT
Neo4j heeft geen ingebouwd `Agent`-concept, maar in een AI-context is naambotsing waarschijnlijk. `MandarinAgent` en `MandarinArtefact` maken de domeinherkomst expliciet en vermijden ambiguïteit in query-schrijfsels.

### K2 — Multi-label voor BESCHRIJVEND_ARTEFACT_TYPE
Het LDM modelleert dit als een apart subtype-entiteit (N5, subtype-supertype relatie). In Neo4j is een apart knooppunt ook geldig, maar een multi-labelaanpak (`ArtefactType` + `BeschrijvendArtefactType`) is compacter en behoudt de directe queryerbaarheid via het supertype-label. De `HEEFT_SUBTYPE`-relatie wordt naast de multi-label bewaard voor achterwaartse compatibiliteit.

### K3 — KADERBRON en WERKBRON als afzonderlijke labels
Het LDM onderscheidt KADERBRON en WERKBRON als afzonderlijke entiteiten. Dit onderscheid wordt bewaard als afzonderlijke labels, niet samengevoegd tot één `Bron`-label. Reden: de twee typen hebben een verschillende relatie-structuur (WERKBRON heeft extra `ONTSTAAN_IN`-relatie naar EXECUTION).

### K4 — Bronregime als extensienode
`bronhouding` is in het LDM een attribuut op AGENT en EXECUTION. In het grafmodel wordt het ook als afzonderlijk `Bronregime`-knooppunt opgenomen, zodat alle agents en executions met hetzelfde regime via één `VALT_ONDER`-relatie bevraagbaar zijn. Dit weerspiegelt de domain-driven structuur in `doctrine-bronhouding-en-exploratie.md`.

### K5 — Workspace als extensienode
`Workspace` is een canoniek domeinconcept (zie `mandarin-domeinconcepten.md`) maar is niet als entiteit opgenomen in het LDM. Het wordt toegevoegd als extensienode voor het graafmodel, omdat workspace-context relevant is voor het bevragen van uitvoeringscontext.

### K6 — Deferred-constraint HERKOMST_KETEN → ARTEFACT
De circulaire relatie (N6 in LDM) wordt als `GESTART_DOOR`-relatie opgenomen. De deferred aard wordt gedocumenteerd als relatie-eigenschap `deferred: true`. In Neo4j bestaan geen declaratieve deferred constraints; de aanmaaksvolgorde (INSERT HERKOMST_KETEN → INSERT ARTEFACT → SET relatie) is applicatie-verantwoordelijkheid.

### K7 — Relatie-eigenschap `deferred` op GESTART_DOOR
Zie K6. De `GESTART_DOOR`-relatie krijgt eigenschap `deferred: true` om de implementatiebeperking expliciet te maken in de grafdata.

---

## 4. Openstaande punten

| Nr | Punt | Impact |
|---|---|---|
| OP-01 | `INVOER_PARAMETER`-nodes zijn niet opgenomen in de seed-data. Hun structuur is wel in het schema gedefinieerd. | Laag |
| OP-02 | `ORCHESTRATIE_RUN` is opgenomen in schema en seed, maar de koppeling naar een werkend orchestratie-mechanisme is buiten scope. | Laag |
| OP-03 | `Workspace`-nodes kennen geen formele PK-conventie in de canon. Voorgesteld formaat: `ws-<naam>`. | Middel |
| OP-04 | De `inhoud*`-attributen (charter, contract, prompt-instructies) zijn grote tekstvelden. Overweeg aparte tekstknooppunten of externe opslag bij schaalvergroting. | Laag |
| OP-05 | De koppeling `MandarinAgent` → `Workspace` via de VALUE_STREAM_FASE is impliciet (AGENT.waardestroomfasecode → FASE → WORKSPACE). Een directe relatie ontbreekt; toevoeging vereist uitbreiding van het LDM. | Middel |

---

## 5. Versiebeheer

| Datum | Versie | Wijziging |
|---|---|---|
| 2026-04-13 | 1.0.0 | Initiële versie: concept-naar-label mapping, relatietype-mapping, eigenschappen per label, K1–K7 ontwerp-keuzes, OP-01–OP-05 | Hans Blok |

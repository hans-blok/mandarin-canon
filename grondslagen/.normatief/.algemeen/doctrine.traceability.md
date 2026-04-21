---
type: doctrine
naam: Doctrine — Traceability en Herkomstcode
code: DTRC
versie: 1.8.0
digest: tbd0
status: vers
---
# Doctrine — Traceability en Herkomstcode


---

## Herkomstverantwoording

Dit normatief artefact is opgesteld op basis van de volgende bronnen:

**Geraadpleegde bronnen**:
- mandarin-ecosysteem-ordeningsconcepten.md — concepten herkomstpositie, initierend, voortbouwend (gelezen op 2026-03-20)
- doctrine-handoff.md (versie 1.0.0, gelezen op 2026-04-06)
- doctrine-agent-charter-normering.md — richtlijn herkomstpositie in contracten (versie 2.4.0, gelezen op 2026-03-20)
- mandarin-domeinconcepten.md — concepten bronpakket, execution-bestand (gelezen op 2026-04-06)
- 2f0b.concept-curator.definieer-concept.md — voorbeeld van een execution-bestand (gelezen op 2026-04-06)
- Gebruikersinvoer over herkomstcode-conventie (ontvangen op 2026-03-20)

**Opsteller**: Constitutioneel Auteur  
**Doel**: Expliciete normering van traceerbaarheid en herkomstcode-generatie binnen het Mandarin-ecosysteem

---

## Classificatie

Deze doctrine positioneert zich als volgt op de vier orthogonale assen:

| Betekeniseffect | Vormingsfase | Werking | Bronhouding |
|---|---|---|---|
| normerend | ordening / vastlegging | procedureel | canon-gebonden |

- **Betekeniseffect** — *normerend*: stelt expliciete normen voor traceerbaarheid en herkomstcode-generatie
- **Vormingsfase** — *ordening / vastlegging*: structureert en formaliseert de keten van herkomstcodes en execution-identiteiten
- **Werking** — *procedureel*: schrijft procedures voor het genereren, erven en valideren van herkomstcodes en YAML-headers
- **Bronhouding** — *canon-gebonden*: baseert zich uitsluitend op canonieke bronnen en templates

---

## 1. Doel en scope

Deze doctrine normeert de **traceerbaarheid** van artefacten binnen het Mandarin-ecosysteem door:

1. Een **herkomstcode** te definiëren die uniek identificeert waar een artefact-keten begint
2. Regels vast te leggen voor **generatie** (bij initierende artefacten) en **overerving** (bij voortbouwende artefacten)
3. De relatie te expliciteren met de handoff-discipline

Traceability waarborgt dat elk artefact herleidbaar is naar zijn oorsprong, ongeacht hoeveel voortbouwende artefacten in de keten zijn ontstaan.

---

## 2. Herkomstcode

### 2.1 — Definitie

Een **herkomstcode** is een unieke, door het systeem gegenereerde identificatiecode die de oorsprong van een artefact-keten markeert.

De herkomstcode:
- wordt uitsluitend gegenereerd door **initierende** artefacten
- wordt overgenomen door alle **voortbouwende** artefacten in dezelfde keten
- is onveranderlijk na generatie
- fungeert als permanente referentie voor audit en traceerbaarheid

### 2.2 — Conventie

```
Format:  JJMM.XXXX
         │  │  └─── 4-karakter hash (alfanumeriek, case-sensitive)
         │  └───── Maand (01-12)
         └─────── Jaar (laatste 2 cijfers)
```

**Voorbeelden**:
- `2603.Tu9x` — Maart 2026, hash Tu9x
- `2601.Ab3K` — Januari 2026, hash Ab3K
- `2512.9xQm` — December 2025, hash 9xQm

### 2.3 — Hash-generatie

De 4-karakter hash wordt gegenereerd op basis van:

```
hash_input = timestamp_iso + agent_id + artefact_type
hash = truncate(base62(md5(hash_input)), 4)
```

**Kenmerken**:
- **Alfanumeriek**: 0-9, a-z, A-Z (62 tekens)
- **Case-sensitive**: `Tu9x` ≠ `tu9x`
- **Deterministische afleiding**: Zelfde input levert zelfde hash
- **Collision-resistent**: 62^4 = 14.776.336 mogelijke waarden per maand

### 2.4 — Verantwoordelijkheid voor generatie

De **runner** is verantwoordelijk voor het genereren van de herkomstcode.

Dit sluit aan bij de handoff-doctrine:
- De runner genereert de handoff-id
- De runner genereert de herkomstcode (indien initierend)
- Agents genereren **geen** herkomstcodes

---

## 3. Herkomstpositie en gedrag

### 3.1 — Vastlegging in agent-contract

De **herkomstpositie** wordt vastgelegd als eigenschap van de output-specificatie in het **agent-contract**:

```yaml
# Voorbeeld: initierend
intent: definieer-concept
output:
  - type: concept-definitie
    herkomstpositie: initierend    # ← vastgelegd in contract
    template: concept.template.md
```

```yaml
# Voorbeeld: voortbouwend
intent: wijzig-concept  
output:
  - type: concept-wijziging
    herkomstpositie: voortbouwend  # ← vastgelegd in contract
    template: concept.template.md
```

**Ontwerpkeuze**: De herkomstpositie is een eigenschap van het contract, niet van een apart register. Dit houdt de definitie bij de bron (het contract) en voorkomt synchronisatieproblemen.

### 3.2 — Runner-logica

De **runner** leest de herkomstpositie uit het contract en handelt dienovereenkomstig:

```
LEES contract.output.herkomstpositie

IF herkomstpositie == "initierend":
    herkomstcode = genereer_nieuwe_code()
ELSE IF herkomstpositie == "voortbouwend":
    herkomstcode = input_artefact.herkomstcode
    initierend_artefact = input_artefact.pad
ELSE:
    FOUT: ongeldige herkomstpositie
```

### 3.3 — Initierend artefact

Een artefact met herkomstpositie **initierend**:

| Actie | Beschrijving |
|-------|--------------|
| **Genereer** | Runner genereert nieuwe herkomstcode volgens conventie |
| **Vastleg** | Herkomstcode wordt opgenomen in artefact-header |
| **Publiceer** | Herkomstcode is beschikbaar voor voortbouwende artefacten |

**Wanneer is een artefact initierend?**
- Eerste definitie van een nieuw concept, charter, contract of doctrine
- Start van een nieuwe taak-executie (execution-file)
- Creatie van een nieuw governance-artefact
- Elke situatie waarin geen eerder initierend artefact in de keten bestaat

### 3.4 — Voortbouwend artefact

Een artefact met herkomstpositie **voortbouwend**:

| Actie | Beschrijving |
|-------|--------------|
| **Erf** | Neem herkomstcode over van initierend artefact |
| **Verwijs** | Refereer expliciet naar het initierende artefact |
| **Propageer** | Verdere voortbouwende artefacten erven dezelfde code |

**Wanneer is een artefact voortbouwend?**
- Wijziging, update of correctie van een bestaand artefact
- Afgeleide output van een eerder geproduceerd artefact
- Vervolgstap in een lopende taak-executie
- Elke situatie waarin een initierend artefact in de keten bestaat

---

## 4. Header-structuur

### 4.1 — Initierend artefact

```yaml
---
herkomstcode: 2603.Tu9x
herkomstpositie: initierend
gegenereerd_door: <agent-id>
datum: 2026-03-20
---
```

### 4.2 — Voortbouwend artefact

```yaml
---
herkomstcode: 2603.Tu9x
herkomstpositie: voortbouwend
initierend_artefact: <pad naar initierend artefact>
gegenereerd_door: <agent-id>
datum: 2026-03-20
---
```

### 4.3 — Integratie met Herkomst-sectie

De herkomstcode wordt opgenomen in de Herkomst-sectie zoals gedefinieerd in de handoff-doctrine (sectie 7):

```markdown
## Herkomst

- Herkomstcode: 2603.Tu9x
- Herkomstpositie: voortbouwend
- Initierend artefact: agent-execution/2603.Tu9x.concept-curator.definieer-concept.md
- Gegenereerd door: concept-curator
- Agent charter: @main:agent-charters/concept-curator.charter.md
- Datum: 2026-03-20
- Handoff-referentie: hf-2603.0001
```

---

## 5. Relatie tot handoff-discipline

### 5.1 — Complementariteit

| Aspect | Handoff-discipline | Traceability-discipline |
|--------|-------------------|------------------------|
| **ID-type** | handoff-id | herkomstcode |
| **Scope** | Eén overdracht | Volledige artefact-keten |
| **Richting** | Horizontaal (agent → agent) | Verticaal (initierend → voortbouwend) |
| **Doel** | Legitimiteit van handeling | Herleidbaarheid van oorsprong |

### 5.2 — Samenwerking

Een artefact kan zowel een **handoff-id** als een **herkomstcode** bevatten:

- **handoff-id**: Identificeert de specifieke overdracht die tot dit artefact leidde
- **herkomstcode**: Identificeert de oorsprong van de keten waar dit artefact deel van uitmaakt

Beide zijn complementair en verplicht bij agent-geproduceerde artefacten.

### 5.3 — Voorbeeld keten

```
┌────────────────────────────────────────────────────────────────┐
│  Initierend artefact                                          │
│  herkomstcode: 2603.Tu9x (GEGENEREERD)                        │
│  handoff-id: hf-2603.0001                                     │
│  bestand: concept-curator.definieer-concept.md                │
└────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌────────────────────────────────────────────────────────────────┐
│  Voortbouwend artefact                                        │
│  herkomstcode: 2603.Tu9x (GEËRFD)                             │
│  handoff-id: hf-2603.0002                                     │
│  bestand: concept-definitie-agentic-ai.md                     │
└────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌────────────────────────────────────────────────────────────────┐
│  Voortbouwend artefact                                        │
│  herkomstcode: 2603.Tu9x (GEËRFD)                             │
│  handoff-id: hf-2603.0003                                     │
│  bestand: mandarin-domeinconcepten.md (update)                │
└────────────────────────────────────────────────────────────────┘
```

---

## 6. Execution-identiteit en koppelmechanisme

### 6.1 — Verplichte execution-identiteit

Een **execution-bestand** is identificeerbaar via minimaal de volgende velden:

- `execution_id`
- `execution_code`
- `execution_digest`
- `agent`
- `intent`
- `timestamp`
- `value_stream_fase`
- `bronhouding`
- `modus`

Deze velden vormen samen de minimale execution-identiteit.

### 6.2 — Onderscheid tussen `execution_id` en `execution_code`

Binnen deze doctrine worden twee verwante maar niet identieke sleutels onderscheiden:

| Veld | Betekenis | Formaat | Gebruik |
|------|-----------|---------|---------|
| `execution_id` | compacte technische kern-id | `JJMM.XXXX` | interne koppeling, sortering, afleiding |
| `execution_code` | canonieke externe execution-identiteit | `exec-JJMM.XXXX` | bestandsverwijzing, bundelnaam, handoff-verwijzing |

**Norm**:
- `execution_code` wordt afgeleid uit `execution_id` via de vaste prefix `exec-`;
- de execution-bundel gebruikt **niet** de kale `execution_id` als mapnaam;
- externe verwijzingen tussen execution-bestand, handoff-bestand en trace-bestand gebruiken `execution_code`.

### 6.3 — Rol van execution_digest

Het **execution_digest** is een stabiel traceerbaarheidsanker binnen de bredere herkomstidentiteit van de executie. Het wordt gebruikt voor:

- koppeling tussen execution-bestand en execution-trace-bestand;
- audit en kruisverwijzing;
- verwijzing vanuit voortbouwende artefacten;
- controle dat tracegegevens bij de juiste technische uitvoering horen.

Het execution_digest vervangt de herkomstcode niet. De herkomstcode identificeert de plaats van de executie in de artefactketen; het execution_digest identificeert de technische uitvoering waarop die ketenverwijzing betrekking heeft.

### 6.4 — Locatieconventie voor execution-bundels

De workspace-doctrine kan een **execution-bundel** voorschrijven als primaire runtime-opslagvorm.

In dat geval geldt de volgende conventie:

```text
executions/
└── {execution_code}.{agent}.{intent}/
  ├── execution.md
  └── trace/execution-trace.yaml
```

De mapnaam is de primaire filesystem-identiteit van de uitvoering. Het execution-bestand en het execution-trace-bestand blijven daarin zelfstandige artefacten met eigen rollen.

### 6.5 — Modus

Elke execution legt expliciet de modus vast:

- `handmatig`
- `tool-ondersteund`

De modus beïnvloedt de eisen aan opnamevorm, compactheid en controleerbaarheid.

---

## 7. YAML-documentheader als verplicht traceerbaarheidsmechanisme

### 7.1 — Norm

Elk canoniek Mandarin-bestand heeft een YAML-frontmatter die overeenkomt met de entiteitsklasse van het bestand. De header is de fysieke drager van de traceerbaarheidsmetadata: zonder header zijn `herkomstcode`, `artefact-id` en `execution-id` niet machine-leesbaar aanwezig en is traceerbaarheid niet afdwingbaar.

De gezaghebbende headerstructuur per entiteitsklasse is vastgelegd in `templates/yaml-header.template.md`.

### 7.2 — Entiteitsklassen en verplichte traceability-velden

| Bestandspatroon | Entiteitsklasse | Verplichte traceability-velden |
|----------------|-----------------|-------------------------------|
| `*.charter.md`, `*agent-boundary*.md` | AGENT | `agent-id` |
| `*.agent.md` (contract) | INTENT | `intent-id`, `agent-id` |
| concept, rapport, datamodel, Gherkin, SQL | ARTEFACT | `artefact-id`, `herkomstcode`, `herkomstpositie`, `execution-id` |
| `*.template.md` | TEMPLATE | `template-id` |
| `*.prompt.md` | EXECUTION | `execution-id`, `execution-code` |
| `hf-*.md`, handoff-bestanden | HANDOFF | `handoff-id`, `van-execution` |

### 7.3 — Vrijgestelde bestanden

De volgende categorieën zijn vrijgesteld van de YAML-header-verplichting:

- Technische configuratiebestanden (`beleid-workspace.md` als workspace-config, `.github/`-configuratie)
- Tijdelijke werkbestanden in `temp/`
- `README.md` en overige documentatiebestanden zonder canonieke governance-status

### 7.4 — Verantwoordelijkheid

| Actie | Verantwoordelijke |
|-------|-------------------|
| Vullen van traceability-velden (`herkomstcode`, `artefact-id`, `execution-id`) | Runner |
| Vullen van overige velden (`versie`, `status`, `digest`) | Auteur / agent |
| Controle op aanwezigheid en correctheid van de header | Runner / Agent-curator |

---

## 8. Execution-trace-bestand

### 8.1 — Norm

Naast elk execution-bestand bestaat een apart **execution-trace-bestand**.

Het execution-trace-bestand:
- is een zelfstandig artefact;
- bevat `execution_id` en `execution_digest`;
- bevat bij voorkeur ook `execution_code`;
- bevat per opgenomen bron of segment herkomstinformatie;
- fungeert als audit- en linkdrager;
- laat het execution-bestand de uitvoeringsdrager blijven.

### 8.2 — Minimale koppeling

Een execution-trace-bestand is alleen geldig als `execution_id` en `execution_digest` exact verwijzen naar één bestaand execution-bestand.

Wanneer de workspace-doctrine een execution-bundel voorschrijft, geldt aanvullend:
- het execution-trace-bestand verwijst naar exact één execution-bundel;
- binnen die bundel verwijst het naar exact één primair execution-bestand;
- de aanwezigheid van een gedeelde bundelmap verandert niets aan de zelfstandigheid van het execution-trace-bestand als artefact.

### 8.3 — Per-bronmodel

Elke opgenomen of samengevatte bron bevat minimaal:

- `bronpad`
- `type`
- `digest` of `versie`
- `reden_van_opname`
- `opnamevorm`

Toegestane waarden voor `opnamevorm` zijn:

- `volledig`
- `fragment`
- `samenvatting`

### 8.4 — Segment-identificatie

Wanneer `opnamevorm = fragment`, wordt minimaal een heading-gebaseerde segment-identificatie vastgelegd.

Optioneel mogen aanvullend worden vastgelegd:

- `bereik`
- `sectie_id`
- andere canonieke segmentverwijzing

### 8.5 — Contextdruk en compressiegebeurtenissen

Wanneer een runner of platform informatie beschikbaar maakt over tokengebruik, contextdruk, truncatie, samenvatting of compressie, legt het execution-trace-bestand deze informatie expliciet vast als contextgebeurtenis.

Per contextgebeurtenis wordt minimaal vastgelegd:

- `event_type`
- `timestamp`
- `meetwijze`
- `bron`
- `detail`

Toegestane waarden voor `event_type` zijn minimaal:

- `preflight_warning`
- `context_loss_known`
- `context_loss_suspected`
- `compression_event`
- `token_measurement`

Toegestane waarden voor `meetwijze` zijn minimaal:

- `exact`
- `schatting`
- `onbekend`

Een runner registreert alleen `context_loss_known` wanneer het onderliggende platform of de runner zelf een hard signaal levert dat context daadwerkelijk is weggevallen of compact is gemaakt. In alle andere gevallen wordt uitsluitend een vermoeden of risico vastgelegd.

---

## 9. Normering voor compacte opname

### 9.1 — Handmatige modus

In `handmatig`e modus moet minimaal expliciet aanwezig zijn:

- de volledige execution-identiteit;
- de opdracht en parameters;
- de bronhouding;
- de expliciete lijst van opgenomen bronnen;
- de normatieve kerninhoud waarop de uitvoering direct steunt.

### 9.2 — Segment-opname

Grote bronnen mogen per segment worden opgenomen, mits:

- het segment expliciet identificeerbaar is;
- het segment inhoudelijk voldoende is voor de uitvoering;
- de opnamevorm in het execution-trace-bestand wordt vastgelegd.

### 9.3 — Samenvatting

Samenvatting is alleen toegestaan wanneer:

- de oorspronkelijke bron expliciet wordt genoemd;
- digest of versie van de bron wordt vastgelegd;
- de reden van samenvatting expliciet wordt verantwoord;
- de samenvatting de normatieve betekenis niet vervangt maar representeert.

### 9.4 — Verbod op stille weglating

Normatieve kerninhoud mag niet stilzwijgend worden weggelaten. Elke weglating of compactie die relevant is voor legitimiteit, interpretatie of besluitvorming moet expliciet traceerbaar zijn.

### 9.5 — Verbod op schijnnauwkeurige contextclaims

Tokengebruik of contextvulling mag alleen als exacte waarde worden vastgelegd wanneer die exactheid volgt uit de gebruikte meetbron.

Indien een waarde is afgeleid, geraamd of onvolledig waarneembaar, wordt zij als schatting of onbekend geregistreerd. Een execution-trace-bestand mag geen schijn van exacte volledigheid wekken.

---

## 10. Validatie en governance

### 10.1 — Verplichtingen

| Verplichting | Verantwoordelijke |
|--------------|-------------------|
| Vastleggen herkomstpositie in contract | Contract-auteur (agent-engineer) |
| Generatie herkomstcode | Runner |
| Overerving herkomstcode | Runner |
| Vastleggen execution-identiteit | Runner |
| Vullen YAML-traceability-velden in documentheader | Runner |
| Generatie execution-trace-bestand | Runner |
| Registratie contextgebeurtenissen en tokenmetingen | Runner |
| Validatie herkomstcode-formaat | Runner / Agent-curator |
| Validatie opnamevorm en segment-traceability | Runner / Agent-curator |
| Controle op aanwezigheid YAML-header | Agent-curator |
| Overzicht artefact-types | Ecosysteem-beschrijver |

### 10.2 — Validatieregels

Een herkomstcode is **geldig** als:

1. Het formaat `JJMM.XXXX` correct is
2. JJMM een geldige jaar-maand combinatie is
3. XXXX exact 4 alfanumerieke karakters bevat
4. Bij voortbouwende artefacten: het initierend artefact bestaat en dezelfde code bevat
5. Elk execution-bestand de verplichte velden van de execution-identiteit bevat
6. Elk canoniek Mandarin-bestand een YAML-header heeft conform `templates/yaml-header.template.md`
7. Elk execution-trace-bestand exact verwijst naar een bestaand execution-bestand via `execution_id` en `execution_digest`
8. Elke bronvermelding in een execution-trace-bestand de verplichte trace-velden bevat
9. Bij `opnamevorm = fragment` minimaal een heading-gebaseerde segment-identificatie aanwezig is
10. Elke geregistreerde contextgebeurtenis een geldig `event_type`, `meetwijze`, `timestamp` en bronverwijzing bevat
11. Geen contextmeting als exact wordt geregistreerd wanneer de meetwijze niet `exact` is

### 10.3 — Foutafhandeling

| Situatie | Actie |
|----------|-------|
| Herkomstcode ontbreekt | Artefact is ongeldig; runner moet code genereren of erven |
| Ongeldig formaat | Runner corrigeert of weigert verwerking |
| Initierend artefact niet gevonden | Escalatie naar menselijke validatie |
| Mismatch in keten | Audit-log entry; escalatie naar canon-curator |
| YAML-header ontbreekt | Bestand is onvolledig; header toevoegen vóór verdere verwerking |
| Execution-trace-bestand ontbreekt | Executie is onvolledig en niet volledig auditbaar |
| Ontbrekend execution_digest | Koppeling ongeldig; verwerking weigeren of corrigeren |
| Samenvatting zonder bronverwijzing | Ongeldige compacte opname; escalatie naar menselijke validatie |
| Contextverlies als exact gemeld zonder hard signaal | Ongeldige trace-claim; verlaag naar vermoeden of escalatie |
| Tokenmeting zonder label exact/schatting/onbekend | Trace-invoer onvolledig; runner weigert of corrigeert |

---

## 11. Scope-afbakening

### 11.1 — Wat valt onder deze doctrine

- Alle agent-geproduceerde artefacten
- Execution-files en hun output
- Execution-trace-bestanden
- Wijzigingen aan bestaande artefacten
- Governance-artefacten (doctrines, charters, contracten)

### 11.2 — Wat valt buiten deze doctrine

- Handmatig door mensen gecreëerde artefacten zonder agent-betrokkenheid
- Tijdelijke werk-artefacten (scratch files)
- Logs en audit-bestanden (hebben eigen traceerbaarheid)

---

## 12. Slotbepaling

Traceability is geen administratieve last,
maar een **architectonisch fundament**.

De herkomstcode maakt herleidbaarheid expliciet,
ketens navolgbaar
en oorsprong toetsbaar.

Een artefact zonder herkomstcode
is een artefact zonder verleden.

---

## Changelog

| Datum | Versie | Wijziging | Uitvoer door |
|---|---|---|---|
| 2026-04-21 | 1.8.0 | Toegevoegd: §8.5 contextdruk en compressiegebeurtenissen; §9.5 verbod op schijnnauwkeurige contextclaims; verplichtingen, validatieregels en foutafhandeling uitgebreid voor tokenmetingen en contextverlies | GitHub Copilot |
| 2026-04-15 | 1.7.0 | Classificatie toegevoegd; subsectiekoppen voorzien van em-dash; Wijzigingslog hernoemd naar Changelog | Hans Blok |
| 2026-04-13 | 1.6.0  | §7 toegevoegd: YAML-documentheader als verplicht traceerbaarheidsmechanisme; `templates/yaml-header.template.md` gepromoveerd als gezaghebbende bron; validatieregels en verplichtingentabel uitgebreid | Hans Blok |
| 2026-04-12 | 1.5.0  | Hernoemd: `execution_identificatie` → `execution_code` conform TDM; `initierend` → `initierend` als canonieke veldwaarde conform TDM | Hans Blok |
| 2026-04-08 | 1.4.0  | Verduidelijkt: onderscheid tussen `execution_id` en `execution_identificatie`; execution-bundel als runtime-locatieconventie; koppeling van trace-bestand aan bundel en primair execution-bestand | Constitutioneel Auteur |
| 2026-04-06 | 1.2.0  | Toegevoegd: execution-identiteit, execution-trace-bestand, verplichte trace-velden en normering voor compacte opname | Concept-curator |
| 2026-03-20 | 1.1.0  | Herkomstpositie als contract-eigenschap; runner-logica; rolverdeling uitgebreid | Constitutioneel Auteur |
| 2026-03-20 | 1.0.0  | Eerste versie: traceability-discipline, herkomstcode-conventie en integratie met handoff-doctrine | Constitutioneel Auteur |

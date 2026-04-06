---
type: doctrine
naam: Doctrine — Traceability en Herkomstcode
versie: 1.3.0
digest: 8d27
status: vers
---
# Doctrine — Traceability en Herkomstcode


---

## Herkomstverantwoording

Dit normatief artefact is opgesteld op basis van de volgende bronnen:

**Geraadpleegde bronnen**:
- mandarin-ecosysteem-ordeningsconcepten.md — concepten herkomstpositie, initiërend, voortbouwend (gelezen op 2026-03-20)
- doctrine-handoff.md (versie 1.0.0, gelezen op 2026-04-06)
- doctrine-agent-charter-normering.md — richtlijn herkomstpositie in contracten (versie 2.4.0, gelezen op 2026-03-20)
- mandarin-domeinconcepten.md — concepten bronpakket, execution-bestand (gelezen op 2026-04-06)
- 2f0b.concept-curator.definieer-concept.md — voorbeeld van een execution-bestand (gelezen op 2026-04-06)
- Gebruikersinvoer over herkomstcode-conventie (ontvangen op 2026-03-20)

**Opsteller**: Constitutioneel Auteur  
**Doel**: Expliciete normering van traceerbaarheid en herkomstcode-generatie binnen het Mandarin-ecosysteem

---

## 1. Doel en scope

Deze doctrine normeert de **traceerbaarheid** van artefacten binnen het Mandarin-ecosysteem door:

1. Een **herkomstcode** te definiëren die uniek identificeert waar een artefact-keten begint
2. Regels vast te leggen voor **generatie** (bij initiërende artefacten) en **overerving** (bij voortbouwende artefacten)
3. De relatie te expliciteren met de handoff-discipline

Traceability waarborgt dat elk artefact herleidbaar is naar zijn oorsprong, ongeacht hoeveel voortbouwende artefacten in de keten zijn ontstaan.

---

## 2. Herkomstcode

### 2.1 Definitie

Een **herkomstcode** is een unieke, door het systeem gegenereerde identificatiecode die de oorsprong van een artefact-keten markeert.

De herkomstcode:
- wordt uitsluitend gegenereerd door **initiërende** artefacten
- wordt overgenomen door alle **voortbouwende** artefacten in dezelfde keten
- is onveranderlijk na generatie
- fungeert als permanente referentie voor audit en traceerbaarheid

### 2.2 Conventie

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

### 2.3 Hash-generatie

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

### 2.4 Verantwoordelijkheid voor generatie

De **runner** is verantwoordelijk voor het genereren van de herkomstcode.

Dit sluit aan bij de handoff-doctrine:
- De runner genereert de handoff-id
- De runner genereert de herkomstcode (indien initiërend)
- Agents genereren **geen** herkomstcodes

---

## 3. Herkomstpositie en gedrag

### 3.1 Vastlegging in agent-contract

De **herkomstpositie** wordt vastgelegd als eigenschap van de output-specificatie in het **agent-contract**:

```yaml
# Voorbeeld: initiërend
intent: definieer-concept
output:
  - type: concept-definitie
    herkomstpositie: initiërend    # ← vastgelegd in contract
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

### 3.2 Runner-logica

De **runner** leest de herkomstpositie uit het contract en handelt dienovereenkomstig:

```
LEES contract.output.herkomstpositie

IF herkomstpositie == "initiërend":
    herkomstcode = genereer_nieuwe_code()
ELSE IF herkomstpositie == "voortbouwend":
    herkomstcode = input_artefact.herkomstcode
    initierend_artefact = input_artefact.pad
ELSE:
    FOUT: ongeldige herkomstpositie
```

### 3.3 Initiërend artefact

Een artefact met herkomstpositie **initiërend**:

| Actie | Beschrijving |
|-------|--------------|
| **Genereer** | Runner genereert nieuwe herkomstcode volgens conventie |
| **Vastleg** | Herkomstcode wordt opgenomen in artefact-header |
| **Publiceer** | Herkomstcode is beschikbaar voor voortbouwende artefacten |

**Wanneer is een artefact initiërend?**
- Eerste definitie van een nieuw concept, charter, contract of doctrine
- Start van een nieuwe taak-executie (execution-file)
- Creatie van een nieuw governance-artefact
- Elke situatie waarin geen eerder initiërend artefact in de keten bestaat

### 3.4 Voortbouwend artefact

Een artefact met herkomstpositie **voortbouwend**:

| Actie | Beschrijving |
|-------|--------------|
| **Erf** | Neem herkomstcode over van initiërend artefact |
| **Verwijs** | Refereer expliciet naar het initiërende artefact |
| **Propageer** | Verdere voortbouwende artefacten erven dezelfde code |

**Wanneer is een artefact voortbouwend?**
- Wijziging, update of correctie van een bestaand artefact
- Afgeleide output van een eerder geproduceerd artefact
- Vervolgstap in een lopende taak-executie
- Elke situatie waarin een initiërend artefact in de keten bestaat

---

## 4. Header-structuur

### 4.1 Initiërend artefact

```yaml
---
herkomstcode: 2603.Tu9x
herkomstpositie: initiërend
gegenereerd_door: <agent-id>
datum: 2026-03-20
---
```

### 4.2 Voortbouwend artefact

```yaml
---
herkomstcode: 2603.Tu9x
herkomstpositie: voortbouwend
initierend_artefact: <pad naar initiërend artefact>
gegenereerd_door: <agent-id>
datum: 2026-03-20
---
```

### 4.3 Integratie met Herkomst-sectie

De herkomstcode wordt opgenomen in de Herkomst-sectie zoals gedefinieerd in de handoff-doctrine (sectie 7):

```markdown
## Herkomst

- Herkomstcode: 2603.Tu9x
- Herkomstpositie: voortbouwend
- Initiërend artefact: agent-execution/2603.Tu9x.concept-curator.definieer-concept.md
- Gegenereerd door: concept-curator
- Agent charter: @main:agent-charters/concept-curator.charter.md
- Datum: 2026-03-20
- Handoff-referentie: hf-2603.0001
```

---

## 5. Relatie tot handoff-discipline

### 5.1 Complementariteit

| Aspect | Handoff-discipline | Traceability-discipline |
|--------|-------------------|------------------------|
| **ID-type** | handoff-id | herkomstcode |
| **Scope** | Eén overdracht | Volledige artefact-keten |
| **Richting** | Horizontaal (agent → agent) | Verticaal (initiërend → voortbouwend) |
| **Doel** | Legitimiteit van handeling | Herleidbaarheid van oorsprong |

### 5.2 Samenwerking

Een artefact kan zowel een **handoff-id** als een **herkomstcode** bevatten:

- **handoff-id**: Identificeert de specifieke overdracht die tot dit artefact leidde
- **herkomstcode**: Identificeert de oorsprong van de keten waar dit artefact deel van uitmaakt

Beide zijn complementair en verplicht bij agent-geproduceerde artefacten.

### 5.3 Voorbeeld keten

```
┌────────────────────────────────────────────────────────────────┐
│  Initiërend artefact                                          │
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

### 6.1 Verplichte execution-identiteit

Een **execution-bestand** is identificeerbaar via minimaal de volgende velden:

- `execution_id`
- `execution_digest`
- `agent`
- `intent`
- `timestamp`
- `value_stream_fase`
- `bronhouding`
- `modus`

Deze velden vormen samen de minimale execution-identiteit.

### 6.2 Rol van execution_digest

Het **execution_digest** is een stabiel traceerbaarheidsanker binnen de bredere herkomstidentiteit van de executie. Het wordt gebruikt voor:

- koppeling tussen execution-bestand en execution-trace-bestand;
- audit en kruisverwijzing;
- verwijzing vanuit voortbouwende artefacten;
- controle dat tracegegevens bij de juiste technische uitvoering horen.

Het execution_digest vervangt de herkomstcode niet. De herkomstcode identificeert de plaats van de executie in de artefactketen; het execution_digest identificeert de technische uitvoering waarop die ketenverwijzing betrekking heeft.

### 6.3 Modus

Elke execution legt expliciet de modus vast:

- `handmatig`
- `tool-ondersteund`

De modus beïnvloedt de eisen aan opnamevorm, compactheid en controleerbaarheid.

---

## 7. Execution-trace-bestand

### 7.1 Norm

Naast elk execution-bestand bestaat een apart **execution-trace-bestand**.

Het execution-trace-bestand:
- is een zelfstandig artefact;
- bevat `execution_id` en `execution_digest`;
- bevat per opgenomen bron of segment herkomstinformatie;
- fungeert als audit- en linkdrager;
- laat het execution-bestand de uitvoeringsdrager blijven.

### 7.2 Minimale koppeling

Een execution-trace-bestand is alleen geldig als `execution_id` en `execution_digest` exact verwijzen naar één bestaand execution-bestand.

### 7.3 Per-bronmodel

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

### 7.4 Segment-identificatie

Wanneer `opnamevorm = fragment`, wordt minimaal een heading-gebaseerde segment-identificatie vastgelegd.

Optioneel mogen aanvullend worden vastgelegd:

- `bereik`
- `sectie_id`
- andere canonieke segmentverwijzing

---

## 8. Normering voor compacte opname

### 8.1 Handmatige modus

In `handmatig`e modus moet minimaal expliciet aanwezig zijn:

- de volledige execution-identiteit;
- de opdracht en parameters;
- de bronhouding;
- de expliciete lijst van opgenomen bronnen;
- de normatieve kerninhoud waarop de uitvoering direct steunt.

### 8.2 Segment-opname

Grote bronnen mogen per segment worden opgenomen, mits:

- het segment expliciet identificeerbaar is;
- het segment inhoudelijk voldoende is voor de uitvoering;
- de opnamevorm in het execution-trace-bestand wordt vastgelegd.

### 8.3 Samenvatting

Samenvatting is alleen toegestaan wanneer:

- de oorspronkelijke bron expliciet wordt genoemd;
- digest of versie van de bron wordt vastgelegd;
- de reden van samenvatting expliciet wordt verantwoord;
- de samenvatting de normatieve betekenis niet vervangt maar representeert.

### 8.4 Verbod op stille weglating

Normatieve kerninhoud mag niet stilzwijgend worden weggelaten. Elke weglating of compactie die relevant is voor legitimiteit, interpretatie of besluitvorming moet expliciet traceerbaar zijn.

---

## 9. Validatie en governance

### 9.1 Verplichtingen

| Verplichting | Verantwoordelijke |
|--------------|-------------------|
| Vastleggen herkomstpositie in contract | Contract-auteur (agent-engineer) |
| Generatie herkomstcode | Runner |
| Overerving herkomstcode | Runner |
| Vastleggen execution-identiteit | Runner |
| Generatie execution-trace-bestand | Runner |
| Validatie herkomstcode-formaat | Runner / Agent-curator |
| Validatie opnamevorm en segment-traceability | Runner / Agent-curator |
| Controle op aanwezigheid | Agent-curator |
| Overzicht artefact-types | Ecosysteem-beschrijver |

### 9.2 Validatieregels

Een herkomstcode is **geldig** als:

1. Het formaat `JJMM.XXXX` correct is
2. JJMM een geldige jaar-maand combinatie is
3. XXXX exact 4 alfanumerieke karakters bevat
4. Bij voortbouwende artefacten: het initiërend artefact bestaat en dezelfde code bevat
5. Elk execution-bestand de verplichte velden van de execution-identiteit bevat
6. Elk execution-trace-bestand exact verwijst naar een bestaand execution-bestand via `execution_id` en `execution_digest`
7. Elke bronvermelding in een execution-trace-bestand de verplichte trace-velden bevat
8. Bij `opnamevorm = fragment` minimaal een heading-gebaseerde segment-identificatie aanwezig is

### 9.3 Foutafhandeling

| Situatie | Actie |
|----------|-------|
| Herkomstcode ontbreekt | Artefact is ongeldig; runner moet code genereren of erven |
| Ongeldig formaat | Runner corrigeert of weigert verwerking |
| Initiërend artefact niet gevonden | Escalatie naar menselijke validatie |
| Mismatch in keten | Audit-log entry; escalatie naar canon-curator |
| Execution-trace-bestand ontbreekt | Executie is onvolledig en niet volledig auditbaar |
| Ontbrekend execution_digest | Koppeling ongeldig; verwerking weigeren of corrigeren |
| Samenvatting zonder bronverwijzing | Ongeldige compacte opname; escalatie naar menselijke validatie |

---

## 10. Scope-afbakening

### 10.1 Wat valt onder deze doctrine

- Alle agent-geproduceerde artefacten
- Execution-files en hun output
- Execution-trace-bestanden
- Wijzigingen aan bestaande artefacten
- Governance-artefacten (doctrines, charters, contracten)

### 10.2 Wat valt buiten deze doctrine

- Handmatig door mensen gecreëerde artefacten zonder agent-betrokkenheid
- Tijdelijke werk-artefacten (scratch files)
- Logs en audit-bestanden (hebben eigen traceerbaarheid)

---

## 11. Slotbepaling

Traceability is geen administratieve last,
maar een **architectonisch fundament**.

De herkomstcode maakt herleidbaarheid expliciet,
ketens navolgbaar
en oorsprong toetsbaar.

Een artefact zonder herkomstcode
is een artefact zonder verleden.

---

## Wijzigingslog

| Datum      | Versie | Wijziging                                                           | Auteur            |
|------------|--------|---------------------------------------------------------------------|-------------------|
| 2026-04-06 | 1.2.0  | Toegevoegd: execution-identiteit, execution-trace-bestand, verplichte trace-velden en normering voor compacte opname | Concept-curator |
| 2026-03-20 | 1.1.0  | Herkomstpositie als contract-eigenschap; runner-logica; rolverdeling uitgebreid | Constitutioneel Auteur |
| 2026-03-20 | 1.0.0  | Eerste versie: traceability-discipline, herkomstcode-conventie en integratie met handoff-doctrine | Constitutioneel Auteur |

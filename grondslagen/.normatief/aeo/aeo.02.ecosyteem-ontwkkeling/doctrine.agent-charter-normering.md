---
type: doctrine
naam: Doctrine — Agent Charter Normering
code: DACN
versie: 2.5.0
value-stream: aeo
digest: tbd0
status: vers
---
# Doctrine — Agent Charter Normering

---

## Herkomstverantwoording

Dit normatief artefact is opgesteld op basis van de volgende bronnen:

**Geraadpleegde bronnen**:
- `mandarin-ecosysteem-ordeningsconcepten.md` — vier orthogonale classificatie-assen, betekeniseffect, vormingsfase, werking, bronhouding (versie 1.9.0, gelezen op 2026-03-01)
- `mandarin-domeinconcepten.md` — concepten agent-charter, capability boundary, agent-identiteit (versie 2.13.0, gelezen op 2026-03-01)
- `doctrine.traceability.md` — richtlijn herkomstpositie in agent-contracten (versie 2.4.0, gelezen op 2026-03-20)
- `constitutie.md` — gezagshiërarchie en architectonische bevoegdheden (versie 2.6.0, gelezen op 2026-03-01)

**Opsteller**: Constitutioneel Auteur  
**Doel**: Normering van het ontwerpdenken voor agent-charters door gemeenschappelijke architectuurprincipes voor identiteit, verantwoordelijkheid en ecosysteem-integratie vast te leggen

---

## Classificatie

Deze doctrine positioneert zich als volgt op de vier orthogonale assen:

| Betekeniseffect | Vormingsfase | Werking | Bronhouding |
|---|---|---|---|
| normerend | ordening / vastlegging | inhoudelijk | canon-gebonden |

- **Betekeniseffect** — *normerend*: normeert het ontwerpdenken voor agent-charters door expliciete principes te verankeren
- **Vormingsfase** — *ordening / vastlegging*: structureert en formaliseert de architectonische principes voor het agent-ecosysteem
- **Werking** — *inhoudelijk*: bepaalt inhoud en structuur van charters, niet alleen randvoorwaarden
- **Bronhouding** — *canon-gebonden*: baseert zich expliciet op de Mandarin-canon en is herleidbaar naar canonieke bronnen

---

## 1. Doel en scope

Deze doctrine beschrijft **hoe het agent-ecosysteem zichzelf ordent** door gemeenschappelijke ontwerpprincipes voor agent-charters.

Zij stelt kaders voor:

- de architectuur van agent-identiteit;
- de relatie tussen verantwoordelijkheid en transparantie;
- de evolutie van het agent-ecosysteem;
- de integriteit van samenwerking tussen agents.

Zij borgt dat:

- elke agent een expliciete en scherpe identiteit heeft;
- charters evolutie mogelijk maken zonder het ecosysteem te breken;
- transparante verantwoording een constitutieve eigenschap is van elke agent.

**Buiten scope**:
- Normering van individuele agent-implementaties
- Specifieke charter-inhoud per agent (dit is per agent bepaald)
- Technische uitvoering van agent-gedrag

Deze doctrine normeert niet individuele agents, maar **het ontwerpdenken dat alle agent-charters ondersteunt**.

---

## 2. Capability boundary

Deze doctrine normeert het **ontwerpdenken voor agent-charters** door principes van expliciete identiteit, evolutionaire integriteit en transparante verantwoording te verankeren, zonder specifieke agent-gedragingen voor te schrijven.

---

## 3. Kernprincipes

### 3.1 — Identiteit vóór Implementatie

Een agent-charter begint bij **expliciete identiteit**: wat de agent WEL is en wat hij NIET is.

Identiteit manifesteert zich in:

- een scherpe capability boundary;
- een extern observeerbaar contract;
- een consistente verantwoordelijkheid.

De ontwerprichting is:

> identiteit → contract → charter → realisatie

Een agent-charter legitimeert wat het ecosysteem van de agent mag verwachten.

### 3.2 — Eenduidige Verantwoordelijkheid

Elke agent heeft **één expliciete verantwoordelijkheid**.

Verantwoordelijkheid kenmerkt zich door:

- scherpte: in één zin uit te leggen;
- volledigheid: wat WEL en wat NIET;
- duurzaamheid: onafhankelijk van implementatie.

Een agent zonder expliciete verantwoordelijkheid compromitteert het ecosysteem.

### 3.3 — Charter als Ecosysteem-Integrator

Het charter integreert de agent in het ecosysteem door:

- identiteit te formaliseren;
- samenwerking te reguleren;
- evolutie mogelijk te maken.

Het charter volgt uit identiteit en contract. Het charter mag geen verantwoordelijkheid introduceren die niet extern observeerbaar is.

### 3.4 — Scheiding van Wat en Hoe

- Contract = extern observeerbaar gedrag
- Charter = ecosysteem-legitimatie
- Implementatie = technische realisatie

Verandering in implementatie mag nooit identiteit of contract compromitteren.

### 3.5 — Evolutionaire Integriteit

Agents evolueren **zonder het ecosysteem te breken**.

Evolutie respecteert:

- **Contractstabiliteit**: bestaande verwachtingen blijven geldig;
- **Identiteitscoherentie**: de kern-verantwoordelijkheid blijft herkenbaar;
- **Transparante wijziging**: veranderingen zijn traceerbaar en begrijpelijk.

Evolutie gebeurt via semantische versioning conform conventie.

### 3.6 — Ecosysteem-Cohesie

Fundamentele wijzigingen vereisen **ecosysteem-brede herbeoordeling**.

Identiteitswijziging vraagt om:

- expliciete impactanalyse op samenwerking;
- herbeoordeling van afhankelijke agents;
- transparantie naar het gehele ecosysteem.

Identiteitswijziging zonder ecosysteem-herbeoordeling compromitteert de integriteit.

### 3.7 — Transparante Verantwoording

Elke agent is **verantwoordelijk voor zijn handelen** naar het ecosysteem toe.

Transparante verantwoording betekent:

- traceerbaarheid van beslissingen;
- observeerbaarheid van effecten;
- reproduceerbaarheid van resultaten.

Transparantie is een **constitutieve eigenschap** van agent-identiteit, geen optionele functionaliteit. Een agent die zijn handelen niet transparant kan verantwoorden, handelt buiten zijn charter.

### 3.8 — Architectonische Flexibiliteit

Het agent-ecosysteem is **evolueerbaar door ontwerp**.

Agents kunnen:

- hun identiteit verfijnen;
- hun verantwoordelijkheid herdefiniëren;
- hun samenwerking aanpassen.

Maar alleen binnen de kaders van:

- expliciete identiteitsherdefinitie;
- transparante ecosysteem-communicatie;
- architectonische coherentie.

### 3.9 — Output-formaat Normering voor Inhoudelijke Agents

Agents die op de as **Werking de positie "Inhoudelijk"** hebben, leveren altijd een bestand als primair artefact.

Omdat deze agents betekenis begrijpen en vastleggen:

- Het **default formaat is Markdown**, tenzij expliciet anders gevraagd in de prompt;
- Alternatieve formaten (zoals YAML) worden alleen toegepast wanneer expliciet aangevraagd;
- De keuze voor het formaat wordt gedocumenteerd in de output.

---

## 4. Richtlijnen

### 4.1 — Template-gebruik

Alle agents die artefacten genereren op basis van templates:

- MOETEN het template-bestand expliciet lezen uit de workspace;
- MOGEN NIET vertrouwen op eerdere kennis van template-structuur;
- MOETEN template-pad en versie loggen in audit.

### 4.2 — Bronhouding

Een agent heeft altijd precies één bronhouding. Het is niet toegestaan dat een agent intents heeft met verschillende bronhoudingen.

De bronhouding bepaalt de epistemische discipline en herleidbaarheid van alle output van de agent. Consistentie in bronhouding voorkomt verwarring, verhoogt traceerbaarheid en borgt de architectonische integriteit van het ecosysteem.

Een agent die canon-gebonden is, mag geen intent hebben die exploratief of input-gebonden is. Alle intents van een agent delen dezelfde bronhouding.

### 4.3 — Herkomstpositie in agent-contracten

Elk agent-contract specificeert voor elke output de **herkomstpositie** als verplichte eigenschap. Dit bepaalt of het geproduceerde artefact een nieuwe keten initieert of voortbouwt op een bestaand artefact.

**Contract-structuur:**

```yaml
intent: <intent-naam>
output:
  - type: <artefact-type>
    herkomstpositie: initierend | voortbouwend
    template: <template-pad>
```

| Waarde | Betekenis | Runner-gedrag |
|--------|-----------|---------------|
| `initierend` | Output start een nieuwe artefact-keten | Runner genereert nieuwe herkomstcode |
| `voortbouwend` | Output bouwt voort op bestaand artefact | Runner erft herkomstcode van input-artefact |

Zie `doctrine.traceability.md` voor de volledige normering van herkomstcodes.

---

## 5. Architectonische discipline

De creatie van een agent-charter volgt een architectonische discipline:

1. **Identiteit articuleren** — Wat is de unieke verantwoordelijkheid?
2. **Grenzen expliciteren** — Wat wel en niet?
3. **Contract formuleren** — Hoe observeerbaar?
4. **Charter afleiden** — Hoe geïntegreerd in het ecosysteem?
5. **Evolutie faciliteren** — Hoe duurzaam veranderbaar?

---

## 6. Reikwijdte en grenzen

Deze doctrine:

- **Richt** het ontwerpdenken voor agent-charters;
- **Normeert** geen specifieke agent-implementaties;
- **Faciliteert** ecosysteem-coherentie zonder rigiditeit;
- **Ondersteunt** evolutie zonder chaos.

Deze doctrine vervangt geen individuele charter, maar **ondersteunt hun architectonische integriteit**.

---

## 7. Relatie tot andere doctrines

| Doctrine | Relatie |
|---|---|
| `doctrine.intent-naming.md` | Normeert de naming van agent-intents; charters definiëren intents volgens deze conventie |
| `doctrine.traceability.md` | Bepaalt herkomstpositie in agent-contracten; runners genereren herkomstcodes conform deze doctrine |
| `doctrine.bronhouding-en-exploratie.md` | Charters leggen bronhouding vast; één bronhouding per agent is verplicht |
| `doctrine.templategebruik.md` | Charters verwijzen naar templates; templategebruik is verplicht conform deze doctrine |

---

## Changelog

| Datum | Versie | Wijziging | Uitvoer door |
|---|---|---|---|
| 2026-04-15 | 2.5.0 | Herkomstverantwoording toegevoegd; naam gecorrigeerd naar `Doctrine —`; value-stream gecorrigeerd naar lowercase `aeo`; Classificatie herschreven conform standaard tabel; Richtlijnen genummerd als §4; Gerelateerde Doctrines hernoemd naar §7 Relatie tot andere doctrines met standaard tabel; Canonieke essentie verwijderd | Hans Blok |
| 2026-03-20 | 2.4.0 | Richtlijn herkomstpositie in agent-contracten toegevoegd; verwijzing naar doctrine-traceability.md | Constitutioneel Auteur |
| 2026-03-01 | 2.3.0 | Classificatie volledig volgens vier assen uit canon, richtlijn één bronhouding per agent toegevoegd | Constitutioneel Auteur |
| 2026-02-21 | 2.2.0 | Classificatie en Principe 9 herschreven conform de 4 nieuwe orthogonale assen | Constitutioneel Auteur |
| 2026-02-13 | 2.1.0 | Principe 9 toegevoegd: output-formaat normering voor inhoudelijke agents | — |
| 2026-02-12 | 2.0.0 | Fundamentele herziening: focus op ecosysteem-architectuur en -integriteit | — |
| YYYY-MM-DD | 1.1.0 | Transparantie- en logplicht expliciet toegevoegd als kernprincipe | — |
| YYYY-MM-DD | 1.0.0 | Initiële doctrine met nadruk op Prompt First en versie-discipline | — |

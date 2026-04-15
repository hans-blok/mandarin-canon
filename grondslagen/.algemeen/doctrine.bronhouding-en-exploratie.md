---
type: doctrine
naam: Doctrine — Bronhouding en Exploratie
versie: 1.1.0
digest: tbd0
status: vers
---
# Doctrine — Bronhouding en Exploratie

---

## Herkomstverantwoording

Dit normatief artefact is opgesteld op basis van de volgende bronnen:

**Geraadpleegde bronnen**:
- `mandarin-domeinconcepten.md` — concepten bronhouding, gesloten bronhouding, exploratieve bronhouding, werkbronnen, kaderbronnen (versie 2.13.0, gelezen op 2026-04-14)
- `mandarin-ecosysteem-ordeningsconcepten.md` — as Bronhouding: canon-gebonden, input-gebonden, exploratief (versie 1.9.0, gelezen op 2026-04-14)
- `constitutie.md` — normatief kader voor kennisgebruik en herleidbaarheid van output (versie 2.6.0, gelezen op 2026-04-14)

**Opsteller**: Hans Blok  
**Doel**: Normering van hoe agents omgaan met bronnen, kennis en onzekerheid, en onder welke condities exploratieve bronhouding is toegestaan

---

## Classificatie

Deze doctrine positioneert zich als volgt op de vier orthogonale assen:

| Betekeniseffect | Vormingsfase | Werking | Bronhouding |
|---|---|---|---|
| normerend | ordening / vastlegging | conditioneel | canon-gebonden |

- **Betekeniseffect** — *normerend*: normeert hoe agents omgaan met bronnen en kennis
- **Vormingsfase** — *ordening / vastlegging*: structureert en formaliseert de bronhouding als fundamentele epistemische discipline
- **Werking** — *conditioneel*: bepaalt onder welke condities welke bronhouding geldt
- **Bronhouding** — *canon-gebonden*: baseert zich uitsluitend op canonieke bronnen

---

## 1. Doel en scope

Deze doctrine beschrijft hoe agents binnen het Mandarin-ecosysteem omgaan met bronnen, kennis en onzekerheid.

Zij borgt dat:

- alle output herleidbaar is tot expliciete bronnen;
- het gebruik van externe kennis gecontroleerd en reproduceerbaar blijft;
- innovatie mogelijk is zonder verlies van canonische consistentie.

**Buiten scope**:
- Technische implementatie van bronnenopslag of retrieval
- Validatie van afzonderlijke bronnen (dit is een runner-verantwoordelijkheid)
- Versie- en conflictbeheer van bronnen

---

## 2. Kernprincipe

Agents werken op basis van een expliciete **bronhouding**.

De bronhouding bepaalt:

- welke bronnen worden gebruikt;
- hoe deze worden geïnterpreteerd;
- in welke mate externe kennis is toegestaan.

---

## 3. Typen bronhouding

Binnen Mandarin worden twee bronhoudingen onderscheiden:

1. **Gesloten bronhouding** (standaard)
2. **Exploratieve bronhouding** (uitzondering)

---

## 4. Gesloten bronhouding

### 4.1 — Definitie

De gesloten bronhouding is de standaard binnen het ecosysteem.

Agents baseren zich uitsluitend op:

- **kaderbronnen** (grondslagen en kaderdefinities)
- **werkbronnen** (object van bewerking)
- **referentiebronnen** (voor consistentie)

### 4.2 — Norm

Agents:

- gebruiken alleen expliciet aangeleverde bronnen;
- introduceren geen impliciete modelkennis;
- gebruiken het LLM uitsluitend als inferentie- en transformatie-mechanisme;
- maken alle output herleidbaar tot gebruikte bronnen.

### 4.3 — Doel

De gesloten bronhouding borgt:

- reproduceerbaarheid;
- consistentie;
- controleerbaarheid;
- expliciete herleidbaarheid van beslissingen.

---

## 5. Rol van het LLM

Binnen alle bronhoudingen geldt:

- het LLM is geen bron van kennis;
- het LLM wordt uitsluitend gebruikt voor:
  - herschrijven;
  - structureren;
  - combineren van informatie;
  - formuleren van output.

Het LLM bepaalt niet wat waar is, maar hoe iets wordt verwoord.

---

## 6. Exploratieve bronhouding

### 6.1 — Definitie

De exploratieve bronhouding is een expliciete afwijking van de gesloten bronhouding.

Deze wordt uitsluitend toegepast voor het **verkennen van nieuwe denkkaders en het stimuleren van innovatie**.

### 6.2 — Toepassing

Exploratieve bronhouding is toegestaan wanneer:

- het domein of probleem onvoldoende begrepen is;
- bestaande grondslagen tekortschieten;
- nieuwe kaders, theorieën of modellen moeten worden ontdekt;
- expliciet wordt ingezet op innovatie of alternatieve benaderingen.

### 6.3 — Gedrag

In exploratieve bronhouding mag een agent:

- gebruik maken van algemene modelkennis;
- externe theorieën en concepten verkennen;
- alternatieve benaderingen voorstellen;
- hypothesen formuleren.

De agent maakt expliciet onderscheid tussen:

- bestaande grondslagen;
- interpretaties;
- hypothesen;
- externe invloeden.

### 6.4 — Beperkingen

Exploratieve output:

- heeft geen normatief karakter;
- wordt niet direct gebruikt in productie;
- wordt niet gebruikt voor besluitvorming;
- wordt altijd beschouwd als voorstel of verkenning.

---

## 7. Overgang naar canon

Resultaten uit exploratie worden pas onderdeel van het ecosysteem na:

1. selectie (door mens of curator);
2. interpretatie en afbakening;
3. vastlegging als **kaderdefinitie**;
4. opname in de grondslagen.

Pas daarna mogen agents deze gebruiken binnen gesloten bronhouding.

---

## 8. Input-gebonden bronhouding en voorbeelden

### 8.1 — Kernregel

Wanneer de bronhouding input-gebonden is, geldt een expliciete negatieve instructie:

> **Illustraties en voorbeelden in beleidsdocumenten mogen nooit als declaratieve input worden geïnterpreteerd.**

### 8.2 — Toelichting

Beleidsdocumenten bevatten regelmatig voorbeelden ter verduidelijking. Deze voorbeelden zijn **illustratief**, niet **normatief**. Het onderscheid is cruciaal:

- een **voorbeeld** toont hoe iets *kan* worden toegepast;
- een **declaratie** stelt vast wat *geldt*.

Agents die dit onderscheid niet maken, lopen het risico illustraties te behandelen als feiten, definities of instructies. Dit is een **kernkwetsbaarheid** binnen input-gebonden verwerking.

### 8.3 — Norm

Agents:

- behandelen voorbeelden in bronnen uitsluitend als illustratie;
- leiden geen definities, regels of constraints af uit voorbeelden;
- baseren output uitsluitend op expliciete declaraties in de bron;
- markeren elk gebruik van voorbeeldmateriaal als niet-normatief.

---

## 9. Samenvattende principes

> De waarheid zit in expliciete bronnen, niet in het model.

> Agents werken standaard binnen gesloten bronregime.

> Voorbeelden zijn illustraties, geen declaraties.

> Exploratie is toegestaan als gecontroleerde uitzondering voor innovatie.

> Nieuwe kennis wordt pas onderdeel van het ecosysteem na canonisering.

> Het LLM ondersteunt formulering, maar bepaalt geen inhoudelijke waarheid.

---

## 10. Relatie tot andere doctrines

| Doctrine | Relatie |
|---|---|
| `doctrine.retrieval-en-contextselectie.md` | Retrieval opereert onder de gesloten bronhouding; context is de werkbron |
| `doctrine.agent-charter-normering.md` | Charters leggen de bronhouding per agent vast; één bronhouding per agent is verplicht |
| `doctrine.traceability.md` | Herleidbaarheid vereist expliciete bronverwijzingen in execution-trace-bestanden |

---

## Changelog

| Datum | Versie | Wijziging | Uitvoer door |
|---|---|---|---|
| 2026-04-15 | 1.1.0 | Herkomstverantwoording toegevoegd; Classificatie toegevoegd; naam gecorrigeerd naar `Doctrine — Bronhouding en Exploratie`; `---` dividers toegevoegd; subsectiekoppen voorzien van em-dash; §8 Input-gebonden bronhouding verplaatst; §10 Relatie tot andere doctrines en Changelog toegevoegd | Hans Blok |
| onbekend | 1.0.0 | Initiële versie | onbekend |

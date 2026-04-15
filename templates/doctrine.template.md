---
template-id: "003"
template-naam: Doctrine Template — Mandarin Doctrines
artefact-type-id: ""
agent-id: ""
versie: 1.0.0
status: vers
digest: tbd0
---
# Doctrine Template — Mandarin Doctrines

Gebruik dit template voor elke nieuwe doctrine in het Mandarin-ecosysteem.
Vervang alle `[PLACEHOLDER]`-velden. Verwijder deze instructieregel bij gebruik.

---

## Routering

| Bestandsnaampatroon | Entiteitsklasse | Template-sectie |
|---|---|---|
| `doctrine-*.md` | ARTEFACT (type: doctrine) | Dit template |

---

## Template

```markdown
---
type: doctrine
naam: Doctrine — [Naam van de doctrine]
versie: 1.0.0
value-stream: [aeo | fnd | sfw | aod | knv | miv]   # optioneel
digest: tbd0
status: vers
---
# Doctrine — [Naam van de doctrine]

---

## Herkomstverantwoording

Dit normatief artefact is opgesteld op basis van de volgende bronnen:

**Geraadpleegde bronnen**:
- `[brondocument].md` — [welke secties / concepten] ([versie], gelezen op [datum])
- `[brondocument].md` — [welke secties / concepten] ([versie], gelezen op [datum])

**Opsteller**: [Naam]  
**Doel**: [Één zin: wat normeert deze doctrine en waarom]

---

## Classificatie

Deze doctrine positioneert zich als volgt op de vier orthogonale assen:

| Betekeniseffect | Vormingsfase | Werking | Bronhouding |
|---|---|---|---|
| [normerend \| beschrijvend \| evaluerend] | [ordening / vastlegging \| uitvoering] | [inhoudelijk \| conditioneel \| procedureel] | [canon-gebonden \| input-gebonden \| exploratief] |

- **Betekeniseffect** — *[waarde]*: [één zin toelichting]
- **Vormingsfase** — *[waarde]*: [één zin toelichting]
- **Werking** — *[waarde]*: [één zin toelichting]
- **Bronhouding** — *[waarde]*: [één zin toelichting]

---

## 1. Doel en scope

[Één à twee alinea's: wat normeert deze doctrine, voor wie en waarom.]

Zij borgt dat:

- [borging 1];
- [borging 2];
- [borging 3].

**Buiten scope**:
- [wat valt expliciet buiten deze doctrine]
- [wat valt expliciet buiten deze doctrine]

---

## 2. [Kernbegrip of kernprincipe]

[Definitie of verklaring van het centrale begrip of principe.]

### 2.1 — [Subbegrip of subprincipe]

[Toelichting]

### 2.2 — [Subbegrip of subprincipe]

[Toelichting]

---

## 3. [Volgende onderwerp]

[Inhoud. Gebruik `###`-koppen voor subsecties. Gebruik `---` na elke `##`-sectie.]

---

## [N]. Relatie tot andere doctrines

| Doctrine | Relatie |
|---|---|
| `doctrine-[naam].md` | [Hoe deze doctrine aansluit of aanvult] |
| `doctrine-[naam].md` | [Hoe deze doctrine aansluit of aanvult] |

---

## Changelog

| Datum | Versie | Wijziging | Uitvoer door |
|---|---|---|---|
| [JJJJ-MM-DD] | 1.0.0 | Initiële versie | [Naam] |
```

---

## Richtlijnen

### Structuur
- Elke `##`-sectie wordt voorafgegaan én gevolgd door een `---`-scheidingslijn.
- Subsecties gebruiken `###`-koppen met het formaat `### N.M — [Naam]`.
- Gebruik nooit `####` of dieper — herstructureer bij te veel nesting.

### YAML-frontmatter
- `type` is altijd `doctrine`
- `naam` is altijd `Doctrine — [naam]` (met hoofdletter en em-dash)
- `versie` volgt semver; start op `1.0.0`
- `digest` staat op `tbd0` tot berekend door de runner
- `value-stream` is optioneel; gebruik alleen als de doctrine specifiek voor één value stream geldt

### Herkomstverantwoording
- Verplicht voor elke doctrine
- Noem altijd welke secties of concepten uit een brondocument zijn geraadpleegd
- Gebruik `versie X.X.X, gelezen op JJJJ-MM-DD` als tijdstempel

### Classificatie
- Vier assen zijn verplicht; zie `mandarin-ecosysteem-ordeningsconcepten.md` voor de toegestane waarden
- Elke as krijgt een korte toelichtingszin onder de tabel

### Changelog
- Laatste versie bovenaan (nieuwste eerste)
- Bij herschrijving: voeg een regel toe zonder de initiële regel te verwijderen

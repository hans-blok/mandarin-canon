---
type: doctrine
naam: Doctrine — Agent Runner Architectuur
code: DARA
versie: 1.1.0
value-stream: aeo
digest: tbd0
status: vers
---
# Doctrine — Agent Runner Architectuur

---

## Herkomstverantwoording

Dit normatief artefact is opgesteld op basis van de volgende bronnen:

**Geraadpleegde bronnen**:
- `doctrine.agent-charter-normering.md` — agent-architectuurprincipes, scheiding van wat en hoe, capability boundary (versie 2.4.0, gelezen op 2026-03-15)
- `mandarin-ecosysteem-ordeningsconcepten.md` — ordeningsconcepten voor agent-structuur en value stream fasen (versie 1.9.0, gelezen op 2026-03-15)
- Gebruikersinvoer over problemen met de "runner per intent" architectuur (ontvangen op 2026-03-15)

**Opsteller**: Constitutioneel Auteur / Capability Architect  
**Doel**: Normering van de CLI-structuur voor agent-runners door één centrale runner per agent voor te schrijven in plaats van één runner per intent

---

## Classificatie

Deze doctrine positioneert zich als volgt op de vier orthogonale assen:

| Betekeniseffect | Vormingsfase | Werking | Bronhouding |
|---|---|---|---|
| normerend | uitvoering | inhoudelijk | canon-gebonden |

- **Betekeniseffect** — *normerend*: stelt de norm voor de "Eén Agent, Eén Runner" architectuur
- **Vormingsfase** — *uitvoering*: richt de technische uitvoering en bestandslocatie van agent-runners in
- **Werking** — *inhoudelijk*: bepaalt inhoud en structuur van runner-architectuur
- **Bronhouding** — *canon-gebonden*: baseert zich op canonieke agent-contracten en architectuurprincipes

---

## 1. Doel en scope

Deze doctrine stelt de norm voor een **"Eén Agent, Eén Runner"** architectuur (CLI-structuur). Zij bundelt alle interactiemogelijkheden (intents) van een specifieke agent achter een enkele deterministische "voordeur".

Zij borgt dat:

- gedeelde logica niet gedupliceerd wordt over meerdere runner-bestanden;
- de samenhang van een agent zichtbaar is vanuit één enkel toegangspunt;
- externe interfaces (zoals VS Code `tasks.json`) geen business-logica bevatten.

**Buiten scope**:
- Interne implementatiedetails van runners buiten de CLI-structuur
- Orkestratie van meerdere agents tegelijk
- Scheduling en cron-triggers

---

## 2. Probleemstelling

Binnen de actieve ontwikkeling van het Mandarin-ecosysteem was de oorspronkelijke aanname om voor elke *intent* een los runner-script te genereren (bijv. `hypothese-vormer.beschrijf-aannames.runner.py`).

In de praktijk leidde deze "runner per intent" architectuur tot aanzienlijke problemen:

1. **Redundantie**: Gedeelde logica (zoals logging, het parseren van argumenten, of canon-verificaties) werd gedupliceerd over tientallen bestanden.
2. **Versplintering**: Om de samenhang van een agent te begrijpen moest een developer door talloze losse bestanden navigeren.
3. **Task-vervuiling**: Configuraties zoals `.vscode/tasks.json` stonden vol met inline PowerShell-lijmcode om executie bij elkaar te knopen, in plaats van aanroep-verantwoordelijkheid bij de agent zelf te leggen.

---

## 3. Architectuurprincipes

### 3.1 — Eén centrale CLI-runner per agent

Een agent heeft in zijn werkgebied precies één executabel runner-bestand. De naamgeving is strict `{agent_naam}.runner.py`.

Deze runner fungeert als de Command Line Interface (CLI) en voordeur voor de buitenwereld.

### 3.2 — Intents zijn sub-commando's

De afzonderlijke vaardigheden of handelingen (intents) van een agent worden in de runner gemodelleerd als sub-commando's (gebruikmakend van standaard bibliotheken zoals `argparse` subparsers).

- *Antipatroon*: `python runner-intent1.py`, `python runner-intent2.py`
- *Normatief*: `python agent.runner.py intent1`, `python agent.runner.py intent2`

### 3.3 — Decentrale en strict gescheiden bestandslocatie

Runners verblijven niet in een centrale of globale `scripts/` map, maar worden expliciet binnen het domein (boundary) van de specifieke agent opgeslagen. Dit borgt de autonomie van de agent in het ecosysteem.

**Locatie**: `artefacten/{vs}/{vs}.{fase}.{agent}/runners/{agent}.runner.py`

### 3.4 — Schone aanroep-interfaces

Externe interfaces (zoals een VS Code `tasks.json`) bevatten zo min mogelijk business-logica of inline command-line generatie (geen zware PowerShell-concatenaties). De taak spreekt uitsluitend de agent runner CLI aan met specifieke argument-vlaggen (`--parameter "waarde"`). De interne abstractie is de verantwoordelijkheid van de runner.

### 3.5 — Bescherming van custom logica

Wanneer een agent (zoals de `agent-engineer`) automatisch runners genereert op basis van contracten, weigert de engineer per definitie om een runner te overschrijven die door een engineer-steward of developer lokaal verrijkt is met specifieke executielogica, tenzij expliciete override-vlaggen zijn opgegeven. Dit voorkomt regressie in custom business logic.

---

## 4. Governance

### 4.1 — Controle op naleving

Deze doctrine wordt afgedwongen door de `agent-engineer` bij het realiseren van agent-structuren en getoetst door de `agent-curator` bij rapportages.

### 4.2 — Verantwoordelijkheid

Beheerd binnen het domein van de canon- en architectuur value streams.

---

## 5. Relatie tot andere doctrines

| Doctrine | Relatie |
|---|---|
| `doctrine.agent-charter-normering.md` | Agents hebben één verantwoordelijkheid; runners implementeren deze als één CLI-voordeur |
| `doctrine.intent-naming.md` | Intents zijn sub-commando's van de runner; naamgeving volgt canonieke werkwoorden |
| `workspace-doctrine.md` | Runners worden opgeslagen conform de workspace-locatieconventies |

---

## Changelog

| Datum | Versie | Wijziging | Uitvoer door |
|---|---|---|---|
| 2026-04-15 | 1.1.0 | YAML-frontmatter vervangen conform standaard (`type`, `naam`, `versie`, `digest`, `status`); Herkomstverantwoording toegevoegd; Classificatie toegevoegd; secties genummerd; `---` dividers toegevoegd; §5 Relatie tot andere doctrines en Changelog toegevoegd | Hans Blok |
| onbekend | 1.0.0 | Initiële versie: "Eén Agent, Eén Runner" architectuur vastgesteld; vijf principes gedefinieerd | Constitutioneel Auteur |

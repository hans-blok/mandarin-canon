---
titel: Doctrine Agent Runner Architectuur
versie: 1.0.0
status: vers
domein: realisatie
beheerd_door: constitutioneel-auteur / capability-architect
digest: c4fe
---
# Doctrine Agent Runner Architectuur

## Achtergrond en Probleemstelling
Binnen de actieve ontwikkeling van het Mandarin Ecosysteem was de oorspronkelijke aanname om voor elke *intent* een los runner-script the genereren (bijv. `hypothese-vormer.beschrijf-aannames.runner.py`). 

In de praktijk leidde deze "runner per intent" architectuur tot aanzienlijke problemen:
1. **Redundantie**: Gedeelde logica (zoals logging, het parseren van argumenten, of canon-verificaties) nam explosief toe en werd gedupliceerd over tientallen bestanden.
2. **Versplintering**: Om de samenhang van een agent te begrijpen moest een developer / orchestrator door talloze losse bestanden navigeren.
3. **Task-vervuiling**: Configuraties zoals `.vscode/tasks.json` stonden vol met inline PowerShell-lijmcode om executie bij elkaar te knopen, in plaats van aanroep-verantwoordelijkheid bij de agent zelf te leggen.

## Doel
Deze doctrine stelt de norm in voor een "Eén Agent, Eén Runner" architectuur (CLI-structuur). Het bundelt alle interactie-mogelijkheden (intents) van een specifieke agent achter een enkele deterministische "voordeur".

---

## Principes

### Principe 1: Eén centrale CLI-Runner per Agent
Een agent heeft in zijn werkgebied precies één executabel runner bestand. De naamgeving is strict `{agent_naam}.runner.py`. 
Deze runner fungeert als de Command Line Interface (CLI) en voordeur voor de buitenwereld.

### Principe 2: Intents zijn Sub-commando's
De afzonderlijke vaardigheden of handelingen (intents) van een agent worden in deze runner gemodelleerd als sub-commando's (gebruikmakend van standaard bibliotheken zoals `argparse` subparsers).
- *Antipatroon*: `python runner-intent1.py`, `python runner-intent2.py`
- *Normatief*: `python agent.runner.py intent1`, `python agent.runner.py intent2`

### Principe 3: Decentrale en Strict Gescheiden Bestandslocatie
Runners verblijven niet in een centrale / globale `scripts/` map, maar worden expliciet binnen het domein (boundary) van de specifieke agent opgeslagen. Dit borgt de autonomie van de agent in het ecosysteem.
- **Locatie**: `artefacten/{vs}/{vs}.{fase}.{agent}/runners/{agent}.runner.py`

### Principe 4: Schone Aanroep-interfaces (Clean Tasks)
Externe interfaces (zoals een VS Code `tasks.json`) bevatten zo min mogelijk business logica of inline command-line generatie (geen zware PowerShell concatenaties). De taak spreekt uitsluitend de agent runner CLI met specifieke argument-vlaggen (`--parameter "waarde"`) aan. De interne abstractie is de verantwoordelijkheid van de runner.

### Principe 5: Bescherming van Custom Logica (Safe Overwrite)
Wanneer een agent (zoals de `agent-engineer`) automatisch de runners genereert op basis van contracten, mag in theorie de scaffolding gegenereerd worden. Echter, wanneer de runner door een *engineer-steward* of developer lokaal verrijkt is met specifieke executielogica (zoals bij de `agent-curator` het geval is), weigert de engineer per definitie om dit bestand te overschrijven zonder expliciete override vlaggen, ter voorkoming van regressie in custom business logic.

---

## Governance

- **Controle op naleving**: Deze doctrine wordt afgedwongen door de `agent-engineer` bij het realiseren van agent-structuren en getoetst door de `agent-curator` bij rapportages.
- **Verantwoordelijkheid**: Beheerd binnen het domein van de canon/architectuur value streams.
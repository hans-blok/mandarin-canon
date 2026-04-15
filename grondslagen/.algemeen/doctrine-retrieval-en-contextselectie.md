---
type: doctrine
naam: Doctrine — Retrieval en Contextselectie
versie: 1.1.0
value-stream: aeo
digest: tbd0
status: vers
---
# Doctrine — Retrieval en Contextselectie

---

## Herkomstverantwoording

Dit normatief artefact is opgesteld op basis van de volgende bronnen:

**Geraadpleegde bronnen**:
- `doctrine-traceability.md` — §6 execution-identiteit, §7 YAML-header (versie 1.6.0, gelezen op 2026-04-14)
- `doctrine-bronhouding-en-exploratie.md` — gesloten bronhouding, werkbronnen, kaderbronnen (versie 1.0.0, gelezen op 2026-04-14)
- `doctrine-agent-charter-normering.md` — capability boundary, charter als legitimatiebron (versie 2.4.0, gelezen op 2026-04-14)
- `mandarin-domeinconcepten.md` — concepten MandarinArtefact, Execution, Bronregime, Intent (versie 2.13.0, gelezen op 2026-04-14)
- `mandarin-ecosysteem-ordeningsconcepten.md` — vier orthogonale classificatie-assen (versie 1.9.0, gelezen op 2026-04-14)

**Opsteller**: Hans Blok  
**Doel**: Normering van deterministische contextselectie uit de Mandarin-graph ten behoeve van agent-executies

---

## Classificatie

Deze doctrine positioneert zich als volgt op de vier orthogonale assen:

| Betekeniseffect | Vormingsfase | Werking | Bronhouding |
|---|---|---|---|
| normerend | ordening / vastlegging | conditioneel | canon-gebonden |

- **Betekeniseffect** — *normerend*: bepaalt hoe selectie moet plaatsvinden
- **Vormingsfase** — *ordening / vastlegging*: structureert en formaliseert het selectieproces
- **Werking** — *conditioneel*: bepaalt onder welke voorwaarden context wordt samengesteld
- **Bronhouding** — *canon-gebonden*: baseert zich uitsluitend op canonieke bronnen

---

## 1. Doel en scope

Deze doctrine normeert hoe context wordt samengesteld uit de Mandarin-graph ten behoeve van agent-executies.

Zij borgt dat:

- contextselectie deterministisch en uitlegbaar is;
- agents uitsluitend werken op expliciet geselecteerde werkbronnen;
- selectie niet afhankelijk is van impliciete modelintelligentie;
- traceability en reproduceerbaarheid behouden blijven.

**Buiten scope**:
- Implementatiedetails van de graph-database zelf (indexering, persistentie, fysieke opslag)
- Semantische zoekalgoritmen en vector-zoekmethoden (zie §8 — deze zijn expliciet verboden)
- Interne stappen binnen één agent-executie die geen context-selectie vereisen
- Versie- en conflictbeheer van onderliggende artefacten in de graph

---

## 2. Kernprincipe

Agents werken nooit direct op de volledige graph, maar uitsluitend op een expliciet samengestelde context die voortkomt uit deterministische selectie.

Deze context vormt de **werkbron** voor de execution.

---

## 3. Begrippen

### 3.1 — Retrieval

De handeling waarbij een subset van de Mandarin-graph wordt geselecteerd op basis van expliciete regels.

### 3.2 — Context

De verzameling van geselecteerde:

- concepten
- relaties
- artefacten
- bronverwijzingen

die als input dienen voor een agent-executie.

### 3.3 — Retrieval-regel

Een expliciet vastgelegde instructie die bepaalt:

- waar selectie start
- welke relaties gevolgd worden
- welke filters gelden
- welke grenzen worden toegepast

---

## 4. Architectuur van retrieval

Retrieval bestaat uit vier opeenvolgende stappen:

### Stap 1 — Startpuntbepaling (intent-gedreven)

Het startpunt wordt bepaald door de intent:

- het **object** van de intent bepaalt het primaire concept
- het **werkwoord** bepaalt het type selectie (werking)

Voorbeeld:

```
definieer-agent-charter
→ startpunt : Agent-charter
→ werking   : normerend
```

Intent-naming is hierbij leidend en niet optioneel.

### Stap 2 — Structurele expansie (graph traversal)

Vanaf het startpunt worden relaties gevolgd volgens vaste regels:

- maximaal N hops (standaard: 2)
- alleen canoniek toegestane relatietypen
- geen vrije of impliciete uitbreiding

Toegestane relaties omvatten onder andere:

- `definieert` / `beschrijft`
- `relateert-aan`
- `behoort-tot`
- `wordt-gebruikt-door`
- `bouwt-voort-op`

### Stap 3 — Contextfiltering

De selectie wordt gefilterd op:

- value stream
- value stream fase
- artefacttype
- bronregime

Alleen elementen die binnen de context van de execution vallen, blijven over.

### Stap 4 — Begrenzing

Om context-explosie te voorkomen gelden harde limieten:

- maximaal aantal concepten
- maximaal aantal artefacten
- maximale graad van relatie-expansie

Bij overschrijding wordt selectie **afgekapt**, niet uitgebreid.

---

## 5. Typen retrieval per intent

Retrieval verschilt per intent-type (werking):

### 5.1 — Beschrijvend (`beschrijf-*`)

- Focus: concept + directe relaties
- Geen normatieve artefacten vereist

### 5.2 — Structurerend (`structureer-*`)

- Focus: concept + relatiestructuur + ordeningsconcepten

### 5.3 — Normerend (`definieer-*`, `leg-vast-*`)

- Focus: concept + normatieve artefacten + doctrines
- Hogere prioriteit voor governance-artefacten

### 5.4 — Evaluerend (`beoordeel-*`)

- Focus: concept + criteria + historisch relevante artefacten

---

## 6. Bronhouding

Retrieval opereert onder de **gesloten bronhouding**:

- alleen expliciet geselecteerde context mag gebruikt worden
- de graph is een *potentiële* bron, geen directe bron
- de selectie vormt de werkbron

Het LLM introduceert geen eigen kennis.

---

## 7. Traceability-eis

Elke execution moet expliciet vastleggen:

```yaml
gebruikte-context:
  concepten: [...]
  artefacten: [...]
  relaties: [...]

ontbrekende-basis:
  - [...]
```

Deze registratie maakt de selectie:

- controleerbaar
- reproduceerbaar
- auditbaar

en sluit aan op de traceability-doctrine (zie §13).

---

## 8. Verboden praktijken

Het is expliciet **niet** toegestaan om:

- de volledige graph ongefilterd als context te gebruiken
- selectie impliciet door het LLM te laten bepalen
- semantische zoekmethoden zonder expliciete regels te gebruiken
- context uit te breiden zonder traceerbare selectie

---

## 9. Rol van de runner

De runner:

- voert retrieval-regels deterministisch uit
- interpreteert geen betekenis
- maakt geen inhoudelijke keuzes
- levert uitsluitend geselecteerde context

---

## 10. Escalatie

Escalatie is verplicht wanneer:

- relevante context ontbreekt binnen de gestelde grenzen
- meerdere conflicterende artefacten worden gevonden
- geen canonieke relatie beschikbaar is
- selectie niet eenduidig kan worden bepaald

---

## 11. Ontwerpprincipe

> Relevantie wordt niet bepaald door interpretatie, maar door expliciete selectiecriteria en begrenzing.

---

## 12. Samenvattende norm

Retrieval is een **expliciete, deterministische en begrensde** selectie van context uit de Mandarin-graph, gebaseerd op intent en canonieke relaties, waarbij alleen de geselecteerde context als werkbron mag dienen voor agent-executie.

---

## 13. Relatie tot andere doctrines

| Doctrine | Relatie |
|---|---|
| `doctrine-bronhouding-en-exploratie.md` | Bepaalt wat als bron mag gelden |
| `doctrine-traceability.md` | Bepaalt hoe selectie herleidbaar wordt vastgelegd |
| `doctrine-intent-naming.md` | Bepaalt het startpunt en type retrieval |
| `doctrine-agent-charter-normering.md` | Bepaalt de boundary waarbinnen selectie relevant is |

---

## 14. Slotopmerking (architectonisch)

Deze doctrine verschuift het systeem van:

```
impliciete interpretatie
```

naar:

```
expliciete selectie
```

en vormt daarmee de noodzakelijke schakel tussen:

- **ontologie** (graph)
- **uitvoering** (agent-executie)

---

## Changelog

| Datum | Versie | Wijziging | Uitvoer door |
|---|---|---|---|
| 2026-04-14 | 1.1.0 | Structuur herschreven conform doctrine-goudstandaard: YAML-frontmatter, Herkomstverantwoording, Classificatietabel, Buiten scope, §§-scheidingslijnen, `###`-subsecties, Changelog toegevoegd; hernoemd van `doctrine.retrieval-en-contextselectie.md` | Hans Blok |
| onbekend | 1.0.0 | Initiële versie | onbekend |

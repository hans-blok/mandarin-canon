# Mandarin Value Streams en Fasen

**Versie**: 1.2.0  
**Status**: Actief  
**Datum**: 2026-02-01  
**Auteur**: Constitutioneel Auteur  

---

## Herkomstverantwoording

Dit normatief artefact is afgeleid op basis van de volgende geraadpleegde bronnen:

**Geraadpleegde bronnen**:
- constitutie.md (versie 1.2.1, als normatief kader voor value stream begrip)
- concepten-en-architectonische-grondslagen.md (versie 1.5.0, voor definities van Value stream en Value stream fase)

**Toelichting**:
Dit document legt vast welke value streams binnen het Mandarin-ecosysteem worden onderkend en welke fasen per value stream bestaan. Adviserende agents en uitvoerende agents worden toegekend aan één of meerdere value stream fasen. Beheeragents opereren in alle fasen. Utility agents staan orthogonaal op de value stream structuur en kunnen in willekeurige contexten worden ingezet.

---

## 1. Inleiding

### 1.1 Doel van dit document

Dit document beschrijft de canonieke set van **value streams** die binnen het Mandarin-ecosysteem worden onderkend, met de bijbehorende **fasen** per value stream. Value streams representeren de verschillende waardestromen waarin agents opereren en waarde-artefacten produceren.

### 1.2 Agent-toekenning aan value streams

Elke Mandarin-agent wordt gepositioneerd volgens één van de volgende categorieën:

#### Value stream agents

**Value stream agents** zijn agents die direct gekoppeld zijn aan één of meerdere fasen binnen een specifieke value stream. Alleen **adviserende agents** en **uitvoerende agents** kunnen value stream agents zijn.

- Value stream agents produceren waarde-artefacten of governance-artefacten die aansluiten bij hun toegekende value stream fase(n).
- Value stream agents opereren binnen de grenzen van hun toegekende fase(n) en mogen niet buiten die scope treden.
- Bij het opstellen van een Agent-charter voor een value stream agent moet expliciet worden aangegeven tot welke value stream fase(n) de agent behoort.

**Voorbeelden**: Feature-analist (fase: Analyse), Architectuurontwerper (fase: Ontwerp), Constitutioneel Auteur (fase: Grondslagvorming).

#### Beheeragents

**Beheeragents** zijn niet aan specifieke fasen gebonden, maar opereren **in alle fasen** van alle value streams. De primaire beheeragent binnen het Mandarin-ecosysteem is de **Moeder agent**.

- Beheeragents wijzigen geen inhoud, maar wel structuur en governance.
- Beheeragents zijn generiek inzetbaar en overstijgen value stream grenzen.
- Beheeragents zorgen voor operationele continuïteit en governance-borging.

**Voorbeeld**: Moeder agent (beheert workspace-state, beleid, handoffs).

#### Utility agents

**Utility agents** staan **orthogonaal** op de value stream structuur. Zij zijn niet gekoppeld aan value stream fasen en kunnen in willekeurige contexten worden ingezet om ondersteunende, generieke diensten te leveren.

- Utility agents leveren technische of ondersteunende capabilities die niet specifiek zijn voor één value stream.
- Utility agents kunnen door meerdere value streams en agents worden gebruikt.
- Utility agents produceren ondersteunende artefacten, geen waarde-artefacten of governance-artefacten.

**Voorbeelden**: Format-vertaler (transformeert documenten), Kort-schrijver (herformuleert teksten), Docker-steward (beheert containers), Python-expert (schrijft/reviewt scripts).

---

## 2. Overzicht Value Streams

Het Mandarin-ecosysteem onderkent de volgende value streams:

| # | Value Stream | Type | Primaire Focus |
|---|--------------|------|----------------|
| 0 | Agent Ecosysteem Ontwikkeling | Ecosysteem | Vorming en evolutie van het agent-ecosysteem |
| 1 | Softwareontwikkeling | Waarde | Realiseren, wijzigen en onderhouden van software |
| 2 | Architectuur- en Oplossingsontwerp | Waarde | Ontwerpen en onderbouwen van oplossingsrichtingen |
| 3 | Kennisvastlegging | Waarde | Expliceren, structureren en vastleggen van kennis |

---

## 3. Value Stream Definities en Fasen

### 3.0 Agent Ecosysteem Ontwikkeling

**Type**: Ecosysteem value stream  
**Omschrijving**: Deze value stream richt zich op het vormen, inrichten en laten evolueren van het agent-ecosysteem zelf. Agents in deze value stream produceren **governance-artefacten** (een specialisatie van normerende artefacten), geen bedrijfs-artefacten. Governance-artefacten worden **alleen en alleen** in deze value stream aangemaakt.

**Fasen**:

1. **Grondslagvorming**  
   Het vaststellen van fundamentele principes, concepten, doctrines en architectonische grondslagen waarop het ecosysteem is gebouwd.

2. **Ecosysteeminrichting**  
   Het operationaliseren van grondslagen door het creëren van Agent-charters, beleid, workspace-structuren en beheer-instrumenten.

---

### 3.1 Softwareontwikkeling

**Type**: Waarde value stream  
**Omschrijving**: De kern value stream voor het realiseren, wijzigen en onderhouden van software. Deze value stream sluit inhoudelijk aan op SAFe (Scaled Agile Framework), maar hanteert Nederlandstalige, architectonisch neutrale terminologie die binnen het Mandarin-ecosysteem is vastgesteld. Agents in deze value stream produceren **bedrijfs-artefacten** (een specialisatie van normerende artefacten).

**Fasen**:

1. **Veranderkenning**  
   Het herkennen en identificeren van een veranderbehoefte of -trigger in de context van bestaande software of gewenste nieuwe functionaliteit.

2. **Werkvoorbereiding**  
   Het voorbereiden van het werk door het vaststellen van scope, prioriteiten, randvoorwaarden en eerste verkenning van haalbaarheid en impact.

3. **Behoefte- en requirements analyse**  
   Het analyseren van eisen, processen en context om een volledig begrip te vormen van wat er moet worden gerealiseerd.

4. **Ontwerp**  
   Het vormgeven van de technische en functionele oplossing, inclusief architectuur, interfaces en datastructuren.

5. **Realisatie**  
   Het daadwerkelijk bouwen en coderen van de softwareoplossing volgens het ontwerp.

6. **Validatie**  
   Het testen en verifiëren dat de gerealiseerde software voldoet aan de gestelde eisen en kwaliteitsnormen.

7. **Vrijgave**  
   Het formeel vrijgeven en implementeren van de software in de productieomgeving.

8. **Beheer en Evolutie**  
   Het onderhouden, monitoren en doorontwikkelen van de software gedurende de operationele levenscyclus.

---

### 3.2 Architectuur- en Oplossingsontwerp

**Type**: Waarde value stream  
**Omschrijving**: Deze value stream richt zich op het ontwerpen en onderbouwen van oplossingsrichtingen, los van concrete implementatie. Het betreft strategische en tactische architectuurkeuzes die richting geven aan softwareontwikkeling. Agents in deze value stream produceren **bedrijfs-artefacten** (een specialisatie van normerende artefacten).

**Fasen**:

1. **Vraagverkenning**  
   Het verkennen en expliciteren van architectuurvraagstukken, drivers en randvoorwaarden.

2. **Architectuurkadering**  
   Het vaststellen van architectuurprincipes, standaarden en kaders waarbinnen oplossingen moeten worden ontworpen.

3. **Oplossingsontwerp**  
   Het uitwerken van concrete oplossingsrichtingen, inclusief afwegingen, varianten en aanbevelingen.

4. **Besluitvorming en Borging**  
   Het formaliseren van architectuurbeslissingen en het borgen van naleving en traceerbaarheid.

---

### 3.3 Kennisvastlegging

**Type**: Waarde value stream  
**Omschrijving**: Deze value stream richt zich op het expliciet maken, structureren en duurzaam vastleggen van kennis. Het doel is om kennis herbruikbaar, doorzoekbaar en overdraagbaar te maken binnen en buiten het ecosysteem. Agents in deze value stream produceren **bedrijfs-artefacten** (een specialisatie van normerende artefacten).

**Fasen**:

1. **Kennisverkenning**  
   Het identificeren van kennisdomeinen, lacunes en bestaande kennisbronnen die geëxpliciteerd moeten worden.

2. **Structurering**  
   Het ordenen en categoriseren van kennis volgens een herkenbare en toegankelijke structuur.

3. **Vastlegging**  
   Het daadwerkelijk documenteren en formaliseren van kennis in een geschikt formaat.

4. **Publicatie en Onderhoud**  
   Het beschikbaar maken van kennis voor gebruikers en het actueel houden ervan gedurende de levenscyclus.

---


---

## 5. Wijzigingshistorie

| Datum | Versie | Wijziging | Auteur |
|-------|--------|-----------|--------|
| 2026-02-01 | 1.2.0 | Verduidelijking artefacttypes per value stream: governance-artefacten (normerende artefacten) alleen in value stream 0, bedrijfs-artefacten (normerende artefacten) in waarde value streams 1-n | Constitutioneel Auteur |
| 2026-01-31 | 1.1.0 | Verduidelijking agent-toekenning per agent-soort: value stream agents (adviserende/uitvoerende), beheeragents (alle fasen), utility agents (orthogonaal) | Constitutioneel Auteur |
| 2026-01-31 | 1.0.0 | Initiële versie — canonieke vastlegging van value streams en fasen | Constitutioneel Auteur |

---

## 6. Relatie tot andere documenten

Dit document is normatief en dient als bron voor:
- **Agent-charters**: Bij het opstellen van een Agent-charter moet worden aangegeven tot welke value stream fase(n) de agent behoort, of dat de agent een utility agent is.
- **Workspace-beleid**: Workspaces kunnen zich richten op specifieke value streams; dit document biedt de canonieke lijst.
- **Doctrine-documenten**: Specifieke doctrines kunnen gelden per value stream of fase.

Dit document verwijst naar:
- **concepten-en-architectonische-grondslagen.md** (v1.5.0) voor de definitie van "Value stream" en "Value stream fase".
- **constitutie.md** (v1.2.1) als hoogste normatieve bron.

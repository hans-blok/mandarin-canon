# Mandarin Value Streams en Fasen

**Versie**: 1.6.0  
**Status**: Actief  
**Datum**: 2026-02-15  
**Auteur**: Constitutioneel Auteur  

---

## Herkomstverantwoording

Dit normatief artefact is afgeleid op basis van de volgende geraadpleegde bronnen:

**Geraadpleegde bronnen**:
- constitutie.md (versie 1.2.1, als normatief kader voor value stream begrip)
- concepten-en-architectonische-grondslagen.md (versie 1.5.0, voor definities van Value stream en Value stream fase)

**Toelichting**:
Dit document legt vast welke value streams binnen het Mandarin-ecosysteem worden onderkend en welke fasen per value stream bestaan. Adviserende agents en uitvoerende agents worden toegekend aan één of meerdere value stream fasen. Beheeragents opereren in alle fasen. Daarnaast zijn er value-stream-overstijgende agents die orthogonaal op de value stream structuur staan en in willekeurige contexten kunnen worden ingezet.

---

## 1. Inleiding

### 1.1 Doel van dit document

Dit document beschrijft de canonieke set van **value streams** die binnen het Mandarin-ecosysteem worden onderkend, met de bijbehorende **fasen** per value stream. Value streams representeren de verschillende waardestromen waarin agents opereren en waarde-artefacten produceren.

### 1.2 Agent-toekenning aan value streams
In project workspaces wordt waarde toegevoegd. Dit gebeurt door minimaal één value stream uit te voeren. Dit kunnen er ook meerdere zijn. 
Bij de inrichting van de workspace worden de agents die operationeel zijn in die value stream _gefechted_ naar deze workspace. Zo ordenen we het eco-systeem en kunnen we workspaces efficient inrichten. 
Daar kent Mandarin agents die value stream overstijgend werk doen. Dit zijn _foundational agents_. Deze worden altijd _gefetched_.

---

## 2. Overzicht Value Streams

Het Mandarin-ecosysteem onderkent de volgende value streams:

| # | Code | Value Stream | Type | Primaire Focus |
|---|------|--------------|------|----------------|
| 0 | AEO  | Agent Ecosysteem Ontwikkeling | Ecosysteem | Vorming en evolutie van het agent-ecosysteem |
| 1 | SFW  | Softwareontwikkeling | Waarde | Realiseren, wijzigen en onderhouden van software |
| 2 | AOD  | Architectuur- en Oplossingsontwerp | Waarde | Ontwerpen en onderbouwen van oplossingsrichtingen |
| 3 | KNV  | Kennisvastlegging | Waarde | Expliceren, structureren en vastleggen van kennis |
| 4 | MIV  | Markt- en Investeringsvorming | Waarde | Orde brengen in markt- en investeringskeuzes onder onzekerheid |

---

## 3. Value Stream Definities en Fasen

### 3.0 Agent Ecosysteem Ontwikkeling (AEO)

**Type**: Ecosysteem value stream  
**Omschrijving**: Deze value stream richt zich op het vormen, inrichten en laten evolueren van het agent-ecosysteem zelf. Agents in deze value stream produceren **governance-artefacten** (een specialisatie van normerende artefacten), geen bedrijfs-artefacten. Governance-artefacten worden **alleen en alleen** in deze value stream aangemaakt.

**Fasen**:

01. **Grondslagvorming**  
   Het vaststellen van fundamentele principes, concepten, doctrines en architectonische grondslagen waarop het ecosysteem is gebouwd.

02. **Ecosysteeminrichting**  
   Het operationaliseren van grondslagen door het creëren van Agent-charters, beleid, workspace-structuren en beheer-instrumenten.

03. **Ecosysteemworkflow en -automatisering**  
   Het ontwerpen, implementeren en onderhouden van geautomatiseerde workflows en pipelines (fetch, runners, publicatie, logging) die de werking van het agent-ecosysteem ondersteunen en afdwingen op basis van de vastgestelde grondslagen en inrichting.

---

### 3.1 Softwareontwikkeling (SFW)

**Type**: Waarde value stream  
**Omschrijving**: De kern value stream voor het realiseren, wijzigen en onderhouden van software. Deze value stream sluit inhoudelijk aan op SAFe (Scaled Agile Framework), maar hanteert Nederlandstalige, architectonisch neutrale terminologie die binnen het Mandarin-ecosysteem is vastgesteld. Agents in deze value stream produceren **bedrijfs-artefacten** (een specialisatie van normerende artefacten).

**Fasen**:

01. **Veranderkenning**  
   Het herkennen en identificeren van een veranderbehoefte of -trigger in de context van bestaande software of gewenste nieuwe functionaliteit.

02. **Werkvoorbereiding**  
   Het voorbereiden van het werk door het vaststellen van scope, prioriteiten, randvoorwaarden en eerste verkenning van haalbaarheid en impact.

03. **Behoefte- en requirements analyse**  
   Het analyseren van eisen, processen en context om een volledig begrip te vormen van wat er moet worden gerealiseerd.

04. **Ontwerp**  
   Het vormgeven van de technische en functionele oplossing, inclusief architectuur, interfaces en datastructuren.

05. **Realisatie**  
   Het daadwerkelijk bouwen en coderen van de softwareoplossing volgens het ontwerp.

06. **Validatie**  
   Het testen en verifiëren dat de gerealiseerde software voldoet aan de gestelde eisen en kwaliteitsnormen.

07. **Vrijgave**  
   Het formeel vrijgeven en implementeren van de software in de productieomgeving.
   Het uitrollen (deployen) van de software naar de productieomgeving en het beschikbaar stellen voor gebruik.
   
---

### 3.2 Architectuur en oplossingsontwerp (TOGAF-fasering)

**Type**: Architectuur value stream  
**Omschrijving**: Voorbeeld van value stream fasering volgens TOGAF ADM, met Nederlandse termen.

**Fasen**:

01. **Voorbereiding architectuurfunctie**  
   Het voorbereiden van de architectuurfunctie, het vaststellen van uitgangspunten en principes.

02. **Architectuurvisie**  
   Het bepalen van de scope, stakeholders en de visie op de architectuur.

03. **Bedrijfsarchitectuur**  
   Het ontwerpen van de bedrijfsarchitectuur (processen, organisatie, bedrijfsfuncties).

04. **Informatie- en applicatiearchitectuur**  
   Het ontwerpen van de informatiearchitectuur en applicatiearchitectuur.

05. **Technische architectuur**  
   Het ontwerpen van de technische architectuur (infrastructuur, platforms, technologie).

06. **Kansen en oplossingsrichtingen**  
   Het bepalen van oplossingsrichtingen en opstellen van transitieplanning.

07. **Migratieplanning**  
   Het opstellen van een migratieplan voor de implementatie van de architectuur.

08. **Implementatiebegeleiding**  
   Het begeleiden en sturen van de implementatie van de architectuur.

09. **Architectuurbeheer**  
   Het beheren en aanpassen van de architectuur bij veranderingen.

---

### 3.3 Kennisvastlegging (KNV)

**Type**: Waarde value stream  
**Omschrijving**: Deze value stream richt zich op het expliciet maken, structureren en duurzaam vastleggen van kennis. Het doel is om kennis herbruikbaar, doorzoekbaar en overdraagbaar te maken binnen en buiten het ecosysteem. Agents in deze value stream produceren **bedrijfs-artefacten** (een specialisatie van normerende artefacten).

**Fasen**:

01. **Kennisverkenning**  
   Het identificeren van kennisdomeinen, lacunes en bestaande kennisbronnen die geëxpliciteerd moeten worden.

02. **Structurering**  
   Het ordenen en categoriseren van kennis volgens een herkenbare en toegankelijke structuur.

03. **Vastlegging**  
   Het daadwerkelijk documenteren en formaliseren van kennis in een geschikt formaat.

04. **Publicatie en Onderhoud**  
   Het beschikbaar maken van kennis voor gebruikers en het actueel houden ervan gedurende de levenscyclus.

---

### 3.4 Markt- en Investeringsvorming (MIV)

**Type**: Waarde value stream  
**Omschrijving**: Deze value stream richt zich op het onder voorwaarden en met orde omgaan met fundamentele onzekerheid rond Mandarin als marktproduct en/of investeringsasset. Het doel is niet om zo snel mogelijk één richting te kiezen, maar om onzekerheid stap voor stap te reduceren en keuzeruimte toetsbaar te maken.

**Fasen**:

01. **Strategische intentie expliciteren**  
   Het expliciet maken waarom Mandarin bestaat buiten eigen gebruik, en of Mandarin primair wordt gezien als intern hefboom-instrument, marktproduct of investeringsasset. In deze fase worden 2–3 strategische intenties en hun spanningen over een horizon van 3–5 jaar expliciet gemaakt, zonder nog te bepalen hoe die worden gerealiseerd.

02. **Waarde-hypotheses formuleren**  
   Het formuleren van meerdere, expliciete waarde-hypotheses (bijvoorbeeld Excel-vervanging, overnamepotentieel, interne capability, licentieproduct) zonder hier al een keuze in te maken. Per hypothese wordt vastgelegd wie de primaire gebruiker is, welk probleem wordt opgelost en waarom iemand hiervoor zou betalen of investeren.

03. **Positioneringsrichtingen verkennen**  
   Het verkennen van mogelijke positioneringen in de markt, niet als marketing maar als identiteit: bijvoorbeeld tool versus platform versus methode, productbedrijf versus dienstverlener, niche-oplossing versus generiek systeem. Meerdere positioneringen mogen naast elkaar bestaan; waar zij elkaar uitsluiten wordt dat expliciet gemaakt.

04. **Monetisatie-logica’s scheiden**  
   Het onderscheiden van mogelijke monetisatie-logica’s (bijvoorbeeld licentie per gebruiker/organisatie, abonnement op hosting en updates, consultancy/dienstverlening met Mandarin als hefboom, of intern houden met indirecte waarde). Monetisatie wordt hier bewust losgekoppeld van productkeuze; per logica worden implicaties voor governance, support en architectuur in kaart gebracht.

05. **Investering en kostenrealiteit expliciet maken**  
   Het inzichtelijk maken van kosten en risico’s van kiezen en van uitstellen, waaronder indicatieve hostingkosten, onderhouds- en supportdruk en risico’s van technische lock-in zonder marktkeuze. Deze fase produceert scenario’s met kosten- en risicoprofielen, inclusief expliciete doorkosten bij uitstel.

06. **Keuzeruimte structureren (geen besluit)**  
   Het structureren van het beslislandschap: welke keuzes nu minimaal nodig zijn (bijvoorbeeld basis-hosting), welke keuzes bewust later kunnen worden genomen, en welke keuzes elkaar blokkeren. De uitkomst is een beslislandschap met expliciete uitstel- en keuzepunten, geen definitief besluit.

---

## 5. Wijzigingshistorie

| Datum | Versie | Wijziging | Auteur |
|-------|--------|-----------|--------|
| 2026-02-15 | 1.6.0 | Herziening value stream AOD: fase 01 hernoemd naar "Strategie en Motivatie" (architectuur-normering), fase 02 "Structureren" (ArchiMate core-framework), fase 03 "Oplossingsontwerp" (ArchiMate en C4) | Constitutioneel Auteur |
| 2026-02-05 | 1.5.0 | Aanpassing: value stream Ondernemingsvorming (ONV) vervangen door Markt- en Investeringsvorming (MIV) met herziene, op onzekerheidsreductie gerichte fasering | Constitutioneel Auteur |
| 2026-02-02 | 1.4.0 | Toegevoegd: value stream Ondernemingsvorming (ONV) met genormeerde fasering van kansverkenning tot ondernemingsinrichting | Constitutioneel Auteur |
| 2026-02-02 | 1.3.0 | Toegevoegd: drie-letterige codes per value stream en genormeerde fasevolgnummers (01, 02, …) per value stream fase | Constitutioneel Auteur |
| 2026-02-01 | 1.2.0 | Verduidelijking artefacttypes per value stream: governance-artefacten (normerende artefacten) alleen in value stream 0, bedrijfs-artefacten (normerende artefacten) in waarde value streams 1-n | Constitutioneel Auteur |
| 2026-01-31 | 1.1.0 | Verduidelijking agent-toekenning per agent-soort: value stream agents (adviserende/uitvoerende), beheeragents (alle fasen), value-stream-overstijgende agents (orthogonaal) | Constitutioneel Auteur |
| 2026-01-31 | 1.0.0 | Initiële versie — canonieke vastlegging van value streams en fasen | Constitutioneel Auteur |

---

## 6. Relatie tot andere documenten

Dit document is normatief en dient als bron voor:
- **Agent-charters**: Bij het opstellen van een Agent-charter moet worden aangegeven tot welke value stream fase(n) de agent behoort, of dat de agent value-stream-overstijgend is.
- **Workspace-beleid**: Workspaces kunnen zich richten op specifieke value streams; dit document biedt de canonieke lijst.
- **Doctrine-documenten**: Specifieke doctrines kunnen gelden per value stream of fase.

Dit document verwijst naar:
- **concepten-en-architectonische-grondslagen.md** (v1.5.0) voor de definitie van "Value stream" en "Value stream fase".
- **constitutie.md** (v1.2.1) als hoogste normatieve bron.

# Overzicht van erkende value streams

## Herkomstverantwoording

Dit normatief artefact is geschreven op basis van de hieronder geraadpleegde
bronnen. Het overzicht van value streams is afgeleid uit de constitutie van
het Mandarin agent-ecosysteem en bestaande governance-documenten, aangevuld
met kennis over value stream management en gebruikersopdrachten.

**Geraadpleegde bronnen**:
- Constitutie Mandarin agent-ecosysteem (versie 1.2.1, gelezen op 2026-01-23 14:00)
- doctrine-it-development.md (gelezen op 2026-01-23 14:00)
- beleid-mandarin-canon.md (gelezen op 2026-01-23 14:00)
- Bestaande value-streams.md (vorige versie met incomplete kennispublicatie
  sectie, gelezen op 2026-01-23 14:00)
- Gebruikersopdracht (ontvangen op 2026-01-23): voeg kennispublicatie value
  stream toe met focus op hoogwaardige, niet AI-herkenbare teksten en publicatie
- Bestaande value-streams.md (versie met kennispublicatie, gelezen op 2026-01-24,
  exacte tijd niet beschikbaar)
- Gebruikersopdracht (ontvangen op 2026-01-24, exacte tijd niet beschikbaar):
  voeg veranderverkenning value stream toe met focus op procesanalyse,
  knelpuntenidentificatie en veranderhypotheses
- Bestaande value-streams.md (versie met veranderverkenning, gelezen op 2026-01-24,
  exacte tijd niet beschikbaar)
- Gebruikersopdracht (ontvangen op 2026-01-24, exacte tijd niet beschikbaar):
  voeg markt-en-investeringsvorming value stream toe met focus op visie,
  marktpositie, businessmodellen en investeringsscenario's
- Bestaande value-streams.md (versie met markt-en-investeringsvorming, gelezen op
  2026-01-25, exacte tijd niet beschikbaar)
- Gebruikersopdracht (ontvangen op 2026-01-25, exacte tijd niet beschikbaar):
  voeg werkvoorbereiding value stream toe met focus op expliciet maken,
  structureren en ordenen van toekomstig werk (thema's, verbeteringen, werktaken)

**Toelichting op structuur en wijzigingen**:
Dit document geeft een workspace-overstijgend overzicht van alle erkende value
streams in het agent-ecosysteem. Per value stream worden doel, stages en
eventuele doctrine-verwijzingen beschreven.

Wijzigingen in deze versie:
- Kennispublicatie value stream volledig uitgewerkt (sectie 3) met focus op
  produceren van niet AI-herkenbare, hoogwaardige teksten
- Kennispublicatie stages toegevoegd: conceptontwikkeling, uitwerking en
  schrijven, redactie en verfijning, publicatie en distributie, evaluatie en
  bijsturing
- Architectuur-en-oplossingsontwerp hernummerd van sectie 5 naar 4
- Veranderverkenning value stream toegevoegd (sectie 4) met focus op
  procesanalyse, knelpuntidentificatie, thema-onderkenning en veranderhypotheses
- Architectuur-en-oplossingsontwerp hernummerd van sectie 4 naar 5
- Markt-en-investeringsvorming value stream toegevoegd (sectie 5) met focus op
  visie, marktpositie, businessmodellen en investeringsscenario's
- Architectuur-en-oplossingsontwerp hernummerd van sectie 5 naar 6
- Werkvoorbereiding value stream toegevoegd (sectie 6) met focus op expliciet
  maken, structureren en ordenen van toekomstig werk
- Architectuur-en-oplossingsontwerp hernummerd van sectie 6 naar 7

---

Dit document geeft een **workspace-overstijgend** overzicht van de value streams
die in het agent eco-systeem worden erkend. Voor elke value stream staat hier:

- waar de bijbehorende doctrine(s) te vinden zijn;
- welke stages (fases) daarin worden onderscheiden, met Nederlandstalige namen.

Het is een aanvulling op de constitutie en de doctrine-documenten in
`artefacten/0-governance/`.

Voor **alle** value streams geldt: zodra er agents worden ingezet om taken
uit te voeren, is de agent-ecosysteem constitutie van toepassing zoals
vastgelegd in de constitutie in `artefacten/0-governance/constitutie.md`.

---

## 1. Agent enablement

De value stream **Agent enablement** richt zich op het ontwerpen, bouwen en
beheren van agents binnen het eco-systeem.

Doel:

- zorgen dat er voor elke behoefte een passende agent-capability is;
- agents duurzaam beheren (introduceren, verbeteren, uitfaseren).

Typische stages (fases):

1. **Behoefte bepalen voor agents**  
   Vaststellen welke capabilities, rollen en automatiseerbare taken nodig zijn.

2. **Ontwerpen van agents**  
   Uitwerken van boundaries, charters, rollen en contracts.

3. **Realiseren van agents**  
   Maken van prompts, runners en benodigde integraties.

4. **Inbedden en beheren van agents**  
   Agents inzetten in workspaces, monitoren, verbeteren en waar nodig uitfaseren.

Een uitgewerkte doctrine voor Agent enablement volgt nog. Tot die tijd worden
deze stages gebruikt als werkbaar referentiekader.

---

## 2. IT-development

De value stream **IT-development** is uitgewerkt in de **Doctrine IT
Development**:

- `doctrine-it-development.md`

Deze doctrine is gebaseerd op SAFe en beschrijft de volledige ontwikkelstroom
van idee tot deployment. De belangrijkste fases (stages) zijn:

1. **Trigger** (A)  
   Initiatie en business cases: kansen identificeren, business value en prioriteit
   bepalen.

2. **Architectuur** (B)  
   Architectuur- en ontwerpbeslissingen: ADR's, patronen, technische richtlijnen.

3. **Specificatie** (C)  
   Requirements, features, datamodellen en processen specificeren, technologie-
   agnostisch.

4. **Ontwerp** (D)  
   Functioneel en technisch ontwerp, API- en contractdesign, data- en
   componentinteracties.

5. **Bouw** (E)  
   Implementatie en integratie: code, scripts, configuratie en CI.

6. **Validatie** (F)  
   Testen en kwaliteitscontrole: geautomatiseerde tests, performance, security.

7. **Deployment** (G)  
   Release en uitrol naar productie: deployment, monitoring en runbooks.

Agents met primary value stream **IT-development** volgen deze doctrine.

---

## 3. Kennispublicatie

De value stream **Kennispublicatie** richt zich op het produceren en publiceren
van hoogwaardige, niet AI-herkenbare teksten die kennis overdragen, inzichten
delen en lezers waardevol informeren.

Doel:

- produceren van teksten die qua stijl, diepgang en originaliteit niet
  onderscheidbaar zijn van menselijk geschreven werk;
- waarborgen van inhoudelijke kwaliteit, leesbaarheid en authenticiteit;
- effectief publiceren en distribueren van kennisproducten naar de juiste
  doelgroepen.

Typische stages (fases):

1. **Conceptontwikkeling**  
   Bepalen van onderwerp, doelgroep, boodschap en tone-of-voice. Verzamelen
   van bronmateriaal en opstellen van contentplan.

2. **Uitwerking en schrijven**  
   Produceren van de tekst met aandacht voor structuur, argumentatie, stijl
   en leesbaarheid. Zorgen voor menselijke nuances en authenticiteit.

3. **Redactie en verfijning**  
   Reviewen en bijschaven van de tekst. Controleren op consistentie, helderheid
   en kwaliteit. Verwijderen van AI-herkenbare patronen of formulering.

4. **Publicatie en distributie**  
   Voorbereiden van het eindproduct voor publicatie. Verzorgen van opmaak,
   metadata en verspreiding via de juiste kanalen.

5. **Evaluatie en bijsturing**  
   Monitoren van respons en impact. Bijsturen van contentstrategie op basis
   van feedback en resultaten.

Deze beschrijving vormt de basis voor een formele **Kennispublicatie-doctrine**
die later in `artefacten/0-governance/` wordt vastgelegd.

---

## 4. Veranderverkenning

De value stream **Veranderverkenning** richt zich op het systematisch analyseren
van bestaande processen, begrippen en knelpunten, en het formuleren van
veranderhypotheses die als basis dienen voor latere oplossings- en
architectuurkeuzes.

Doel:

- in kaart brengen van bestaande processen, systemen en werkwijzen;
- identificeren van knelpunten, inefficiënties en verbetermogelijkheden;
- onderkennen van strategische thema's die richting geven aan verandering;
- formuleren van veranderhypotheses voor epics en thema's;
- beschrijven van concrete verbeteringen als features die later worden uitgewerkt.

Typische stages (fases):

1. **Huidige situatie analyseren** (As-Is Analysis)  
   Verzamelen en documenteren van bestaande processen, systemen en werkwijzen.
   Identificeren van stakeholders, rollen en verantwoordelijkheden. Vastleggen
   van begrippen en definities die binnen de huidige situatie worden gebruikt.

2. **Knelpunten identificeren** (Pain Point Identification)  
   Onderzoeken waar inefficiënties, risico's of problemen zich voordoen.
   Analyseren van root causes en impact. Prioriteren van knelpunten op basis
   van business value en urgentie.

3. **Thema's onderkennen** (Theme Recognition)  
   Clusteren van gerelateerde knelpunten tot strategische thema's. Vaststellen
   van de scope en richting van verandering per thema. Definiëren van de
   gewenste business outcomes en doelstellingen.

4. **Veranderhypotheses formuleren** (Change Hypothesis Formulation)  
   Opstellen van hypotheses over hoe verandering waarde oplevert. Beschrijven
   van epics die de thema's vertalen naar uitvoerbare initiatieven. Valideren
   van aannames en haalbaarheid met stakeholders.

5. **Verbeteringen beschrijven** (Feature Definition)  
   Uitwerken van concrete features die de veranderhypotheses realiseren.
   Specificeren van acceptance criteria en success metrics. Voorbereiden van
   overdracht naar oplossings- en architectuurtrajecten.

Deze beschrijving vormt de basis voor een formele **Veranderverkenning-doctrine**
die later in `artefacten/0-governance/` wordt vastgelegd.

---

## 5. Markt-en-investeringsvorming

De value stream **Markt-en-investeringsvorming** richt zich op het uitwerken
van visie, marktpositie, businessmodellen en investeringsscenario's om de
onderneming levensvatbaar en investeerbaar te maken.

Doel:

- ontwikkelen van een heldere ondernemingsvisie en strategische richting;
- bepalen van marktpositie, propositie en concurrentievoordeel;
- uitwerken van levensvatbare businessmodellen en revenue streams;
- formuleren van investeringsscenario's en financiële haalbaarheid;
- creëren van vertrouwen bij investeerders, stakeholders en partners.

Typische stages (fases):

1. **Visie en strategische richting** (Vision & Strategic Direction)  
   Formuleren van de ondernemingsvisie, missie en langetermijndoelen. Bepalen
   van strategische keuzes en prioriteiten. Identificeren van kernwaarden en
   unique selling points.

2. **Marktanalyse en positionering** (Market Analysis & Positioning)  
   Onderzoeken van doelmarkten, klantbehoeften en concurrentielandschap.
   Bepalen van marktpositie en propositie. Identificeren van
   concurrentievoordelen en differentiatie.

3. **Businessmodel-uitwerking** (Business Model Elaboration)  
   Ontwerpen van businessmodel met revenue streams, kostenstructuur en
   waardeketens. Specificeren van klantrelaties, kanalen en key partnerships.
   Valideren van aannames en haalbaarheid.

4. **Investeringsscenario's en financiële planning** (Investment Scenarios & Financial Planning)  
   Opstellen van investeringsscenario's met financiële prognoses. Uitwerken
   van funding requirements, ROI en break-even analyses. Voorbereiden van
   pitch decks en investeerderscommunicatie.

5. **Go-to-market en realisatie** (Go-to-Market & Realization)  
   Voorbereiden van marktintroductie en commerciële strategie. Opstellen van
   implementatieplannen en mijlpalen. Monitoren van business performance en
   bijsturen van strategie.

Deze beschrijving vormt de basis voor een formele **Markt-en-investeringsvorming-doctrine**
die later in `artefacten/0-governance/` wordt vastgelegd.

---

## 6. Werkvoorbereiding

De value stream **Werkvoorbereiding** is verantwoordelijk voor het expliciet
maken, structureren, ordenen en prioriteren van toekomstig werk in de vorm van
thema's (epics), verbeteringen (features) en werktaken (stories). Deze value
stream ontvangt input uit Veranderverkenning en levert geprioriteerd werk op
dat als input dient voor IT-development en andere realisatie-value streams.

Doel:

- expliciet maken van toekomstig werk door beschrijving en structurering;
- vertalen van veranderhypotheses en knelpunten (uit Veranderverkenning) naar gestructureerde werkitems;
- waarborgen van volledigheid en heldere afbakening per werkitem;
- prioriteren van werk op basis van business value, urgentie en afhankelijkheden;
- opleveren van geprioriteerde backlog die klaar is voor IT-development en realisatie;
- creëren van gedeeld begrip over wat er moet gebeuren en in welke volgorde.

Typische stages (fases):

1. **Thema's identificeren** (Theme Identification)  
   Identificeren en beschrijven van strategische thema's (epics) op basis van
   veranderhypotheses uit Veranderverkenning. Vastleggen van de scope,
   business value en relatie tot organisatiedoelen.

2. **Verbeteringen uitwerken** (Feature Elaboration)  
   Uitwerken van thema's in concrete verbeteringen (features) met heldere
   beschrijvingen, acceptance criteria en afhankelijkheden. Waarborgen dat
   elke feature zelfstandig begrijpelijk is en gereed voor schatting.

3. **Werktaken specificeren** (Story Specification)  
   Opsplitsen van features in uitvoerbare werktaken (stories) met duidelijke
   beschrijving, acceptatiecriteria en definitie van 'done'. Zorgen dat stories
   klein genoeg zijn voor uitvoering binnen één iteratie.

4. **Afhankelijkheden en relaties vastleggen** (Dependencies & Relationships)  
   Identificeren en documenteren van afhankelijkheden tussen werkitems.
   Vastleggen van relaties tussen stories, features en thema's. Detecteren
   van potentiële blokkades en kritieke paden.

5. **Prioritering en backlog-ordening** (Prioritization & Backlog Ordering)  
   Prioriteren van werkitems op basis van business value, risico, afhankelijkheden
   en capaciteit. Ordenen van de backlog voor overdracht naar IT-development.
   Waarborgen dat hoogste prioriteit werk klaar is voor realisatie.

6. **Validatie en overdracht** (Validation & Handover)  
   Reviewen van werkitems en backlog op volledigheid, helderheid en haalbaarheid.
   Verfijnen van beschrijvingen en criteria. Formaliseren van overdracht naar
   IT-development of andere realisatie-value streams.

Deze beschrijving vormt de basis voor een formele **Werkvoorbereiding-doctrine**
die later in `artefacten/0-governance/` wordt vastgelegd.

---

## 7. Architectuur-en-oplossingsontwerp

De value stream **Architectuur-en-oplossingsontwerp** richt zich op het
systematisch ontwerpen van architecturen en oplossingen die beantwoorden aan
complexe vraagstukken, waarbij rekening wordt gehouden met technische,
functionele en organisatorische aspecten.

Doel:

- vertalen van behoeften en eisen naar coherente architectuur- en
  oplossingsconcepten;
- waarborgen van technische haalbaarheid, schaalbaarheid en onderhoudbaarheid;
- creëren van gedeeld begrip tussen stakeholders door heldere architectuur-
  documentatie;
- faciliteren van gefundeerde ontwerpbeslissingen op basis van afwegingen en
  trade-offs.

Typische stages (fases):

1. **Probleemverkenning en context** (Problem Exploration & Context)  
   Begrijpen van het vraagstuk, stakeholders, randvoorwaarden en bestaande
   situatie. Identificeren van drivers, constraints en kwaliteitsattributen.

2. **Conceptueel ontwerp** (Conceptual Design)  
   Uitwerken van architectuurvisie en hoofdlijnen. Definiëren van
   architectuurprincipes, patronen en high-level componenten. Maken van
   initiële architectuurschetsen en conceptuele modellen.

3. **Oplossingsuitwerking** (Solution Elaboration)  
   Detailleren van de gekozen oplossingsrichting. Specificeren van componenten,
   interfaces, data-flows en integraties. Opstellen van Architecture Decision
   Records (ADR's) voor belangrijke ontwerpkeuzes.

4. **Validatie en verfijning** (Validation & Refinement)  
   Toetsen van het ontwerp aan requirements en kwaliteitsattributen. Uitvoeren
   van architecture reviews, proof-of-concepts en haalbaarheidsanalyses.
   Bijstellen op basis van feedback en bevindingen.

5. **Formalisering en overdracht** (Formalization & Handover)  
   Vastleggen van definitieve architectuur in standaard documentatieformaten.
   Voorbereiden van overdracht naar realisatieteams. Opstellen van
   implementatierichtlijnen en architectuurbewakingsafspraken.

Een formele **Doctrine Architectuur-en-oplossingsontwerp** die deze value
stream uitwerkt, inclusief rollen, deliverables en kwaliteitscriteria, volgt
in een later stadium en wordt opgenomen in `artefacten/0-governance/`.

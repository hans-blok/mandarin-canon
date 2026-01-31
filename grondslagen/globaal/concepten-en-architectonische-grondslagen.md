# De Mandarin concepten

**Type**: Concepten en Definities  
**Repository**: mandarin-canon  
**Identifier**: mandarin-canon.concepten.actieve-structuren  
**Version**: 1.3.0  
**Status**: Active  
**Last Updated**: 2026-01-31  
**Owner**: Hans Blok

---

## Herkomstverantwoording

Dit document is opgesteld door Hans Blok op 31 januari 2026 als definitie van concepten en architectonische grondslagen voor actieve structuren in het Mandarin-ecosysteem.

**Opsteller**: Hans Blok  
**Datum**: 2026-01-31  
**Doel**: Expliciete afbakening en structurering van concepten die betrekking hebben op actieve structuren binnen het Mandarin-ecosysteem

**Ontwerpkeuze**: De bewuste scheiding tussen structurele en gedragsmatige aspecten maakt agents voorspelbaarder, toetsbaarder en consistenter. Concepten over gedrag, werking en sturing worden in een afzonderlijk document vastgelegd.

**Normatief fundament**: Dit document vormt onderdeel van de grondslagen binnen mandarin-canon en volgt de documentatie-standaarden conform workspace-doctrine en doctrine-agent-charter-normering.

---

## Inhoudsopgave

### Fundamentele Concepten
- [Mandarin-concept](#mandarin-concept) — Expliciet gedefinieerd, herbruikbaar bouwblok
- [Actieve structuur](#actieve-structuur) — Functioneel element dat handelt en output produceert
- [Mandarin-ecosysteem](#mandarin-ecosysteem) — Overkoepelende context van alle concepten
- [Mandarin-architectuurprincipe](#mandarin-architectuurprincipe) — Richtinggevende regel voor ontwerp

### Capabilities en Value Streams
- [Mandarin-capability](#mandarin-capability) — Duurzaam, herbruikbaar vermogen
- [Value stream](#value-stream) — Samenhangende reeks van activiteiten
- [Value stream fase](#value-stream-fase) — Afgebakende stap binnen value stream
- [Workspace](#workspace) — Bevat alle artefacten voor een specifiek doel

### Agent-Gerelateerde Concepten
- [Mandarin-agent](#mandarin-agent) — Gecharterd element dat taken uitvoert
- [Agent-charter](#agent-charter) — Normatief contract van een agent
- [Agent-capability](#agent-capability) — Wat een agent kan leveren
- [Agent-contract](#agent-contract) — Specificatie van input, output en gedrag
- [Agent-boundary](#agent-boundary) — Expliciete afbakening van verantwoordelijkheid
- [Agent-soort](#agent-soort) — Classificatie op basis van output-type en impact

### Agent-Soorten
- [Adviserende agent](#adviserende-agent) — Levert alleen informatieve output
- [Uitvoerende agent](#uitvoerende-agent) — Wijzigt inhoud en levert artefacten
- [Beheeragent](#beheeragent) — Beheert structuur en configuratie
- [Ecosysteem uitvoerende agent](#ecosysteem-uitvoerende-agent) — Beheert governance-artefacten
- [Waarde uitvoerende agent](#waarde-uitvoerende-agent) — Levert waarde-artefacten

### Agent Positionering
- [Value stream agent](#value-stream-agent) — Agent gebonden aan value stream fasen
- [Utility agent](#utility-agent) — Agent orthogonaal op value streams

### Artefacten
- [Mandarin-artefact](#mandarin-artefact) — Expliciet vastgelegd, overdraagbaar resultaat
- [Governance-artefact](#governance-artefact) — Artefact dat governance vastlegt
- [Waarde-artefact](#waarde-artefact) — Artefact uit value stream fase

### Relaties
- [Relatie value stream ↔ agent-soort](#relatie-value-stream--agent-soort) — Hoe agents aan value streams bijdragen

---

## Inleiding

Dit document beschrijft de concepten die betrekking hebben op de **actieve structuren** van het **Mandarin-ecosysteem**.  
Onder actieve structuren verstaan we de samenstellende en functionele elementen die het ecosysteem laten handelen, samenwerken en output produceren.

Naast de actieve structuren bevat dit document ook de meta-concepten **Mandarin-concept** en **Mandarin-architectuurprincipe**. Deze hebben een beschrijvend en duidend karakter en ondersteunen menselijke leesbaarheid en begripsvorming van het ecosysteem zelf.

De expliciete afbakening en structurering van deze concepten is een **bewuste ontwerpkeuze**. Door structurele en gedragsmatige aspecten strikt te scheiden, worden agents voorspelbaarder in hun handelen, beter toetsbaar en consistenter in hun output. Dit vergroot de bestuurbaarheid van het ecosysteem en zorgt ervoor dat agents aantoonbaar handelen binnen de bedoelde kaders.

Concepten die betrekking hebben op **gedrag, werking en sturing** van het ecosysteem — zoals governance, inferentie, intentie en logging — worden daarom vastgelegd in een afzonderlijk document. Deze scheiding voorkomt vermenging van verantwoordelijkheden en draagt bij aan meer grip op wat agents doen, waarom zij dat doen en wanneer zij moeten escaleren.

### Gebruik van Synoniemen

Bij elk concept worden **synoniemen** vermeld onder de sectie 🏷️. Deze synoniemen zijn **uitsluitend bedoeld voor menselijke spreektaal** en **NIET toegestaan binnen het Mandarin-ecosysteem**.

**Strikte regel**: Binnen het ecosysteem (in governance-artefacten, agent-charters, doctrines, agent-contracts, agent-communicatie) wordt **altijd de volledige, officiële conceptnaam gebruikt**. Synoniemen zijn verboden in formele context.

**Rationale**: Door consequent de officiële conceptnamen te gebruiken, wordt spraakverwarring voorkomen en weten **mandarin-agents** precies wat wordt bedoeld. Synoniemen zijn uitsluitend hulpmiddel voor mensen om het ecosysteem te begrijpen in informele gesprekken.

**Voorbeelden van VERPLICHT gebruik**:
- ✅ **Agent-contract** (NIET: "contract")
- ✅ **Mandarin-artefact** (NIET: "artefact")
- ✅ **Agent-soort** (NIET: "agent-type" of "agent-classificatie")
- ✅ **Mandarin-capability** (NIET: "capability")
- ✅ **Agent-charter** (NIET: "charter")
- ✅ **Governance-artefact** (NIET: "governance-document" of "systeemartefact")
- ✅ **Waarde-artefact** (NIET: "resultaat-artefact" of "value artefact")

**Toegestaan**: In informele menselijke communicatie (gesprekken, notities, brainstorms) mogen synoniemen gebruikt worden voor leesbaarheid. Zodra het ecosysteem wordt geadresseerd (documenten, agent-interacties), gelden de officiële termen.

--- 
## Mandarin-concept

### Definitie 📝
Een **Mandarin-concept** is een expliciet gedefinieerd, samenhangend en herbruikbaar bouwblok binnen het **Mandarin-ecosysteem**, dat een fundamenteel begrip, structuur of mechanisme beschrijft en als referentie dient voor ontwerp, implementatie en governance.

- Is onderdeel van het canon van Mandarin

- Geen tijdelijke afspraak of conventie

- Agent, agent-contract, artefact, value stream, workspace
- Governance-artefact, capability, agent-boundary
Kernbegrip, Bouwsteen

- In Archimate een Concept 

### Toelichting 💬
**Mandarin-concepten** vormen het fundament voor alle verdere uitwerking, structurering en automatisering binnen het **Mandarin-ecosysteem.**

---

## Actieve structuur

### Definitie 📝
Een **actieve structuur** in het **Mandarin-ecosysteem** is een expliciet gedefinieerd, functioneel element dat zelfstandig of in samenwerking met andere structuren taken uitvoert, interactie aangaat en output produceert, en daarmee het dynamisch functioneren van het ecosysteem mogelijk maakt.

### Kenmerken ⭐
- Heeft een expliciete, afgebakende rol of functie binnen het ecosysteem
- Is in staat tot handelen, samenwerken en output genereren
- Is structureel en functioneel onderscheiden van passieve of beschrijvende elementen
- Kan zelfstandig of in samenhang met andere actieve structuren opereren
- Is toetsbaar op gedrag en output

### Wat het niet is ❌
- Geen passief, beschrijvend of uitsluitend informatief element
- Geen tijdelijke of impliciete structuur
- Geen abstracte regel, principe of conventie
- Geen gedrag

### Voorbeelden 💡
- Mandarin-agent
- Workspace
- Value stream

### Synoniemen 🏷️
Functioneel element, Dynamische component

### Analogieën 🔄
- Vergelijkbaar met actieve structuren in ArchiMate (bijv. component, actor, device)
- In softwareontwikkeling: service, proces, actor

### Toelichting 💬
Actieve structuren vormen het handelende en uitvoerende deel van het **Mandarin-ecosysteem**. Zij maken samenwerking, automatisering en waardecreatie mogelijk door expliciet gedrag en output te leveren binnen de afgesproken kaders.

---

## Mandarin-ecosysteem

### Definitie 📝
Het **Mandarin-ecosysteem** is de overkoepelende, samenhangende verzameling van alle **Mandarin-concepten**, **actieve structuren**, **artefacten**, governance-mechanismen en hun onderlinge relaties, die samen een expliciet, adaptief en bestuurbaar geheel vormen voor het realiseren van waarde binnen gedefinieerde **value streams**.

### Kenmerken ⭐
- Omvat alle Mandarin-concepten en hun relaties
- Is uitbreidbaar en aanpasbaar zonder verlies van samenhang
- Waarborgt expliciete contracten en governance
- Biedt een coherent kader voor agents, artefacten en value streams
- Maakt automatisering, samenwerking en waardecreatie mogelijk
- Is adaptief en zelfbeschrijvend (meta-concepten zijn onderdeel van het ecosysteem)

### Wat het niet is ❌
- Geen statisch systeem of vaste architectuur
- Geen enkelvoudige applicatie of tool
- Geen organisatie of bedrijfseenheid
- Geen tijdelijke samenwerkingsvorm

### Voorbeelden 💡
- De combinatie van alle agents, charters, doctrines, workspaces en value streams die samen het Mandarin-systeem vormen
- Het geheel van governance-artefacten en waarde-artefacten in samenhang

### Synoniemen 🏷️
- Mandarin-systeem, Mandarin-omgeving

### Analogieën 🔄
- Vergelijkbaar met een platform-ecosysteem in software (zoals een cloud platform met services, API's en governance)
- In enterprise architectuur: een capability-gebaseerd operating model
- In biologie: een ecosysteem met verschillende soorten en hun interacties

### Toelichting 💬
Het **Mandarin-ecosysteem** vormt de overkoepelende context waarbinnen alle Mandarin-concepten samenkomen en waarde leveren. Het is ontworpen om adaptief, expliciet en samenhangend te zijn. Het ecosysteem is zelfbeschrijvend: de concepten die het ecosysteem beschrijven (zoals **Mandarin-concept** en **Mandarin-architectuurprincipe**) maken zelf deel uit van het ecosysteem.

---
## Mandarin-capability

### Definitie 📝
Een **Mandarin-capability** is een duurzaam, herbruikbaar vermogen van het **Mandarin-ecosysteem** om een bepaald type waarde te realiseren, onafhankelijk van specifieke **agents**, tooling of uitvoering, en inzetbaar binnen één of meer **value stream fasen**.

### Kenmerken ⭐
- Beschrijft wat het ecosysteem kan
- Is stabiel in de tijd
- Is niet aan één agent gekoppeld
- Kan door meerdere agents gerealiseerd worden
- Wordt ingezet door value stream fasen, maar hoort daar niet bij
- Bestaat ook als er (tijdelijk) geen agent actief is

### Voorbeelden 💡
- Veranderhypotheses formuleren

- **Artefact**

### Analogieën 🔄
- Vergelijkbaar met een capability in enterprise architectuur
- In softwareontwikkeling: een herbruikbare service of functie

### Toelichting 💬

---
## Mandarin-architectuurprincipe

### Definitie 📝
Een **Mandarin-architectuurprincipe** is een expliciet geformuleerde, richtinggevende regel of afspraak die het ontwerp, de inrichting en de evolutie van het Mandarin-ecosysteem structureel stuurt en begrenst, en die als toetssteen geldt voor alle architecturale keuzes binnen het ecosysteem.

### Kenmerken ⭐
- Is expliciet vastgelegd en breed gedragen binnen het ecosysteem
- Geen operationele regel of processtap
- Geen organisatieprincipe of bedrijfswaarde
- "Artefacten zijn altijd overdraagbaar en inspecteerbaar"
- "Governance is gescheiden van uitvoering"
Ecosysteemprincipe

- In softwareontwikkeling: design principle, guiding rule

---

## Mandarin-agent

### Definitie 📝
Een **mandarin-agent** is een expliciet gedefinieerde, autonome software-entiteit binnen het **Mandarin-ecosysteem** die, op basis van een formeel agent-charter en agent-contract, specifieke taken uitvoert, Mandarin-artefacten produceert of informatie levert, en daarbij altijd opereert binnen een afgebakende agent-boundary en volgens de geldende governance.

### Kenmerken ⭐
- Heeft een expliciet agent-charter en agent-contract
- Is autonoom en verantwoordelijk voor eigen uitvoering binnen boundary
- Voert één of meer agent-capabilities uit
- Produceert Mandarin-artefacten of levert informatie
- Is herbruikbaar en vervangbaar binnen het ecosysteem
- Werkt altijd volgens expliciete input/output-afspraken

### Wat het niet is ❌
- Geen impliciete of ad-hoc softwarecomponent
- Geen menselijke actor
- Geen agent zonder expliciet agent-contract of agent-charter
- Geen monolithische applicatie

### Voorbeelden 💡
- Mandarin architect, Logisch datamodelleur, Technisch datamodelleur, Agent smeder

### Synoniemen 🏷️
- Agent, Software-agent

### Analogieën 🔄
- Vergelijkbaar met een microservice, bot of autonome service in softwareontwikkeling
- In enterprise architectuur: een performer of actor met expliciete verantwoordelijkheden

### Toelichting 💬
Een **mandarin-agent** is altijd expliciet ontworpen, beschreven en begrensd. De agent ontleent zijn legitimiteit aan het **agent-charter** en het **agent-contract**, en is alleen via formele interfaces aanspreekbaar. Dit waarborgt consistentie, vervangbaarheid en governance binnen het **Mandarin-ecosysteem**.

---

## Agent-charter

### Definitie 📝
Een **agent-charter** is een formeel, expliciet document dat de missie, verantwoordelijkheden, grenzen en governance van een specifieke **mandarin-agent** vastlegt, en daarmee de legitimiteit, autonomie en het bestaansrecht van de agent binnen het **Mandarin-ecosysteem** waarborgt.

### Kenmerken ⭐
- Legt de missie en het bestaansrecht van de agent vast
- Bepaalt de grenzen (boundary) en verantwoordelijkheden
- Beschrijft de governance, policies en randvoorwaarden
- Is expliciet, versieerbaar en bindend
- Is leidend voor ontwerp, implementatie en evaluatie van de agent
- Vormt de basis voor het agent-contract

### Wat het niet is ❌
- Geen impliciete afspraak of mondelinge instructie
- Geen technische specificatie of implementatiedocument
- Geen agent-contract (maar vormt wel de basis daarvoor)
- Geen tijdelijke of informele notitie

### Voorbeelden 💡
- Charter van een publicatie-agent waarin missie, scope en governance zijn vastgelegd
- Charter van een beheeragent met expliciete operationele grenzen

### Synoniemen 🏷️
- Mandaat, rolbeschrijving

### Analogieën 🔄
- Vergelijkbaar met een projectcharter, mandaat of mission statement in projectmanagement
- In enterprise architectuur: purpose statement of governance charter

### Toelichting 💬
Het **agent-charter** is het fundament voor de legitimiteit en autonomie van een agent. Zonder charter bestaat een agent niet formeel binnen het **Mandarin-ecosysteem**. Het **agent-charter** is leidend voor alle ontwerp- en governancekeuzes rondom de **mandarin-agent**.

---
## Agent-capability

### Definitie 📝
Een **agent-capability** is een expliciet aanroepbare functie van een **mandarin-agent**, vastgelegd in een **agent-contract**.

### Kenmerken ⭐
- Eén capability = één intent / operation
- Capability bestaat alleen in het **agent-contract**
- Capability is aanroepbaar (uitvoerbaar), niet beschrijvend

### Wat het niet is ❌
- Geen beschrijvende eigenschap
- Geen interne implementatie
- Geen losstaande functie buiten contract

### Voorbeelden 💡
- workflow-architect.1-ontwerp.workflow
- vertaler.vertaal

### Synoniemen 🏷️
- Intent, Intentie

### Analogieën 🔄
- Vergelijkbaar met een operation in een API
- In softwareontwikkeling: een expliciete functie of methode

### Toelichting 💬
Soms wordt dit de prompt genoemd. In Mandarin noemen we dit niet de prompt!

---

## Agent-contract

### Definitie 📝
Een **agent-contract** definieert formeel de intent (**agent-capability**) van de **mandarin-agent**, de input die het verwacht en de output (**artefact**) die hij creëert of antwoorden die hij geeft, evenals de beleidsregels en beperkingen waaronder die mogelijkheden toegankelijk zijn.
 
 ### Wat het niet is ❌
 - Geen beschrijving van interne werking
 - Geen implementatiedetails
 - Geen impliciet agent-contract

### Voorbeelden 💡
 - Zie mandarin-architect.schrijf-concept.agent.md
 - Zie workflow-architect.1-ontwerp-workflow.agent.md

### Synoniemen 🏷️
 Service contract, Interface contract

### Analogieën 🔄
 - Vergelijkbaar met een API-agent-contract in softwareontwikkeling
 - In SOA: WSDL of service agreement

### Toelichting 💬
Totdat agent-charter en agent-contract bestaan, is dit géén agent, maar een agent-capability-voornemen.

---
## Agent-boundary

### Definitie 📝
Een **agent-boundary** is de expliciet vastgelegde servicegrens waarbinnen een **mandarin-agent** zijn interne werking, governance en **agent-capabilities** organiseert, en waarbuiten interactie uitsluitend plaatsvindt via formele **agent-contracts**.

### Kenmerken ⭐
- Bepaalt wat tot de agent behoort en wat daarbuiten ligt
- Scheidt interne werking van externe interactie
- Is leidend voor governance en autonomie van de agent
- Waarborgt dat alleen via contracten interactie mogelijk is
- Is de eerste en verplichte stap in agent-ontwerp

### Wat het niet is ❌
- Geen impliciete grens
- Geen technische implementatiegrens
- Geen optionele ontwerpkeuze

### Voorbeelden 💡
- De mapstructuur van een agent in een repository
- De scope van een agent in een C4-model

### Synoniemen 🏷️
- Agent-grens
- Service boundary

### Analogieën 🔄
- Vergelijkbaar met een bounded context in DDD, een microservice boundary, of een package boundary in OOP
- In SOA: service boundary waarbinnen interne details verborgen blijven
- Workspace als project workspace, repository, of solution folder
- In DevOps: deployment workspace of CI/CD pipeline context

### Toelichting 💬
Het expliciet definiëren van de agent-boundary voorkomt dat agents samenvallen met tooling of prompts, verantwoordelijkheden vervagen of contracten impliciet worden. Alles binnen de boundary valt onder het agent-charter, de bijbehorende agent-contracten en de interne governance van de agent. Alles buiten de boundary is alleen toegankelijk via formele, expliciete contracten.

---
## Agent-soort

### Definitie 📝
Een **agent-soort** is een expliciete classificatie van **mandarin-agents** op basis van het type output dat zij leveren en de structurele impact die zij veroorzaken binnen het **Mandarin-ecosysteem**.

### Kenmerken ⭐
- Is een taxonomische indeling van agents
- Onderscheidt agents op basis van output-type en impact
- Bepaalt welke governanceregels van toepassing zijn
- Maakt duidelijk welke rol een agent speelt in het ecosysteem
- Is leidend voor contractontwerp en template-vereisten
- Bepaalt of een agent aan value stream fasen wordt toegekend:
  - **Adviserende agents** en **uitvoerende agents** → toegekend aan één of meerdere value stream fasen
  - **Beheeragents** → opereren in alle fasen
  - Orthogonaal hierop: **utility agents** (niet aan fasen gebonden)

### Wat het niet is ❌
- Geen rol of functie van een specifieke agent
- Geen technische implementatievariant
- Geen tijdelijke of impliciete classificatie
- Geen agent zelf, maar een categorisering ervan

### Voorbeelden 💡
- Adviserende agent — levert alleen informatie
- Uitvoerende agent — levert artefacten (met sub-typen: ecosysteem uitvoerend, waarde uitvoerend)
- Beheeragent — beheert workspace en runtime

### Synoniemen 🏷️
- Agent-type
- Agent-classificatie
- Agent-categorie

### Analogieën 🔄
- Vergelijkbaar met een actor-type in enterprise architectuur
- In software engineering: service type (read-only, write, admin)
- In objectgeoriënteerd ontwerp: interface-classificatie

### Toelichting 💬
Het concept **agent-soort** maakt het mogelijk om agents te groeperen naar hun fundamentele verantwoordelijkheid en impact. Elke agent-soort heeft eigen governanceregels (bijvoorbeeld: uitvoerende agents hebben verplichte templates, adviserende agents niet). De agent-soort wordt vastgelegd in het **agent-charter** en bepaalt mede welke normen uit **doctrine-agent-charter-normering** van toepassing zijn.

---
## Mandarin-artefact

### Definitie 📝
Een **Mandarin-artefact** is een duurzame, expliciete en overdraagbare vastlegging van resultaat of besluitvorming, die binnen een **value stream fase** waarde representeert en als input kan dienen voor vervolgwerk.

### Kenmerken ⭐
- Duurzaam (blijft bestaan)
- Expliciet (leesbaar, inspecteerbaar)
- Overdraagbaar (kan door anderen of agents gebruikt worden)
- Waarde-dragend (vertegenwoordigt gerealiseerde waarde)

### Wat het niet is ❌
- Geen tijdelijke notitie
- Geen impliciete kennis
- Geen niet-overdraagbaar resultaat

### Voorbeelden 💡
- Zie: **waarde-artefacten** en **governance-artefacten**

### Synoniemen 🏷️
- **Artefact**

### Analogieën 🔄
- Vergelijkbaar met een **artefact** in softwareontwikkeling (build-artifact, document)
- In projectmanagement: **deliverable**
- In DDD: **Aggregate Result** of **Documented Outcome**

### Toelichting
Er zijn twee hoofdklassen van **artefacten**: **governance-artefacten** en **waarde-artefacten**.

---

## Governance-artefact

### Definitie 📝
Een **governance-artefact** is een normatieve of contractuele vastlegging die het functioneren van het **Mandarin-ecosysteem** mogelijk maakt, maar zelf geen directe waarde levert in een **value stream fase**.

### Kenmerken ⭐
- Levert geen business- of oplossingswaarde
- Is geen output van value stream fasen
- Maakt waardecreatie mogelijk
- Is randvoorwaardelijk

### Wat het niet is ❌
- Geen waarde-artefact
- Geen resultaat van een value stream fase
- Geen input voor volgende fasen

### Voorbeelden 💡
- Agent-charter
- Agent-contract (.agent.md)
- Prompt (.prompt.md)
- Templates
- Beleid / constitutie

### Synoniemen 🏷️
- **Systeem-artefact**
- **Ecosysteem-artefact**

### Analogieën 🔄
- Vergelijkbaar met **policies**, **API contracts**, **infrastructuurdefinities** in DevOps
- In SOA: **WSDL's**, **policies**, **service agreements**

### Toelichting 💬
Deze artefacten horen bij het ecosysteem, niet bij een value stream fase.

---
## Waarde-artefact

### Definitie 📝
Een **waarde-artefact** is een **artefact** dat expliciet het resultaat van een **value stream fase** vastlegt en daarmee gerealiseerde waarde vertegenwoordigt.

### Kenmerken ⭐
- Ontstaat binnen een value stream fase
- Vertegenwoordigt voortgang en waarde
- Is input voor volgende fasen
- Wordt geleverd door uitvoerende agents

### Wat het niet is ❌
- Geen governance-artefact
- Geen randvoorwaardelijk document
- Geen interne notitie

### Voorbeelden 💡
- Logisch datamodel
- Architectuurmodel
- C4-DSL
- SQL / PostgreSQL-schema
- Requirements, specificaties
- Ontwerpdocumenten
- Code, configuratie

### Synoniemen 🏷️
Value artefact
Resultaat-artefact

### Analogieën 🔄
- Vergelijkbaar met business deliverables, user stories, output van een pipeline
- In DDD: Entities of Value Objects als resultaat van een proces

### Toelichting 💬
Waarde-artefacten zijn de tastbare resultaten van het werk binnen value streams.
---## Adviserende agent

### Definitie 📝
Een **adviserende agent** levert uitsluitend informatieve output (advies, analyse, overzicht) en veroorzaakt geen duurzame wijziging in het **Mandarin-ecosysteem**.

### Kenmerken ⭐
- Maakt geen artefacten
- Wijzigt geen bestanden
- Veroorzaakt geen side-effects
- Produceert tekstuele of visuele output
- Output is ephemeral (verdwijnt na gebruik)
- Output is niet-normatief
- Geen templates vereist
- Output is niet bedoeld voor downstream automatisering
- **Fase-toekenning**: Adviserende agents kunnen worden toegekend aan één of meerdere value stream fasen

### Wat het niet is ❌
- Geen uitvoerende agent
- Geen beheeragent
- Geen agent die artefacten of structurele wijzigingen veroorzaakt

### Voorbeelden 💡
- Analyse- of adviesagent
- Agent die alleen rapportages of overzichten maakt

### Synoniemen 🏷️
- Adviesagent
- Analyseagent

### Analogieën 🔄
- Function-style service in SOA
- Query/read-only service

### Toelichting 💬
De adviserende agent ondersteunt met informatie, maar levert geen artefacten of structurele waarde.

---
## Uitvoerende agent

### Definitie 📝
Een **uitvoerende agent** levert duurzame **artefacten** als expliciet onderdeel van een **value stream** en veroorzaakt daarmee structurele wijziging in de **workspace**.

### Kenmerken ⭐
- Maakt artefacten (documenten, modellen, DSL, code, configuratie)
- Output is persistent
- Output is downstream input voor andere agents of mensen
- Output MOET voldoen aan een vooraf gedefinieerd template
- Template is verplicht onderdeel van capability policy
- Contract faalt als template ontbreekt
- **Fase-toekenning**: Uitvoerende agents kunnen worden toegekend aan één of meerdere value stream fasen

### Wat het niet is ❌
- Geen adviserende agent
- Geen beheeragent
- Wijzigt geen governance of workspace-inrichting
- Geen agent die alleen informatie levert

### Voorbeelden 💡
- Agent die code, modellen of documenten oplevert
- Agent die een artefact toevoegt aan de workspace

### Synoniemen 🏷️
- Producerende agent
- Artefact-agent

### Analogieën 🔄
- Resource-creating service in SOA
- Command met persistent effect
- Write-side van een value stream

### Toelichting 💬
De uitvoerende agent levert tastbare resultaten en structurele wijzigingen in de workspace.

---
## Beheeragent

### Definitie 📝
Een **beheeragent** wijzigt de operationele staat van de **workspace** of runtime-omgeving, zonder waarde-**artefacten** te produceren.

### Kenmerken ⭐
- Wijzigt bestanden zoals .gitignore, folders, config
- Start/stop containers of tooling
- Produceert geen waarde-artefacten
- Levert geen inhoudelijke waarde aan de value stream
- **Fase-toekenning**: Beheeragents zijn NIET gebonden aan specifieke fasen, maar opereren in **alle fasen** van alle value streams
- Primair voorbeeld: **Moeder agent**

### Wat het niet is ❌
- Geen adviserende agent
- Geen uitvoerende agent
- Geen agent die artefacten of structurele waarde levert

### Voorbeelden 💡
- Agent die .gitignore of config-bestanden aanpast
- Agent die een container start of stopt

### Synoniemen 🏷️
- Operationele agent
- Systeemagent

### Analogieën 🔄
- Administrative/management API in SOA
- Infrastructure service
- Control-plane gedrag

### Toelichting 💬
De beheeragent ondersteunt de operationele kant van de workspace, maar levert geen artefacten of directe waarde in de value stream.

---
## Value stream

### Definitie 📝
Een **value stream** is een expliciet gedefinieerde keten van waarde-creërende stappen die samen leiden tot een herkenbaar resultaat, en die richting geeft aan welke **artefacten**, **mandarin-agents** en beslissingen bijdragen aan die waarde.

### Kenmerken ⭐
- Definieert stappen, geen taken
- Is artefact-gericht
- Is agent-agnostisch, maar agent-sturend
- Meerdere value streams per ecosysteem mogelijk

### Wat het niet is ❌
- Geen workflow of proces
- Geen lijst van taken
- Geen beschrijving van implementatie

### Voorbeelden 💡
- IT-development value stream
- Kennispublicatie value stream
- Werkvoorbereiding value stream

### Synoniemen 🏷️
- Waardestroom

### Analogieën 🔄
- Vergelijkbaar met een waardeketen in Lean of een pipeline in DevOps

### Toelichting 💬
Value streams structureren het werk en maken waardecreatie inzichtelijk via expliciete stappen en artefacten.

---
## Value stream fase

### Definitie 📝
Een **value stream fase** is een logisch afgebakende, waarde-creërende eenheid binnen een **value stream**, waarin een specifiek type waarde tot stand komt, herkenbaar via expliciete **artefacten** en kwaliteitscriteria, onafhankelijk van de wijze van uitvoering.

### Kenmerken ⭐
- Is een waardemoment, geen handeling
- Beschrijft wat voor waarde ontstaat, niet hoe
- Heeft een helder doel binnen de value stream
- Wordt zichtbaar via expliciete artefacttypen en bijbehorende kwaliteitsverwachtingen
- Vormt context voor agents die daarin opereren
- Produceert geen taken en stuurt geen workflow

### Wat het niet is ❌
- Geen proces
- Geen stappenplan
- Geen activiteit of taak
- Geen agent of rol
- Geen implementatiefase

### Voorbeelden 💡
- Analyse-fase
- Ontwerpfase
- Realisatie-fase

### Synoniemen 🏷️
- Waardemoment
- Fase

### Analogieën 🔄
- Vergelijkbaar met een stage in een pipeline
- In Lean: een waardemoment in de waardestroom

### Toelichting 💬
**Value stream fasen** structureren het werk en maken expliciet welke waarde in elke stap ontstaat. **Artefacten** zijn herleidbaar van **mandarin-agent** → **value stream fase** → **value stream**.

---
## Workspace

### Definitie 📝
Een **workspace** is een afgebakende werkomgeving die wordt ingericht om één of meer **value stream fasen** uit te werken, met bijbehorende **artefacten**, governance en ondersteunende **agents**.

### Kenmerken ⭐
- Activeert agents
- Contextualiseert werk tot specifieke fasen
- Kan één of meerdere fasen ondersteunen
- Agents worden gefetched uit de Mandarin workspace

### Wat het niet is ❌
- Geen **value stream**
- Geen **mandarin-agent**
- Geen **artefact**

### Voorbeelden 💡
- **Workspace** voor alleen Veranderverkenning
- **Workspace** voor Werkvoorbereiding + Specificatie

### Synoniemen 🏷️
- Werkomgeving

### Analogieën 🔄
- Vergelijkbaar met een project workspace, repository of solution folder

### Toelichting 💬
In de eerste fase van ontwikkeling worden agents gefetched uit de Mandarin workspace. De workspaces bevatten dus wel agents, maar deze worden hier niet aangepast. In die zin 'bevatten' deze workspaces geen agents.

---
## Uitvoerende agent

### Definitie 📝
Een **uitvoerende agent** is een **mandarin-agent** die duurzame **artefacten** levert als expliciet onderdeel van een **value stream** en daarmee structurele wijziging veroorzaakt in de **workspace**.

Er zijn twee sub-typen:
- **Ecosysteem uitvoerende agent** — levert governance-artefacten
- **Waarde uitvoerende agent** — levert waarde-artefacten

### Kenmerken ⭐
- Maakt artefacten (documenten, modellen, DSL, code, configuratie)
- Output is persistent
- Output is downstream input voor andere agents of mensen
- Output MOET voldoen aan een vooraf gedefinieerd template
- Template is verplicht onderdeel van capability policy
- Contract faalt als template ontbreekt
- **Fase-toekenning**: Uitvoerende agents kunnen worden toegekend aan één of meerdere value stream fasen

### Wat het niet is ❌
- Geen adviserende agent
- Geen beheeragent
- Wijzigt geen governance of workspace-inrichting (tenzij ecosysteem uitvoerende agent)
- Geen agent die alleen informatie levert

### Voorbeelden 💡
- Agent die code, modellen of documenten oplevert
- Agent die een artefact toevoegt aan de workspace
- Agent die governance-artefacten publiceert (ecosysteem uitvoerend)

### Synoniemen 🏷️
- Producerende agent
- Artefact-agent

### Analogieën 🔄
- Resource-creating service in SOA
- Command met persistent effect
- Write-side van een value stream

### Toelichting 💬
De uitvoerende agent levert tastbare resultaten en structurele wijzigingen in de workspace. Dit concept is de parent van zowel ecosysteem uitvoerende agent als waarde uitvoerende agent.

---
## Ecosysteem uitvoerende agent

### Definitie 📝
Een **ecosysteem uitvoerende agent** is een agent die artefacten of wijzigingen levert die het functioneren, de governance of de structuur van het Mandarin-ecosysteem zelf beïnvloeden, zonder directe waarde te leveren in een value stream fase.

### Kenmerken ⭐
- Levert governance-artefacten, policies, templates of systeemwijzigingen
- Wijzigt de randvoorwaarden of structuur van het ecosysteem
- Heeft geen directe business-waarde in een value stream
- Is essentieel voor het functioneren en de samenhang van het ecosysteem

### Wat het niet is ❌
- Geen uitvoerende agent binnen een value stream
- Geen adviserende agent
- Geen agent die waarde-artefacten levert

### Voorbeelden 💡
- Agent die een nieuw governance-artefact publiceert
- Agent die policies of templates aanpast
- Agent die systeeminstellingen wijzigt

### Synoniemen 🏷️
Governance-agent
Systeem-agent

### Analogieën 🔄
- Vergelijkbaar met een infrastructuurbeheerder in DevOps
- In enterprise architectuur: policy manager, platformbeheerder

### Toelichting 💬
De ecosysteem uitvoerende agent zorgt voor de randvoorwaarden en structuur waarbinnen alle andere agents en value streams kunnen functioneren.

---

## Waarde uitvoerende agent

### Definitie 📝
Een **waarde uitvoerende agent** is een agent die expliciete waarde-artefacten levert als resultaat van een value stream fase, en daarmee directe waarde toevoegt aan het Mandarin-ecosysteem.

### Kenmerken ⭐
- Levert waarde-artefacten (documenten, modellen, code, configuratie)
- Werkt binnen een value stream fase
- Output is persistent en overdraagbaar
- Output is input voor volgende fasen of agents
- Moet voldoen aan vooraf gedefinieerde templates en kwaliteitscriteria

### Wat het niet is ❌
- Geen ecosysteem uitvoerende agent
- Geen adviserende agent
- Geen agent die alleen informatie levert

### Voorbeelden 💡
- Agent die een ontwerpdocument oplevert
- Agent die code of configuratie toevoegt aan de workspace
- Agent die een model of specificatie publiceert

### Synoniemen 🏷️
Business-agent
Producerende agent

### Analogieën 🔄
- Vergelijkbaar met een resource-creating service in SOA
- In softwareontwikkeling: developer, modelleur, documentgenerator

### Toelichting 💬
De waarde uitvoerende agent levert tastbare resultaten en directe waarde binnen het Mandarin-ecosysteem, als onderdeel van een value stream.

---

## Value stream agent

### Definitie 📝
Een **value stream agent** is een **adviserende agent** of **uitvoerende agent** die expliciet is toegekend aan één of meerdere **value stream fasen** en daar specifieke waarde of inzicht levert.

### Kenmerken ⭐
- Gebonden aan specifieke value stream fase(n)
- Produceert waarde-artefacten, governance-artefacten of informatieve output binnen hun toegekende fase(n)
- Opereert binnen de grenzen van hun toegekende fase(n)
- Agent-soort: adviserende agent of uitvoerende agent (inclusief sub-typen)
- Mag niet buiten de scope van hun toegekende fase(n) treden

### Wat het niet is ❌
- Geen beheeragent (beheeragents opereren in alle fasen)
- Geen utility agent (utility agents staan orthogonaal op value streams)
- Geen agent zonder fase-toekenning

### Voorbeelden 💡
- **Constitutioneel Auteur** — ecosysteem uitvoerende agent, fase: Grondslagvorming
- **Canon Curator** — ecosysteem uitvoerende agent, fase: Ecosysteeminrichting
- **Feature-analist** — waarde uitvoerende agent, value stream: Softwareontwikkeling, fase: Analyse
- **Service-architect** — waarde uitvoerende agent, value stream: Softwareontwikkeling, fase: Ontwerp
- **Architectuuradviseur** — adviserende agent, value stream: Architectuur- en Oplossingsontwerp, fase: Oplossingsontwerp

### Synoniemen 🏷️
- Value stream gebonden agent
- Fase-agent

### Analogieën 🔄
- Vergelijkbaar met een role-based actor in een proces
- In SAFe: een rol die specifiek in één of meerdere program increments werkt
- In DevOps: een pipeline-stage-specifieke service

### Toelichting 💬
**Value stream agents** zijn de tegenterm van **utility agents**. Waar value stream agents expliciet aan fasen zijn gebonden en daar specifieke waarde leveren, staan utility agents orthogonaal op de value stream structuur en zijn generiek inzetbaar.

Bij het opstellen van een **Agent-charter** voor een value stream agent moet expliciet worden aangegeven:
- Tot welke value stream de agent behoort
- Tot welke fase(n) de agent is toegekend
- Welke waarde of inzicht de agent in die fase(n) levert

---

## Utility agent

### Definitie 📝
Een **utility agent** is een **mandarin-agent** die **orthogonaal** op de **value stream** structuur staat en generieke, ondersteunende diensten levert die niet specifiek aan één value stream fase zijn gebonden.

### Kenmerken ⭐
- Niet gebonden aan value stream fasen
- Levert technische of ondersteunende capabilities
- Kan in willekeurige contexten worden ingezet
- Kan door meerdere value streams en agents worden gebruikt
- Produceert ondersteunende artefacten, geen waarde-artefacten
- Valt wel onder dezelfde governance-principes als andere agents
- Heeft een Agent-charter dat scope en verantwoordelijkheden vastlegt

### Wat het niet is ❌
- Geen value stream agent (niet aan fasen gebonden)
- Geen beheeragent (wijzigt geen workspace-structuur)
- Geen agent met specifieke value stream fase-toekenning

### Voorbeelden 💡
- **format-vertaler** — transformeert documenten tussen formaten (Markdown ↔ Word)
- **kort-schrijver** — herformuleert en optimaliseert teksten
- **docker-steward** — beheert container-infrastructuur
- **python-expert** — schrijft en reviewt Python-scripts
- **layout-optimizer** — optimaliseert documentstructuur
- **publicatie-agent** — publiceert artefacten naar diverse kanalen

### Synoniemen 🏷️
- Ondersteunende agent
- Generieke agent
- Hulpagent

### Analogieën 🔄
- Vergelijkbaar met shared services in enterprise architectuur
- In DevOps: cross-cutting concerns of platform services
- In software engineering: utility libraries of helper functions

### Toelichting 💬
**Utility agents** staan orthogonaal op de value stream structuur. Dit betekent dat zij niet aan specifieke fasen zijn gebonden, maar in willekeurige contexten kunnen worden ingezet om ondersteunende diensten te leveren.

**Verschil met value stream agents**:

| Aspect | Value stream agent | Utility agent |
|--------|-------------------|---------------|
| **Value stream koppeling** | Ja, specifieke value stream | Nee, orthogonaal |
| **Fase koppeling** | Ja, één of meerdere fasen | Nee, willekeurig inzetbaar |
| **Primaire output** | Waarde-artefacten, governance-artefacten of informatieve output | Ondersteunende artefacten |
| **Scope** | Beperkt tot toegekende fase(n) | Generiek, meerdere contexten |

**Verschil met beheeragents**:
- Beheeragents opereren in **alle fasen** en wijzigen workspace-structuur
- Utility agents zijn **niet fase-gebonden** en leveren ondersteunende diensten zonder structurele wijziging

Bij het opstellen van een **Agent-charter** voor een utility agent moet expliciet worden aangegeven:
- Dat de agent een utility agent is (niet aan value stream fasen gebonden)
- Welke generieke diensten de agent levert
- In welke contexten de agent kan worden ingezet

---

## Change Log

| Datum      | Versie | Wijziging                                                           | Auteur     |
|------------|--------|---------------------------------------------------------------------|------------|
| 2026-01-31 | 1.3.0  | Toevoeging concepten Value stream agent en Utility agent; verduidelijking fase-toekenning per agent-soort: adviserende/uitvoerende agents aan fasen, beheeragents in alle fasen, utility agents orthogonaal | Constitutioneel Auteur  |
| 2026-01-31 | 1.2.1  | Aanscherping "Gebruik van Synoniemen" — Synoniemen VERBODEN binnen ecosysteem, uitsluitend toegestaan in menselijke spreektaal; voorbeelden toegevoegd | Canon Curator  |
| 2026-01-31 | 1.2.0  | Subsectie toegevoegd in Inleiding: "Gebruik van Synoniemen" — Verduidelijkt dat synoniemen spreektaal zijn en niet erkend binnen ecosysteem | Canon Curator  |
| 2026-01-31 | 1.1.1  | Herstel Mandarin-ecosysteem definitie — Ontbrekende definitie-sectie toegevoegd | Canon Curator  |
| 2026-01-31 | 1.1.0  | Toevoeging definitie Agent-soort — Expliciete classificatie toegevoegd | Canon Curator  |
| 2026-01-31 | 1.0.0  | Initiële versie — Concepten en definities voor actieve structuren opgesteld | Hans Blok  |

---

**Einde document**

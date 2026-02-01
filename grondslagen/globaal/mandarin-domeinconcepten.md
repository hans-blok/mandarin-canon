# De Mandarin concepten

**Type**: Concepten en Definities 
**Repository**: mandarin-canon 
**Identifier**: mandarin-canon.concepten.actieve-structuren 
**Version**: 2.3.0 
**Status**: Active 
**Last Updated**: 2026-02-01 
**Owner**: Hans Blok

---

## Herkomstverantwoording

Dit document is opgesteld door Hans Blok op 31 januari 2026 als definitie van concepten en architectonische grondslagen voor actieve structuren in het Mandarin-ecosysteem.

**Geraadpleegde bronnen**:


**Opsteller**: Hans Blok 
**Datum**: 2026-01-31 
**Laatste wijziging**: 2026-02-01 (Constitutioneel Auteur) 
**Doel**: Expliciete definitie van operationele concepten (actieve structuren) binnen het Mandarin-ecosysteem

**Ontwerpkeuze**: De bewuste scheiding tussen operationele concepten (actieve structuren en hun werking) en meta-concepten (classificatie en artefactstructuur) maakt **mandarin-agents** voorspelbaarder, toetsbaarder en consistenter. Meta-concepten zijn verplaatst naar mandarin-meta-concepten.md. Concepten over gedrag, werking en sturing worden vastgelegd in een afzonderlijk document.

**Normatief fundament**: Dit document vormt onderdeel van de grondslagen binnen mandarin-canon en volgt de documentatie-standaarden conform workspace-doctrine en doctrine-agent-charter-normering.

---

## Inhoudsopgave

### Fundamentele Concepten
- [Mandarin-concept](#mandarin-concept) — Expliciet gedefinieerd, herbruikbaar bouwblok
- [Actieve structuur](#actieve-structuur) — Functioneel element dat handelt en output produceert
- [Mandarin-ecosysteem](#mandarin-ecosysteem) — Overkoepelende context van alle concepten

### Capabilities
- [Mandarin-capability](#mandarin-capability) — Duurzaam, herbruikbaar vermogen

### mandarin-agent-gerelateerde Concepten
- [Mandarin-agent](#mandarin-agent) — Gecharterd element dat taken uitvoert
- [agent-boundary](#agent-boundary) — Expliciete servicegrens van een **mandarin-agent**
- [agent-charter](#agent-charter) — Missie, verantwoordelijkheid en governance van een **mandarin-agent**
- [agent-capability](#agent-capability) — Aanroepbare functie van een **mandarin-agent**
- [agent-contract](#agent-contract) — Specificatie van intentie, input, output en beleid
 - [Prompt](#prompt) — Concreet aanroep- of instructiepatroon richting een **mandarin-agent**

### Artefacten en Value Streams
- [Mandarin-artefact](#mandarin-artefact) — Duurzame, overdraagbare vastlegging van resultaat
- [Template](#template) — Herbruikbare structuur voor artefacten en prompts
- [Value stream](#value-stream) — Waarde-creërende keten van stappen
- [Value stream fase](#value-stream-fase) — Waardemoment binnen een value stream
- [Workspace](#workspace) — Afgebakende werkomgeving voor value stream fasen

---

## Inleiding

Dit document beschrijft de concepten die betrekking hebben op de **actieve structuren** van het **Mandarin-ecosysteem**. 
Onder actieve structuren verstaan we de samenstellende en functionele elementen die het ecosysteem laten handelen, samenwerken en output produceren.

Naast de actieve structuren bevat dit document ook de meta-concepten **Mandarin-concept** en **Mandarin-architectuurprincipe**. Deze hebben een beschrijvend en duidend karakter en ondersteunen menselijke leesbaarheid en begripsvorming van het ecosysteem zelf.

De expliciete afbakening en structurering van deze concepten is een **bewuste ontwerpkeuze**. Door structurele en gedragsmatige aspecten strikt te scheiden, worden **mandarin-agents** voorspelbaarder in hun handelen, beter toetsbaar en consistenter in hun output. Dit vergroot de bestuurbaarheid van het ecosysteem en zorgt ervoor dat **mandarin-agents** aantoonbaar handelen binnen de bedoelde kaders.

Concepten die betrekking hebben op **gedrag, werking en sturing** van het ecosysteem — zoals governance, inferentie, intentie en logging — worden daarom vastgelegd in een afzonderlijk document. Deze scheiding voorkomt vermenging van verantwoordelijkheden en draagt bij aan meer grip op wat **mandarin-agents** doen, waarom zij dat doen en wanneer zij moeten escaleren.

### Gebruik van Synoniemen

Bij elk concept worden **synoniemen** vermeld onder de sectie 🏷️. Deze synoniemen zijn **uitsluitend bedoeld voor menselijke spreektaal** en **NIET toegestaan binnen het Mandarin-ecosysteem**.

**Strikte regel**: Binnen het ecosysteem (in governance-artefacten, **agent-charter**s, doctrines, **agent-contract**s, **mandarin-agent**-communicatie) wordt **altijd de volledige, officiële conceptnaam gebruikt**. Synoniemen zijn verboden in formele context.

**Rationale**: Door consequent de officiële conceptnamen te gebruiken, wordt spraakverwarring voorkomen en weten **mandarin-agents** precies wat wordt bedoeld. Synoniemen zijn uitsluitend hulpmiddel voor mensen om het ecosysteem te begrijpen in informele gesprekken.

**Voorbeelden van VERPLICHT gebruik**:
- ✅ **Agent-contract** (NIET: "contract")
- ✅ **Mandarin-artefact** (NIET: "artefact")
- ✅ **Agent-soort** (NIET: "agent-type" of "agent-classificatie")
- ✅ **Mandarin-capability** (NIET: "capability")
- ✅ **Agent-charter** (NIET: "charter")
- ✅ **Governance-artefact** (NIET: "governance-document" of "systeemartefact")
- ✅ **Waarde-artefact** (NIET: "resultaat-artefact" of "value artefact")

**Toegestaan**: In informele menselijke communicatie (gesprekken, notities, brainstorms) mogen synoniemen gebruikt worden voor leesbaarheid. Zodra het ecosysteem wordt geadresseerd (documenten, **mandarin-agent**-interacties), gelden de officiële termen.

--- 
## Mandarin-concept

### Definitie 📝
Een **Mandarin-concept** is een expliciet gedefinieerd, samenhangend en herbruikbaar bouwblok binnen het **Mandarin-ecosysteem**, dat een fundamenteel begrip, structuur of mechanisme beschrijft en als referentie dient voor ontwerp, implementatie en governance.

- Is onderdeel van het canon van Mandarin

- Geen tijdelijke afspraak of conventie

- **mandarin-agent**, **agent-contract**, artefact, value stream, workspace
- Governance-artefact, capability, **agent-boundary**
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
- Biedt een coherent kader voor **mandarin-agents**, artefacten en value streams
- Maakt automatisering, samenwerking en waardecreatie mogelijk
- Is adaptief en zelfbeschrijvend (meta-concepten zijn onderdeel van het ecosysteem)

### Wat het niet is ❌
- Geen statisch systeem of vaste architectuur
- Geen enkelvoudige applicatie of tool
- Geen organisatie of bedrijfseenheid
- Geen tijdelijke samenwerkingsvorm

### Voorbeelden 💡
- De combinatie van alle **mandarin-agents**, **Agent-charter**s, doctrines, workspaces en value streams die samen het Mandarin-systeem vormen
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
- Is niet aan één **mandarin-agent** gekoppeld
- Kan door meerdere **mandarin-agents** gerealiseerd worden
- Wordt ingezet door value stream fasen, maar hoort daar niet bij
- Bestaat ook als er (tijdelijk) geen **mandarin-agent** actief is

### Voorbeelden 💡
- Veranderhypotheses formuleren

- **Artefact**

### Analogieën 🔄
- Vergelijkbaar met een capability in enterprise architectuur
- In softwareontwikkeling: een herbruikbare service of functie

### Toelichting 💬
Een Mandarin capability is uniek in de wereld.
---

## Mandarin-agent

### Definitie 📝
Een **mandarin-agent** is een expliciet gedefinieerde, autonome software-entiteit binnen het **Mandarin-ecosysteem** die, op basis van een formeel **agent-charter** en **agent-contract**, specifieke taken uitvoert, Mandarin-artefacten produceert of informatie levert, en daarbij altijd opereert binnen een afgebakende **agent-boundary** en volgens de geldende governance.

### Kenmerken ⭐
- Heeft een expliciet **agent-charter** en **agent-contract**
- Is autonoom en verantwoordelijk voor eigen uitvoering binnen boundary
- Voert één of meer **mandarin-agent**-capabilities uit
- Produceert Mandarin-artefacten of levert informatie
- Is herbruikbaar en vervangbaar binnen het ecosysteem
- Werkt altijd volgens expliciete input/output-afspraken

### Wat het niet is ❌
- Geen impliciete of ad-hoc softwarecomponent
- Geen menselijke actor
- Geen **mandarin-agent** zonder expliciet **agent-contract** of **agent-charter**
- Geen monolithische applicatie

### Voorbeelden 💡
- Mandarin architect, Logisch datamodelleur, Technisch datamodelleur, **mandarin-agent** smeder

### Synoniemen 🏷️
- **mandarin-agent**, Software-agent

### Analogieën 🔄
- Vergelijkbaar met een microservice, bot of autonome service in softwareontwikkeling
- In enterprise architectuur: een performer of actor met expliciete verantwoordelijkheden

### Toelichting 💬
Een **mandarin-agent** is altijd expliciet ontworpen, beschreven en begrensd. De **mandarin-agent** ontleent zijn legitimiteit aan het **agent-charter** en het **agent-contract**, en is alleen via formele interfaces aanspreekbaar. Dit waarborgt consistentie, vervangbaarheid en governance binnen het **Mandarin-ecosysteem**.

---
## agent-boundary

### Definitie 📝
Een **agent-boundary** is de expliciet vastgelegde servicegrens waarbinnen een **mandarin-agent** zijn interne werking, governance en **agent-capabilities** organiseert, en waarbuiten interactie uitsluitend plaatsvindt via formele **agent-contracts**.

### Kenmerken ⭐
- Bepaalt wat tot de **mandarin-agent** behoort en wat daarbuiten ligt
- Scheidt interne werking van externe interactie
- Is leidend voor governance en autonomie van de **mandarin-agent**
- Waarborgt dat alleen via contracten interactie mogelijk is
- Is de eerste en verplichte stap in mandarin-agent-ontwerp

### Wat het niet is ❌
- Geen impliciete grens
- Geen technische implementatiegrens
- Geen optionele ontwerpkeuze

### Voorbeelden 💡
- {bedenk betere voorbeelden} 

### Synoniemen 🏷️
- Agent-grens
- Service boundary

### Analogieën 🔄
- Vergelijkbaar met een bounded context in DDD, een microservice boundary, of een package boundary in OOP
- In SOA: service boundary waarbinnen interne details verborgen blijven
- Workspace als project workspace, repository, of solution folder
- In DevOps: deployment workspace of CI/CD pipeline context

### Toelichting 💬
Het expliciet definiëren van de **agent-boundary** voorkomt dat **mandarin-agents** samenvallen met tooling of prompts, verantwoordelijkheden vervagen of contracten impliciet worden. Alles binnen de boundary valt onder het **agent-charter**, de bijbehorende **agent-contracten** en de interne governance van de **mandarin-agent**. Alles buiten de boundary is alleen toegankelijk via formele, expliciete contracten.
---

## agent-charter

### Definitie 📝
Een **agent-charter** is een formeel, expliciet document dat de missie, verantwoordelijkheden, grenzen en governance van een specifieke **mandarin-agent** vastlegt, en daarmee de legitimiteit, autonomie en het bestaansrecht van de **mandarin-agent** binnen het **Mandarin-ecosysteem** waarborgt.

### Kenmerken ⭐
- Legt de missie en het bestaansrecht van de **mandarin-agent** vast
- Bepaalt de grenzen (boundary) en verantwoordelijkheden
- Beschrijft de governance, policies en randvoorwaarden
- Is expliciet, versieerbaar en bindend
- Is leidend voor ontwerp, implementatie en evaluatie van de **mandarin-agent**
- Vormt de basis voor het **agent-contract**

### Wat het niet is ❌
- Geen impliciete afspraak of mondelinge instructie
- Geen technische specificatie of implementatiedocument
- Geen **agent-contract** (maar vormt wel de basis daarvoor)
- Geen tijdelijke of informele notitie

### Voorbeelden 💡
- **Agent-charter** van een publicatie-agent waarin missie, scope en governance zijn vastgelegd
- **Agent-charter** van een beheeragent met expliciete operationele grenzen

### Synoniemen 🏷️
- Mandaat, rolbeschrijving

### Analogieën 🔄
- Vergelijkbaar met een projectcharter, mandaat of mission statement in projectmanagement
- In enterprise architectuur: purpose statement of governance **Agent-charter**

### Toelichting 💬
Het **agent-charter** is het fundament voor de legitimiteit en autonomie van een **mandarin-agent**. Zonder **Agent-charter** bestaat een **mandarin-agent** niet formeel binnen het **Mandarin-ecosysteem**. Het **agent-charter** is leidend voor alle ontwerp- en governancekeuzes rondom de **mandarin-agent**.

---
## agent-capability

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

## agent-contract

### Definitie 📝
Een **agent-contract** definieert formeel de intent (**agent-capability**) van de **mandarin-agent**, de input die het verwacht en de output (**artefact**) die hij creëert of antwoorden die hij geeft, evenals de beleidsregels en beperkingen waaronder die mogelijkheden toegankelijk zijn.
 
 ### Wat het niet is ❌
 - Geen beschrijving van interne werking
 - Geen implementatiedetails
 - Geen impliciet **agent-contract**

### Voorbeelden 💡
 - Zie mandarin-architect.schrijf-concept.agent.md
 - Zie workflow-architect.1-ontwerp-workflow.agent.md

### Synoniemen 🏷️
 Service contract, Interface contract

### Analogieën 🔄
 - Vergelijkbaar met een API-agent-contract in softwareontwikkeling
 - In SOA: WSDL of service agreement

### Toelichting 💬
Totdat **agent-charter** en **agent-contract** bestaan, is dit géén **mandarin-agent**, maar een agent-capability-voornemen.

---

## Prompt

### Definitie 📝
Een **prompt** is een concrete, tekstuele of gestructureerde uitdrukking van een aanroep of instructie aan een **mandarin-agent**, die in natuurlijke taal of een andere representatievorm is geformuleerd, maar zelf **geen** canoniek onderdeel vormt van het **agent-contract**.

### Kenmerken ⭐
- Is gericht aan één specifieke **mandarin-agent** (of een groep) in een gegeven context
- Bestaat uit tekst, voorbeelden, constraints en eventueel contextfragmenten
- Is een **representatie** van een beoogde aanroep, geen formele capability-definitie
- Is tijdelijk en situationeel: kan per gebruik of sessie verschillen
- Is tooling- en implementatiegebonden (UI, CLI, editor, API)

### Wat het niet is ❌
- Geen **agent-capability** (die wordt formeel gedefinieerd in het **agent-contract**)
- Geen **agent-contract** of formele interfacebeschrijving
- Geen **agent-charter** of bron van legitimiteit
- Geen normerend artefact of canoniek vastgelegde definitie

### Voorbeelden 💡
- Een tekstblok in een editor waarin een gebruiker een opdracht voor een specifieke **mandarin-agent** formuleert
- Een HTTP-body of CLI-parameter die een aanroep naar een **mandarin-agent** beschrijft
- Een tijdelijke instructie in een REPL of chat-venster gericht aan een **mandarin-agent**

### Synoniemen 🏷️
- Aanroeptekst (alleen in spreektaal)
- Instructieprompt

### Analogieën 🔄
- In LLM-systemen: de prompt waarmee een model wordt aangestuurd
- In klassieke software: de combinatie van command-line parameters en input die een proces start

### Toelichting 💬
Binnen Mandarin is **prompt** nadrukkelijk géén canoniek alternatief voor **agent-capability** of **agent-contract**. Een prompt is een *concrete uitdrukking* van een aanroep naar een bestaande capability, maar de formele waarheid ligt altijd in het **agent-contract**. Prompt-vormen kunnen veranderen met tooling of interface, terwijl capabilities en contracten stabiel en toetsbaar blijven.

Bestanden in de `.github`-map met namen van de vorm `{agent-naam}.prompt` worden uitsluitend gebruikt om VS Code Copilot te voeden; ondanks deze naamgeving worden zij in de Mandarin-concepten niet als **prompt** beschouwd, maar als tooling-specifieke representaties van concrete aanroepen.

---
## Mandarin-artefact

### Definitie 📝
Een **Mandarin-artefact** is een duurzame, expliciete en overdraagbare vastlegging van resultaat of besluitvorming, die binnen een **value stream fase** waarde representeert en als input kan dienen voor vervolgwerk.

### Kenmerken ⭐
- Duurzaam (blijft bestaan)
- Expliciet (leesbaar, inspecteerbaar)
- Overdraagbaar (kan door anderen of **mandarin-agents** gebruikt worden)
- Waarde-dragend (vertegenwoordigt gerealiseerde waarde)

### Wat het niet is ❌
- Geen tijdelijke notitie
- Geen impliciete kennis
- Geen niet-overdraagbaar resultaat

### Voorbeelden 💡
- Governance-artefacten (bijv. constitutie, doctrines, agent-charters)
- Richtinggevende artefacten (bijv. requirements, oplossingsontwerpen)
- Realiserende artefacten (bijv. code, DDL, infrastructuur-als-code)
- Beschrijvende en documenterende artefacten (bijv. handleidingen, modellen)

### Synoniemen 🏷️
- **Artefact**

### Analogieën 🔄
- Vergelijkbaar met een **artefact** in softwareontwikkeling (build-artifact, document)
- In projectmanagement: **deliverable**
- In DDD: **Aggregate Result** of **Documented Outcome**

### Toelichting 💬
De **Mandarin-artefacten** worden geordend in hoofdklassen. Deze zijn vastegelegd in mandarin-ordeningsconcepten.md.
Deze indeling scheidt **betekenis van vorm**, maakt tooling verwisselbaar, houdt governance scherp en klein, en erkent modellen als uitleg (niet als waarheid).

---

## Template

### Definitie 📝
Een **template** is een herbruikbare, gestructureerde opzet voor een **Mandarin-artefact** of prompt, die de minimale inhoud, secties en structuur voorschrijft, zodat **value-stream-specifieke** (inzet-as) **mandarin-agents** binnen een value stream fase consistente en toetsbare output leveren.

### Kenmerken ⭐
- Legt structuur en verplichte onderdelen van een artefact of prompt vast
- Wordt gebruikt als startpunt voor concrete artefacten binnen een **value stream fase**
- Ondersteunt vooral **mandarin-agents** die op de **inzet-as** als *value-stream-specifiek* zijn gepositioneerd
- Verhoogt voorspelbaarheid, vergelijkbaarheid en herbruikbaarheid van resultaten
- Is zelf geen normerend artefact, maar kan verwijzen naar normerende artefacten
- Wordt beheerd in de `templates/`-folder van een workspace

### Wat het niet is ❌
- Geen vervanging van het onderliggende **Mandarin-artefact** of **agent-contract**
- Geen volledige beschrijving van gedrag of governance
- Geen tijdelijke notitie of ad-hoc sjabloon
- Geen tooling-specifieke prompt op zichzelf

### Voorbeelden 💡
- `templates/agent.charter.template.md` — opzet voor een **agent-charter**
- `templates/phase.charter.template.md` — opzet voor een fase-charter binnen een **value stream fase**
- Prompt-templates die vaste secties bieden voor context, opdracht en constraints richting een **mandarin-agent**

### Synoniemen 🏷️
- Sjabloon (alleen in spreektaal)

### Analogieën 🔄
- Vergelijkbaar met document- of code-templates in ontwikkelomgevingen
- In enterprise architectuur: standaardformats voor architectuurdocumenten en besluiten

### Toelichting 💬
**Templates** verbinden de ordeningslaag (structuur en classificatie) met de operationele laag waarin **mandarin-agents** daadwerkelijk artefacten produceren. Door templates expliciet te definiëren en centraal op te slaan, kunnen vooral **value-stream-specifieke** **mandarin-agents** binnen een bepaalde **value stream fase** snel, consistent en toetsbaar werken, zonder dat de normatieve waarheid verschuift van normerende artefacten naar de template zelf.

---

## Value stream

### Definitie 📝
Een **value stream** is een expliciet gedefinieerde keten van waarde-creërende stappen die samen leiden tot een herkenbaar resultaat, en die richting geeft aan welke **artefacten**, **mandarin-agents** en beslissingen bijdragen aan die waarde.

### Kenmerken ⭐
- Definieert stappen, geen taken
- Is artefact-gericht
- Is **mandarin-agent**-agnostisch, maar **mandarin-agent**-sturend
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
- Vormt context voor **mandarin-agents** die daarin opereren
- Produceert geen taken en stuurt geen workflow

### Wat het niet is ❌
- Geen proces
- Geen stappenplan
- Geen activiteit of taak
- Geen **mandarin-agent** of rol
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
- Activeert **mandarin-agents**
- Contextualiseert werk tot specifieke fasen
- Kan één of meerdere fasen ondersteunen
- **mandarin-agents** worden gefetched uit de Mandarin workspace

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
In de eerste fase van ontwikkeling worden **mandarin-agents** gefetched uit de Mandarin workspace. De workspaces bevatten dus wel **mandarin-agents**, maar deze worden hier niet aangepast. In die zin 'bevatten' deze workspaces geen **mandarin-agents**.

---


## Change Log

| Datum   | Versie | Wijziging                              | Auteur   |
|------------|--------|---------------------------------------------------------------------|------------|
| 2026-02-01 | 2.3.0 | Toegevoegd: domeinconcept Template als herbruikbare structuur voor artefacten en prompts, met nadruk op gebruik door value-stream-specifieke mandarin-agents | Constitutioneel Auteur |
| 2026-02-01 | 2.2.0 | Verduidelijking: `.github/{agent-naam}.prompt`-bestanden zijn tooling-specifieke representaties voor VS Code Copilot en geen canonieke prompts binnen Mandarin | Constitutioneel Auteur |
| 2026-02-01 | 2.1.0 | Toegevoegd: concept Prompt als concrete, niet-canonieke representatie van een aanroep naar een mandarin-agent | Constitutioneel Auteur |
| 2026-02-01 | 2.0.0 | Scheiding meta-concepten: Mandarin-architectuurprincipe, **agent-boundary**, **mandarin-agent**classificatie (inclusief As en 4 assen), en Mandarin-artefact (inclusief alle specialisaties) verplaatst naar mandarin-meta-concepten.md; document bevat nu alleen operationele concepten (actieve structuren) | Constitutioneel Auteur |
| 2026-02-01 | 1.6.0 | Herijking **mandarin-agent**-classificatie: vervanging **mandarin-agent**-soort door **mandarin-agent**classificatie met 4 orthogonale assen (Inhoudelijke as, Inzet-as, Vorm-as, Werkingsas); alle oude **mandarin-agent**-soorten verwijderd (Adviserende **mandarin-agent**, Uitvoerende **mandarin-agent**, Beheeragent, Ecosysteem uitvoerende **mandarin-agent**, Waarde uitvoerende **mandarin-agent**); **mandarin-agents** niet langer als "soort" maar als posities op assen | Constitutioneel Auteur |
| 2026-02-01 | 1.5.0 | Herziening artefacten-hiërarchie: Governance-artefact en Bedrijfs-artefact zijn nu specialisaties van Normerend artefact; Governance-artefacten ontstaan alleen in value stream "Agent Ecosysteem Ontwikkeling"; Normerende artefacten operationeel in maximaal één value stream fase | Constitutioneel Auteur |
| 2026-02-01 | 1.4.0 | Herijking artefacten-indeling: Mandarin-artefacten nu ingedeeld in 5 hoofdklassen (Normerend, Governance, Bedrijfs-, Beschrijvend, Documenterend) i.p.v. 2 (Governance, Waarde); scheidt betekenis van vorm, maakt tooling verwisselbaar | Constitutioneel Auteur |
| 2026-01-31 | 1.3.0 | Toevoeging concepten Value stream **mandarin-agent** en Utility **mandarin-agent**; verduidelijking fase-toekenning per **mandarin-agent**-soort: adviserende/uitvoerende **mandarin-agents** aan fasen, beheeragents in alle fasen, utility **mandarin-agents** orthogonaal | Constitutioneel Auteur |
| 2026-01-31 | 1.2.1 | Aanscherping "Gebruik van Synoniemen" — Synoniemen VERBODEN binnen ecosysteem, uitsluitend toegestaan in menselijke spreektaal; voorbeelden toegevoegd | Canon Curator |
| 2026-01-31 | 1.2.0 | Subsectie toegevoegd in Inleiding: "Gebruik van Synoniemen" — Verduidelijkt dat synoniemen spreektaal zijn en niet erkend binnen ecosysteem | Canon Curator |
| 2026-01-31 | 1.1.1 | Herstel Mandarin-ecosysteem definitie — Ontbrekende definitie-sectie toegevoegd | Canon Curator |
| 2026-01-31 | 1.1.0 | Toevoeging definitie **mandarin-agent**-soort — Expliciete classificatie toegevoegd | Canon Curator |
| 2026-01-31 | 1.0.0 | Initiële versie — Concepten en definities voor actieve structuren opgesteld | Hans Blok |

---

**Einde document**

# De Mandarin concepten

**Type**: Concepten en Definities 
**Repository**: mandarin-canon 
**Identifier**: mandarin-canon.concepten.actieve-structuren 
**Version**: 2.5.0 
**Status**: Active 
**Last Updated**: 2026-02-21 
**Owner**: Hans Blok

---

## Herkomstverantwoording

Dit document is opgesteld door Hans Blok op 31 januari 2026 als definitie van concepten en architectonische grondslagen voor actieve structuren in het Mandarin-ecosysteem.

**Geraadpleegde bronnen**:


**Opsteller**: Hans Blok 
**Datum**: 2026-01-31 
**Laatste wijziging**: 2026-02-21 (Constitutioneel Auteur) 
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

### Bronnen en Kennisbasis
- [Bronregime](#bronregime) — Expliciet vastgelegd stelsel van toegestane kennisbronnen en afleidingsregels
- [Externe grondslagen](#externe-grondslagen) — Ruwe externe denkkaders als potentiële grondslag voor het ecosysteem
- [Kaderdefinitie](#kaderdefinitie) — Geïnternaliseerde, gecontroleerde versie van een externe grondslag

---

## Inleiding

Dit document beschrijft de concepten die betrekking hebben op de **actieve structuren** van het **Mandarin-ecosysteem**. 
Onder actieve structuren verstaan we de samenstellende en functionele elementen die het ecosysteem laten handelen, samenwerken en output produceren.

Naast de actieve structuren bevat dit document ook de meta-concepten **Mandarin-concept** en **Mandarin-architectuurprincipe**. Deze hebben een registrerend en interpreterend karakter en ondersteunen menselijke leesbaarheid en begripsvorming van het ecosysteem zelf.

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
- Is structureel en functioneel onderscheiden van passieve of registrerende elementen
- Kan zelfstandig of in samenhang met andere actieve structuren opereren
- Is toetsbaar op gedrag en output

### Wat het niet is ❌
- Geen passief, registrerend of uitsluitend informatief element
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
- Is adaptief en zelfregistrerend (meta-concepten zijn onderdeel van het ecosysteem)

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
Het **Mandarin-ecosysteem** vormt de overkoepelende context waarbinnen alle Mandarin-concepten samenkomen en waarde leveren. Het is ontworpen om adaptief, expliciet en samenhangend te zijn. Het ecosysteem is zelfregistrerend: de concepten die het ecosysteem beschrijven (zoals **Mandarin-concept** en **Mandarin-architectuurprincipe**) maken zelf deel uit van het ecosysteem.


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
- Is expliciet, versieerbaar en vastleggend
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
- Capability is aanroepbaar (uitvoerbaar), niet registrerend

### Wat het niet is ❌
- Geen registrerende eigenschap
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
- Geen vastleggend artefact of canoniek vastgelegde definitie

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

## Bronregime

### Definitie 📝
Een **bronregime** is het expliciet vastgelegde stelsel van toegestane kennisbronnen en afleidingsregels waarbinnen een **mandarin-agent** betekenis mag vormen, oordelen mag vellen of artefacten mag produceren.

### Kenmerken ⭐
- Bepaalt welke bronnen geldig zijn
- Bepaalt welke bronnen uitgesloten zijn
- Bepaalt of interpretatie is toegestaan
- Bepaalt of synthese is toegestaan
- Bepaalt of nieuwe betekenis mag ontstaan
- Bepaalt hoe herleidbaarheid aantoonbaar wordt gemaakt

### Wat het niet is ❌
- Geen classificatie-as (dat is de Bronhouding)
- Geen impliciete aanname over brongebruik

### Voorbeelden 💡
- Een strikt bronregime waarbij alleen de input-prompt als bron mag dienen (passend bij input-gebonden)
- Een bronregime waarbij de gehele Mandarin-canon geraadpleegd mag worden (passend bij canon-gebonden)

### Synoniemen 🏷️
- Kennisregime, Bronkader

### Analogieën 🔄
- Vergelijkbaar met bewijsregels in de rechtspraak
- In de wetenschap: methodologische verantwoording van brongebruik

### Toelichting 💬
De **Bronhouding** positioneert een **mandarin-agent** op de classificatie-as. Het **bronregime** operationaliseert die positie in concrete regels. Het zorgt ervoor dat de grenzen van wat een agent mag "weten" en "vinden" expliciet en toetsbaar zijn.

Daarnaast reguleert het bronregime de balans tussen **determinisme** en **probabilisme** in het gedrag van de agent. Een strikt bronregime (zoals bij input-gebonden) dwingt deterministisch gedrag af: dezelfde input leidt gegarandeerd tot dezelfde output, zonder probabilistische interpretatie. Een exploratiever bronregime (zoals bij canon-gebonden of exploratief) staat probabilistisch gedrag toe, waarbij de agent (vaak een LLM) ruimte krijgt voor synthese, interpretatie en het genereren van nieuwe betekenis op basis van waarschijnlijkheden, zolang dit binnen de gestelde kaders van het regime blijft.

Bij een **exploratief bronregime** is de mate van probabilisme het hoogst. Dit heeft als gevolg dat de output sterk generatief en creatief kan zijn, maar tegelijkertijd de minste voorspelbaarheid en herleidbaarheid kent. De verantwoordelijkheid verschuift hierdoor: de agent moet gemaakte aannames expliciet maken, en de validatie van de output (bijvoorbeeld op hallucinaties of ongewenste afwijkingen) vereist vaak menselijke controle (human-in-the-loop) of een navolgende interpreterende agent.

---

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
- Normerende artefacten van het agent ecosysteem (bijv. constitutie, doctrines, agent-charters)
- Normerende artefacten van de de project workspace  (bijv. requirements, oplossingsontwerpen)
- Realisererende artefacten (bijv. code, DDL, infrastructuur-als-code)
- Beschrijvende artefacten (bijv. handleidingen, modellen)

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
- Is zelf geen vastleggend artefact, maar kan verwijzen naar vastleggende artefacten
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
**Templates** verbinden de ordeningslaag (structuur en classificatie) met de operationele laag waarin **mandarin-agents** daadwerkelijk artefacten produceren. Door templates expliciet te definiëren en centraal op te slaan, kunnen vooral **value-stream-specifieke** **mandarin-agents** binnen een bepaalde **value stream fase** snel, consistent en toetsbaar werken, zonder dat de normatieve waarheid verschuift van vastleggende artefacten naar de template zelf.

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

# Concept — bronrol

---

## Definitie 📝
Een **bronrol** is de relatie die een artefact heeft tot een specifieke agent-executie. Bronrol beschrijft niet wat een artefact *is* (dat is **artefactfunctie**), maar hoe het artefact *wordt gebruikt* binnen een concrete uitvoering door een **mandarin-agent**.

## Kenmerken ⭐
- Is relationeel: een eigenschap van het gebruik, niet van het artefact zelf
- Ontstaat pas in de context van een agent-executie
- Hetzelfde artefact kan in verschillende executies verschillende bronrollen vervullen
- Kent twee posities: **kaderbron** en **werkbron**
- Is orthogonaal aan **artefactfunctie** (semantische positie van het artefact zelf)
- Is traceerbaar via de execution-file en canon-referentie

## Wat het niet is ❌
- Geen intrinsieke eigenschap van het artefact (dat is **artefactfunctie**)
- Geen classificatie-as voor artefact-taxonomie
- Geen output-rol — betreft uitsluitend inputgebruik tijdens een executie
- Geen vaste toekenning: een artefact "is" geen werkbron, het "wordt gebruikt als" werkbron

## Posities op deze as

| Positie | Beschrijving |
|---------|--------------|
| **Kaderbron** | Artefact dat kader, mandaat en kennis levert waarop de agent zijn handelen legitimeert |
| **Werkbron** | Artefact dat wordt ingelezen om te bewerken, analyseren of verwerken |

## Voorbeelden 💡
- Een agent-charter wordt gebruikt als **kaderbron** in een definieer-concept-executie
- De mandarin-canon wordt gebruikt als **kaderbron** voor ecosysteem-brede definities
- Een bestaand concept-bestand wordt gebruikt als **werkbron** bij een validatie-executie
- Hetzelfde artefact kan kaderbron zijn in de ene executie en werkbron in een andere

## Synoniemen 🏷️
- Gebruiksrol (alleen in spreektaal)

## Analogieën 🔄
- In rechtspraak: de wet (kaderbron) versus het dossier (werkbron) — de wet verandert niet van aard, maar de *rol* in het proces verschilt
- In onderwijs: het curriculum (kaderbron) versus het werkstuk dat wordt nagekeken (werkbron)

## Context en gebruik 💬
Binnen het mandarin-ecosysteem beschrijft bronrol hoe artefacten worden ingezet bij een agent-executie. Het onderscheid met **artefactfunctie** is essentieel: artefactfunctie beschrijft de semantische positie van het artefact zelf, bronrol beschrijft de relatie tot een uitvoering. Een doctrine-document heeft als artefactfunctie "normerend", maar wordt in een specifieke executie *gebruikt als* kaderbron. Dit maakt expliciet op welke gronden een agent handelt, zonder het artefact zelf te herdefiniëren.

**Taalconventie**: Zeg niet "dit artefact *is* een werkbron", maar "dit artefact *wordt gebruikt als* werkbron in deze uitvoering".

---

# Concept — kaderbron

---

## Definitie 📝
Een **kaderbron** is een positie op de as **bronrol** die aangeeft dat een artefact binnen een agent-executie wordt gebruikt als bron van kader, mandaat en kennis waarop de **mandarin-agent** zijn handelen legitimeert.

## Kenmerken ⭐
- Levert de normatieve en kennisbasis voor de agent-executie
- Wordt niet bewerkt of gewijzigd door de agent tijdens de executie
- Bepaalt wat de agent mag, weet en moet naleven
- Typische artefacten in deze rol: charters, canon, doctrines, beleidsdocumenten

## Wat het niet is ❌
- Geen vaste eigenschap van het artefact — het is een rol *in* een executie
- Geen werkmateriaal dat wordt geanalyseerd of getransformeerd
- Geen output van de executie

## Voorbeelden 💡
- Het agent-charter (`concept-curator.charter.md`) als kaderbron bij een definieer-concept-executie
- De mandarin-canon als kaderbron voor ecosysteem-brede verificatie
- Een doctrine-document als kaderbron bij een validatie-executie

## Relatie tot andere concepten
- **Bronrol**: kaderbron is één van de twee posities op deze as
- **Werkbron**: de complementaire positie op dezelfde as
- **Bronregime**: bepaalt welke kaderbronnen een agent mag raadplegen

## Traceerbaarheid
- Vastgesteld door: concept-curator (fnd.02.concept-curator)
- Laatst gewijzigd: 2026-03-22
- Bron(nen): gebruikersinvoer, concept-curator.charter.md

---

# Concept — werkbron

---

## Definitie 📝
Een **werkbron** is een positie op de as **bronrol** die aangeeft dat een artefact binnen een agent-executie wordt ingelezen om te bewerken, analyseren of verwerken als het materiaal waarop de agent zijn intent toepast.

## Kenmerken ⭐
- Is het materiaal waarop de agent actief handelt
- Kan worden gelezen, geanalyseerd, gevalideerd of getransformeerd
- Bepaalt de inhoudelijke scope van de executie
- Typische artefacten in deze rol: bestaande concepten, artefact-bestanden, inputlijsten

## Wat het niet is ❌
- Geen vaste eigenschap van het artefact — het is een rol *in* een executie
- Geen kaderbron die mandaat of kennis levert
- Geen output van de executie (al kan de bewerking van een werkbron tot output leiden)

## Voorbeelden 💡
- Een bestaand concept-bestand als werkbron bij een valideer-concept-coherentie-executie
- Een lijst van domeinconcepten als werkbron bij een rapporteer-concept-status-executie
- Een artefact dat moet worden verrijkt als werkbron bij een verweef-concepten-executie

## Relatie tot andere concepten
- **Bronrol**: werkbron is één van de twee posities op deze as
- **Kaderbron**: de complementaire positie op dezelfde as

## Traceerbaarheid
- Vastgesteld door: concept-curator (fnd.02.concept-curator)
- Laatst gewijzigd: 2026-03-22
- Bron(nen): gebruikersinvoer, concept-curator.charter.md

---

# Externe grondslagen

---

## Definitie 📝
Een **externe grondslag** is een bron van buiten het **Mandarin-ecosysteem** die een bruikbaar denkkader biedt. Externe grondslagen zijn ruwe, nog niet-gecontroleerde kennis die pas na expliciete selectie en kadering binnen het ecosysteem normatieve status kan krijgen.

## Kenmerken ⭐
- Is afkomstig van buiten het **Mandarin-ecosysteem**
- Biedt een bruikbaar denkkader, model of theorie
- Is in oorsprong ruwe, niet-gecontroleerde kennis
- Heeft geen normatieve status totdat selectie en kadering hebben plaatsgevonden
- Is traceerbaar naar de oorspronkelijke externe bron
- Kan meerdere domeinen binnen het ecosysteem raken

## Wat het niet is ❌
- Geen automatisch geldige of normatieve bron binnen het ecosysteem
- Geen gecurateerde of gevalideerde kennis — dat ontstaat pas na kadering
- Geen vervanging van interne Mandarin-concepten of -doctrines
- Geen "alles wat bestaat" — alleen bronnen die een bruikbaar denkkader bieden

## Voorbeelden 💡
- TOGAF (architectuurframework)
- Business Model Canvas (BMC)
- Psychologische modellen (bijv. cognitieve belastingstheorie, motivatiemodellen)
- Economische theorieën (bijv. transactiekostentheorie, speltheorie)

## Synoniemen 🏷️
- External Foundations (alleen in Engelstalige context)

## Analogieën 🔄
- In rechtspraak: buitenlandse jurisprudentie die pas geldig wordt nadat een rechter deze expliciet overneemt en kadert
- In wetenschap: een literatuurbron die pas meetelt na opname in de methodologische verantwoording
- In enterprise architectuur: een referentiemodel dat pas geldt na formele adoptie en afbakening

## Context en gebruik 💬
Externe grondslagen zijn de **ruwe grondstof** waaruit het ecosysteem kan putten. Zij bieden denkkaders, modellen en theorieën die potentieel waardevol zijn, maar zij zijn in hun oorspronkelijke vorm nog niet gecontroleerd of gekaderd voor gebruik binnen Mandarin. Het ecosysteem behandelt externe grondslagen daarom als input die eerst moet worden geselecteerd en gekaderd voordat zij invloed mogen uitoefenen op governance, ontwerp of agent-gedrag.

**Strikte regel**: Een **mandarin-agent** mag een externe grondslag **nooit** rechtstreeks raadplegen als basis voor handelen. Toegang tot externe kennis verloopt **uitsluitend** via een **kaderdefinitie**. Dit voorkomt dat ongefilterde externe modellen stilzwijgend invloed uitoefenen op het ecosysteem.

## Traceerbaarheid
- Vastgesteld door: concept-curator (fnd.02.concept-curator)
- Laatst gewijzigd: 2026-03-23
- Bron(nen): gebruikersinvoer

---

# Kaderdefinitie

---

## Definitie 📝
Een **kaderdefinitie** is de geïnternaliseerde, gecontroleerde versie van een **externe grondslag** binnen het **Mandarin-ecosysteem**. Zij legt vast welk deel van de externe bron wordt overgenomen, met welke interpretatie, scope en beperkingen, en vormt daarmee de enige toegestane basis waarop **mandarin-agents** de externe kennis mogen gebruiken.

## Kenmerken ⭐
- Is altijd afgeleid van één specifieke **externe grondslag**
- Legt expliciet de Mandarin-interpretatie, scope en beperkingen vast
- Is de gecontroleerde, normatieve representatie van externe kennis binnen het ecosysteem
- Is het enige wat **mandarin-agents** mogen raadplegen — niet de externe grondslag zelf
- Is versieerbaar, toetsbaar en traceerbaar
- Wordt beheerd als grondslag-artefact binnen het ecosysteem

## Wat het niet is ❌
- Geen ongewijzigde kopie van de externe bron
- Geen **externe grondslag** — die is ruw en potentieel; een kaderdefinitie is gecontroleerd en toegestaan
- Geen vrije interpretatie — scope en beperkingen zijn expliciet vastgelegd
- Geen tijdelijk werkdocument

## Voorbeelden 💡
- `TOGAF.kaderdefinitie.md` — legt vast welke TOGAF-concepten worden overgenomen, hoe ze zich verhouden tot Mandarin-**value streams**, en welke delen buiten scope vallen
- `BMC.kaderdefinitie.md` — kadert het Business Model Canvas voor gebruik binnen waardepropositieanalyse, inclusief Mandarin-specifieke scope en beperkingen
- Een kaderdefinitie van cognitieve belastingstheorie die vastlegt welke principes gelden voor agent-interactieontwerp en welke niet

## Synoniemen 🏷️
- Gekaderde grondslag (alleen in spreektaal)

## Analogieën 🔄
- In rechtspraak: een rechterlijke uitspraak die buitenlandse jurisprudentie expliciet overneemt en afbakent voor nationaal gebruik
- In wetenschap: de operationalisering van een theorie in een concreet onderzoeksprotocol
- In enterprise architectuur: een adoptiedocument dat vastlegt welke delen van een referentiemodel (bijv. TOGAF) gelden en welke niet

## Context en gebruik 💬
De kaderdefinitie vormt de brug tussen **externe grondslagen** en het operationele gebruik binnen het ecosysteem. Waar een externe grondslag potentieel bruikbare kennis biedt, maakt de kaderdefinitie die kennis **daadwerkelijk toegestaan**. Zonder kaderdefinitie mag een **mandarin-agent** een externe grondslag niet als basis voor handelen gebruiken.

De transformatie van externe grondslag naar kaderdefinitie omvat: (1) interpretatie — wat betekent dit binnen Mandarin, (2) scope — welke delen worden overgenomen, (3) beperkingen — wat wordt expliciet uitgesloten. Dit voorkomt dat externe modellen ongefilterd invloed uitoefenen op governance, ontwerp of agent-gedrag.

**Bronrol en aeo.01**: Een kaderdefinitie heeft geen vaste **bronrol**. In de value stream fase **aeo.01 (Grondslagvorming)** wordt een kaderdefinitie doorgaans als **werkbron** gebruikt — het is het materiaal waaraan gewerkt wordt. In alle overige fasen wordt dezelfde kaderdefinitie als **kaderbron** gebruikt — het levert het kader waarop agents hun handelen legitimeren. De bronrol wordt dus bepaald door de executie, niet door het artefact zelf.

## Traceerbaarheid
- Vastgesteld door: concept-curator (fnd.02.concept-curator)
- Laatst gewijzigd: 2026-03-23
- Bron(nen): gebruikersinvoer

---


## Change Log

| Datum   | Versie | Wijziging                              | Auteur   |
|------------|--------|---------------------------------------------------------------------|------------|
| 2026-03-23 | 2.9.0 | Aangescherpt: Externe grondslagen mogen NOOIT direct door agents geraadpleegd worden; Kaderdefinitie bronrol varieert per executie (werkbron in aeo.01, kaderbron elders) | Concept-Curator |
| 2026-03-23 | 2.8.0 | Toegevoegd: concept Kaderdefinitie — geïnternaliseerde, gecontroleerde versie van een externe grondslag; de enige toegestane basis voor agent-gebruik | Concept-Curator |
| 2026-03-23 | 2.7.0 | Toegevoegd: concept Externe grondslagen — ruwe externe denkkaders als potentiële grondslag voor het ecosysteem | Concept-Curator |
| 2026-03-22 | 2.6.0 | Concept agent-bronbestanden vervangen door bronrol (relationeel, niet intrinsiek); posities kaderbron en werkbron toegevoegd; taalconventie vastgelegd | Concept-Curator |
| 2026-02-21 | 2.5.0 | Toegevoegd: concept Bronregime als operationalisering van de Bronhouding-as | Constitutioneel Auteur |
| 2026-02-21 | 2.4.0 | Verwijderd: concept Interventieniveau (is verplaatst naar mandarin-ordeningsconcepten.md) | Constitutioneel Auteur |
| 2026-02-01 | 2.3.0 | Toegevoegd: domeinconcept Template als herbruikbare structuur voor artefacten en prompts, met nadruk op gebruik door value-stream-specifieke mandarin-agents | Constitutioneel Auteur |
| 2026-02-01 | 2.2.0 | Verduidelijking: `.github/{agent-naam}.prompt`-bestanden zijn tooling-specifieke representaties voor VS Code Copilot en geen canonieke prompts binnen Mandarin | Constitutioneel Auteur |
| 2026-02-01 | 2.1.0 | Toegevoegd: concept Prompt als concrete, niet-canonieke representatie van een aanroep naar een mandarin-agent | Constitutioneel Auteur |
| 2026-02-01 | 2.0.0 | Scheiding meta-concepten: Mandarin-architectuurprincipe, **agent-boundary**, **mandarin-agent**classificatie (inclusief As en 4 assen), en Mandarin-artefact (inclusief alle specialisaties) verplaatst naar mandarin-meta-concepten.md; document bevat nu alleen operationele concepten (actieve structuren) | Constitutioneel Auteur |
| 2026-02-01 | 1.6.0 | Herijking **mandarin-agent**-classificatie: vervanging **mandarin-agent**-soort door **mandarin-agent**classificatie met 4 orthogonale assen (Inhoudelijke as, Inzet-as, Vorm-as, Werkingsas); alle oude **mandarin-agent**-soorten verwijderd (Adviserende **mandarin-agent**, Uitvoerende **mandarin-agent**, Beheeragent, Ecosysteem uitvoerende **mandarin-agent**, Waarde uitvoerende **mandarin-agent**); **mandarin-agents** niet langer als "soort" maar als posities op assen | Constitutioneel Auteur |
| 2026-02-01 | 1.5.0 | Herziening artefacten-hiërarchie: Governance-artefact en Bedrijfs-artefact zijn nu specialisaties van Vastleggend artefact; Governance-artefacten ontstaan alleen in value stream "Agent Ecosysteem Ontwikkeling"; Vastleggende artefacten operationeel in maximaal één value stream fase | Constitutioneel Auteur |
| 2026-02-01 | 1.4.0 | Herijking artefacten-indeling: Mandarin-artefacten nu ingedeeld in 5 hoofdklassen (Vastleggend, Governance, Bedrijfs-, Registrerend, Documenterend) i.p.v. 2 (Governance, Waarde); scheidt betekenis van vorm, maakt tooling verwisselbaar | Constitutioneel Auteur |
| 2026-01-31 | 1.3.0 | Toevoeging concepten Value stream **mandarin-agent** en value-stream-overstijgende **mandarin-agent**; verduidelijking fase-toekenning per **mandarin-agent**-soort: adviserende/uitvoerende **mandarin-agents** aan fasen, beheeragents in alle fasen, value-stream-overstijgende **mandarin-agents** orthogonaal | Constitutioneel Auteur |
| 2026-01-31 | 1.2.1 | Aanscherping "Gebruik van Synoniemen" — Synoniemen VERBODEN binnen ecosysteem, uitsluitend toegestaan in menselijke spreektaal; voorbeelden toegevoegd | Canon Curator |
| 2026-01-31 | 1.2.0 | Subsectie toegevoegd in Inleiding: "Gebruik van Synoniemen" — Verduidelijkt dat synoniemen spreektaal zijn en niet erkend binnen ecosysteem | Canon Curator |
| 2026-01-31 | 1.1.1 | Herstel Mandarin-ecosysteem definitie — Ontbrekende definitie-sectie toegevoegd | Canon Curator |
| 2026-01-31 | 1.1.0 | Toevoeging definitie **mandarin-agent**-soort — Expliciete classificatie toegevoegd | Canon Curator |
| 2026-01-31 | 1.0.0 | Initiële versie — Concepten en definities voor actieve structuren opgesteld | Hans Blok |

---

**Einde document**

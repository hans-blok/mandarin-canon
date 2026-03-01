# Mandarin **ordenings-concepten**

**Type**: Concepten en Definities  
**Repository**: mandarin-canon  
**Identifier**: mandarin-canon.concepten.meta  
**Version**: 1.2.01  
**Status**: Active  
**Last Updated**: 2026-02-28  
**Owner**: Hans Blok

---

## Herkomstverantwoording

Dit document is afgeleid van "concepten-en-architectonische-grondslagen.md" (versie 1.6.0) door Constitutioneel Auteur op 1 februari 2026.

**Geraadpleegde bronnen**:
- concepten-en-architectonische-grondslagen.md (versie 1.6.0, gelezen op 2026-02-01)
- herijking 2.md (gelezen op 2026-02-01)

**Datum**: 2026-02-01  
**Doel**: Expliciete scheiding tussen **ordenings-concepten** (die structuur en classificatie beschrijven) en **domein-concepten** (actieve structuren en hun werking)

**Ontwerpkeuze**: **ordenings-concepten** beschrijven hoe het ecosysteem zichzelf structureert en classificeert. Door deze in een apart document te plaatsen, wordt de architectonische lagenstructuur expliciet: **ordenings-concepten** definiëren het classificatiestelsel en de artefactstructuur, terwijl operationele concepten de actieve elementen beschrijven die binnen dat stelsel werken.

---

## Inhoudsopgave

### Classificatie en Structuur
- [Mandarin-architectuurprincipe](#mandarin-architectuurprincipe) — Richtinggevende regel voor ontwerp
- [**mandarin-agent**-boundary](#**mandarin-agent**-boundary) — Expliciete afbakening van verantwoordelijkheid
- [mandarin-agent-classificatie](#mandarin-agent-classificatie) — Positionering langs orthogonale assen
- [As](#as) — Ordeningsdimensie voor positionering
- [Artefact-functie-as](#artefact-functie-as) — Functierol van Mandarin-artefacten
- [Artefactclassificatie](#artefactclassificatie) — Indeling van Mandarin-artefacten

### mandarin-agent-classificatie Assen
- [Betekeniseffect](#betekeniseffect) — Effect op betekenis
- [Werking](#werking) — Inhoud, representatie of voorwaarden
- [Vormingsfase](#vormingsfase) — Fase van vorming of ontwikkeling
- [Bronhouding](#bronhouding) — Kennisbronnen en herleidbaarheid

### Artefacten
- [Mandarin-artefact](#mandarin-artefact) — Expliciet vastgelegd, overdraagbaar resultaat
- [Vastleggend artefact](#vastleggend-artefact) — Artefact dat normen en regels vastlegt
  - [Governance-artefact](#governance-artefact) — Specialisatie: governance in ecosysteem (value stream 0)
  - [Richtinggevend artefact](#richtinggevend-artefact) — Specialisatie: vastleggende richting in waarde value streams (1-n)
- [Vastleggend artefact](#vastleggend-artefact) — Artefact dat gedrag of structuur in systemen realiseert
- [Structurerend artefact](#structurerend-artefact) — Artefact dat architectuurelementen en relaties expliciteert
- [Registrerend artefact](#registrerend-artefact) — Artefact dat inzicht en uitleg biedt
- [Representatie](#representatie) — Concrete uitdrukking van betekenis
- [Afleidingspositie](#afleidingspositie) — Leidend of afgeleid in de keten
  
### Prompts
- [Prompt canon-curator: publiceer normatieve wijziging](#prompt-canon-curator-publiceer-normatieve-wijziging)

---


## Mandarin-agent-classificatie

### Definitie
**Mandarin-agent-classificatie** is het expliciet positioneren van een **mandarin-agent** langs een vast stelsel van orthogonale assen. Hiermee wordt vastgelegd wat het effect van de agent is, waarop hij intervenieert, in welke context hij inzetbaar is en hoe hij handelt.

### Kenmerken
- Geen enkelvoudig label of hiërarchie
- Een agent neemt posities in op meerdere assen
- Elke as beschrijft een fundamenteel ander architectonisch aspect
- Samen bepalen de posities het gedrag, de bevoegdheid en de beperkingen van de agent
- Bestaat uit vier orthogonale assen:
  1. **Betekeniseffect** — effect op betekenis
  2. **Vormingsfase** — fase van vorming of ontwikkeling
  3. **Werking** — inhoud, representatie of voorwaarden
  4. **Bronhouding** — kennisbronnen en herleidbaarheid

### Wat het niet is
- Geen enkelvoudig label (zoals "adviserende agent")
- Geen hiërarchische structuur
- Geen technische implementatie-eigenschap
- Geen tijdelijke classificatie

### Voorbeelden
- Een agent kan registrerend zijn (betekeniseffect), in de werkvormingsfase acteren (vormingsfase), en inhoudelijk zijn (werking)
- Een agent kan vastleggend, in de architectuurvormingsfase, en inhoudelijk zijn
- Een agent kan conditioneel zijn (werking), in de ecosysteemvormingsfase (vormingsfase)

### Synoniemen
- Agent-positionering
- Multi-dimensionale agent-classificatie

### Analogieën
- Multi-dimensionale classificatie in taxonomie
- Orthogonale concerns in softwareontwikkeling (aspect-oriented programming)
- Capability matrix in enterprise architectuur

### Toelichting
Deze classificatie vervangt het concept "agent-soort" door een genuanceerd stelsel van orthogonale assen. Elke agent heeft op elke as een expliciete positie; samen bepalen deze het gedrag, de bevoegdheden en de beperkingen van de agent.

### Gerelateerde Doctrines
- **Intent-naming**: [doctrine-intent-naming.md](doctrine-intent-naming.md) koppelt canonieke werkwoorden aan elke classificatie-positie op de werking en het betekeniseffect
- **Combinatiematrices**: [mandarin-classificatie-matrices.md](mandarin-classificatie-matrices.md) toont welke combinaties van as-posities architectonisch mogelijk en logisch zijn.


---

## Betekeniseffect

### Definitie
**Betekeniseffect** is een classificatie-as die het effect van een agent op de betekenis van het werk beschrijft.

**Leidende vraag:** Wat is het effect van deze agent op de betekenis van het werk?

### Kenmerken
- Eén van vier orthogonale assen
- Onderscheidt agents op basis van hun effect op betekenis
- Onafhankelijk van andere assen
- Bepaalt fundamentele rol en impact van de agent

### Wat het niet is
- Geen technische implementatievariant
- Geen organisatorische indeling
- Geen enkelvoudig label

### Categorieën
0. **Geen betekenis (Nul-positie)**
  - Geen effect op betekenis; geldt voor conditionele werking (randvoorwaarden, hygiëne)
  - Voorbeeld: workspace stewards, formatters
1. **Beschrijvend**
  - Legt vast, legt uit, documenteert wat er is of was
  - Voorbeeld: verslagen, overzichten
2. **Structurerend**
  - Maakt samenhang, relaties en architectuur expliciet
  - Voorbeeld: ArchiMate-modelleur
3. **Normerend**
  - Normeert structuur en indeling van toekomstig werk
  - Voorbeeld: thema-vormende agent
4. **Vastleggend**
  - Realiseert direct gedrag, structuur of configuratie
  - Voorbeeld: codegenerator, deployment-configurator
5. **Realiserend**
  - Realiseert feitelijk gedrag, structuur of configuratie
  - Voorbeeld: Angular-UI-agent
6. **Evaluerend**
  - Legt oordeel of duiding vast, beoordeelt kwaliteit
  - Voorbeeld: review-agent, test-agent

### Synoniemen
- Effect-as
- Betekenis-as

### Analogieën
- Prescriptive vs descriptive vs evaluative in informatiekunde
- Read vs write vs validate in softwareontwikkeling

### Toelichting
Het betekeniseffect is de primaire as voor agent-classificatie omdat deze de fundamentele rol en impact van een agent op betekenis bepaalt. Het onderscheid tussen structuur-normering (werk) en ecosysteem-normering (spelregels) is cruciaal.

---

## Werking

### Definitie
**Werking** is een classificatie-as die beschrijft of een agent intervenieert in de inhoud of in de voorwaarden waaronder inhoudelijk werk kan plaatsvinden.

**Leidende vraag:** Intervenieert deze agent in de inhoud, of in de voorwaarden waaronder inhoudelijk werk kan plaatsvinden?

### Kenmerken
- Eén van vier orthogonale assen
- Onderscheidt agents op basis van interventiegebied
- Onafhankelijk van andere assen
- Bepaalt of de agent op inhoud of voorwaarden werkt

### Wat het niet is
- Geen kwaliteitsmaatstaf
- Geen hiërarchische indeling
- Geen technische eigenschap

### Categorieën
1. **Inhoudelijk**
  - Werkt direct op betekenisvolle artefacten
  - Omvat alle categorieën van het betekeniseffect
2. **Representatie-omvormend**
  - Zet inhoud om van de ene representatie naar de andere
  - Betekenis-blind; infrastructuurachtig
3. **Conditioneel**
  - Werkt niet op inhoud, maar op voorwaarden en hygiëne
  - Subtypen: workspace steward, engineering steward

### Synoniemen
- Werkgebied-as

### Analogieën
- Business logic vs infrastructure in softwareontwikkeling
- Content vs governance layers in enterprise architectuur

### Toelichting
Werking maakt onderscheid tussen agents die inhoud beïnvloeden en agents die voorwaarden voor inhoudelijk werk bewaken. Conditionele agents zijn essentieel, maar werken op een ander niveau.

---

## Vormingsfase

### Definitie
**Vormingsfase** beschrijft in welke fase van de totstandkoming van werk een rol of interventie plaatsvindt. Zij positioneert het werk in de keten van intentie tot operationalisatie.

**Leidende vraag:** Waar in het systeem vindt de ingreep plaats?

### Kenmerken
- Orthogonaal aan het betekeniseffect
- Classificeert de fase van ingreep, niet het type handeling
- Geldt voor alle inhoudelijke categorieën
- Maakt onderscheid tussen werk, ontwerp, architectuur, operationalisatie en ecosysteem
- Verhoogt bestuurbaarheid en traceerbaarheid

### Wat het niet is
- Geen hiërarchische waardering
- Geen inhoudelijke classificatie
- Geen technische laag
- Geen waardeoordeel

### Fasen
1. **Verkenning**
  - Onderzoeken van intentie, probleemstelling of richting
  - Voorbeeld: probleemanalyse, hypothesevorming
2. **Ordening**
  - Structureren van intentie en expliciet maken van samenhang
  - Voorbeeld: uitwerking van een thema, processtructuur
3. **Vastlegging**
  - Betekenis bindend vaststellen binnen de workspace
  - Voorbeeld: vaststellen van requirements, architectuurprincipes
4. **Realisatie**
  - Betekenis werkend maken in systemen of processen
  - Voorbeeld: implementatie, deployment
5. **Toetsing**
  - Gerealiseerd artefact beoordelen tegen een norm
  - Voorbeeld: review, test, audit
6. **Operationalisatie**
  - Gerealiseerde structuur formeel in werking stellen in de praktijk
  - Voorbeeld: go-live, migratie, monitoring

### Synoniemen
- Fase-as
- Systeem- of ecosysteemfase

### Analogieën
- Projectfasering, value stream mapping

### Toelichting
Vormingsfase zegt niets over de aard van de betekenisinterventie (dat is het betekeniseffect), maar uitsluitend over waar in het proces de interventie plaatsvindt.




---

**Patroon:** Canon → Input → Exploratief → Canon  
Dit reflecteert cyclische besturing: governance stuurt aan, operatie volgt, onzekerheden worden beheerd, resultaat wordt genormeerd.

## Artefacten en betekeniseffecten bij Operationalisatie

Bij de fase **Operationalisatie** horen specifieke artefacten en bijbehorende betekeniseffecten. Deze artefacten markeren de overgang van gerealiseerde structuur naar geldende werkelijkheid en zijn essentieel voor het daadwerkelijk van kracht worden van besluiten, systemen of processen.

### Typische artefacten bij Operationalisatie

| Subfase         | Artefacttype                | Voorbeelden                                              |
|-----------------|----------------------------|----------------------------------------------------------|
| Besluiten       | Vastleggend artefact        | Go-live besluit, change approval, investeringsbesluit    |
| Activering      | Vastleggend artefact        | Deployment scripts, feature flag activatie, contractstart|
| Begeleiding     | Beschrijvend artefact       | Migratieplan, overdrachtsdocument, cutover-rapportage    |
| Bestendiging    | Beschrijvend artefact       | Monitoringrapport, evaluatieverslag, governance-update   |

### Betekeniseffecten per artefact

- **Vastleggend artefact**:  
	- Betekeniseffect: *Vastleggend*  
	- Maakt formeel of feitelijk een nieuwe werkelijkheid van kracht (bijv. besluit, activering).
- **Registrerend artefact**:  
	- Betekeniseffect: *Beschrijvend* of *evaluerend*  
	- Legt de overgang, begeleiding en borging vast, biedt inzicht en verantwoording.

### Samenvatting

- **Operationalisatie** vereist vastleggende artefacten voor besluiten en activering (vastleggend betekeniseffect).
- Begeleiding en bestendiging worden ondersteund door registrerende artefacten (beschrijvend/evaluerend betekeniseffect).
- De artefacten zijn essentieel voor traceerbaarheid, governance en het daadwerkelijk realiseren van de bedoelde verandering.
# Operationalisatie

## Definitie

**Operationalisatie** is de fase waarin een gerealiseerde en geverifieerde structuur formeel in werking wordt gesteld binnen de beoogde context, waardoor zij geldende werkelijkheid wordt.

Waar:

- **Vastlegging** betekenis bindend maakt,  
- **Realisatie** betekenis werkend maakt,  

maakt **Operationalisatie** de werkende structuur daadwerkelijk van kracht in de praktijk.

Operationalisatie markeert de overgang van:

> werkende structuur in de workspace  
> naar  
> geldende structuur in de werkelijkheid.

---

## Kenmerken

- Contextovergang (van workspace naar praktijk)  
- Formele of feitelijke activering  
- Wijziging van de geldende werkelijkheid  
- Kan juridische, organisatorische of technische consequenties hebben  
- Is onomkeerbaarder dan realisatie  
- Heeft vaak governance-implicaties  

---

## Subfasen van Operationalisatie

Deze subfasen zijn value-stream generiek en toepasbaar op software, governance, organisatie, investeringen, etc.


### Besluiten

Formeel of impliciet besluit dat de gerealiseerde structuur in werking mag treden.

### Kenmerken

- Mandaat of bevoegdheid wordt geëffectueerd  
- Acceptatie wordt bekrachtigd  
- Risico-overgang wordt erkend  

### Voorbeelden

**Software**

- Go-live besluit  
- Change approval  

**Niet-software**

- Formele bekrachtiging van nieuw beleid  
- Investeringsgoedkeuring  
- Bestuurlijk besluit tot invoering  

---

### Activering

Het daadwerkelijk technisch, organisatorisch of juridisch in werking stellen van de structuur.

### Kenmerken

- Concrete overgang naar actieve status  
- Wijziging van runtime- of praktijkcondities  
- Niet langer hypothetisch  

### Voorbeelden

**Software**

- Deployment naar productie  
- Feature flag activeren  
- Configuratie live zetten  

**Niet-software**

- Nieuw proces starten  
- Organisatiestructuur doorvoeren  
- Contract laten ingaan  

---

### Begeleiding

Het begeleiden van de overgang van oude naar nieuwe situatie.

### Kenmerken

- Overgangsmaatregelen  
- Afbouw of migratie  
- Stabilisatie  

### Voorbeelden

**Software**

- Datamigratie  
- Parallel run  
- Cutover  

**Niet-software**

- Overdrachtsperiode  
- Gefaseerde invoering  
- Inwerken van betrokkenen  

---

## Bestendiging

Het verankeren van de nieuwe structuur als reguliere werkelijkheid.

### Kenmerken

- Monitoring en stabilisatie  
- Verankering in beleid of praktijk  
- Normalisatie  

### Voorbeelden

**Software**

- Monitoring in productie  
- Incidentmanagement  
- Performance-optimalisatie  

**Niet-software**

- Evaluatie van nieuw proces  
- Formele opname in governance  
- Structurele budgettering  


## Bronhouding bij subfasen van Operationalisatie

De subfasen van **Operationalisatie** (Besluiten, Activering, Begeleiding, Bestendiging) hebben elk een karakteristieke **bronhouding**:

### 1. Besluiten
**Bronhouding: Canon-gebonden**
- Baseert zich op vastgelegde governance-artefacten en mandaten
- Besluitvorming volgt canonieke procedures en bevoegdheidsregels
- Output moet traceerbaar zijn naar governance-artefacten

### 2. Activering
**Bronhouding: Input-gebonden**
- Haalt instructies uit richtinggevende en vastleggende artefacten
- Transformeert deze rechtstreeks naar technische, organisatorische of juridische status
- Geen creatieve of exploratieve interpreatie; zuiver procedureel

### 3. Begeleiding
**Bronhouding: Exploratief**
- Omgaat met onzekerheden in overgangsprocessen
- Maakt context-afhankelijke aanpassingen
- Expliciteert aannames over migratie, stabilisatie en risico's
- Voor grote transities: maximaal 3 expliciete aannames per subfase-iteratie

### 4. Bestendiging
**Bronhouding: Canon-gebonden**
- Verankert nieuwe structuur in canonieke governance en beleid
- Documenteert permanente wijzigingen
- Maakt normatieve vastlegging voor toekomstig onderhoud


### Orthogonaliteit

Vormingsfase moet altijd gecombineerd worden met het betekeniseffect.

**Voorbeeldmatrix**:

| Betekeniseffect     | Vormingsfase      | Werking           | Bronhouding        |
|---------------------|-------------------|-------------------|--------------------|
| seschrijvend        | Verkenning		  | Inhoudelijk       | open (exploratief) |
| structurerend       | Ordening          | Inhoudelijk       | workspace-gebonden |
| normerend           | Vastlegging       | Inhoudelijk       | canon-gebonden     |
| realiserend         | Realisatie        | Inhoudelijk       | gesloten (input-gebonden)    |
| evaluerend          | Toetsing          | Inhoudelijk       | gesloten (input-gebonden) / beschrijvend |
| beschrijvend        | verantwoording    | Inhoudelijk       | canon-gebonden     |
| operationalisatie   | Operationalisatie | Inhoudelijk       | canon-gebonden / open (exploratief) / gesloten (input-gebonden) |

---

## Bronhouding

### Definitie
**Bronhouding** is een classificatie-as die beschrijft op welke kennisbronnen een agent zich baseert en in welke mate de output herleidbaar is tot expliciete bronnen.

**Leidende vraag:** Op welke kennisbronnen baseert deze agent zich, en hoe herleidbaar is de output?

### Kenmerken
- Eén van vier orthogonale assen
- Onderscheidt agents op basis van kennisbrongebruik en herleidbaarheid
- Onafhankelijk van andere assen
- Bepaalt de epistemische verantwoordelijkheid en controleerbaarheid van de agent

### Wat het niet is
- Geen kwaliteitsmaatstaf van de output
- Geen technische implementatiekeuze
- Geen indicatie van complexiteit of waarde

### Categorieën
1. **Input-gebonden**
  - Output is 100% herleidbaar tot de input
  - Geen externe kennisbronnen
  - Voorbeeld: sorteerders, parsers
2. **Canon-gebonden**
  - Baseert zich expliciet op de Mandarin-canon
  - Canon-verwijzing verplicht in de output
  - Voorbeeld: doctrine-interpreterende agent
3. **Externe-bron gebonden**
  - Haalt kennis uit specifieke bronnen buiten de canon
  - Bronvermelding verplicht
  - Voorbeeld: documentatie-samenvattende agent
4. **Exploratief**
  - Genereert output op basis van trained knowledge en redenering
  - Maakt aannames en afleidingen (max 3 expliciet)
  - Voorbeeld: architectuur-ontwerpende agent

### Verplichte checks per categorie
| Categorie           | Verplichte checks                |
|---------------------|----------------------------------|
| Input-gebonden      | 100% herleidbaar                 |
| Canon-gebonden      | Canon-verwijzing verplicht       |
| Externe-bron gebonden | Bronvermelding verplicht      |
| Exploratief         | Aannames expliciet (max 3)       |

### Synoniemen
- Epistemische houding
- Kennisbron-as
- Herleidbaarheidsdimensie

### Analogieën
- Transparency levels in AI systems
- Primaire vs secundaire bronnen in onderzoek
- Pure functions vs database-driven vs AI-augmented in software

### Toelichting
Bronhouding maakt expliciet hoe een agent tot zijn kennis komt en in welke mate de output controleerbaar en herleidbaar is. Dit is cruciaal voor vertrouwen, governance en kwaliteitsborging.

---
## Artefact-functie-as

### Definitie
De **artefact-functie-as** is een classificatie-as voor **Mandarin-artefacten** die beschrijft *welke functie* een artefact vervult in de besluit- en waardeketen binnen het ecosysteem.

**Leidende vraag:** *Welke vastleggende, structurerende, vastleggende of registrerende functie heeft dit artefact in het ecosysteem?*

### Kenmerken
- Is een ordenings-as specifiek voor **Mandarin-artefacten** (niet voor **mandarin-agents**)
- Positioneert artefacten op basis van hun rol in besluitvorming, structurering, uitvoering en inzicht
- Vormt samen met de **representatie-as** de kern van **Artefactclassificatie**
- Is onafhankelijk van bestandsformaat, tooling of repository-structuur
- Is onafhankelijk van procesfase of value stream-fase; hetzelfde artefact kan in meerdere fasen worden gebruikt, maar heeft één primaire functie

### Posities

Op de **artefact-functie-as** worden de volgende vier canonieke posities onderscheiden:

**1. Vastleggend artefact**
- Legt normen, regels, kaders of richting vast
- Bevat vastleggende afspraken of voorschriften
- Specialisaties: **governance-artefact** (ecosysteem- en value-stream-overstijgend) en **richtinggevend artefact** (waarde value streams 1-n)

**2. Structurerend artefact**
- Representeert een coherent geheel van architectuurelementen en hun onderlinge relaties
- Geordend volgens een metamodel of kader
- Maakt de structuur van een systeem expliciet en beredeneerbaar
- Voorbeelden: architectuurmodellen, metamodellen, structuurontwerpen

**3. Vastleggend artefact**
- Realiseert direct gedrag, structuur of configuratie in systemen of processen
- Heeft uitvoerbare of door tooling direct interpreteerbare impact
- Voorbeelden: database-schema's, deployment-configuraties, codegeneratie-templates met vastleggend karakter

**4. Registrerend artefact**
- Maakt bestaande of voorgenomen werkelijkheid inzichtelijk
- Legt analyse, structuur of samenhang vast zonder zelf vastleggend of vastleggend te zijn
- Voorbeelden: modellen, analyses, overzichten, documentatie, handleidingen

### Wat het niet is

## Vormingsfase

### Definitie
De **vormingsfase** beschrijft in welke fase van de totstandkoming van werk een rol of interventie plaatsvindt. Zij positioneert het werk in de keten van intentie tot operationalisatie.

De vormingsfase zegt niets over de aard van de betekenisinterventie (dat is het betekeniseffect), maar uitsluitend over **waar in het proces** de interventie plaatsvindt.

Er worden zes fasen onderscheiden:

1. Verkenning
2. Ordening
3. Vastlegging
4. Realisatie
5. Toetsing
6. Operationalisatie

**Leidende vraag**: Waar in het systeem vindt de ingreep plaats?

### Kenmerken
- Is orthogonaal aan het betekeniseffect (effect op betekenis)
- Classificeert de fase van ingreep, niet het type handeling
- Geldt voor alle inhoudelijke categorieën (normerend, beschrijvend, realiserend, vastleggend, evaluerend, operationaliserend)
- Maakt onderscheid tussen werk, ontwerp, architectuur, operationalisatie en ecosysteem
- Verhoogt bestuurbaarheid en traceerbaarheid

### Wat het niet is
- Geen hiërarchische waardering (geen fase is per definitie belangrijker dan een andere)
- Geen inhoudelijke classificatie (dat is het betekeniseffect)
- Geen technische laag (zoals runtime, tooling of infrastructuur)
- Geen waardeoordeel

### Fasen

#### 1. Verkenning
Fase waarin intentie, probleemstelling of richting wordt onderzocht en verkend.

#### 2. Ordening
Fase waarin intentie wordt gestructureerd en samenhang expliciet wordt gemaakt.

#### 3. Vastlegging
Fase waarin betekenis bindend wordt vastgesteld binnen de workspace.

#### 4. Realisatie
Fase waarin betekenis werkend wordt gemaakt in systemen of processen.

#### 5. Toetsing
Fase waarin een gerealiseerd of gespecificeerd artefact wordt beoordeeld tegen een vastgelegde norm.

#### 6. Operationalisatie
Fase waarin een gerealiseerde en geverifieerde structuur formeel in werking wordt gesteld binnen de beoogde context, waardoor zij geldende werkelijkheid wordt.

Operationalisatie markeert de overgang van werkende structuur in de workspace naar geldende structuur in de werkelijkheid.

**Subfasen van Operationalisatie:**
  - Besluiten (canon-gebonden)
  - Activering (input-gebonden)
  - Begeleiding (exploratief)
  - Bestendiging (canon-gebonden)

**Voorbeelden:**
- Go-live besluit, deployment naar productie, migratieplan, monitoringrapport, governance-update

### Matrix (voorbeeld)

| Betekeniseffect     | Vormingsfase      | Werking           | Bronhouding        |
|---------------------|-------------------|-------------------|--------------------|
| beschrijvend        | Verkenning        | Inhoudelijk       | open (exploratief) |
| structurerend       | Ordening          | Inhoudelijk       | workspace-gebonden |
| normerend           | Vastlegging       | Inhoudelijk       | canon-gebonden     |
| realiserend         | Realisatie        | Inhoudelijk       | gesloten (input-gebonden)    |
| evaluerend          | Toetsing          | Inhoudelijk       | gesloten (input-gebonden) / beschrijvend |
| operationaliserend  | Operationalisatie | Inhoudelijk       | canon-gebonden / open (exploratief) / gesloten (input-gebonden) |
- Workspace-state
- Handoff-documenten

### Synoniemen
- Systeem-artefact
- Ecosysteem-artefact
- Faciliterend artefact

### Analogieën 
- Vergelijkbaar met **API contracts**, **infrastructuurdefinities**, **configuration files** in DevOps
- In SOA: **WSDL's**, **service agreements**, **orchestration definitions**
- In projectmanagement: **charter**, **governance framework**

### Toelichting  
**Governance-artefacten** zijn vastleggend voor het ecosysteem en ontstaan uitsluitend in value stream "**mandarin-agent** Ecosysteem Ontwikkeling". Zij maken het mogelijk dat **mandarin-agents**, workspaces en value streams gecontroleerd en consistent kunnen functioneren. Als specialisatie van vastleggend artefact zijn governance-artefacten vastleggend en prescriptief, en operationeel in specifieke fasen (Grondslagvorming of Ecosysteeminrichting) van value stream 0.

---

## Richtinggevend artefact

### Definitie
Een **richtinggevend artefact** (synoniem: **value-stream-artefact**) is een specialisatie van een **vastleggend artefact** dat expliciet de gewenste inhoud, structuur of randvoorwaarden van een **value stream fase** in een **waarde value stream** (value streams 1-n) vastlegt en daarmee richting geeft aan realisatie en verdere uitwerking.

### Kenmerken
- Is een **specialisatie van vastleggend artefact**
- Ontstaat binnen een value stream fase in waarde value streams (value streams 1-n, niet in value stream 0)
- Vertegenwoordigt inhoudelijke keuzes, richting en gewenste resultaten
- Is input voor volgende fasen en voor vastleggende artefacten
- Wordt geleverd door uitvoerende **mandarin-agents** met inhoudelijke verantwoordelijkheid
- Is primair artefact (niet afgeleid uit andere artefacten)
- Erft alle kenmerken van vastleggend artefact (vastleggend, prescriptief, versieerbaar, operationeel in maximaal één value stream fase)

### Wat het niet is
- Geen algemeen vastleggend artefact (is specifiek voor waarde value streams)
- Geen governance-artefact (ontstaat niet in value stream "**mandarin-agent** Ecosysteem Ontwikkeling")
- Geen vastleggend artefact (legt niet de feitelijke implementatie vast)
- Geen afgeleide representatie (is niet primair afgeleid uit andere artefacten)
- Geen interne notitie

### Voorbeelden
- Requirements en specifieke eisenpakketten
- Ontwerpdocumenten en solution outlines
- Logische datamodellen (primair, richtinggevend)
- Richtlijnen voor API-contracten of berichtenstructuren

### Synoniemen
- Value-stream-artefact
- Waarde-artefact
- Richtinggevend normatief artefact

### Analogieën 
- Vergelijkbaar met business requirements, solution outlines, logical data models
- In DDD: ontwerp- en specificatie-artefacten die implementatie sturen

### Toelichting  
**Richtinggevende artefacten** leggen vast wat er inhoudelijk moet gelden in een waarde value stream (1-n), zonder te bepalen *hoe* dit technisch precies wordt gerealiseerd. Zij sturen daarmee de creatie van **vastleggende artefacten** (zoals code en DDL) en vormen het primaire, vastleggende referentiepunt voor afgeleide modellen en documentatie.

---

## Vastleggend artefact

### Definitie
Een **vastleggend artefact** is een **Mandarin-artefact** dat direct gedrag, structuur of configuratie in een werkend systeem realiseert op basis van richtinggevende artefacten.

### Kenmerken
- Is uitvoerbaar, interpreteerbaar of direct toepasbaar door tooling of runtime-omgevingen
- Realiseert beslissingen en structuren die eerder in richtinggevende artefacten zijn vastgelegd
- Is meestal niet zelf vastleggend, maar volgt vastleggende artefacten
- Wijzigingen hebben direct effect op systeemgedrag of data
- Kan gegenereerd zijn uit andere artefacten of handmatig gemaakt

### Wat het niet is
- Geen richtinggevend artefact (legt geen norm of intentie vast)
- Geen puur registrerend artefact
- Geen afgeleide representatie die alleen structuur uitlegt zonder iets te realiseren

### Voorbeelden
- PostgreSQL- of andere database-DDL (CREATE TABLE, CONSTRAINTS, etc.)
- Angular- of andere frontend/backend-code die functionaliteit realiseert
- Scripts om een database initieel te vullen met data (seed-scripts)
- Infrastructuur-als-code bestanden (bijv. Terraform, Ansible, Kubernetes manifests)

### Synoniemen
- Implementatie-artefact
- Uitvoerbaar artefact

### Analogieën 
- In softwareontwikkeling: gecompileerde of interpreteerbare artefacten die in productie draaien
- In DevOps: deployment- en configuratiebestanden die gedrag bepalen

### Toelichting  
**Vastleggende artefacten** vormen de brug tussen richtinggevende artefacten en het werkende systeem. Zij maken de bedoelde structuur en het gewenste gedrag feitelijk waar in code, data en configuratie.


---

## Structurerend artefact

### Definitie
Een **structurerend artefact** is een **Mandarin-artefact** dat een coherent geheel van architectuurelementen en hun onderlinge relaties representeert, geordend volgens een metamodel of kader, met als doel de structuur van een systeem expliciet en beredeneerbaar te maken.

### Kenmerken
- Representeert architectuurelementen en hun onderlinge relaties
- Volgt een expliciet metamodel of ordeningskader
- Maakt systeemstructuur expliciet en beredeneerbaar
- Is coherent en intern consistent
- Biedt structurele ordening zonder directe realisering
- Kan vastleggend of registrerend zijn, afhankelijk van de intentie

### Wat het niet is
- Geen direct vastleggende structuur (zoals database-schema's)
- Geen losse beschrijving zonder coherent kader
- Geen ad-hoc visualisatie zonder metamodel
- Geen implementatie of uitvoering

### Voorbeelden
- ArchiMate-modellen met bedrijfsarchitectuur
- UML-klassendiagrammen (structureel)
- Enterprise architectuurmodellen
- Domeinmodellen met relaties en constraints
- Metamodellen
- C4-modellen (container- en componentniveau)

### Synoniemen
- Architectuurmodel
- Structuurmodel
- Metamodel-conform artefact

### Analogieën 
- Vergelijkbaar met blueprints in de bouw (tonen structuur, niet het gebouw zelf)
- In enterprise architectuur: architectural models, viewpoints
- In softwareontwikkeling: UML class diagrams, domain models

### Toelichting  
**Structurerende artefacten** maken de architectonische structuur van systemen expliciet door elementen en hun relaties te ordenen volgens een coherent kader. Zij verschillen van **registrerende artefacten** door hun focus op structurele coherentie en metamodel-conformiteit, en van **vastleggende artefacten** omdat zij structuur representeren maar niet direct uitvoeren.

---


# Beschrijvingsmodus

## Definitie

**Beschrijvingsmodus** is een classificatie van een beschrijvend artefact die vastlegt onder welk kennis- en verantwoordingsregime de beschrijving tot stand is gekomen en geïnterpreteerd moet worden.

De beschrijvingsmodus specificeert:

- de intentie van de beschrijving (verkennen of verantwoorden),
- de mate van canonbinding,
- de vereiste herleidbaarheid,
- de epistemische discipline van het artefact.

Beschrijvingsmodus verandert niet de artefactfunctie.  
Het artefact blijft beschrijvend; de modus bepaalt de epistemische positie ervan.

## Kenmerken

- Is alleen betekenisvol bij artefactfunctie = beschrijvend.
- Modelleert kennisintentie, niet ecosysteemeffect.
- Is orthogonaal aan:
  - Artefactfunctie
  - Representatie
  - Afleidingspositie
- Heeft implicaties voor bronhouding en verantwoordingsdiscipline.
- Kan normatieve gevolgen hebben indien governance dat expliciet vastlegt.

## Geldige waarden

### Verkennend

**Doel**: verkennen, onderzoeken, hypothesevorming  
**Canonbinding**: niet verplicht  
**Herleidbaarheid**: situationeel  
**Karakter**: open, voorlopig  

**Effect**:

> Genereren van inzicht zonder legitimerende pretentie.

Exploratieve beschrijvingen mogen:

- alternatieve interpretaties bevatten,
- onzekerheid expliciteren,
- meerdere perspectieven naast elkaar zetten.

---

### 2. Verantwoordend

**Doel**: legitimeren, aantonen, expliciet herleidbaar maken  
**Canonbinding**: verplicht indien relevant  
**Herleidbaarheid**: expliciet en controleerbaar  
**Karakter**: disciplinair, toetsbaar  

**Effect**:

> Verantwoorden van inzicht binnen geldige grondslagen.

Verantwoordende beschrijvingen vereisen:

- expliciete bronverwijzing,
- consistente toepassing van canon,
- uitsluiting van speculatieve redeneringen zonder markering.

---

## Representatie

### Definitie
Een **representatie** is de specifieke vorm waarin een artefact of betekenis wordt vastgelegd, weergegeven of uitgewisseld, zonder de onderliggende betekenis zelf te bepalen.

### Toelichting  
Een **representatie** beschrijft *hoe* iets wordt uitgedrukt, niet *wat* het betekent. Zij maakt betekenis waarneembaar, deelbaar of verwerkbaar, maar is niet die betekenis zelf.

Dezelfde inhoud kan in meerdere representaties bestaan, bijvoorbeeld:
- tekst
- diagram
- programma code
- machine taal

Deze representaties zijn inhoudelijk equivalent, maar functioneel verschillend: zij dienen andere doelen en doelgroepen.

### Kenmerken
Een representatie:
- is afgeleid van een onderliggende betekenis of structuur
- heeft geen eigen normatieve kracht
- kan worden vertaald naar andere representaties
- is context- en doelafhankelijk (mens, machine, visualisatie)
- verandert niet de betekenis, alleen de toegankelijkheid of bruikbaarheid
- heeft altijd een **afleidingspositie** (leidend of afgeleid)

### Wat het niet is
- Geen artefact op zichzelf (het is een eigenschap van een artefact)
- Geen normering of besluit
- Geen inhoudelijke structuur
- Geen model van de werkelijkheid

Een representatie draagt betekenis, maar bepaalt haar niet.

### Voorbeelden
- Markdown, XML, JSON, YAML (tekst / programma code)
- ArchiMate view, UML diagram (diagram)
- Binaire executable (machine taal)

In al deze gevallen blijft de onderliggende betekenis gelijk, terwijl de vorm verschilt.

### Relatie tot **mandarin-agents**

**Inhoudelijke **mandarin-agents****
- Werken op betekenis en creëren of wijzigen representaties.

**Representatie-omvormende **mandarin-agents****
- Werken uitsluitend op representaties, zonder begrip van betekenis.

Een representatie-omvormende **mandarin-agent** verandert de uitdrukking, niet de inhoud.

---

## Afleidingspositie

### Definitie
**Afleidingspositie** is het meta-concept dat vastlegt of een **representatie** geldt als leidende bron van betekenis, dan wel is afgeleid van een andere representatie, zonder de onderliggende betekenis zelf te wijzigen.

De afleidingspositie zegt niets over de inhoud, maar alles over de positie van een representatie in de keten van afleiding.

### Categorieën binnen afleidingspositie

#### 1. Leidend

##### Definitie
Een **leidende** representatie is een representatie die geldt als het primaire vastleggingspunt van betekenis binnen een context.

Dit is de representatie:
- waar betekenis formeel aan wordt ontleend
- die leidend is bij interpretatie
- die niet afhankelijk is van een andere representatie voor haar geldigheid

##### Kenmerken
Een leidende representatie:
- is autoritatief binnen haar domein of scope
- fungeert als referentie voor afgeleide representaties
- kan door mensen worden vastgesteld, beoordeeld of gewijzigd
- heeft wijzigingen die doorwerken naar afgeleiden
- is vaak expliciet aangewezen (door governance of afspraak)

##### Wat een leidende representatie niet is
- Geen "eerste bestand" per se
- Geen technisch origineel
- Geen onveranderlijke waarheid

Een leidende representatie is leidend bij verschil van interpretatie, niet per definitie ouder of technischer.

#### 2. Afgeleid

##### Definitie
Een **afgeleide** representatie is een representatie die mechanisch of procedureel is gegenereerd of afgeleid uit een leidende representatie.

##### Kenmerken
Een afgeleide representatie:
- ontleent haar geldigheid volledig aan de leidende representatie
- mag worden overschreven of opnieuw gegenereerd zonder verlies van betekenis
- dient vaak een specifiek doel (bijv. leesbaarheid, machine-verwerking)

---

## Prompt canon-curator: publiceer normatieve wijziging

Deze bijlage legt de canonieke prompt vast voor de **mandarin.canon-curator**-agent met intentie **publiceer-normatieve-wijziging**. Dit is een governance-artefact in de vorm van een promptdefinitie.

```yaml
---
agent: mandarin.canon-curator
intent: publiceer-normatieve-wijziging
charter_ref: @main:charters-agents/canon-curator.charter.md
---
```

Deze prompt verankert de relatie tussen de canon-curator en het bijbehorende charter en maakt expliciet onder welke intentie normatieve wijzigingen in de canon worden gepubliceerd.

---

## Change Log

| Datum      | Versie | Wijziging                                                           | Auteur     |
|------------|--------|---------------------------------------------------------------------|------------|
| 2026-03-01 | 1.6.1  | Terminologie geharmoniseerd (interventieniveau → vormingsfase), alle concepten uniform beschreven, matrix en toelichtingen aangepast, richtlijn bronhouding toegevoegd, bronnen Agentic AI toegevoegd, structuur en opmaak verbeterd. | Constitutioneel Auteur  |
| 2026-02-22 | 1.13.0 | Betekeniseffect-as voor agents gemapt op artefactfuncties: Structurerend toegevoegd als categorie. | Constitutioneel Auteur  |
| 2026-02-22 | 1.12.0 | Artefactclassificatie herzien naar 3 concepten: Functie (vastleggend, structurerend, vastleggend, registrerend), Representatie (tekst, diagram, programma code, machine taal) en Afleidingspositie (leidend, afgeleid). Documenterend en Afgeleid artefact verwijderd als functies. | Constitutioneel Auteur  |
| 2026-02-21 | 1.11.0 | Toegevoegd: Nul-positie (Geen betekenis) aan Betekeniseffect-as voor conditionele en representatie-omvormende werking | Constitutioneel Auteur  |
| 2026-02-21 | 1.11.0 | Posities op as Bronhouding hernoemd naar: Input-gebonden, Canon-gebonden, Externe-bron gebonden, Exploratief | Constitutioneel Auteur  |
| 2026-02-21 | 1.10.0 | Toegevoegd: Bronhouding (voorheen Epistemische as) als vierde orthogonale as voor mandarin-agent-classificatie, met vier categorieën (Deterministisch, Canon-gebonden, Retrieval-gebonden, Generatief) en verplichte checks per categorie | Constitutioneel Auteur  |
| 2026-02-15 | 1.9.0  | Toegevoegd: Architectuur-structurerend als positie op betekenis-as voor mandarin-agents | Constitutioneel Auteur  |
| 2026-02-15 | 1.8.0  | Toegevoegd: Structurerend artefact als positie op artefact-functie-as | Constitutioneel Auteur  |
| 2026-02-02 | 1.7.0  | Toegevoegd: Artefact-functie-as als expliciete ordenings-as voor Mandarin-artefacten, gekoppeld aan Artefactclassificatie | Constitutioneel Auteur  |
| 2026-02-02 | 1.6.0  | Herziening Artefactclassificatie: expliciete tweedimensionale ordening langs artefact-functie-as en representatievorm-as, voorbeelden uitgebreid | Constitutioneel Auteur  |
| 2026-02-01 | 1.5.0  | Bedrijfs-artefact hernoemd naar Richtinggevend artefact; toegevoegd: Vastleggend artefact en Afgeleid artefact als aanvullende ordeningsconcepten | Constitutioneel Auteur  |
| 2026-02-01 | 1.4.0  | Toegevoegd: meta-concept Representatiestatus met categorie Bronrepresentatie | Constitutioneel Auteur  |
| 2026-02-01 | 1.3.0  | Toegevoegd: meta-concept Representatie als concrete uitdrukking van betekenis in een representatievorm | Constitutioneel Auteur  |
| 2026-02-01 | 1.2.0  | Toegevoegd: meta-concept Representatievorm als onderscheid tussen betekenis en vorm van artefacten | Constitutioneel Auteur  |
| 2026-02-01 | 1.1.0  | Toegevoegd: meta-concept Artefactclassificatie als ordeningskader voor Mandarin-artefacten en hun typen | Constitutioneel Auteur  |
| 2026-02-01 | 1.0.0  | Initiële versie — **ordenings-concepten** afgesplitst van concepten-en-architectonische-grondslagen.md v1.6.0; bevat classificatie-concepten (mandarin-agent-classificatie, As, 4 assen) en artefact-structuur (Mandarin-artefact met specialisaties) | Constitutioneel Auteur  |

---

**Einde document**

---

# Aanbevelingen voor verdere ontwikkeling en borging

<!--
Deze aanbevelingen zijn toegevoegd op basis van analyse en review van de huidige ordeningsconcepten en classificatiestructuren. Ze zijn bedoeld om de stabiliteit, systematiek en normatieve kracht van het Mandarin-ecosysteem te versterken.
Bron: temp/aanbevelingen.md, versie en datum zie changelog.
-->

## 1. Stabiliseer meta sneller dan domein

**Probleem:**
Terminologie binnen de artefact- en classificatielagen evolueert zichtbaar (bijv. normerend → vastleggend), wat risico geeft op interpretatieverschuiving bij agents en in intent-naming.

**Aanbeveling:**
Bevries de hoofdassen van mandarin-agent-classificatie.
Bevries de hoofdcategorieën van artefact-classificatie.
Sta alleen evolutie toe in subklassen of toelichtingen.
Hanteer een expliciete “meta-stabiliteitsregel”: Meta-terminologie evolueert trager dan domeinterminologie.

**Doel:**
Voorkomen dat classificatie verschuift terwijl implementaties en doctrines daarop vertrouwen.

## 2. Maak artefact-classificatie even systematisch als agent-classificatie

**Probleem:**
Agent-classificatie is orthogonaal en matrix-gebaseerd. Artefact-classificatie is momenteel een typologische lijst zonder expliciete assen.

**Aanbeveling:**
Introduceer een orthogonaal classificatiemodel voor artefacten, bijvoorbeeld langs assen als:
- Normatief effect (vastleggend / richtinggevend / registrerend)
- Interventieniveau (ecosysteem / architectuur / werk)
- Temporaliteit (tijdloos / fasegebonden / contextueel)
- Afleidingspositie (leidend / afgeleid)

Maak expliciet:
- Dat artefacten posities innemen op meerdere assen.
- Dat artefact-classificatie geen platte categorie-indeling is.

**Doel:**
Consistente systematiek tussen mandarin-agent-classificatie en artefact-classificatie. Architectonische symmetrie verhoogt overdraagbaarheid.

## 3. Scheid expliciet beschrijvend van normatief bindend

**Probleem:**
Ordeningsconcepten beschrijven classificatie, maar hebben impliciet normatieve gevolgen (bijv. voor intent-naming, governance, value stream-toekenning).
<!-- ...vervolg aanbevelingen indien gewenst... -->


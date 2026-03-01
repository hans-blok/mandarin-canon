# Conceptuele Grondslagen van het Mandarin-ecosysteem

**Type**: Concepten en Definities  
**Repository**: mandarin-canon  
**Identifier**: mandarin-canon.concepten.conceptuele-grondslagen  
**Version**: 1.1.0  
**Status**: Active  
**Last Updated**: 2026-02-21  
**Owner**: Hans Blok

---

## Herkomstverantwoording

Dit document is opgesteld door Constitutioneel Auteur op 1 februari 2026 om de conceptuele grondslagen van het Mandarin-ecosysteem expliciet, herbruikbaar en toetsbaar vast te leggen. Herijkt op 21 februari 2026 op basis van de nieuwe ordeningsconcepten.

**Geraadpleegde bronnen**:
- grondslagen/globaal/constitutie.md
- grondslagen/globaal/workspace-doctrine.md
- grondslagen/aeo/mandarin-ordeningsconcepten.md (gelezen op 2026-02-21)
- templates/concept-template.md

**Datum**: 2026-02-21  
**Doel**: Vastleggen van conceptuele grondslagen, ordeningsconcepten en basisbegrippen (concept, definitie, term, kenmerk) die gebruikt worden om het Mandarin-ecosysteem en de domeinconcepten consistent te structureren.

**Ontwerpkeuze**: Dit document gebruikt het format uit templates/concept-template.md als standaard voor conceptbeschrijvingen. De hier vastgelegde concepten zijn zelf meta van aard (ordenend en begripsvormend) en worden gebruikt als referentie door andere canonicale documenten.

**Normatief fundament**: Dit document volgt de documentatie-standaarden conform workspace-doctrine en doctrine-agent-charter-normering, en sluit aan op de ordeningsconcepten in mandarin-ordeningsconcepten.md.

---

## Inhoudsopgave

- [Concept — Conceptuele grondslagen](#concept--conceptuele-grondslagen)
- [Concept — Ordeningsconcepten](#concept--ordeningsconcepten)
- [Concept — Domeinconcepten](#concept--domeinconcepten)
- [Concept — Concept](#concept--concept)
- [Concept — Definitie](#concept--definitie)
- [Concept — Term](#concept--term)
- [Concept — Kenmerk](#concept--kenmerk)
- [Concept — As](#concept--as)

---

## Concept — Conceptuele grondslagen

### Definitie 
**Conceptuele grondslagen** zijn de kleinste, expliciet vastgelegde begrippen en ordeningskeuzes die gezamenlijk bepalen hoe we het Mandarin-ecosysteem begrijpen, beschrijven en structureren.

### Kenmerken 
- Bieden een stabiel referentiekader voor alle andere canonieke documenten
- Bestaan uit een beperkte set zorgvuldig gekozen basisbegrippen
- Zijn tooling- en implementatie-onafhankelijk
- Liggen vast in vastleggende artefacten (zoals dit document)

### Wat het niet is 
- Geen uitputtende woordenlijst van alle termen in het ecosysteem
- Geen procesbeschrijvingen of werkinstructies
- Geen technische architectuur of implementatiedetails

### Voorbeelden 
- Het onderscheid tussen **concept**, **term** en **definitie**

### Synoniemen  
- Begripsfundament
- Conceptuele basis

### Analogieën 
- In wiskunde: axioma's waarop een theorie rust
- In software-architectuur: funderende design principles

### Context en gebruik  
**Conceptuele grondslagen** worden gebruikt als referentiepunt bij het schrijven, toetsen en onderhouden van alle andere canonieke documenten. Wanneer er onzekerheid ontstaat over betekenis of structuur, wordt eerst teruggegrepen op deze grondslagen.


---

## Concept — Ordeningsconcepten

### Definitie 
**Ordeningsconcepten** zijn begrippen die niet het werk zelf beschrijven, maar de manier waarop andere concepten, artefacten en structuren worden geordend, geclassificeerd en met elkaar in relatie worden gebracht.

### Kenmerken 
- Werken op meta-niveau: ze beschrijven *hoe* we ordenen, niet *wat* er inhoudelijk is
- Structureren domeinconcepten, artefacten en agents
- Worden vastgelegd in meta-documenten (zoals mandarin-ordeningsconcepten.md)
- Zijn relatief stabiel en veranderen alleen bij expliciete herijking

### Wat het niet is 
- Geen domeininhoud (zoals business rules of functionele begrippen)
- Geen concrete artefacten of modellen
- Geen technische taxonomie van bestanden of folders

### Voorbeelden 
- **Artefactclassificatie** (indeling in vastleggende, structurerende, interpreterende en registrerende artefacten)
- **mandarin-agent-classificatie** (positionering langs orthogonale assen: Betekeniseffect, Interventieniveau, Werking, Bronhouding)
- **Representatie**, **representatievorm** en **representatiestatus**

### Synoniemen  
- Meta-concepten
- Ordenende begrippen

### Analogieën 
- In bibliotheekwetenschap: classificatiesystemen zoals Dewey of UDC
- In enterprise architectuur: metamodel dat domeinmodellen structureert

### Context en gebruik  
Ordeningsconcepten zorgen ervoor dat verschillende delen van de canon consistent met elkaar omgaan. Zij bepalen bijvoorbeeld hoe artefacten worden ingedeeld, hoe agents worden geclassificeerd en hoe domeinconcepten worden gegroepeerd.


---

## Concept — Domeinconcepten

### Definitie 
**Domeinconcepten** zijn begrippen die beschrijven waar het Mandarin-ecosysteem *inhoudelijk* uit bestaat en hoe waarde wordt geleverd, zoals agents, value streams, werkfases en artefacten.

### Kenmerken 
- Beschrijven de inhoud en werking van het ecosysteem
- Zijn direct gekoppeld aan value streams, agents en artefacten
- Worden gebruikt in specificaties, ontwerpen en implementaties
- Kunnen per value stream verschillen, maar delen dezelfde begripsgrondslag

### Wat het niet is 
- Geen meta-concepten of ordeningskeuzes
- Geen technische implementatie-details (zoals bestandsformaten of tools)
- Geen incidentele of tijdelijke termen zonder canonieke status

### Voorbeelden 
- **Mandarin-agent**, **value stream**, **value stream fase**, **workspace**
- **Bronregime**, **agent-boundary**, **agent-charter**
- Specifieke begrippen per value stream (bijv. klant, product, dienst)

### Synoniemen  
- Domeinbegrippen
- Inhoudelijke concepten

### Analogieën 
- In DDD: ubiquitous language van een bounded context
- In enterprise architectuur: business concepts in een business architecture

### Context en gebruik  
Domeinconcepten vormen de taal waarmee stakeholders, **mandarin-agents** en artefacten over hetzelfde werk spreken. Zij worden doorgaans vastgelegd in value-stream-specifieke documenten en sluiten aan bij de hier vastgelegde **conceptuele grondslagen**.


---

## Concept — Concept

### Definitie 
Een **concept** is een betekenisdragend begrip dat gebruikt wordt om werkelijkheid, werk of structuur te duiden, en dat expliciet kan worden vastgelegd in een definitie en gekoppeld aan één of meer termen.

### Kenmerken 
- Heeft een eigen, onderscheidbare betekenis binnen een context
- Kan expliciet worden gedefinieerd en hergebruikt
- Staat los van taal: dezelfde betekenis kan verschillende termen hebben
- Is de drager van betekenis waar artefacten, modellen en documenten naar verwijzen

### Wat het niet is 
- Geen woord of zin op zichzelf (dat is een **term**)
- Geen definitie (dat is de expliciete beschrijving van het concept)
- Geen concreet artefact of document

### Voorbeelden 
- **Value stream**, **mandarin-agent**, **workspace**, **governance-artefact**
- **Representatie**, **representatievorm**, **representatiestatus**

### Synoniemen  
- Begrip

### Analogieën 
- In logica: het intensionele deel van een begrip
- In DDD: het onderliggende domeinbegrip waar de ubiquitous language naar verwijst

### Context en gebruik  
Concepten vormen de bouwstenen van de canon. Eerst wordt een concept vastgesteld, daarna worden termen en definities gekozen om dat concept eenduidig te communiceren.


---

## Concept — Definitie

### Definitie 
Een **definitie** is een expliciete, canonieke beschrijving van een concept, bedoeld om de betekenis ervan eenduidig vast te leggen binnen het Mandarin-ecosysteem.

### Kenmerken 
- Verbindt een concept, een term en een betekenis
- Is zo kort mogelijk en zo precies als nodig
- Is tooling- en implementatie-onafhankelijk
- Is versieerbaar en herleidbaar tot een vastleggend artefact

### Wat het niet is 
- Geen losse omschrijving of voorbeeldtekst
- Geen marketing- of communicatieslogan
- Geen volledige handleiding of procesbeschrijving

### Voorbeelden 
- De canonieke definitie van **Mandarin-agent** in mandarin-domeinconcepten.md
- De definitie van **governance-artefact** in mandarin-ordeningsconcepten.md

### Synoniemen  
- Begripsdefinitie

### Analogieën 
- In woordenboeken: lemma-omschrijving van een woord
- In formele logica: exacte beschrijving van een predicaat

### Context en gebruik  
Definities worden gebruikt om misverstanden te voorkomen en om consistentie tussen documenten te borgen. Bij twijfel over betekenis gaat de canonieke definitie vóór gebruik in losse teksten.


---

## Concept — Term

### Definitie 
Een **term** is de gekozen taalvorm (woord of uitdrukking) waarmee binnen het Mandarin-ecosysteem naar een specifiek concept wordt verwezen.

### Kenmerken 
- Is taal- en notatiegebonden (bijv. Nederlands, Engels, afkorting)
- Kan meerdere varianten hebben voor hetzelfde concept (synoniemen)
- Kan per context verschillen, terwijl het onderliggende concept gelijk blijft
- Wordt in de canon expliciet gekoppeld aan een definitie en een concept

### Wat het niet is 
- Geen concept zelf (dat is de betekenis)
- Geen definitie (dat is de beschrijving van het concept)
- Geen incidentele formulering in een gesprek of e-mail

### Voorbeelden 
- De term **"agent"** als verwijzing naar het concept Mandarin-agent
- De term **"workspace"** als verwijzing naar het concept workspace
- De term **"governance-artefact"** als verwijzing naar het gelijknamige concept

### Synoniemen  
- Begripsetiket
- Naamvorm

### Analogieën 
- In programmeertalen: de naam van een klasse voor een onderliggend type
- In woordenboeken: het lemma waaronder een betekenis is geordend

### Context en gebruik  
Bij het invoeren van nieuwe termen wordt altijd eerst gecontroleerd of er al een passend concept bestaat. Zo niet, dan wordt eerst het concept en de definitie vastgesteld en pas daarna de term.


---

## Concept — Kenmerk

### Definitie 
Een **kenmerk** is een expliciete, onderscheidende eigenschap van een concept, gebruikt om het concept te verduidelijken, af te bakenen en te onderscheiden van andere, nabijgelegen concepten.

### Kenmerken 
- Verduidelijkt wat essentieel is voor een concept binnen zijn context
- Verschijnt doorgaans in lijstvorm onder een definitie
- Is stabiel zolang het concept zelf niet wijzigt
- Ondersteunt toetsbaarheid en herkenbaarheid van het concept in de praktijk

### Wat het niet is 
- Geen volledige beschrijving van alle mogelijke eigenschappen
- Geen incidentele eigenschap die niet tot de kern van het concept behoort
- Geen voorbeeld of gebruiksscenario

### Voorbeelden 
- Bij **Mandarin-artefact**: duurzaam, expliciet, overdraagbaar, waarde-dragend
- Bij **governance-artefact**: ontstaat in value stream 0, faciliteert ecosysteem-governance
- Bij **representatie**: concreet, observeerbaar, afgeleid van betekenis

### Synoniemen  
- Eigenschap (in deze canon met nadruk op onderscheidend karakter)

### Analogieën 
- In UML: attributen die het verschil tussen klassen verduidelijken
- In taxonomie: karakteristieken die soorten onderscheiden

### Context en gebruik  
Kenmerken worden in de canon gebruikt om definities te verdiepen zonder ze langer of diffuser te maken. Zij zijn leidend bij het beoordelen of een concreet geval onder een bepaald concept valt.


---

## Concept — As

### Definitie 
Een **as** is een expliciete ordeningsdimensie waarmee een **mandarin-agent** (of ander concept) wordt gepositioneerd langs een samenhangende set categorieën, die samen een betekenisvol spanningsveld beschrijven.

### Kenmerken 
- Beschrijft één fundamenteel aspect van een **mandarin-agent** (bijvoorbeeld: effect op betekenis, interventieniveau, werking, bronhouding)
- Is orthogonaal aan andere assen (posities op verschillende assen beïnvloeden elkaar niet)
- Bestaat uit minimaal twee categorieën die samen een onderscheidend spectrum vormen
- Kan een nulcategorie bevatten die een expliciete afwezigheid van het beschreven aspect representeert (bijv. 'N.v.t.' voor niet-inhoudelijke agents op de as Betekeniseffect)
- Maakt het mogelijk om alles op de as te plaatsen zonder uitzonderingen
- **Differentieert**: maakt onderscheid mogelijk tussen **mandarin-agents** die anders moeilijk te vergelijken zijn
- **Dwingt positionering af**: elke **mandarin-agent** heeft op elke as een expliciete positie
- **Is betekenisvast**: de betekenis van de **as** verandert niet door tooling, implementatie of context
- **Is niet hiërarchisch**: de volgorde van categorieën drukt geen waardeoordeel uit, maar een verschil in aard of effect

### Wat het niet is 
- Geen hiërarchische classificatie
- Geen lijst van "soorten" of "typen"
- Geen implementatie-eigenschap
- Geen waardeoordeel tussen categorieën
- Geen afhankelijke dimensie (orthogonaliteit is essentieel)

### Voorbeelden 
**As: Betekeniseffect**
- Registrerend
- Interpreterend
- Structurerend
- Vastleggend

**As: Bronhouding**
- Input-gebonden
- Canon-gebonden
- Externe-bron gebonden
- Exploratief

### Synoniemen 
- Classificatie-as
- Ordeningsdimensie
- Positionerings-as

### Analogieën 
- Vergelijkbaar met dimensies in multidimensionale analyse
- In taxonomie: orthogonale classificatie-dimensies
- In wiskunde: onafhankelijke vectordimensies in een vectorruimte
- In enterprise architectuur: capability dimensions of concern dimensions

### Toelichting 
Een **as** is fundamenteel voor mandarin-agent-classificatie omdat het één specifiek architectonisch aspect isoleert en meetbaar maakt. Door meerdere orthogonale assen te combineren, ontstaat een precisiebeeld van een **mandarin-agent** zonder de complexiteit van hiërarchische classificaties of overlap tussen "soorten".

Elke as binnen mandarin-agent-classificatie (Betekeniseffect, Interventieniveau, Werking, Bronhouding) volgt deze principes en maakt daarmee een volledige, consistente en overdraagbare positionering van alle **mandarin-agents** mogelijk.


---

**Einde document**

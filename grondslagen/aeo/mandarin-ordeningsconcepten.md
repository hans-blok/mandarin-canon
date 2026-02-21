# Mandarin **ordenings-concepten**

**Type**: Concepten en Definities  
**Repository**: mandarin-canon  
**Identifier**: mandarin-canon.concepten.meta  
**Version**: 1.10.0  
**Status**: Active  
**Last Updated**: 2026-02-21  
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
- [Interventieniveau](#interventieniveau) — Systeemniveau van ingreep
- [Epistemische houding](#epistemische-houding) — Kennisbronnen en herleidbaarheid

### Artefacten
- [Mandarin-artefact](#mandarin-artefact) — Expliciet vastgelegd, overdraagbaar resultaat
- [Normerend artefact](#normerend-artefact) — Artefact dat normen en regels vastlegt
  - [Governance-artefact](#governance-artefact) — Specialisatie: governance in ecosysteem (value stream 0)
  - [Richtinggevend artefact](#richtinggevend-artefact) — Specialisatie: normerende richting in waarde value streams (1-n)
- [Realiserend artefact](#realiserend-artefact) — Artefact dat gedrag of structuur in systemen realiseert
- [Structurerend artefact](#structurerend-artefact) — Artefact dat architectuurelementen en relaties expliciteert
- [Beschrijvend artefact](#beschrijvend-artefact) — Artefact dat inzicht en uitleg biedt
- [Documenterend artefact](#documenterend-artefact) — Artefact dat documenteert (inclusief modellen)
- [Representatievorm](#representatievorm) — Vorm waarin betekenis wordt uitgedrukt
- [Representatie](#representatie) — Concrete uitdrukking van betekenis
- [Representatiestatus](#representatiestatus) — Bron of afgeleid in de keten
  
### Prompts
- [Prompt canon-curator: publiceer normatieve wijziging](#prompt-canon-curator-publiceer-normatieve-wijziging)

---

## Mandarin-agent-classificatie

### Definitie
mandarin-agent-classificatie is het expliciet positioneren van een **mandarin-agent** langs een vast stelsel van orthogonale assen, waarmee wordt vastgelegd wat het effect van de **mandarin-agent** is, waarop hij intervenieert, in welke context hij inzetbaar is en hoe hij handelt.

### Kenmerken
- Is geen enkelvoudig label en geen hiërarchie
- Een **mandarin-agent** is niet "een soort", maar neemt posities in op meerdere assen
- Elke as beschrijft een fundamenteel ander architectonisch aspect van de **mandarin-agent**
- Samen maken deze posities het gedrag, de bevoegdheid en de beperkingen van een **mandarin-agent** uitlegbaar, toetsbaar en overdraagbaar
- Bestaat uit 4 orthogonale assen:
  1. **Betekeniseffect** — effect op betekenis
  2. **Interventieniveau** — systeemniveau van ingreep
  3. **Werking** — inhoud, representatie of voorwaarden
  4. **Epistemische houding** — kennisbronnen en herleidbaarheid

### Wat het niet is
- Geen enkelvoudig label (zoals "adviserende **mandarin-agent**" of "uitvoerende **mandarin-agent**")
- Geen hiërarchische structuur
- Geen technische implementatie-eigenschap
- Geen tijdelijke classificatie

### Voorbeelden
- Een **mandarin-agent** kan beschrijvend zijn (betekeniseffect), op werk-niveau acteren (interventieniveau), en inhoudelijk zijn (werking)
- Een **mandarin-agent** kan normerend, op architectuur-niveau, en inhoudelijk zijn
- Een **mandarin-agent** kan conditioneel zijn (werking), op ecosysteem-niveau (interventieniveau)

### Synoniemen
- **mandarin-agent**-positionering
- Multi-dimensionale **mandarin-agent**-classificatie

### Analogieën 
- Vergelijkbaar met multi-dimensionale classificatie in taxonomie
- In softwareontwikkeling: orthogonale concerns (zoals in aspect-oriented programming)
- In enterprise architectuur: capability matrix met meerdere dimensies

### Toelichting 
mandarin-agent-classificatie vervangt het concept "**mandarin-agent**-soort" door een meer genuanceerd stelsel van orthogonale assen. Dit maakt het mogelijk om **mandarin-agents** preciezer te positioneren en te begrijpen. Elke **mandarin-agent** heeft op elke as een expliciete positie, en deze posities bepalen samen het gedrag, de bevoegdheden en de beperkingen van de **mandarin-agent**.

### Gerelateerde Doctrines
- **Intent-naming**: [doctrine-intent-naming.md](doctrine-intent-naming.md) koppelt canonieke werkwoorden aan elke classificatie-positie op de werking en betekeniseffect
- **Combinatiematrices**: [mandarin-classificatie-matrices.md](mandarin-classificatie-matrices.md) toont welke combinaties van as-posities architectonisch mogelijk en logisch zijn.


---
## Betekeniseffect

### Definitie 
Het **betekeniseffect** is een classificatie-as binnen mandarin-agent-classificatie die het effect van een **mandarin-agent** op de betekenis van het werk beschrijft.

**Leidende vraag:** *Wat is het effect van deze **mandarin-agent** op de betekenis van het werk?*

### Kenmerken 
- Is één van vier orthogonale assen voor mandarin-agent-classificatie
- Onderscheidt **mandarin-agents** op basis van hun effect op betekenis
- Vier categorieën: Beschrijvend, Realiserend, Evaluerend, Normerend
- Onafhankelijk van andere assen (Interventieniveau, Werking, Epistemische houding)
- Bepaalt fundamentele rol en impact van de **mandarin-agent**

### Wat het niet is
- Geen technische implementatievariant
- Geen organisatorische indeling
- Geen enkelvoudig label

### Categorieën 

**1. Beschrijvend**
- Vastleggen, uitleggen en documenteren wat er is of was
- Achteraf: beschrijven bestaande werkelijkheid
- Wijzigen geen artefacten
- Voorbeelden: Verslagen, Overzichten, Uitlegdocumentatie

**2. Realiserend**
- Maken impliciete samenhang, relaties en consistentie expliciet
- Instantiëren een samenhangend architectuurmodel over lagen en aspecten binnen de gestelde kaders
- Realiseren modellen, relaties, nummering
- Voorbeelden: Logisch datamodel-**mandarin-agent**, ArchiMate-modelleur

**3. Evaluerend**
- Beschrijvende **mandarin-agents** die expliciet oordeel of duiding vastleggen
- Beoordelen kwaliteit, samenhang en risico's
- Leggen oordeel vast, geen besluit
- Voorbeelden: Review-mandarin-agents, Samenhangbeoordeling

**4. Normerend**
- Normeren vooraf de structuur en indeling van toekomstig werk
- Vaststellen of wijzigen van regels, kaders en constituerende afspraken
- Bepalen *wat als werk bestaat* of *hoe het systeem mag bestaan*
- Voorbeelden: Thema-vormende **mandarin-agents**, Constitutie-**mandarin-agents**

### Synoniemen
- Effect-as
- Betekenis-as

### Analogieën 
- Vergelijkbaar met prescriptive vs descriptive vs evaluative in informatiekunde
- In softwareontwikkeling: read vs write vs validate operaties

### Toelichting  
Het **betekeniseffect** is de primaire as voor mandarin-agent-classificatie omdat deze de fundamentele rol en impact van een **mandarin-agent** op betekenis bepaalt. Het onderscheid tussen structuur-normering (werk) en ecosysteem-normering (spelregels) is cruciaal.

---
## Werking

### Definitie 
De **werking** is een classificatie-as binnen mandarin-agent-classificatie die beschrijft of een **mandarin-agent** intervenieert in de inhoud of in de voorwaarden waaronder inhoudelijk werk kan plaatsvinden.

**Leidende vraag:** *Intervenieert deze **mandarin-agent** in de inhoud, of in de voorwaarden waaronder inhoudelijk werk kan plaatsvinden?*

### Kenmerken 
- Is één van vier orthogonale assen voor mandarin-agent-classificatie
- Onderscheidt **mandarin-agents** op basis van interventiegebied
- Drie categorieën: Inhoudelijk, Representatie-omvormend, Conditioneel
- Onafhankelijk van andere assen (Betekeniseffect, Interventieniveau, Epistemische houding)
- Bepaalt of **mandarin-agent** op inhoud of op voorwaarden werkt

### Wat het niet is 
- Geen kwaliteitsmaatstaf
- Geen hiearchische indeling
- Geen technische eigenschap

### Categorieën

**1. Inhoudelijk**
- Werken direct op betekenisvolle artefacten
- Omvat alle categorieën van het betekeniseffect (Beschrijvend, Realiserend, Evaluerend, Normerend)
- Begrijpt betekenis van het werk

**2. Representatie-omvormend**
- Zet inhoud om van de ene representatie naar de andere
- Betekenis-blind
- Infrastructuurachtig
- Vormtransformatie (bijv. Markdown → XML → diagram)

**3. Conditioneel**
- Werken niet op inhoud, maar op voorwaarden en hygiëne
- Geen betekenis
- Geen value-stream-artefacten
- Bewaken randvoorwaarden
- Subtypen:
  - **Workspace Steward** — structuur, beleid, scope, mappen, gitignore
  - **Engineering Steward** — codekwaliteit, veiligheid, onderhoudbaarheid

### Synoniemen 
- Werkgebied-as

### Analogieën 
- Vergelijkbaar met business logic vs infrastructure in softwareontwikkeling
- In enterprise architectuur: content vs governance layers

### Toelichting  
De **werking** maakt cruciaal onderscheid tussen **mandarin-agents** die inhoud beïnvloeden en **mandarin-agents** die de voorwaarden voor inhoudelijk werk bewaken. Conditionele **mandarin-agents** zijn essentieel maar werken op een ander niveau.

---
## Interventieniveau

### Definitie
**Interventieniveau** is het ordeningsconcept dat beschrijft op welk systeemniveau een rol, **mandarin-agent** of capability ingrijpt of betekenis beïnvloedt.

**Leidende vraag**: Waar in het systeem vindt de ingreep plaats?

Interventieniveau zegt niets over *wat* er met betekenis gebeurt (dat beschrijft het betekeniseffect), maar uitsluitend *waar* dat gebeurt.

### Kenmerken
- Is orthogonaal aan het betekeniseffect (effect op betekenis)
- Classificeert het niveau van ingreep, niet het type handeling
- Geldt voor alle inhoudelijke categorieën (beschrijvend, structurerend, normerend, curator)
- Maakt onderscheid tussen werk, ontwerp, architectuur en ecosysteem
- Verhoogt bestuurbaarheid en traceerbaarheid

### Wat het niet is
- Geen hiërarchische waardering (ecosysteem is niet "belangrijker" dan werk)
- Geen inhoudelijke classificatie (dat is het betekeniseffect)
- Geen technische laag (zoals runtime, tooling of infrastructuur)
- Geen waardeoordeel

### Niveaus
1. **Werk-niveau** — interventie op concrete werk-elementen.
	 - Voorbeelden:
		 - Requirements
		 - Features
		 - Werktaakbeschrijvingen
		 - Backlog-items
		 - Acceptatiecriteria

2. **Ontwerp-niveau** — interventie op de structurele representatie van een systeem of oplossing.
	 - Voorbeelden:
		 - Applicatie-views
		 - Domeinmodellen
		 - Architectuurdiagrammen
		 - Capability-maps

3. **Architectuur-niveau** — interventie op ordeningsprincipes en structurele kaders van oplossingen.
	 - Voorbeelden:
		 - Capability-boundaries
		 - Servicegrenzen
		 - Architectuurprincipes
		 - Domeinindelingen

4. **Ecosysteem-niveau** — interventie op het regelsysteem van het agent-ecosysteem zelf.
	 - Voorbeelden:
		 - Constitutie
		 - Doctrines
		 - Classificatie-assen
		 - Normering voor agents

### Orthogonaliteit

Interventieniveau moet altijd gecombineerd worden met het betekeniseffect.

**Voorbeeldmatrix**:

| Inhoudelijk effect     | Interventieniveau  | Betekenis                              |
|------------------------|--------------------|----------------------------------------|
| Beschrijvend           | Werk               | Vastleggen van requirement-status      |
| Structuurrealiserend   | Ontwerp            | Modelleren van applicatie-view         |
| Normerend              | Architectuur       | Vaststellen capability-boundary        |
| Curator                | Ecosysteem         | Beoordelen van canon-consistentie      |

---
## Epistemische houding

### Definitie
De **epistemische houding** is een classificatie-as binnen mandarin-agent-classificatie die beschrijft op welke kennisbronnen een **mandarin-agent** zich baseert en in welke mate de output herleidbaar is tot expliciete bronnen.

**Leidende vraag:** *Op welke kennisbronnen baseert deze **mandarin-agent** zich, en hoe herleidbaar is de output?*

### Kenmerken
- Is één van vier orthogonale assen voor mandarin-agent-classificatie
- Onderscheidt **mandarin-agents** op basis van kennisbrongebruik en herleidbaarheid
- Vier categorieën: Deterministisch, Canon-gebonden, Retrieval-gebonden, Generatief
- Onafhankelijk van andere assen (Betekeniseffect, Interventieniveau, Werking)
- Bepaalt de epistemische verantwoordelijkheid en controleerbaarheid van de **mandarin-agent**

### Wat het niet is
- Geen kwaliteitsmaatstaf van de output
- Geen technische implementatiekeuze
- Geen indicatie van complexiteit of waarde

### Categorieën

** 1. Deterministisch (Input-only)**
- Output is 100% herleidbaar tot de input
- Geen externe kennisbronnen
- Volledig voorspelbaar en reproduceerbaar
- Transformeert of herordent alleen de gegeven input
- Voorbeelden: Sorteerders, Formatters, Parsers

** 2. Canon-gebonden**
- Baseert zich expliciet op de Mandarin-canon
- Canon-verwijzing is verplicht in de output
- Leest en interpreteert canonieke documenten
- Output is traceerbaar naar specifieke canon-artefacten
- Voorbeelden: Doctrine-interpreterende **mandarin-agents**, Charter-validerende **mandarin-agents**

** 3. Retrieval-gebonden**
- Haalt kennis op uit specifieke, geïdentificeerde bronnen
- Bronvermelding is verplicht
- Gebruikt RAG (Retrieval-Augmented Generation) of vergelijkbare technieken
- Output is herleidbaar naar concrete brondocumenten
- Voorbeelden: Documentatie-samenvattende **mandarin-agents**, Context-verzamelende **mandarin-agents**

** 4. Generatief**
- Genereert output op basis van trained knowledge en redenering
- Maakt aannames en afleidingen
- Aannames moeten expliciet worden gemaakt (maximaal 3)
- Minst herleidbaar, hoogst creatief
- Voorbeelden: Architectuur-ontwerpende **mandarin-agents**, Creatieve schrijf-**mandarin-agents**

### Verplichte checks per categorie

| Categorie | Verplichte checks |
|-----------|-------------------|
| Deterministisch | 100% herleidbaar |
| Canon-gebonden | Canon-verwijzing verplicht |
| Retrieval-gebonden | Bronvermelding verplicht |
| Generatief | Aannames expliciet (max 3) |

### Synoniemen
- Kennisbron-as
- Herleidbaarheidsdimensie
- Epistemologische as

### Analogieën 
- Vergelijkbaar met transparency levels in AI systems
- In wetenschappelijk onderzoek: primaire vs secundaire bronnen vs interpretatie
- In softwareontwikkeling: pure functions vs database-driven vs AI-augmented

### Toelichting  
De **epistemische houding** maakt expliciet hoe een **mandarin-agent** tot zijn kennis komt en in welke mate de output controleerbaar en herleidbaar is. Dit is cruciaal voor vertrouwen, governance en kwaliteitsborging. Hoe verder naar rechts op de as (van deterministisch naar generatief), hoe meer epistemische verantwoordelijkheid de **mandarin-agent** draagt om zijn bronnen en aannames expliciet te maken.

Deze as stelt het ecosysteem in staat om:
- Bewust te kiezen voor het juiste niveau van herleidbaarheid per use case
- Expliciete eisen te stellen aan bronvermelding en traceerbaarheid
- Risico's te beheersen door aannames te beperken en expliciet te maken
- Vertrouwen te borgen door transparantie over kennisbronnen

---
## Artefact-functie-as

### Definitie
De **artefact-functie-as** is een classificatie-as voor **Mandarin-artefacten** die beschrijft *welke functie* een artefact vervult in de besluit- en waardeketen binnen het ecosysteem.

**Leidende vraag:** *Welke normerende, realiserende, structurerende, beschrijvende, documenterende of afgeleide functie heeft dit artefact in het ecosysteem?*

### Kenmerken
- Is een ordenings-as specifiek voor **Mandarin-artefacten** (niet voor **mandarin-agents**)
- Positioneert artefacten op basis van hun rol in besluitvorming, uitvoering, inzicht, documentatie en afleiding
- Vormt samen met de **representatievorm-as** de kern van **Artefactclassificatie**
- Is onafhankelijk van bestandsformaat, tooling of repository-structuur
- Is onafhankelijk van procesfase of value stream-fase; hetzelfde artefact kan in meerdere fasen worden gebruikt, maar heeft één primaire functie
- Maakt onderscheid tussen primaire, normerende artefacten en afgeleide of ondersteunende artefacten

### Posities

Op de **artefact-functie-as** worden ten minste de volgende canonieke posities onderscheiden:

**1. Normerend artefact**
- Legt normen, regels, kaders of richting vast
- Bevat bindende afspraken of voorschriften
- Specialisaties: **governance-artefact** (ecosysteem- en value-stream-overstijgend) en **richtinggevend artefact** (waarde value streams 1-n)

**2. Realiserend artefact**
- Realiseert direct gedrag, structuur of configuratie in systemen of processen
- Heeft uitvoerbare of door tooling direct interpreteerbare impact
- Voorbeelden: database-schema's, deployment-configuraties, codegeneratie-templates met normerend karakter

**3. Structurerend artefact**
- Representeert een coherent geheel van architectuurelementen en hun onderlinge relaties
- Geordend volgens een metamodel of kader
- Maakt de structuur van een systeem expliciet en beredeneerbaar
- Voorbeelden: architectuurmodellen, metamodellen, structuurontwerpen

**4. Beschrijvend artefact**
- Maakt bestaande of voorgenomen werkelijkheid inzichtelijk
- Legt analyse, structuur of samenhang vast zonder zelf normerend of realiserend te zijn
- Voorbeelden: modellen, analyses, overzichten

**5. Documenterend artefact**
- Documenteert keuzes, werking, besluiten of context
- Is vaak (deels) afgeleid van andere artefacten
- Voorbeelden: handleidingen, README's, API-documentatie

**6. Afgeleid artefact**
- Is expliciet afgeleid van één of meer andere artefacten
- Kan beschrijvend of documenterend zijn, maar is niet primair normerend
- Voorbeelden: gegenereerde documentatie, views, samenvattende overzichten

### Wat het niet is
- Geen indeling naar bestandsformaat, repository of tooling
- Geen kwaliteitsmeting of volwassenheidsniveau van artefacten
- Geen fasering van werk of levenscyclus-status (concept, draft, definitief)
- Geen indeling naar betrokken personen, teams of rollen

### Voorbeelden
- Een **constitutie** of **doctrine** staat op de **artefact-functie-as** als **normerend artefact** (met rol **governance-artefact**)
- Een **application-charter** of themabeschrijving staat als **richtinggevend artefact** (dus normerend binnen een specifieke value stream)
- Een logisch datamodel dat direct systeemgedrag bepaalt staat als **realiserend artefact**
- Een ArchiMate-model of domeinmodel met coherente structuur staat als **structurerend artefact**
- Een architectuurdiagram of analysemodel zonder bindende normatieve status staat als **beschrijvend artefact**
- Een gegenereerde API-referentie of gebruikershandleiding staat als **documenterend artefact**, vaak ook als **afgeleid artefact**

### Synoniemen
- Artefact-rol-as
- Functie-as voor artefacten

### Analogieën 
- In informatiebeheer: beleid / proces / registratie als verschillende functies van informatie-objecten
- In softwareontwikkeling: onderscheid tussen specificatie, implementatie, documentatie en gegenereerde artefacten

### Toelichting  
De **artefact-functie-as** maakt zichtbaar *wat* een artefact doet in het ecosysteem: of het kaders schept (normerend), gedrag realiseert (realiserend), structuur expliciteert (structurerend), inzicht geeft (beschrijvend), vastlegt en uitlegt (documenterend) of is afgeleid van andere artefacten (afgeleid). Deze as werkt samen met de **representatievorm-as**: dezelfde functie kan in verschillende representatievormen bestaan zonder dat de positie op de **artefact-functie-as** verandert.

De posities op de **artefact-functie-as** corresponderen direct met de ordeningsconcepten **normerend artefact**, **governance-artefact**, **richtinggevend artefact**, **realiserend artefact**, **structurerend artefact**, **beschrijvend artefact**, **documenterend artefact** en **afgeleid artefact**. **Artefactclassificatie** gebruikt deze as expliciet om artefacten te positioneren naar hun functie, los van vorm, tooling en proces.

---
## Artefactclassificatie

### Definitie
**Artefactclassificatie** is het expliciet ordenen en positioneren van **Mandarin-artefacten** langs twee orthogonale assen:
- een **artefact-functie-as** (normerend, richtinggevend, realiserend, structurerend, beschrijvend, documenterend, afgeleid), en
- een **representatievorm-as** (tekstueel, gestructureerd, visueel, machine-leesbaar, â€¦),
zodat helder is *welk* type artefact iets is en *in welke vorm* het wordt uitgedrukt.

### Kenmerken
- Biedt een consistent, tweedimensionaal classificatiekader voor alle **Mandarin-artefacten**
- Gebruikt op de **artefact-functie-as** posities als: **normerend artefact** (met specialisaties **governance-artefact** en **richtinggevend artefact**), **realiserend artefact**, **structurerend artefact**, **beschrijvend artefact**, **documenterend artefact** en **afgeleid artefact**
- Gebruikt op de **representatievorm-as** de concepten uit **representatievorm** (bijv. tekstueel, gestructureerd, visueel, machine-leesbaar) zonder voor elke positie een apart concept te introduceren
- Is tooling-onafhankelijk: de classificatie verandert niet door bestandsformaat, repository of implementatiedetail
- Verbindt artefacten expliciet met hun rol in **value streams** en in het ecosysteem
- Maakt duidelijk welke artefacten primair zijn (niet-afgeleid) en welke artefacten afgeleid of ondersteunend zijn

### Wat het niet is
- Geen lijst van bestandsformaten of tooling-keuzes
- Geen hiërarchie van belangrijkheid of waarde
- Geen procesindeling of fasering van werk
- Geen technische classificatie (bijvoorbeeld op basis van repository of folderstructuur)

### Voorbeelden
- Een **doctrine** of **constitutie** wordt geclassificeerd als **normerend artefact** met rol **governance-artefact**, meestal in een tekstuele representatievorm (bijv. Markdown)
- Een requirements-specificatie of thema-beschrijving wordt geclassificeerd als **richtinggevend artefact** (normerend binnen een waarde value stream), vaak tekstueel of gestructureerd
- Een logisch datamodel dat direct systeemgedrag realiseert wordt geclassificeerd als **realiserend artefact** in een gestructureerde, machine-leesbare vorm (bijv. DDL, model-XML)
- Een **ArchiMate-model** of domeinmodel met coherente architectuurstructuur wordt geclassificeerd als **structurerend artefact** in een visuele of model-gebaseerde representatievorm
- Een architectuurdiagram of ad-hoc analysemodel zonder metamodel wordt geclassificeerd als **beschrijvend artefact** in een visuele representatievorm
- Een **handleiding**, README, mandarin-agent-overzicht of **API-documentatie** wordt geclassificeerd als **documenterend artefact**, vaak deels gegenereerd uit andere artefacten

### Synoniemen
- Artefact-positionering
- Artefact-typenindeling

### Analogieën 
- Vergelijkbaar met de indeling in policy / process / record in informatiebeheer
- In softwareontwikkeling: onderscheid tussen source artefacts, design docs en generated documentation

### Toelichting  
**Artefactclassificatie** vormt de meta-laag boven op de concrete definities van **Mandarin-artefact**, **normerend artefact**, **governance-artefact**, **richtinggevend artefact**, **realiserend artefact**, **structurerend artefact**, **beschrijvend artefact**, **documenterend artefact**, **afgeleid artefact**, **representatie** en **representatievorm**. Zij legt vast *langs welke assen* artefacten worden geordend en welke posities op die assen canoniek zijn.

Samengevat:
- de **artefact-functie-as** Positioneert artefacten op basis van hun normerende en afgeleide functie binnen het ecosysteem. Met deze functie krijgt het artefact betekenis.
- de **representatievorm-as** maakt zichtbaar *hoe* die betekenis wordt uitgedrukt (tekstueel, gestructureerd, visueel, machine-leesbaar, â€¦).

Door deze tweedimensionale classificatie wordt helder welke artefacten bindend en prescriptief zijn, welke artefacten uitleg en inzicht bieden, welke artefacten duurzame documentatie en modellen leveren en hoe al deze artefacten in verschillende representatievormen kunnen bestaan zonder dat hun rol verandert. Dit maakt het mogelijk om werk, governance en documentatie scherp van elkaar te scheiden, tooling verwisselbaar te houden en de betekenis van elk artefacttype vast en toetsbaar te maken.


---

## Normerend artefact

### Definitie
Een **normerend artefact** is een **Mandarin-artefact** dat expliciete normen, regels, principes of standaarden vastlegt die bindend zijn voor het **Mandarin-ecosysteem** of een specifiek domein, en dat operationeel is in maximaal één **value stream fase**.

**Specialisaties**:
- **Governance-artefact** — normerend artefact voor het ecosysteem, ontstaat in value stream "mandarin-agent Ecosysteem Ontwikkeling"
- **Richtinggevend artefact** — normerend artefact uit waarde value streams (1-n)

### Kenmerken
- Legt bindende normen, regels of principes vast
- Is prescriptief (schrijft voor wat moet)
- Is leidend voor ontwerp, implementatie en evaluatie
- Vormt de hoogste autoriteit binnen zijn scope
- Is versieerbaar en traceerbaar
- Wordt niet afgeleid uit andere artefacten
- **Is operationeel in maximaal één value stream fase**
- Heeft twee specialisaties: governance-artefact en richtinggevend artefact

### Wat het niet is
- Geen beschrijving van huidige situatie
- Geen advies of aanbeveling
- Geen implementatie of uitvoering
- Geen documentatie of uitleg

### Voorbeelden
- Constitutie
- Doctrines
- Beleid
- Architectuurprincipes
- Standaarden en richtlijnen

### Synoniemen
- Normatief artefact
- Prescriptief artefact
- Regel-artefact

### Analogieën 
- Vergelijkbaar met wetgeving, standaarden (zoals ISO), policies
- In enterprise architectuur: principles, standards, guidelines
- In softwareontwikkeling: coding standards, architectural decision records (bindende variant)

### Toelichting  
**Normerende artefacten** hebben de hoogste autoriteit en zijn bindend. Zij vormen het fundament waarop alle andere artefacten voortbouwen. Normerende artefacten zijn primair (niet afgeleid) en stabiel in de tijd.

---

## Governance-artefact

### Definitie
Een **governance-artefact** is een specialisatie van een **normerend artefact** dat het functioneren, de besturing en de continuïteit van het **Mandarin-ecosysteem** mogelijk maakt. Governance-artefacten worden **alleen en alleen** aangemaakt in de value stream "mandarin-agent Ecosysteem Ontwikkeling"**.

### Kenmerken
- Is een **specialisatie van normerend artefact**
- Ontstaat uitsluitend in value stream "**mandarin-agent** Ecosysteem Ontwikkeling" (value stream 0)
- Maakt governance en besturing van het ecosysteem mogelijk
- Is operationeel en faciliterend voor het ecosysteem
- Is normerend voor het ecosysteem zelf
- Is randvoorwaardelijk voor alle andere value streams
- Levert geen directe waarde in waarde value streams (1-n)
- Erft alle kenmerken van normerend artefact (bindend, prescriptief, versieerbaar)

### Wat het niet is
- Geen algemeen normerend artefact (is specifiek voor ecosysteem-governance)
- Geen bedrijfs-artefact (ontstaat niet in waarde value streams)
- Geen beschrijvend of documenterend artefact
- Geen artefact buiten value stream "**mandarin-agent** Ecosysteem Ontwikkeling"

### Voorbeelden
- **agent-charter**
- **agent-contract** 
- Prompt (.prompt.md)
- Templates
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
**Governance-artefacten** zijn normerend voor het ecosysteem en ontstaan uitsluitend in value stream "**mandarin-agent** Ecosysteem Ontwikkeling". Zij maken het mogelijk dat **mandarin-agents**, workspaces en value streams gecontroleerd en consistent kunnen functioneren. Als specialisatie van normerend artefact zijn governance-artefacten bindend en prescriptief, en operationeel in specifieke fasen (Grondslagvorming of Ecosysteeminrichting) van value stream 0.

---

## Richtinggevend artefact

### Definitie
Een **richtinggevend artefact** (synoniem: **value-stream-artefact**) is een specialisatie van een **normerend artefact** dat expliciet de gewenste inhoud, structuur of randvoorwaarden van een **value stream fase** in een **waarde value stream** (value streams 1-n) vastlegt en daarmee richting geeft aan realisatie en verdere uitwerking.

### Kenmerken
- Is een **specialisatie van normerend artefact**
- Ontstaat binnen een value stream fase in waarde value streams (value streams 1-n, niet in value stream 0)
- Vertegenwoordigt inhoudelijke keuzes, richting en gewenste resultaten
- Is input voor volgende fasen en voor realiserende artefacten
- Wordt geleverd door uitvoerende **mandarin-agents** met inhoudelijke verantwoordelijkheid
- Is primair artefact (niet afgeleid uit andere artefacten)
- Erft alle kenmerken van normerend artefact (bindend, prescriptief, versieerbaar, operationeel in maximaal één value stream fase)

### Wat het niet is
- Geen algemeen normerend artefact (is specifiek voor waarde value streams)
- Geen governance-artefact (ontstaat niet in value stream "**mandarin-agent** Ecosysteem Ontwikkeling")
- Geen realiserend artefact (legt niet de feitelijke implementatie vast)
- Geen afgeleid artefact (is niet primair afgeleid uit andere artefacten)
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
**Richtinggevende artefacten** leggen vast wat er inhoudelijk moet gelden in een waarde value stream (1-n), zonder te bepalen *hoe* dit technisch precies wordt gerealiseerd. Zij sturen daarmee de creatie van **realiserende artefacten** (zoals code en DDL) en vormen het primaire, normerende referentiepunt voor afgeleide modellen en documentatie.

---

## Realiserend artefact

### Definitie
Een **realiserend artefact** is een **Mandarin-artefact** dat direct gedrag, structuur of configuratie in een werkend systeem realiseert op basis van richtinggevende artefacten.

### Kenmerken
- Is uitvoerbaar, interpreteerbaar of direct toepasbaar door tooling of runtime-omgevingen
- Realiseert beslissingen en structuren die eerder in richtinggevende artefacten zijn vastgelegd
- Is meestal niet zelf normerend, maar volgt normerende artefacten
- Wijzigingen hebben direct effect op systeemgedrag of data
- Kan gegenereerd zijn uit andere artefacten of handmatig gemaakt

### Wat het niet is
- Geen richtinggevend artefact (legt geen norm of intentie vast)
- Geen puur beschrijvend of documenterend artefact
- Geen afgeleid artefact dat alleen structuur uitlegt zonder iets te realiseren

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
**Realiserende artefacten** vormen de brug tussen richtinggevende artefacten en het werkende systeem. Zij maken de bedoelde structuur en het gewenste gedrag feitelijk waar in code, data en configuratie.


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
- Kan normerend of beschrijvend zijn, afhankelijk van de intentie

### Wat het niet is
- Geen direct realiserende structuur (zoals database-schema's)
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
**Structurerende artefacten** maken de architectonische structuur van systemen expliciet door elementen en hun relaties te ordenen volgens een coherent kader. Zij verschillen van **beschrijvende artefacten** door hun focus op structurele coherentie en metamodel-conformiteit, en van **realiserende artefacten** omdat zij structuur representeren maar niet direct uitvoeren.

---

## Beschrijvend artefact

### Definitie
Een **beschrijvend artefact** is een **Mandarin-artefact** dat inzicht, uitleg of overzicht biedt over bestaande structuren, besluiten of situaties, zonder zelf normerend, governerend of waardevol in een value stream fase te zijn.

### Kenmerken
- Biedt inzicht en uitleg
- Is descriptief (beschrijft wat is)
- Is niet bindend of prescriptief
- Kan afgeleid zijn uit andere artefacten
- Ondersteunt begripsvorming en communicatie

### Wat het niet is
- Geen normerend artefact (schrijft niets voor)
- Geen governance-artefact (maakt geen besturing mogelijk)
- Geen richtinggevend artefact (geen normerend output van value stream fase)
- Geen formele documentatie

### Voorbeelden
- Overzichtsdocumenten
- Analyse-rapporten
- Conceptuele modellen (ter uitleg)
- Architectuurvisies
- Rationale-documenten (waarom-uitleg)
- Kennisbankartikelen

### Synoniemen
- Descriptief artefact
- Uitleg-artefact
- Inzicht-artefact

### Analogieën 
- Vergelijkbaar met white papers, explanatory documents, vision documents
- In enterprise architectuur: viewpoints, perspectives
- In softwareontwikkeling: architectural decision records (beschrijvende variant), design rationale

### Toelichting  
**Beschrijvende artefacten** helpen mensen het ecosysteem te begrijpen. Zij zijn vaak afgeleid uit normerende, governance- of richtinggevende artefacten. Beschrijvende artefacten zijn ondersteunend en niet bindend.

---

## Documenterend artefact

### Definitie
Een **documenterend artefact** is een **Mandarin-artefact** dat kennis, structuren of besluiten vastlegt in een formele, toegankelijke vorm (inclusief model-gebaseerde beschrijvingen zoals ArchiMate), bedoeld voor duurzame raadpleegbaarheid en kennisoverdracht.

### Kenmerken
- Legt kennis en structuren formeel vast
- Bedoeld voor duurzame raadpleegbaarheid
- Kan model-gebaseerd zijn (bijv. ArchiMate, UML)
- Kan afgeleid of gegenereerd zijn uit andere artefacten
- Ondersteunt kennisoverdracht en onderhoud

### Wat het niet is
- Geen normerend artefact (legt geen regels vast)
- Geen governance-artefact (maakt geen besturing mogelijk)
- Geen richtinggevend artefact (geen normerend output van value stream fase)
- Geen informele notitie of tijdelijk document

### Voorbeelden
- Technische documentatie
- Gebruikershandleidingen
- ArchiMate-modellen (documenterende variant)
- UML-diagrammen (documenterende variant)
- API-documentatie (gegenereerd)
- Release notes
- Geëxporteerde visualisaties

### Synoniemen
- Documentatie-artefact
- Formeel document
- Model-artefact (als het model documenteert)

### Analogieën 
- Vergelijkbaar met technical documentation, reference manuals, generated docs
- In enterprise architectuur: repository exports, model documentation
- In softwareontwikkeling: Javadoc, Swagger/OpenAPI specs, architecture diagrams

### Toelichting  
**Documenterende artefacten** maken kennis toegankelijk en duurzaam. Zij zijn vaak afgeleid of gegenereerd uit primaire artefacten. **Model-gebaseerde beschrijvingen** (zoals ArchiMate) worden gezien als documenterende artefacten: zij leggen structuur vast, maar zijn uitleg, niet waarheid. Deze indeling scheidt betekenis van vorm en maakt tooling verwisselbaar.

---

## Representatievorm

### Definitie
Een **representatievorm** is de specifieke manier waarop een artefact of betekenis wordt vastgelegd, weergegeven of uitgewisseld, zonder de onderliggende betekenis zelf te bepalen.

### Toelichting  
Een **representatievorm** beschrijft *hoe* iets wordt uitgedrukt, niet *wat* het betekent.

Dezelfde inhoud kan in meerdere representatievormen bestaan, bijvoorbeeld:
- tekstueel
- gestructureerd
- visueel
- machine-leesbaar

Deze representaties zijn inhoudelijk equivalent, maar functioneel verschillend: zij dienen andere doelen en doelgroepen.

### Kenmerken
Een representatievorm:
- is afgeleid van een onderliggende betekenis of structuur
- heeft geen eigen normatieve kracht
- kan worden vertaald naar andere representatievormen
- is context- en doelafhankelijk (mens, machine, visualisatie)
- verandert niet de betekenis, alleen de toegankelijkheid of bruikbaarheid

### Wat het niet is
- Geen artefact op zichzelf
- Geen normering of besluit
- Geen inhoudelijke structuur
- Geen model van de werkelijkheid

Een representatievorm draagt betekenis, maar bepaalt haar niet.

### Voorbeelden
- Markdown, XML, JSON, YAML
- Diagram, visualisatie, schema
- Tabel, lijst, tekstuele beschrijving

In al deze gevallen blijft de onderliggende betekenis gelijk, terwijl de vorm verschilt.

---

## Representatie

### Definitie
Een **representatie** is een concrete uitdrukking van een onderliggende betekenis, structuur of inhoud, vastgelegd in een specifieke representatievorm.

### Toelichting  
Een **representatie** is de manifestatie van iets dat betekenis heeft.
Zij maakt betekenis waarneembaar, deelbaar of verwerkbaar, maar is niet die betekenis zelf.

Dezelfde betekenis kan meerdere representaties hebben, bijvoorbeeld:

- een tekstuele beschrijving
- een model
- een schema
- een visualisatie

Elke representatie drukt dezelfde onderliggende inhoud uit, maar op een andere manier.

### Kenmerken
Een representatie:
- is afgeleid van betekenis, niet andersom
- bestaat altijd in een representatievorm
- is concreet en observeerbaar
- kan worden vertaald naar andere representaties
- kan verouderen of wijzigen zonder dat de betekenis verandert

### Wat het niet is
- Niet de betekenis zelf
- Niet het besluit of de norm
- Niet per definitie het artefact
- Niet de waarheid, maar een uitdrukking daarvan

Een representatie toont betekenis, maar definieert haar niet.

### Relatie tussen betekenis, representatie en representatievorm 

Canoniek onderscheid:

- **Betekenis** â€“ datgene wat inhoudelijk geldt of bedoeld is
- **Representatie** â€“ de concrete uitdrukking van die betekenis
- **Representatievorm** â€“ de manier waarop die representatie is vastgelegd

In relatie:

> Betekenis → wordt uitgedrukt in → representatie → heeft een → representatievorm

### Voorbeelden
- Een architectuurbesluit (betekenis)
  → vastgelegd als een ADR (representatie)
  → geschreven in Markdown (representatievorm)

- Een logisch datamodel (betekenis/structuur)
  → vastgelegd als een ER-diagram (representatie)
  → weergegeven als afbeelding of XML (representatievorm)

### Relatie tot **mandarin-agents**

**Inhoudelijke **mandarin-agents****
- Werken op betekenis en creëren of wijzigen representaties.

**Representatieomvormende **mandarin-agents****
- Werken uitsluitend op representaties en hun representatievormen, zonder begrip van betekenis.

Een representatieomvormende **mandarin-agent** verandert de uitdrukking, niet de inhoud.

### Canonieke zin (kort)

Een representatie is de concrete uitdrukking van betekenis; zij maakt betekenis zichtbaar zonder haar te bepalen.

---

## Representatiestatus

### Definitie
**Representatiestatus** is het meta-concept dat vastlegt of een **representatie** geldt als bron van betekenis, dan wel is afgeleid van een andere representatie, zonder de onderliggende betekenis zelf te wijzigen.

De representatiestatus zegt niets over de inhoud, maar alles over de positie van een representatie in de keten van afleiding.

### Categorieën binnen representatiestatus

#### 1. Bronrepresentatie

##### Definitie
Een **bronrepresentatie** is een representatie die geldt als het primaire vastleggingspunt van betekenis binnen een context.

Dit is de representatie:
- waar betekenis formeel aan wordt ontleend
- die leidend is bij interpretatie
- die niet afhankelijk is van een andere representatie voor haar geldigheid

##### Kenmerken
Een bronrepresentatie:
- is autoritatief binnen haar domein of scope
- fungeert als referentie voor afgeleide representaties
- kan door mensen worden vastgesteld, beoordeeld of gewijzigd
- heeft wijzigingen die doorwerken naar afgeleiden
- is vaak expliciet aangewezen (door governance of afspraak)

##### Wat een bronrepresentatie niet is
- Geen â€œeerste bestandâ€ per se
- Geen technisch origineel
- Geen onveranderlijke waarheid

Een bronrepresentatie is leidend bij verschil van interpretatie, niet per definitie ouder of technischer.

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
| 2026-02-21 | 1.10.0 | Toegevoegd: Epistemische as als vijfde orthogonale as voor mandarin-agent-classificatie, met vier categorieën (Deterministisch, Canon-gebonden, Retrieval-gebonden, Generatief) en verplichte checks per categorie | Constitutioneel Auteur  |
| 2026-02-15 | 1.9.0  | Toegevoegd: Architectuur-structurerend als positie op betekenis-as voor mandarin-agents | Constitutioneel Auteur  |
| 2026-02-15 | 1.8.0  | Toegevoegd: Structurerend artefact als positie op artefact-functie-as | Constitutioneel Auteur  |
| 2026-02-02 | 1.7.0  | Toegevoegd: Artefact-functie-as als expliciete ordenings-as voor Mandarin-artefacten, gekoppeld aan Artefactclassificatie | Constitutioneel Auteur  |
| 2026-02-02 | 1.6.0  | Herziening Artefactclassificatie: expliciete tweedimensionale ordening langs artefact-functie-as en representatievorm-as, voorbeelden uitgebreid | Constitutioneel Auteur  |
| 2026-02-01 | 1.5.0  | Bedrijfs-artefact hernoemd naar Richtinggevend artefact; toegevoegd: Realiserend artefact en Afgeleid artefact als aanvullende ordeningsconcepten | Constitutioneel Auteur  |
| 2026-02-01 | 1.4.0  | Toegevoegd: meta-concept Representatiestatus met categorie Bronrepresentatie | Constitutioneel Auteur  |
| 2026-02-01 | 1.3.0  | Toegevoegd: meta-concept Representatie als concrete uitdrukking van betekenis in een representatievorm | Constitutioneel Auteur  |
| 2026-02-01 | 1.2.0  | Toegevoegd: meta-concept Representatievorm als onderscheid tussen betekenis en vorm van artefacten | Constitutioneel Auteur  |
| 2026-02-01 | 1.1.0  | Toegevoegd: meta-concept Artefactclassificatie als ordeningskader voor Mandarin-artefacten en hun typen | Constitutioneel Auteur  |
| 2026-02-01 | 1.0.0  | Initiële versie — **ordenings-concepten** afgesplitst van concepten-en-architectonische-grondslagen.md v1.6.0; bevat classificatie-concepten (mandarin-agent-classificatie, As, 4 assen) en artefact-structuur (Mandarin-artefact met specialisaties) | Constitutioneel Auteur  |

---

**Einde document**


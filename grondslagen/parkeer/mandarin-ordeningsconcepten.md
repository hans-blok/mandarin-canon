# Mandarin **ordenings-concepten**

**Type**: Concepten en Definities  
**Repository**: mandarin-canon  
**Identifier**: mandarin-canon.concepten.meta  
**Version**: 1.0.0  
**Status**: Active  
**Last Updated**: 2026-02-22  
**Owner**: Hans Blok

---

## Herkomstverantwoording

Dit document is afgeleid van "concepten-en-architectonische-grondslagen.md" (versie 1.6.0) door Constitutioneel Auteur op 1 februari 2026, en op 22 februari 2026 afgesplitst voor specifieke ordening binnen workspaces (value streams 1-n).

**Geraadpleegde bronnen**:
- concepten-en-architectonische-grondslagen.md (versie 1.6.0, gelezen op 2026-02-01)
- herijking 2.md (gelezen op 2026-02-01)

**Datum**: 2026-02-22  
**Doel**: Expliciete scheiding tussen **ordenings-concepten** voor het ecosysteem en voor de workspaces. Dit document bevat uitsluitend de ordening voor de workspaces (value streams 1-n).

**Ontwerpkeuze**: **ordenings-concepten** beschrijven hoe de workspace zichzelf structureert en classificeert. Door deze in een apart document te plaatsen, wordt de architectonische lagenstructuur expliciet: **ordenings-concepten** definiëren het classificatiestelsel en de artefactstructuur voor de workspace, terwijl operationele concepten de actieve elementen beschrijven die binnen dat stelsel werken.

---

## Inhoudsopgave

### Classificatie en Structuur
- [Mandarin-architectuurprincipe](#mandarin-architectuurprincipe) — Richtinggevende regel voor ontwerp
- [**mandarin-agent**-boundary](#**mandarin-agent**-boundary) — Expliciete afbakening van verantwoordelijkheid
- [mandarin-agent-classificatie](#mandarin-agent-classificatie) — Positionering langs orthogonale assen
- [As](#as) — Ordeningsdimensie voor positionering
- [Artefact-functie-as](#artefact-functie-as) — Functierol van Mandarin-[artefacten](../../artefacten/README.md)
- [Artefactclassificatie](#artefactclassificatie) — Indeling van Mandarin-[artefacten](../../artefacten/README.md)

### mandarin-agent-classificatie Assen
- [Betekeniseffect](#betekeniseffect) — Effect op betekenis
- [Werking](#werking) — Inhoud, representatie of voorwaarden
- [Vormingsfase](#vormingsfase) — Fase van totstandkoming
- [Bronhouding](#bronhouding) — Kennisbronnen en herleidbaarheid

### [artefacten](../../artefacten/README.md)
- [Mandarin-artefact](#mandarin-artefact) — Expliciet vastgelegd, overdraagbaar resultaat
- [Vastleggend artefact](#vastleggend-artefact) — Artefact dat normen, regels of direct uitvoerbaar gedrag vastlegt
  - [Richtinggevend artefact](#richtinggevend-artefact) — Specialisatie: bindende richting in workspaces
- [Structurerend artefact](#structurerend-artefact) — Artefact dat architectuurelementen en relaties expliciteert
- [Interpreterend artefact](#interpreterend-artefact) — Artefact dat betekenis, interpretatie of oordeel geeft
- [Registrerend artefact](#registrerend-artefact) — Artefact dat inzicht en uitleg biedt
- [Representatie](#representatie) — Concrete uitdrukking van betekenis
- [Afleidingspositie](#afleidingspositie) — Leidend of afgeleid in de keten

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
  2. **Vormingsfase** — fase van totstandkoming
  3. **Werking** — inhoud, representatie of voorwaarden
  4. **Bronhouding** — kennisbronnen en herleidbaarheid

### Wat het niet is
- Geen enkelvoudig label (zoals "adviserende **mandarin-agent**" of "uitvoerende **mandarin-agent**")
- Geen hiërarchische structuur
- Geen technische implementatie-eigenschap
- Geen tijdelijke classificatie

### Voorbeelden
- Een **mandarin-agent** kan registrerend zijn (betekeniseffect), in de beschrijven-fase acteren (vormingsfase), en inhoudelijk zijn (werking)
- Een **mandarin-agent** kan vastleggend, in de vastleggings-fase, en inhoudelijk zijn
- Een **mandarin-agent** kan conditioneel zijn (werking), in de realisatie-fase (vormingsfase)

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
- Vijf categorieën: Geen betekenis (Nul-positie), Registrerend, Interpreterend, Structurerend, Vastleggend
- Onafhankelijk van andere assen (Vormingsfase, Werking, Bronhouding)
- Bepaalt fundamentele rol en impact van de **mandarin-agent**

### Wat het niet is
- Geen technische implementatievariant
- Geen organisatorische indeling
- Geen enkelvoudig label

### Categorieën 

**0. Geen betekenis (Nul-positie)**
- Heeft geen effect op de betekenis van de inhoud
- Geldt voor de conditionele werking (waarbij de agent zich richt op randvoorwaarden en hygiëne, niet op inhoud)
- Bij representatie-omvorming heeft de nieuwe representatie exact dezelfde betekenis als de bron die is omgevormd
- Voorbeelden: Workspace stewards, formatters, syntax-checkers, converters

**1. Interpreterend**
- **Definitie**: Geeft betekenis, interpretatie of oordeel aan bestaande structuren, voorstellen of resultaten.
- **Kenmerken**: Voegt duiding of beoordeling toe, is niet vastleggend, sluit interpretatie niet af.
- **Voorbeelden van rollen**: Architectuurbeoordelaar, Risico-analist, Hypotheseformuleerder, Samenhangduider, Kwaliteitsreviewer.

### Definitie
De **Betekeniseffect-as** beschrijft het type interventie dat een mandarin-agent uitvoert op betekenis.
Het gaat niet om de procesfase, maar om wat er met betekenis gebeurt.

### Categorieën
- **0. Geen betekenis (Nul-positie)**
  Heeft geen effect op de betekenis van de inhoud.
  Geldt voor de conditionele werking (waarbij de agent zich richt op randvoorwaarden en hygiëne, niet op inhoud).
  Bij representatie-omvorming heeft de nieuwe representatie exact dezelfde betekenis als de bron die is omgevormd.
  Voorbeelden: Workspace stewards, formatters, syntax-checkers, converters.
- **Beschrijvend**
  Legt bestaande werkelijkheid vast zonder deze te veranderen.
- **Structuurrealiserend**
  Maakt impliciete samenhang expliciet en expliciteert relaties of structuur.
- **Normerend**
  Verklaart een structuur, regel of gedraging als geldend of verplicht.
- **Realiserend**
  Zet een norm of ontwerp om in werkende implementatie.
- **Evaluerend**
  Beoordeelt een artefact of realisatie tegen een norm of verwachting.

### Synoniemen
- Effect-as
- Betekenis-as

### Toelichting
De Betekeniseffect-as is de primaire as voor mandarin-agent-classificatie omdat deze de fundamentele rol en impact van een mandarin-agent op betekenis bepaalt. Het onderscheid tussen structuur-normering (werk) en workspace-normering (spelregels) is cruciaal.
- Betekenis-blind (de nieuwe representatie heeft exact dezelfde betekenis als de bron die is omgevormd)
- Infrastructuurachtig
- Vormtransformatie (bijv. Markdown → XML → diagram)

**3. Conditioneel**
- Werken niet op inhoud, maar op voorwaarden en hygiëne
- Geen betekenis (nul-positie op de betekeniseffect-as)
- Geen value-stream-[artefacten](../../artefacten/README.md)
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
## Vormingsfase

### Definitie
**Vormingsfase** is het ordeningsconcept dat beschrijft in welke fase van de totstandkoming van een oplossing een rol, **mandarin-agent** of capability ingrijpt of betekenis beïnvloedt.

**Leidende vraag**: In welke fase van de totstandkoming vindt de ingreep plaats?

Vormingsfase zegt niets over *wat* er met betekenis gebeurt (dat beschrijft het betekeniseffect), maar uitsluitend *wanneer* in het proces dat gebeurt.

### Kenmerken
- Is orthogonaal aan het betekeniseffect (effect op betekenis)
- Classificeert de fase van ingreep, niet het type handeling
- Geldt voor alle inhoudelijke categorieën (registrerend, interpreterend, structurerend, vastleggend)
- Maakt onderscheid tussen verkenning, ordening, vastlegging, toetsing en verantwoording
- Verhoogt bestuurbaarheid en traceerbaarheid binnen de workspace

### Wat het niet is
- Geen hiërarchische waardering (verkenning is niet "belangrijker" dan vastlegging)
- Geen inhoudelijke classificatie (dat is het betekeniseffect)
- Geen technische laag (zoals runtime, tooling of infrastructuur)
- Geen waardeoordeel

### Fasen

#### 1. Verkenning

**Definitie**  
Fase waarin intentie, probleemstelling of richting wordt onderzocht en verkend.

**Kenmerken**
- Open en onderzoekend karakter  
- Alternatieven worden verkend  
- Geen bindende besluiten  


**Voorbeelden**

- Probleemanalyse  
- Hypothesevorming  
- Contextverkenning  
- Stakeholderanalyse  
- Initiële impactverkenning  

---

#### 2. Ordening

**Definitie**  
Fase waarin intentie wordt gestructureerd en samenhang expliciet wordt gemaakt.

**Kenmerken**

- Brengt structuur aan  
- Maakt relaties zichtbaar  
- Nog niet bindend  

**Voorbeelden**
- Uitwerking van een THEMA  

- Structureren van VERBETERINGEN en WERKTAKEN  
- Conceptueel domeinmodel  
- Capability-indeling  
- Processtructuur  


---
#### 3. Vastlegging


**Definitie**  
Fase waarin betekenis bindend wordt vastgesteld binnen de workspace.


**Kenmerken**
- Sluit interpretatie  
- Formele of uitvoerende status  
- Creëert richtinggevende of realiserende [artefacten](../../artefacten/README.md)  

**Voorbeelden**
- Vaststellen van Gherkin-requirements  
- Formeel goedkeuren van een logisch datamodel  
- Vaststellen van architectuurprincipes  
- Vastleggen van runtime-configuratie  
- Publiceren van een leidende OpenAPI-specificatie  

---

#### 4. Toetsing

**Definitie**  
Fase waarin vastgesteld werk wordt gecontroleerd tegen eerder vastgelegde normen of verwachtingen.

**Kenmerken**
- Vergelijkt realisatie met vastgelegde kaders  
- Geen nieuwe normering  
- Geen nieuwe vastlegging  

**Voorbeelden**

- Testuitvoering  
- Review tegen architectuurprincipes  
- Compliance-check  
- Validatie van datamodel tegen requirements  

---

#### 5. Verantwoording

**Definitie**  
Fase waarin gerealiseerd en getoetst werk wordt toegelicht, gedocumenteerd of verantwoord.

**Kenmerken**
- Uitleggend en informerend  
- Geen normerende werking  
- Ondersteunt transparantie en overdraagbaarheid  

**Voorbeelden**
- Release notes  
- Systeemdocumentatie  
- Architectuurtoelichting  
- Auditverslag  
- Besluitvormingsverslag  

### Orthogonaliteit

Vormingsfase moet altijd gecombineerd worden met het betekeniseffect.

**Voorbeeldmatrix**:

|Betekenis effect        | Vormingsfase       | Voorbeeld                              |
|------------------------|--------------------|----------------------------------------|
| Beschrijvend           | Verkenning         | Vastleggen van context, analyse, bestaande situatie |
| Structuurrealiserend   | Ordening           | Expliciteren van relaties, domeinstructuur, capability-indeling |
| Normerend              | Vastlegging        | Formeel vaststellen van architectuurprincipes, normen, regels |
| Realiserend            | Vastlegging        | Implementeren van ontwerp, schrijven van code, configuratie |
| Evaluerend             | Toetsing           | Beoordelen van realisatie, review, compliance-check |
| Beschrijvend           | Verantwoording     | Documenteren van systeemwerking, release notes, auditverslag |

---
## Bronhouding

### Definitie
De **bronhouding** is een classificatie-as binnen mandarin-agent-classificatie die beschrijft op welke kennisbronnen een **mandarin-agent** zich baseert en in welke mate de output herleidbaar is tot expliciete bronnen.

**Leidende vraag:** *Op welke kennisbronnen baseert deze **mandarin-agent** zich, en hoe herleidbaar is de output?*

### Kenmerken
- Is één van vier orthogonale assen voor mandarin-agent-classificatie
- Onderscheidt **mandarin-agents** op basis van kennisbrongebruik en herleidbaarheid
- Vijf categorieën: Input-gebonden, Canon-gebonden, Workspace-gebonden, Externe-bron gebonden, Exploratief (Open)
- Onafhankelijk van andere assen (Betekeniseffect, Vormingsfase, Werking)
- Bepaalt de epistemische verantwoordelijkheid en controleerbaarheid van de **mandarin-agent**

### Wat het niet is
- Geen kwaliteitsmaatstaf van de output
- Geen technische implementatiekeuze
- Geen indicatie van complexiteit of waarde

### Categorieën

** 1. Input-gebonden**
- Output is 100% herleidbaar tot de input
- Geen externe kennisbronnen
- Volledig voorspelbaar en reproduceerbaar
- Transformeert of herordent alleen de gegeven input
- Voorbeelden: Sorteerders, Formatters, Parsers

** 2. Canon-gebonden**
- Baseert zich expliciet op de Mandarin-canon
- Canon-verwijzing is verplicht in de output
- Leest en interpreteert canonieke documenten
- Output is traceerbaar naar specifieke canon-[artefacten](../../artefacten/README.md)
- Voorbeelden: Richtlijn-interpreterende **mandarin-agents**, Charter-validerende **mandarin-agents**

** 3. Workspace-gebonden**
- Baseert zich expliciet op de workspace
- Output is herleidbaar tot workspace-specifieke bronnen, configuraties of policies
- Kan verwijzen naar workspace-documentatie, lokale afspraken of project-specifieke artefacten
- Voorbeelden: Workspace-specifieke validatieagents, configuratie-checkers, agents die lokale policies afdwingen

** 4. Externe-bron gebonden**
- Haalt kennis op uit specifieke, geïdentificeerde bronnen buiten de canon
- Bronvermelding is verplicht
- Gebruikt RAG (Retrieval-Augmented Generation) of vergelijkbare technieken
- Output is herleidbaar naar concrete brondocumenten
- Voorbeelden: Documentatie-samenvattende **mandarin-agents**, Context-verzamelende **mandarin-agents**

** 5. Exploratief**
- Genereert output op basis van trained knowledge en redenering
- Maakt aannames en afleidingen
- Aannames moeten expliciet worden gemaakt (maximaal 3)
- Minst herleidbaar, hoogst creatief
- Voorbeelden: Architectuur-ontwerpende **mandarin-agents**, Creatieve schrijf-**mandarin-agents**

### Verplichte checks per categorie

| Categorie | Verplichte checks | Mate van probalisme |
|-----------|-------------------|---------------------|
| Input-gebonden | 100% herleidbaar | Deterministisch |
| Canon-gebonden | Canon-verwijzing verplicht | Laag |
| Externe-bron gebonden | Bronvermelding verplicht | Middel |
| Exploratief | Aannames expliciet (max 3) | Hoog |

### Synoniemen
- Epistemische houding
- Kennisbron-as
- Herleidbaarheidsdimensie
- Epistemologische as

### Analogieën 
- Vergelijkbaar met transparency levels in AI systems
- In wetenschappelijk onderzoek: primaire vs secundaire bronnen vs interpretatie
- In softwareontwikkeling: pure functions vs database-driven vs AI-augmented

### Toelichting  
De **bronhouding** maakt expliciet hoe een **mandarin-agent** tot zijn kennis komt en in welke mate de output controleerbaar en herleidbaar is. Dit is cruciaal voor vertrouwen, governance en kwaliteitsborging. Hoe verder naar rechts op de as (van input-gebonden naar exploratief), hoe meer epistemische verantwoordelijkheid de **mandarin-agent** draagt om zijn bronnen en aannames expliciet te maken.

Deze as stelt de workspace in staat om:
- Bewust te kiezen voor het juiste niveau van herleidbaarheid per use case
- Expliciete eisen te stellen aan bronvermelding en traceerbaarheid
- Risico's te beheersen door aannames te beperken en expliciet te maken
- Vertrouwen te borgen door transparantie over kennisbronnen

---
## Artefact-functie-as

### Definitie
De **artefact-functie-as** is een classificatie-as voor **Mandarin-[artefacten](../../artefacten/README.md)** die beschrijft *welke functie* een artefact vervult in de besluit- en waardeketen binnen de workspace.

**Leidende vraag:** *Welke vastleggende, structurerende, interpreterende of registrerende functie heeft dit artefact in de workspace?*

### Kenmerken
- Is een ordenings-as specifiek voor **Mandarin-[artefacten](../../artefacten/README.md)** (niet voor **mandarin-agents**)
- Positioneert [artefacten](../../artefacten/README.md) op basis van hun rol in besluitvorming, structurering, uitvoering en inzicht
- Vormt samen met de **representatie-as** de kern van **Artefactclassificatie**
- Is onafhankelijk van bestandsformaat, tooling of repository-structuur
- Is onafhankelijk van procesfase of vormingsfase; hetzelfde artefact kan in meerdere fasen worden gebruikt, maar heeft één primaire functie

### Posities

Op de **artefact-functie-as** worden de volgende vier canonieke posities onderscheiden:

**1. Vastleggend artefact**
- Legt betekenis vast als geldend binnen de workspace
- Bevat bindende afspraken, voorschriften, of direct uitvoerbaar gedrag
- Heeft uitvoerbare of door tooling direct interpreteerbare impact, of stelt harde kaders
- Voorbeelden: programmacode, Gherkin-requirements, database-schema's, deployment-configuraties
- Specialisatie: **richtinggevend artefact** (workspaces)

**2. Structurerend artefact**
- Structureert intentie zonder die te fixeren
- Representeert een coherent geheel van architectuurelementen en hun onderlinge relaties
- Geordend volgens een metamodel of kader
- Maakt de structuur van een systeem expliciet en beredeneerbaar
- Voorbeelden: architectuurmodellen, metamodellen, structuurontwerpen

**3. Interpreterend artefact**
- Geeft betekenis, interpretatie of oordeel
- Beoordeelt kwaliteit, samenhang en risico's
- Legt een oordeel vast, geen besluit
- Voorbeelden: review-rapporten, compliance-checks, kwaliteitsmetingen

**4. Registrerend artefact**
- Legt vast wat is
- Maakt bestaande of voorgenomen werkelijkheid inzichtelijk
- Legt analyse, structuur of samenhang vast zonder zelf vastleggend of structurerend te zijn
- Voorbeelden: modellen, analyses, overzichten, documentatie, handleidingen

### Wat het niet is
- Geen indeling naar bestandsformaat, repository of tooling
- Geen kwaliteitsmeting of volwassenheidsniveau van [artefacten](../../artefacten/README.md)
- Geen fasering van werk of levenscyclus-status (concept, draft, definitief)
- Geen indeling naar betrokken personen, teams of rollen

### Voorbeelden
- Een **application-charter** of themabeschrijving staat als **richtinggevend artefact** (dus vastleggend binnen een specifieke workspace)
- Een ArchiMate-model of domeinmodel met coherente structuur staat als **structurerend artefact**
- Een logisch datamodel dat direct systeemgedrag bepaalt of programmacode staat als **vastleggend artefact**
- Een architectuurdiagram, analysemodel, API-referentie of gebruikershandleiding staat als **registrerend artefact**
- Een testrapport of review-bevinding staat als **interpreterend artefact**

### Synoniemen
- Artefact-rol-as
- Functie-as voor [artefacten](../../artefacten/README.md)

### Analogieën 
- In informatiebeheer: beleid / proces / registratie als verschillende functies van informatie-objecten
- In softwareontwikkeling: onderscheid tussen specificatie, design, implementatie en documentatie

### Toelichting  
De **artefact-functie-as** maakt zichtbaar *wat* een artefact doet in de workspace: of het kaders schept en gedrag realiseert (vastleggend), structuur expliciteert (structurerend), oordeelt (interpreterend) of inzicht geeft en vastlegt (registrerend). Deze as werkt samen met de **representatie-as**: dezelfde functie kan in verschillende representaties bestaan zonder dat de positie op de **artefact-functie-as** verandert.

De posities op de **artefact-functie-as** corresponderen direct met de ordeningsconcepten **vastleggend artefact**, **structurerend artefact**, **interpreterend artefact** en **registrerend artefact**. **Artefactclassificatie** gebruikt deze as expliciet om [artefacten](../../artefacten/README.md) te positioneren naar hun functie, los van vorm, tooling en proces.

---
## Artefactclassificatie

### Definitie
**Artefactclassificatie** is het expliciet ordenen en positioneren van **Mandarin-[artefacten](../../artefacten/README.md)** langs twee orthogonale assen:
- een **artefact-functie-as** (vastleggend, structurerend, interpreterend, registrerend), en
- een **representatie-as** (tekst, diagram, programma code, machine taal, â€¦),
waarbij de representatie tevens een **afleidingspositie** (leidend of afgeleid) heeft. Dit zorgt ervoor dat helder is *welke functie* een artefact heeft, *in welke vorm* het wordt uitgedrukt, en *wat de status* van die uitdrukking is.
zodat helder is *welk* type artefact iets is en *in welke vorm* het wordt uitgedrukt.

### Kenmerken
- Biedt een consistent classificatiekader voor alle **Mandarin-[artefacten](../../artefacten/README.md)**
- Gebruikt op de **artefact-functie-as** posities als: **vastleggend artefact** (met specialisatie **richtinggevend artefact**), **structurerend artefact**, **interpreterend artefact** en **registrerend artefact**
- Gebruikt op de **representatie-as** de concepten uit **representatie** (bijv. tekst, diagram, programma code, machine taal)
- Gebruikt de **afleidingspositie** (leidend of afgeleid) om de status van de representatie aan te geven
- Is tooling-onafhankelijk: de classificatie verandert niet door bestandsformaat, repository of implementatiedetail
- Verbindt [artefacten](../../artefacten/README.md) expliciet met hun rol in de workspace

### Wat het niet is
- Geen lijst van bestandsformaten of tooling-keuzes
- Geen hiërarchie van belangrijkheid of waarde
- Geen procesindeling of fasering van werk
- Geen technische classificatie (bijvoorbeeld op basis van repository of folderstructuur)

### Voorbeelden
- Een requirements-specificatie of thema-beschrijving wordt geclassificeerd als **richtinggevend artefact** (vastleggend binnen een workspace), vaak tekstueel
- Een **ArchiMate-model** of domeinmodel met coherente architectuurstructuur wordt geclassificeerd als **structurerend artefact** in een diagram- of model-gebaseerde representatie
- Een logisch datamodel dat direct systeemgedrag realiseert of programmacode wordt geclassificeerd als **vastleggend artefact** in een programma code of machine taal representatie (bijv. DDL, model-XML)
- Een architectuurdiagram, ad-hoc analysemodel of gegenereerde documentatie wordt geclassificeerd als **registrerend artefact**, vaak met een afgeleide afleidingspositie
- Een testrapport of review-bevinding wordt geclassificeerd als **interpreterend artefact**

### Synoniemen
- Artefact-positionering
- Artefact-typenindeling

### Analogieën 
- Vergelijkbaar met de indeling in policy / process / record in informatiebeheer
- In softwareontwikkeling: onderscheid tussen source artefacts, design docs en generated documentation

### Toelichting  
**Artefactclassificatie** vormt de meta-laag boven op de concrete definities van **Mandarin-artefact**, **vastleggend artefact**, **richtinggevend artefact**, **structurerend artefact**, **interpreterend artefact**, **registrerend artefact**, **representatie** en **afleidingspositie**. Zij legt vast *langs welke assen* [artefacten](../../artefacten/README.md) worden geordend en welke posities op die assen canoniek zijn.

Samengevat:
- de **artefact-functie-as** positioneert [artefacten](../../artefacten/README.md) op basis van hun functie binnen de workspace. Met deze functie krijgt het artefact betekenis.
- de **representatie-as** maakt zichtbaar *hoe* die betekenis wordt uitgedrukt (tekst, diagram, programma code, machine taal, â€¦).
- de **afleidingspositie** geeft aan of deze representatie de leidende bron is, of is afgeleid van een andere representatie.

Door deze classificatie wordt helder welke [artefacten](../../artefacten/README.md) vastleggend en prescriptief zijn, welke [artefacten](../../artefacten/README.md) structuur of inzicht bieden, en hoe al deze [artefacten](../../artefacten/README.md) in verschillende representaties kunnen bestaan zonder dat hun rol verandert. Dit maakt het mogelijk om werk en governance scherp van elkaar te scheiden, tooling verwisselbaar te houden en de betekenis van elk artefacttype vast en toetsbaar te maken.

---

## Vastleggend artefact

### Definitie
Een **vastleggend artefact** is een **Mandarin-artefact** dat expliciete normen, regels, principes, standaarden of direct uitvoerbaar gedrag vastlegt die geldend zijn voor een specifiek domein binnen de workspace.

### Kenmerken
- Legt betekenis vast als geldend binnen de workspace
- Is prescriptief (schrijft voor wat moet) of direct uitvoerbaar
- Is leidend voor ontwerp, implementatie en evaluatie
- Vormt de hoogste autoriteit binnen zijn scope
- Is versieerbaar en traceerbaar
- Wordt niet afgeleid uit andere [artefacten](../../artefacten/README.md)
- **Is operationeel in maximaal één vormingsfase**
- Heeft één specialisatie: richtinggevend artefact

### Wat het niet is
- Geen beschrijving van huidige situatie
- Geen advies of aanbeveling
- Geen documentatie of uitleg

### Voorbeelden
- Architectuurprincipes
- Ontwerprichtlijnen
- Kwaliteitseisen
- Domeinindelingen
- Standaarden en richtlijnen
- Programmacode
- Gherkin-requirements
- Database-schema's (DDL)
- Deployment-configuraties

### Synoniemen
- Normatief artefact
- Prescriptief artefact
- Regel-artefact
- Vastleggend artefact
- Vastleggend artefact

### Analogieën 
- Vergelijkbaar met wetgeving, standaarden (zoals ISO), policies
- In enterprise architectuur: principles, standards, guidelines
- In softwareontwikkeling: coding standards, architectural decision records (vastleggende variant), source code, infrastructure-as-code

### Toelichting  
**Vastleggende [artefacten](../../artefacten/README.md)** hebben de hoogste autoriteit en zijn geldend. Zij vormen het fundament waarop alle andere [artefacten](../../artefacten/README.md) voortbouwen, of ze realiseren direct het gedrag van het systeem. Vastleggende [artefacten](../../artefacten/README.md) zijn primair (niet afgeleid) en stabiel in de tijd.

---

## Structurerend artefact

### Definitie
Een **structurerend artefact** is een **Mandarin-artefact** dat een coherent geheel van architectuurelementen en hun onderlinge relaties representeert, geordend volgens een metamodel of kader, met als doel de structuur van een systeem expliciet en beredeneerbaar te maken zonder deze te fixeren.

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
**Structurerende [artefacten](../../artefacten/README.md)** maken de architectonische structuur van systemen expliciet door elementen en hun relaties te ordenen volgens een coherent kader. Zij verschillen van **registrerende [artefacten](../../artefacten/README.md)** door hun focus op structurele coherentie en metamodel-conformiteit, en van **vastleggende [artefacten](../../artefacten/README.md)** omdat zij structuur representeren maar niet direct uitvoeren of fixeren.

---

## Interpreterend artefact

### Definitie
Een **interpreterend artefact** is een **Mandarin-artefact** dat betekenis, interpretatie of een oordeel geeft over andere [artefacten](../../artefacten/README.md) of systemen.

### Kenmerken
- Beoordeelt kwaliteit, samenhang en risico's
- Legt een oordeel vast, geen besluit
- Is evaluatief van aard
- Kan gegenereerd zijn uit geautomatiseerde checks of handmatige reviews

### Wat het niet is
- Geen vastleggend artefact (legt geen norm of intentie vast)
- Geen puur registrerend artefact (het bevat een oordeel of interpretatie)
- Geen structurerend artefact

### Voorbeelden
- Formuleringshypothese voor een verandering
- Testrapporten
- Review-bevindingen
- Compliance-checks
- Kwaliteitsmetingen
- Security-audits

### Synoniemen
- Interpreterend artefact
- Beoordelings-artefact
- Interpreterend artefact

### Analogieën 
- In softwareontwikkeling: test results, linting reports, code review comments
- In kwaliteitszorg: audit reports, inspectierapporten

### Toelichting  
**Interpreterende [artefacten](../../artefacten/README.md)** vormen de feedbackloop binnen de workspace. Zij toetsen of de gerealiseerde of ontworpen [artefacten](../../artefacten/README.md) voldoen aan de gestelde kaders en leveren de interpretatie die nodig is voor verdere besluitvorming.

---

## Registrerend artefact

### Definitie
Een **registrerend artefact** is een **Mandarin-artefact** dat inzicht, uitleg of overzicht biedt over bestaande structuren, besluiten of situaties, zonder zelf vastleggend of structurerend te zijn.

### Kenmerken
- Biedt inzicht en uitleg
- Is descriptief (beschrijft wat is)
- Is niet vastleggend of prescriptief
- Kan afgeleid zijn uit andere [artefacten](../../artefacten/README.md)
- Ondersteunt begripsvorming en communicatie

### Wat het niet is
- Geen vastleggend artefact (schrijft niets voor)
- Geen richtinggevend artefact (geen vastleggende output van vormingsfase)
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
- Registrerend artefact

### Analogieën 
- Vergelijkbaar met white papers, explanatory documents, vision documents
- In enterprise architectuur: viewpoints, perspectives
- In softwareontwikkeling: architectural decision records (registrerende variant), design rationale

### Toelichting  
**Registrerende [artefacten](../../artefacten/README.md)** helpen mensen de workspace te begrijpen. Zij zijn vaak afgeleid uit vastleggende of richtinggevende [artefacten](../../artefacten/README.md). Registrerende [artefacten](../../artefacten/README.md) zijn ondersteunend en niet vastleggend.

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

## Bijlage - Onderscheid tussen Canon-gebonden en Workspace-gebonden

Het benaderen van artefacten in een workspace betekent niet automatisch dat de bronhouding workspace-gebonden is.

De locatie van een artefact (bijv. in een Git-repository of projectmap) bepaalt niet het bronregime.  
Het bronregime wordt bepaald door het type geslotenheid waarin wordt geopereerd.

### Canon-gebonden (Normatief gesloten)

Een activiteit is **canon-gebonden** wanneer:

- uitsluitend normatief vastgelegde artefacten worden geraadpleegd;
- geen implementatie of operationele uitvoering plaatsvindt;
- geen nieuwe selectie of exploratie wordt uitgevoerd;
- de interventie gericht is op betekenisvorming of normering.

Typische voorbeelden:
- Bekrachtiging & formele fixatie
- Toetsbaarheid expliciteren
- Publicatie & verankering
- Conceptuele toetsing

Hier verandert geen realiteit, alleen de normatieve status van betekenis.

---

### Workspace-gebonden (Operationeel gesloten)

Een activiteit is **workspace-gebonden** wanneer:

- wordt gewerkt binnen een gesloten technische werkset;
- implementatie of configuratie plaatsvindt;
- realiteit operationeel wordt gerealiseerd;
- geen nieuwe betekenisvorming plaatsvindt.

Typische voorbeelden:
- Code schrijven
- DDL genereren
- Configuratie opstellen
- Build en deployment

Hier verandert realiteit, niet betekenis.

---

### Kernonderscheid

De beslissende vraag is niet:

> Wordt de workspace benaderd?

Maar:

> Wordt betekenis normatief gesloten, of wordt realiteit operationeel gerealiseerd?

- Vastlegging → Canon-gebonden  
- Realisatie → Workspace-gebonden  

Het onderscheid tussen normeren en realiseren mag niet vervagen.

## Change Log

| Datum      | Versie | Wijziging                                                           | Auteur     |
|------------|--------|---------------------------------------------------------------------|------------|
| 2026-02-22 | 1.0.0  | Harde afsplitsing voor workspace-ordening. Interventieniveau vervangen door Vormingsfase. Ecosysteem-concepten verwijderd. | Hans Blok  |

---

**Einde document**



## Relaties
- **Gerelateerd aan**: [artefacten](../../artefacten/README.md)
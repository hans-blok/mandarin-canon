# ArchiMate samenvatting voor LLM en architectuurwerk

**Status**: Werkdocument  
**Doel**: compacte kennisbron voor interpretatie van ArchiMate-views, modelleerkeuzes en agentondersteuning  
**Gebruik**: intern, als afgeleide samenvatting in eigen woorden

---

## 1. Doel en gebruik van deze kennisbron

Deze samenvatting is bedoeld als praktische referentie voor architecten en LLM-gebaseerde agents die werken met ArchiMate-views in deze repository. Het document is nadrukkelijk **geen vervanging van de formele standaard**, maar een compacte, repo-specifieke interpretatiehulp.

De focus ligt op:

- het herkennen van elementtypen in views;
- het correct duiden van veelgebruikte relaties;
- het koppelen van ArchiMate aan Common Ground, GEMMA en GGM-context;
- het verminderen van interpretatiefouten in viewbeschrijvingen en architectuurteksten.

---

## 2. Basisidee van ArchiMate

ArchiMate is een modeltaal voor enterprise-architectuur. De taal maakt het mogelijk om samenhang te beschrijven tussen:

- gedrag: services, processen, functies, interacties;
- structuur: actoren, rollen, componenten, interfaces, objecten;
- informatie: data-objecten, business-objecten en hun gebruik;
- verandering en motivatie: doelen, uitkomsten, requirements, work packages en roadmap-elementen.

Een ArchiMate-view is daarom nooit alleen een plaatje. Een view is een **bewuste selectie van elementen en relaties** voor een bepaald doel, bijvoorbeeld:

- context tonen;
- dataflow uitleggen;
- componenten en integraties afbakenen;
- een roadmap of transitie uitleggen.

---

## 3. Werken met viewpoints

Een goede ArchiMate-view heeft impliciet of expliciet een viewpoint. In deze repository zijn vooral de volgende viewpoints relevant:

| Viewpoint | Gebruik in deze repo |
|---|---|
| Contextview | Positionering van componenten en services in het Common Ground-landschap |
| Informatieflowview | Transformatie, mapping en gegevensstromen tussen bron, canoniek model en doel |
| Applicatieview | Application services, application components, interfaces en hun relaties |
| Roadmapview | Fasering van features, work packages en mijlpalen |
| Motivatieview | Doelen, outcomes, capabilities, principes en requirements |

LLM-regel:

- Vraag altijd eerst: *wat probeert deze view uit te leggen?*
- Kies pas daarna elementtypen en relaties.

---

## 4. Kernlagen voor deze repository

ArchiMate kent eigen lagen, maar in deze repository wordt vaak gecombineerd met het Common Ground 5-lagenmodel. Gebruik daarom onderstaande werkmapping als interpretatiehulp.

| Common Ground-laag | Typische ArchiMate-elementen | Voorbeeld in deze repo |
|---|---|---|
| 5 Interactie | Business actor, business role, application service, application interface | Mijn Omgeving, KISS, Team Digitale dienstverlening |
| 4 Procesinrichting | Business process, application component, application service | XXLLNC Zaken, zaakafhandeling |
| 3 Connectiviteit | Application component, application interface, application collaboration, flow | Synchronisatiebrug, FSC Gateway, notificatiestromen |
| 2 Dienstenaanbieder | Application service, application component, data object | Open Zaak, Open Notificaties, KPC |
| 1 Databron | Data object, artifact, technology object | Open Zaak-database, bestanden, registers |

Let op:

- Common Ground-lagen zijn **geen ArchiMate-elementtypen**.
- Ze helpen bij positionering, niet bij notatiekeuze.

---

## 5. Kernconcepten: elementen

### 5.1 Actor en rol

| Element | Betekenis | Gebruik |
|---|---|---|
| Business actor | Organisatorische partij of team | Team Digitale dienstverlening |
| Business role | Verantwoordelijkheid of rol | KCC-medewerker, redacteur |

Regel:

- Gebruik `Business actor` voor een team of organisatie-eenheid.
- Gebruik `Business role` voor een functie of verantwoordelijkheid.

### 5.2 Gedragselementen

| Element | Betekenis | Gebruik |
|---|---|---|
| Business process | Geordende reeks activiteiten in de business | Publiceren van vraag-antwoordcombinaties |
| Business function | Stabiele capabilityachtige functie aan businesszijde | Alleen gebruiken als het echt een organisatorische functie is |
| Application service | Extern waarneembare applicatieve dienst | Ontsluiten van kennis, Geleiden van klanten |
| Application function | Interne applicatieve functie | Alleen gebruiken als intern gedrag centraal staat |
| Application process | Sequentieel intern applicatieproces | Batch of orkestratieproces |

Regel:

- Kies `Application service` als iets wordt aangeboden of afgenomen.
- Kies `Application function` of `Application process` als het interne werking beschrijft.

### 5.3 Structuurelementen

| Element | Betekenis | Gebruik |
|---|---|---|
| Application component | Deploybare of logisch afgebakende applicatiecomponent | Strapi, KISS, Open Zaak |
| Application interface | Aansluitpunt of API | OpenProduct API, ZGW API |
| Collaboration | Samenwerking tussen meerdere componenten of rollen | Alleen gebruiken als samenwerking zelf relevant is |

Regel:

- Een component **realiseert** vaak een service.
- Een interface is geen losse dienst, maar een toegangspunt of contract naar die dienst.

### 5.4 Informatie-elementen

| Element | Betekenis | Gebruik |
|---|---|---|
| Business object | Bedrijfsmatig betekenisvol object | Producttype, Product |
| Data object | Gegevensobject voor applicatief gebruik | Kennisartikel, Zaakobject, CG Objecttype Kennisartikel |
| Artifact | Fysieke of digitale representatie | document, export, bestand |

Regel:

- Gebruik `Business object` als het concept primair vanuit businessbetekenis wordt gemodelleerd.
- Gebruik `Data object` als het informatieobject in een applicatieve context wordt gebruikt of beheerd.

---

## 6. Kernconcepten: relaties

### 6.1 Serving

**Betekenis**: een element levert bruikbaarheid of ondersteuning aan een ander element.

Gebruik:

- een service bedient een afnemende component of actor;
- een interface bedient een consumer;
- een applicatieve dienst ondersteunt een businessservice of gebruiker.

Vuistregel:

- Als je kunt zeggen: *A levert iets bruikbaars aan B*, is `Serving` vaak juist.

Voorbeeld:

- `Ontsluiten van kennis` bedient `KISS`.

Verwissel niet met:

- `Realization`: dat gaat over implementeren of concreet maken;
- `Assignment`: dat gaat over toewijzing van verantwoordelijkheid of uitvoering.

### 6.2 Realization

**Betekenis**: een concreter element verwezenlijkt of implementeert een abstracter element.

Gebruik:

- application component realiseert application service;
- work package realiseert plateau of deliverable;
- data-implementatie realiseert logisch object.

Vuistregel:

- Als je kunt zeggen: *A maakt B concreet of implementeert B*, is `Realization` waarschijnlijk juist.

Voorbeeld:

- `Strapi` realiseert `Ontsluiten van kennis`.

### 6.3 Assignment

**Betekenis**: gedrag of verantwoordelijkheid wordt toegewezen aan een actor, rol of component.

Gebruik:

- team voert proces uit;
- component voert functie uit.

Vuistregel:

- Als het gaat om *wie doet het* in plaats van *wie levert iets aan wie*, gebruik eerder `Assignment`.

### 6.4 Access

**Betekenis**: een gedragselement leest, schrijft of gebruikt een object.

Gebruik:

- proces gebruikt data object;
- service leest of wijzigt business object;
- component schrijft naar register.

Vuistregel:

- Als het gaat om werken op een informatieobject, is `Access` meestal passender dan `Association`.

Voorbeeld:

- `Ondersteunen van kennisbeheer` werkt op `Kennisartikel`.

### 6.5 Specialization

**Betekenis**: een element is een specifiekere variant van een ander element.

Gebruik:

- specifieke beheerfunctie als deeltype van een generieke functie;
- gespecialiseerd objecttype onder een generiek objecttype.

Vuistregel:

- Gebruik dit alleen als de subtype-relatie inhoudelijk echt klopt, niet alleen omdat iets gerelateerd is.

### 6.6 Association

**Betekenis**: er is een relatie, maar het type is inhoudelijk niet verder gespecificeerd.

Gebruik:

- alleen als specifieker modelleren nu niet kan of niet nodig is.

LLM-regel:

- `Association` is de fallback, niet de standaardkeuze.

### 6.7 Composition en Aggregation

| Relatie | Gebruik |
|---|---|
| Composition | Sterke deel-geheelrelatie; onderdeel hoort structureel bij het geheel |
| Aggregation | Lossere bundeling; onderdeel kan zelfstandiger bestaan |

### 6.8 Flow

**Betekenis**: overdracht of stroom van informatie, materiaal of waarde.

Gebruik in deze repo:

- gegevensstromen tussen XXLLNC, canoniek model, Open Zaak en reconciliation-service.

---

## 7. Praktische interpretatieregels voor LLM's

### 7.1 Service versus realisatie

- Als een service een component **bedient**, gebruik dan `Serving` van service naar component.
- Als een component die service **implementeert**, gebruik dan `Realization` van component naar service.

### 7.2 Gedrag op informatieobjecten

- Als een proces of service werkt op een object, kies eerst `Access`.
- Kies alleen `Association` als niet duidelijk is of het om lezen, schrijven of gebruiken gaat.

### 7.3 Business process versus application service

- `Business process` beschrijft werkstappen of organisatorisch handelen.
- `Application service` beschrijft wat de applicatie aanbiedt aan haar omgeving.

### 7.4 Business object versus data object

- Als de nadruk ligt op gemeentelijke betekenis of bedrijfsbegrip, kies `Business object`.
- Als de nadruk ligt op applicatieve gegevensstructuur of systeemgebruik, kies `Data object`.

### 7.5 Interface versus service

- Een interface is het toegangspunt.
- Een service is de aangeboden functionaliteit.

---

## 8. Repo-specifieke voorbeelden

| Casus | Leerpunt |
|---|---|
| Kennisbank huidig | `Ontsluiten van kennis` bedient `KISS`; `Strapi` realiseert de service |
| Kennisbank doel | onderscheid tussen service, component en data object moet expliciet blijven |
| Open Product doel | een API-interface is niet hetzelfde als de component die haar implementeert |
| ARA Patroon B2 | contextview, informatieflowview, applicatieview en roadmapview vragen elk een andere selectie van elementtypen en relaties |

---

## 9. Koppeling met GGM, GEMMA en Common Ground

- **GGM** helpt bij semantische verankering van data-objecten;
- **GEMMA** helpt bij referentiearchitectuur en positionering van gemeentelijke functies en componenten;
- **Common Ground** helpt bij lagenpositionering en scheiding van proces, connectiviteit, diensten en data.

ArchiMate vervangt deze kaders niet, maar biedt een taal om ze consistent samen te beschrijven.

---

## 10. Gebruik in agentinjectie

Gebruik deze samenvatting nooit volledig in elke prompt. Selecteer alleen:

- relevante viewpointregels;
- relevante elementen;
- relevante relaties;
- één of twee repo-voorbeelden.

Bij taken over viewinterpretatie zijn de belangrijkste regels meestal:

1. bepaal eerst het viewpoint;
2. bepaal daarna of een relatie `Serving`, `Realization`, `Assignment` of `Access` is;
3. gebruik `Association` alleen als fallback;
4. koppel informatieobjecten waar mogelijk aan GGM of een expliciet werkmodel.
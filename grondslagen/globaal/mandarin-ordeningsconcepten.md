# Mandarin **ordenings-concepten**

**Type**: Concepten en Definities  
**Repository**: mandarin-canon  
**Identifier**: mandarin-canon.concepten.meta  
**Version**: 1.5.0  
**Status**: Active  
**Last Updated**: 2026-02-01  
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
- [Artefactclassificatie](#artefactclassificatie) — Indeling van Mandarin-artefacten

### mandarin-agent-classificatie Assen
- [Inhoudelijke as](#inhoudelijke-as) — Effect op betekenis
- [Inzet-as](#inzet-as) — Context van gebruik
- [Vorm-as](#vorm-as) — Betekenis of representatie
- [Werkingsas](#werkingsas) — Inhoud of voorwaarden

### Artefacten
- [Mandarin-artefact](#mandarin-artefact) — Expliciet vastgelegd, overdraagbaar resultaat
- [Normerend artefact](#normerend-artefact) — Artefact dat normen en regels vastlegt
  - [Governance-artefact](#governance-artefact) — Specialisatie: governance in ecosysteem (value stream 0)
  - [Richtinggevend artefact](#richtinggevend-artefact) — Specialisatie: normerende richting in waarde value streams (1-n)
- [Realiserend artefact](#realiserend-artefact) — Artefact dat gedrag of structuur in systemen realiseert
- [Afgeleid artefact](#afgeleid-artefact) — Artefact dat is afgeleid uit andere artefacten
- [Beschrijvend artefact](#beschrijvend-artefact) — Artefact dat inzicht en uitleg biedt
- [Documenterend artefact](#documenterend-artefact) — Artefact dat documenteert (inclusief modellen)
- [Representatievorm](#representatievorm) — Vorm waarin betekenis wordt uitgedrukt
- [Representatie](#representatie) — Concrete uitdrukking van betekenis
- [Representatiestatus](#representatiestatus) — Bron of afgeleid in de keten

---

## mandarin-agent-classificatie

### Definitie 📝
mandarin-agent-classificatie is het expliciet positioneren van een **mandarin-agent** langs een vast stelsel van orthogonale assen, waarmee wordt vastgelegd wat het effect van de **mandarin-agent** is, waarop hij intervenieert, in welke context hij inzetbaar is en hoe hij handelt.

### Kenmerken ⭐
- Is geen enkelvoudig label en geen hiërarchie
- Een **mandarin-agent** is niet "een soort", maar neemt posities in op meerdere assen
- Elke as beschrijft een fundamenteel ander architectonisch aspect van de **mandarin-agent**
- Samen maken deze posities het gedrag, de bevoegdheid en de beperkingen van een **mandarin-agent** uitlegbaar, toetsbaar en overdraagbaar
- Bestaat uit 4 orthogonale assen:
  1. **Inhoudelijke as** — effect op betekenis
  2. **Inzet-as** — context van gebruik
  3. **Vorm-as** — betekenis of representatie
  4. **Werkingsas** — inhoud of voorwaarden

### Wat het niet is ❌
- Geen enkelvoudig label (zoals "adviserende **mandarin-agent**" of "uitvoerende **mandarin-agent**")
- Geen hiërarchische structuur
- Geen technische implementatie-eigenschap
- Geen tijdelijke classificatie

### Voorbeelden 💡
- Een **mandarin-agent** kan beschrijvend zijn (inhoudelijke as), value-stream-specifiek (inzet-as), vormvast (vorm-as) en inhoudelijk (werkingsas)
- Een **mandarin-agent** kan structuur-normerend, value-stream-specifiek, vormvast en inhoudelijk zijn
- Een **mandarin-agent** kan conditioneel zijn (werkingsas), value-stream-overstijgend (inzet-as)

### Synoniemen 🏷️
- **mandarin-agent**-positionering
- Multi-dimensionale **mandarin-agent**-classificatie

### Analogieën 🔄
- Vergelijkbaar met multi-dimensionale classificatie in taxonomie
- In softwareontwikkeling: orthogonale concerns (zoals in aspect-oriented programming)
- In enterprise architectuur: capability matrix met meerdere dimensies

### Toelichting 💬
mandarin-agent-classificatie vervangt het concept "**mandarin-agent**-soort" door een meer genuanceerd stelsel van orthogonale assen. Dit maakt het mogelijk om **mandarin-agents** preciezer te positioneren en te begrijpen. Elke **mandarin-agent** heeft op elke as een expliciete positie, en deze posities bepalen samen het gedrag, de bevoegdheden en de beperkingen van de **mandarin-agent**.


---
## Inhoudelijke as

### Definitie 📝
De **inhoudelijke as** is een classificatie-as binnen mandarin-agent-classificatie die het effect van een **mandarin-agent** op de betekenis van het werk beschrijft.

**Leidende vraag:** *Wat is het effect van deze **mandarin-agent** op de betekenis van het werk?*

### Kenmerken ⭐
- Is één van vier orthogonale assen voor mandarin-agent-classificatie
- Onderscheidt **mandarin-agents** op basis van hun effect op betekenis
- Vijf categorieën: Beschrijvend, Structuurrealiserend, Structuur-normerend, Curator, Ecosysteem-normerend
- Onafhankelijk van andere assen (Inzet, Vorm, Werkingsas)
- Bepaalt fundamentele rol en impact van de **mandarin-agent**

### Wat het niet is ❌
- Geen technische implementatievariant
- Geen organisatorische indeling
- Geen enkelvoudig label

### Categorieën 💫

**1. Beschrijvende **mandarin-agents** (achteraf)**
- Vastleggen, uitleggen en documenteren wat er is of was
- Achteraf: beschrijven bestaande werkelijkheid
- Wijzigen geen artefacten
- Voorbeelden: Verslagen, Overzichten, Uitlegdocumentatie

**2. Structuurrealiserende **mandarin-agents****
- Maken impliciete samenhang, relaties en consistentie expliciet
- Impliciet → expliciet
- Realiseren modellen, relaties, nummering
- Geen richting, geen besluit
- Voorbeelden: Logisch datamodel-**mandarin-agent**, Nummerende **mandarin-agent**

**3. Structuur-normerende **mandarin-agents** (vooraf)**
- Normeren vooraf de structuur en indeling van toekomstig werk
- Beschrijven vooruit
- Normeren *wat als werk bestaat*
- Value-stream-gebonden
- Geen uitvoering, geen ecosysteemregels
- Voorbeelden: Thema-vormende **mandarin-agents**, Feature-beschrijvende **mandarin-agents**

**4. Curator-mandarin-agents**
- Beschrijvende **mandarin-agents** die expliciet oordeel of duiding vastleggen
- Maken overzichten
- Beoordelen kwaliteit, samenhang en risico's
- Leggen oordeel vast, geen besluit
- Escaleren i.p.v. corrigeren
- Voorbeelden: Review-mandarin-agents, Samenhangbeoordeling

**5. Ecosysteem-normerende **mandarin-agents****
- Vaststellen of wijzigen van regels, kaders en constituerende afspraken van het **mandarin-agent**-ecosysteem
- Meta-niveau
- Zeldzaam en zwaar
- Workspace- en value-stream-overstijgend
- Bepalen *hoe het systeem mag bestaan*
- Voorbeelden: Constitutie-**mandarin-agents**, Doctrine-**mandarin-agents**, Charter-**mandarin-agents**

### Synoniemen 🏷️
- Effect-as
- Betekenis-as

### Analogieën 🔄
- Vergelijkbaar met prescriptive vs descriptive vs evaluative in informatiekunde
- In softwareontwikkeling: read vs write vs validate operaties

### Toelichting 💬
De **inhoudelijke as** is de primaire as voor mandarin-agent-classificatie omdat deze de fundamentele rol en impact van een **mandarin-agent** op betekenis bepaalt. Het onderscheid tussen structuur-normering (werk) en ecosysteem-normering (spelregels) is cruciaal.

---
## Inzet-as

### Definitie 📝
De **inzet-as** is een classificatie-as binnen mandarin-agent-classificatie die de context van gebruik van een **mandarin-agent** beschrijft.

**Leidende vraag:** *Waar mag deze **mandarin-agent** worden ingezet?*

### Kenmerken ⭐
- Is één van vier orthogonale assen voor mandarin-agent-classificatie
- Onderscheidt **mandarin-agents** op basis van inzetbaarheid
- Twee categorieën: Value-stream-specifiek, Value-stream-overstijgend
- Onafhankelijk van andere assen (Inhoudelijke as, Vorm, Werkingsas)
- Bepaalt waar en wanneer een **mandarin-agent** kan worden ingezet

### Wat het niet is ❌
- Geen kwaliteitsmaatstaf
- Geen indicatie van waarde of belang
- Geen hiërarchische indeling

### Categorieën 💫

**1. Value-stream-specifiek**
- Inzetbaar binnen één value stream
- Vaak fase-gebonden
- Leest en begrijpt context van die value stream

**2. Value-stream-overstijgend**
- Inzetbaar in meerdere value streams
- Leest context maar bepaalt die niet
- Generiek inzetbaar

### Synoniemen 🏷️
- Inzetbaarheids-as
- Context-as

### Analogieën 🔄
- Vergelijkbaar met bounded vs shared services in enterprise architectuur
- In softwareontwikkeling: domain-specific vs cross-cutting concerns

### Toelichting 💬
De **inzet-as** bepaalt of een **mandarin-agent** specifiek voor één value stream werkt of generiek inzetbaar is over meerdere value streams.

---
## Vorm-as

### Definitie 📝
De **vorm-as** is een classificatie-as binnen mandarin-agent-classificatie die beschrijft of een **mandarin-agent** werkt op betekenis of alleen op representatie.

**Leidende vraag:** *Werkt deze **mandarin-agent** op betekenis, of alleen op vorm?*

### Kenmerken ⭐
- Is één van vier orthogonale assen voor mandarin-agent-classificatie
- Onderscheidt **mandarin-agents** op basis van begrip van betekenis
- Twee categorieën: Vormvast, Representatieomvormend
- Onafhankelijk van andere assen (Inhoudelijke as, Inzet, Werkingsas)
- Bepaalt of **mandarin-agent** betekenis begrijpt

### Wat het niet is ❌
- Geen kwaliteitsmaatstaf
- Geen indicatie van complexiteit
- Geen technische implementatie-eigenschap

### Categorieën 💫

**1. Vormvast**
- Output is betekenisdragend
- Kan inhoudelijk beoordeeld worden
- Begrijpt betekenis van het werk

**2. Representatieomvormend**
- Zet inhoud om van de ene representatie naar de andere
- Betekenis-blind
- Infrastructuurachtig
- Vormtransformatie (bijv. Markdown → XML → diagram)

### Synoniemen 🏷️
- Representatie-as
- Betekenisbegrip-as

### Analogieën 🔄
- Vergelijkbaar met semantic vs syntactic transformations
- In enterprise architectuur: content vs format converters

### Toelichting 💬
De **vorm-as** maakt onderscheid tussen **mandarin-agents** die betekenis begrijpen en **mandarin-agents** die alleen vorm transformeren. Dit onderscheid is belangrijk voor tooling-onafhankelijkheid.

---
## Werkingsas

### Definitie 📝
De **werkingsas** is een classificatie-as binnen mandarin-agent-classificatie die beschrijft of een **mandarin-agent** intervenieert in de inhoud of in de voorwaarden waaronder inhoudelijk werk kan plaatsvinden.

**Leidende vraag:** *Intervenieert deze **mandarin-agent** in de inhoud, of in de voorwaarden waaronder inhoudelijk werk kan plaatsvinden?*

### Kenmerken ⭐
- Is één van vier orthogonale assen voor mandarin-agent-classificatie
- Onderscheidt **mandarin-agents** op basis van interventiegebied
- Twee categorieën: Inhoudelijk, Conditioneel
- Onafhankelijk van andere assen (Inhoudelijke as, Inzet, Vorm)
- Bepaalt of **mandarin-agent** op inhoud of op voorwaarden werkt

### Wat het niet is ❌
- Geen kwaliteitsmaatstaf
- Geen hiërarchische indeling
- Geen technische eigenschap

### Categorieën 💫

**1. Inhoudelijke **mandarin-agents****
- Werken direct op betekenisvolle artefacten
- Omvat alle categorieën van de inhoudelijke as:
  - Beschrijvende **mandarin-agents**
  - Structuurrealiserende **mandarin-agents**
  - Structuur-normerende **mandarin-agents**
  - Curator-**mandarin-agents**
  - Ecosysteem-normerende **mandarin-agents**

**2. Conditionele **mandarin-agents****
- Werken niet op inhoud, maar op voorwaarden en hygiëne
- Geen betekenis
- Geen value-stream-artefacten
- Bewaken randvoorwaarden
- Subtypen:
  - **Workspace Steward** — structuur, beleid, scope, mappen, gitignore
  - **Engineering Steward** — codekwaliteit, veiligheid, onderhoudbaarheid

### Synoniemen 🏷️
- Interventie-as
- Werkgebied-as

### Analogieën 🔄
- Vergelijkbaar met business logic vs infrastructure in softwareontwikkeling
- In enterprise architectuur: content vs governance layers

### Toelichting 💬
De **werkingsas** maakt cruciaal onderscheid tussen **mandarin-agents** die inhoud beïnvloeden en **mandarin-agents** die de voorwaarden voor inhoudelijk werk bewaken. Conditionele **mandarin-agents** zijn essentieel maar werken op een ander niveau.

---
## Artefactclassificatie

### Definitie 📝
**Artefactclassificatie** is het expliciet ordenen en positioneren van **Mandarin-artefacten** langs een samenhangende set van artefact-typen, zodat helder is welk artefact normen vastlegt, welke artefacten waarde vertegenwoordigen, welke artefacten beschrijven en welke artefacten documenteren.

### Kenmerken ⭐
- Biedt een consistent classificatiekader voor alle Mandarin-artefacten
- Onderscheidt drie hoofdklassen: **normerende artefacten**, **beschrijvende artefacten** en **documenterende artefacten**
- Maakt binnen **normerende artefacten** onderscheid tussen **governance-artefacten** en **richtinggevende artefacten**
- Is tooling-onafhankelijk: de classificatie verandert niet door formaat of implementatie
- Verbindt artefacten expliciet met hun rol in value streams en in het ecosysteem
- Maakt duidelijk welke artefacten primair zijn (niet-afgeleid) en welke artefacten afgeleid of ondersteunend zijn

### Wat het niet is ❌
- Geen lijst van bestandsformaten of tooling-keuzes
- Geen hiërarchie van belangrijkheid of waarde
- Geen procesindeling of fasering van werk
- Geen technische classificatie (bijvoorbeeld op basis van repository of folderstructuur)

### Voorbeelden 💡
- Een **doctrine** of **constitutie** wordt geclassificeerd als **normerend artefact** (deze zijn ecosysteemgericht; van toepassing is de specialisatie **governance-artefact**)
- Een requirements-specificatie of thema-beschrijving wordt geclassificeerd als **richtinggevende-artefacten** (normerend binnen een waarde value stream)
- Een **architectuurvisie**, **ArchiMate-model** of **analyse-rapport** wordt geclassificeerd als **beschrijvend artefact**
- Een **handleiding**, README, een mandarin-agent-overzicht, of **API-documentatie** wordt geclassificeerd als **documenterend artefact**

### Synoniemen 🏷️
- Artefact-positionering
- Artefact-typenindeling

### Analogieën 🔄
- Vergelijkbaar met de indeling in policy / process / record in informatiebeheer
- In softwareontwikkeling: onderscheid tussen source artefacts, design docs en generated documentation

### Toelichting 💬
**Artefactclassificatie** vormt de meta-laag boven op de concrete definities van **Mandarin-artefact**, **normerend artefact**, **governance-artefact**, **richtinggevend artefact**, **beschrijvend artefact**, **realiserend-artefact**,  en **documenterend artefact**. Zij legt vast *hoe* deze artefact-typen zich tot elkaar verhouden en welke rol zij spelen in het Mandarin-ecosysteem.

Door deze classificatie wordt helder:
- welke artefacten bindend en prescriptief zijn (normerend, met governance- en richtinggevende artefacten als specialisaties),
- welke artefacten uitleg en inzicht bieden (beschrijvend), en
- welke artefacten duurzame documentatie en modellen leveren (documenterend).

Dit maakt het mogelijk om werk, governance en documentatie scherp van elkaar te scheiden, tooling verwisselbaar te houden en de betekenis van elk artefact type vast en toetsbaar te maken.

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
- Zie: **waarde-artefacten** en **governance-artefacten**

### Synoniemen 🏷️
- **Artefact**

### Analogieën 🔄
- Vergelijkbaar met een **artefact** in softwareontwikkeling (build-artifact, document)
- In projectmanagement: **deliverable**
- In DDD: **Aggregate Result** of **Documented Outcome**

### Toelichting 💬
Er zijn drie hoofdklassen van **Mandarin-artefacten**:
1. **Normerende artefacten** — leggen normen en regels vast, operationeel in maximaal één value stream fase
   - **Governance-artefacten** (specialisatie) — ontstaan in value stream "**mandarin-agent** Ecosysteem Ontwikkeling"
  - **Richtinggevende artefacten** (specialisatie) — ontstaan in waarde value streams (1-n)
2. **Beschrijvende artefacten** — bieden inzicht en uitleg
3. **Documenterende artefacten** — documenteren (inclusief modellen)

Deze indeling scheidt **betekenis van vorm**, maakt tooling verwisselbaar, houdt governance scherp en klein, en erkent modellen als uitleg (niet als waarheid).

---

## Normerend artefact

### Definitie 📝
Een **normerend artefact** is een **Mandarin-artefact** dat expliciete normen, regels, principes of standaarden vastlegt die bindend zijn voor het **Mandarin-ecosysteem** of een specifiek domein, en dat operationeel is in maximaal één **value stream fase**.

**Specialisaties**:
- **Governance-artefact** — normerend artefact voor het ecosysteem, ontstaat in value stream "mandarin-agent Ecosysteem Ontwikkeling"
- **Richtinggevend artefact** — normerend artefact uit waarde value streams (1-n)

### Kenmerken ⭐
- Legt bindende normen, regels of principes vast
- Is prescriptief (schrijft voor wat moet)
- Is leidend voor ontwerp, implementatie en evaluatie
- Vormt de hoogste autoriteit binnen zijn scope
- Is versieerbaar en traceerbaar
- Wordt niet afgeleid uit andere artefacten
- **Is operationeel in maximaal één value stream fase**
- Heeft twee specialisaties: governance-artefact en richtinggevend artefact

### Wat het niet is ❌
- Geen beschrijving van huidige situatie
- Geen advies of aanbeveling
- Geen implementatie of uitvoering
- Geen documentatie of uitleg

### Voorbeelden 💡
- Constitutie
- Doctrines
- Beleid
- Architectuurprincipes
- Standaarden en richtlijnen

### Synoniemen 🏷️
- Normatief artefact
- Prescriptief artefact
- Regel-artefact

### Analogieën 🔄
- Vergelijkbaar met wetgeving, standaarden (zoals ISO), policies
- In enterprise architectuur: principles, standards, guidelines
- In softwareontwikkeling: coding standards, architectural decision records (bindende variant)

### Toelichting 💬
**Normerende artefacten** hebben de hoogste autoriteit en zijn bindend. Zij vormen het fundament waarop alle andere artefacten voortbouwen. Normerende artefacten zijn primair (niet afgeleid) en stabiel in de tijd.

---

## Governance-artefact

### Definitie 📝
Een **governance-artefact** is een specialisatie van een **normerend artefact** dat het functioneren, de besturing en de continuïteit van het **Mandarin-ecosysteem** mogelijk maakt. Governance-artefacten worden **alleen en alleen** aangemaakt in de value stream "mandarin-agent Ecosysteem Ontwikkeling"**.

### Kenmerken ⭐
- Is een **specialisatie van normerend artefact**
- Ontstaat uitsluitend in value stream "**mandarin-agent** Ecosysteem Ontwikkeling" (value stream 0)
- Maakt governance en besturing van het ecosysteem mogelijk
- Is operationeel en faciliterend voor het ecosysteem
- Is normerend voor het ecosysteem zelf
- Is randvoorwaardelijk voor alle andere value streams
- Levert geen directe waarde in waarde value streams (1-n)
- Erft alle kenmerken van normerend artefact (bindend, prescriptief, versieerbaar)

### Wat het niet is ❌
- Geen algemeen normerend artefact (is specifiek voor ecosysteem-governance)
- Geen bedrijfs-artefact (ontstaat niet in waarde value streams)
- Geen beschrijvend of documenterend artefact
- Geen artefact buiten value stream "**mandarin-agent** Ecosysteem Ontwikkeling"

### Voorbeelden 💡
- **agent-charter**
- **agent-contract** 
- Prompt (.prompt.md)
- Templates
- Workspace-state
- Handoff-documenten

### Synoniemen 🏷️
- Systeem-artefact
- Ecosysteem-artefact
- Faciliterend artefact

### Analogieën 🔄
- Vergelijkbaar met **API contracts**, **infrastructuurdefinities**, **configuration files** in DevOps
- In SOA: **WSDL's**, **service agreements**, **orchestration definitions**
- In projectmanagement: **charter**, **governance framework**

### Toelichting 💬
**Governance-artefacten** zijn normerend voor het ecosysteem en ontstaan uitsluitend in value stream "**mandarin-agent** Ecosysteem Ontwikkeling". Zij maken het mogelijk dat **mandarin-agents**, workspaces en value streams gecontroleerd en consistent kunnen functioneren. Als specialisatie van normerend artefact zijn governance-artefacten bindend en prescriptief, en operationeel in specifieke fasen (Grondslagvorming of Ecosysteeminrichting) van value stream 0.

---

## Richtinggevend artefact

### Definitie 📝
Een **richtinggevend artefact** (synoniem: **value-stream-artefact**) is een specialisatie van een **normerend artefact** dat expliciet de gewenste inhoud, structuur of randvoorwaarden van een **value stream fase** in een **waarde value stream** (value streams 1-n) vastlegt en daarmee richting geeft aan realisatie en verdere uitwerking.

### Kenmerken ⭐
- Is een **specialisatie van normerend artefact**
- Ontstaat binnen een value stream fase in waarde value streams (value streams 1-n, niet in value stream 0)
- Vertegenwoordigt inhoudelijke keuzes, richting en gewenste resultaten
- Is input voor volgende fasen en voor realiserende artefacten
- Wordt geleverd door uitvoerende **mandarin-agents** met inhoudelijke verantwoordelijkheid
- Is primair artefact (niet afgeleid uit andere artefacten)
- Erft alle kenmerken van normerend artefact (bindend, prescriptief, versieerbaar, operationeel in maximaal één value stream fase)

### Wat het niet is ❌
- Geen algemeen normerend artefact (is specifiek voor waarde value streams)
- Geen governance-artefact (ontstaat niet in value stream "**mandarin-agent** Ecosysteem Ontwikkeling")
- Geen realiserend artefact (legt niet de feitelijke implementatie vast)
- Geen afgeleid artefact (is niet primair afgeleid uit andere artefacten)
- Geen interne notitie

### Voorbeelden 💡
- Requirements en specifieke eisenpakketten
- Ontwerpdocumenten en solution outlines
- Logische datamodellen (primair, richtinggevend)
- Richtlijnen voor API-contracten of berichtenstructuren

### Synoniemen 🏷️
- Value-stream-artefact
- Waarde-artefact
- Richtinggevend normatief artefact

### Analogieën 🔄
- Vergelijkbaar met business requirements, solution outlines, logical data models
- In DDD: ontwerp- en specificatie-artefacten die implementatie sturen

### Toelichting 💬
**Richtinggevende artefacten** leggen vast wat er inhoudelijk moet gelden in een waarde value stream (1-n), zonder te bepalen *hoe* dit technisch precies wordt gerealiseerd. Zij sturen daarmee de creatie van **realiserende artefacten** (zoals code en DDL) en vormen het primaire, normerende referentiepunt voor afgeleide modellen en documentatie.

---

## Realiserend artefact

### Definitie 📝
Een **realiserend artefact** is een **Mandarin-artefact** dat direct gedrag, structuur of configuratie in een werkend systeem realiseert op basis van richtinggevende artefacten.

### Kenmerken ⭐
- Is uitvoerbaar, interpreteerbaar of direct toepasbaar door tooling of runtime-omgevingen
- Realiseert beslissingen en structuren die eerder in richtinggevende artefacten zijn vastgelegd
- Is meestal niet zelf normerend, maar volgt normerende artefacten
- Wijzigingen hebben direct effect op systeemgedrag of data
- Kan gegenereerd zijn uit andere artefacten of handmatig gemaakt

### Wat het niet is ❌
- Geen richtinggevend artefact (legt geen norm of intentie vast)
- Geen puur beschrijvend of documenterend artefact
- Geen afgeleid artefact dat alleen structuur uitlegt zonder iets te realiseren

### Voorbeelden 💡
- PostgreSQL- of andere database-DDL (CREATE TABLE, CONSTRAINTS, etc.)
- Angular‑ of andere frontend/backend‑code die functionaliteit realiseert
- Scripts om een database initieel te vullen met data (seed-scripts)
- Infrastructuur-als-code bestanden (bijv. Terraform, Ansible, Kubernetes manifests)

### Synoniemen 🏷️
- Implementatie-artefact
- Uitvoerbaar artefact

### Analogieën 🔄
- In softwareontwikkeling: gecompileerde of interpreteerbare artefacten die in productie draaien
- In DevOps: deployment- en configuratiebestanden die gedrag bepalen

### Toelichting 💬
**Realiserende artefacten** vormen de brug tussen richtinggevende artefacten en het werkende systeem. Zij maken de bedoelde structuur en het gewenste gedrag feitelijk waar in code, data en configuratie.


---

## Beschrijvend artefact

### Definitie 📝
Een **beschrijvend artefact** is een **Mandarin-artefact** dat inzicht, uitleg of overzicht biedt over bestaande structuren, besluiten of situaties, zonder zelf normerend, governerend of waardevol in een value stream fase te zijn.

### Kenmerken ⭐
- Biedt inzicht en uitleg
- Is descriptief (beschrijft wat is)
- Is niet bindend of prescriptief
- Kan afgeleid zijn uit andere artefacten
- Ondersteunt begripsvorming en communicatie

### Wat het niet is ❌
- Geen normerend artefact (schrijft niets voor)
- Geen governance-artefact (maakt geen besturing mogelijk)
- Geen richtinggevend artefact (geen normerend output van value stream fase)
- Geen formele documentatie

### Voorbeelden 💡
- Overzichtsdocumenten
- Analyse-rapporten
- Conceptuele modellen (ter uitleg)
- Architectuurvisies
- Rationale-documenten (waarom-uitleg)
- Kennisbankartikelen

### Synoniemen 🏷️
- Descriptief artefact
- Uitleg-artefact
- Inzicht-artefact

### Analogieën 🔄
- Vergelijkbaar met white papers, explanatory documents, vision documents
- In enterprise architectuur: viewpoints, perspectives
- In softwareontwikkeling: architectural decision records (beschrijvende variant), design rationale

### Toelichting 💬
**Beschrijvende artefacten** helpen mensen het ecosysteem te begrijpen. Zij zijn vaak afgeleid uit normerende, governance- of richtinggevende artefacten. Beschrijvende artefacten zijn ondersteunend en niet bindend.

---

## Documenterend artefact

### Definitie 📝
Een **documenterend artefact** is een **Mandarin-artefact** dat kennis, structuren of besluiten vastlegt in een formele, toegankelijke vorm (inclusief model-gebaseerde beschrijvingen zoals ArchiMate), bedoeld voor duurzame raadpleegbaarheid en kennisoverdracht.

### Kenmerken ⭐
- Legt kennis en structuren formeel vast
- Bedoeld voor duurzame raadpleegbaarheid
- Kan model-gebaseerd zijn (bijv. ArchiMate, UML)
- Kan afgeleid of gegenereerd zijn uit andere artefacten
- Ondersteunt kennisoverdracht en onderhoud

### Wat het niet is ❌
- Geen normerend artefact (legt geen regels vast)
- Geen governance-artefact (maakt geen besturing mogelijk)
- Geen richtinggevend artefact (geen normerend output van value stream fase)
- Geen informele notitie of tijdelijk document

### Voorbeelden 💡
- Technische documentatie
- Gebruikershandleidingen
- ArchiMate-modellen (documenterende variant)
- UML-diagrammen (documenterende variant)
- API-documentatie (gegenereerd)
- Release notes
- Geëxporteerde visualisaties

### Synoniemen 🏷️
- Documentatie-artefact
- Formeel document
- Model-artefact (als het model documenteert)

### Analogieën 🔄
- Vergelijkbaar met technical documentation, reference manuals, generated docs
- In enterprise architectuur: repository exports, model documentation
- In softwareontwikkeling: Javadoc, Swagger/OpenAPI specs, architecture diagrams

### Toelichting 💬
**Documenterende artefacten** maken kennis toegankelijk en duurzaam. Zij zijn vaak afgeleid of gegenereerd uit primaire artefacten. **Model-gebaseerde beschrijvingen** (zoals ArchiMate) worden gezien als documenterende artefacten: zij leggen structuur vast, maar zijn uitleg, niet waarheid. Deze indeling scheidt betekenis van vorm en maakt tooling verwisselbaar.

---

## Representatievorm

### Definitie 📝
Een **representatievorm** is de specifieke manier waarop een artefact of betekenis wordt vastgelegd, weergegeven of uitgewisseld, zonder de onderliggende betekenis zelf te bepalen.

### Toelichting 💬
Een **representatievorm** beschrijft *hoe* iets wordt uitgedrukt, niet *wat* het betekent.

Dezelfde inhoud kan in meerdere representatievormen bestaan, bijvoorbeeld:
- tekstueel
- gestructureerd
- visueel
- machine-leesbaar

Deze representaties zijn inhoudelijk equivalent, maar functioneel verschillend: zij dienen andere doelen en doelgroepen.

### Kenmerken ⭐
Een representatievorm:
- is afgeleid van een onderliggende betekenis of structuur
- heeft geen eigen normatieve kracht
- kan worden vertaald naar andere representatievormen
- is context- en doelafhankelijk (mens, machine, visualisatie)
- verandert niet de betekenis, alleen de toegankelijkheid of bruikbaarheid

### Wat het niet is ❌
- Geen artefact op zichzelf
- Geen normering of besluit
- Geen inhoudelijke structuur
- Geen model van de werkelijkheid

Een representatievorm draagt betekenis, maar bepaalt haar niet.

### Voorbeelden 💡
- Markdown, XML, JSON, YAML
- Diagram, visualisatie, schema
- Tabel, lijst, tekstuele beschrijving

In al deze gevallen blijft de onderliggende betekenis gelijk, terwijl de vorm verschilt.

---

## Representatie

### Definitie 📝
Een **representatie** is een concrete uitdrukking van een onderliggende betekenis, structuur of inhoud, vastgelegd in een specifieke representatievorm.

### Toelichting 💬
Een **representatie** is de manifestatie van iets dat betekenis heeft.
Zij maakt betekenis waarneembaar, deelbaar of verwerkbaar, maar is niet die betekenis zelf.

Dezelfde betekenis kan meerdere representaties hebben, bijvoorbeeld:

- een tekstuele beschrijving
- een model
- een schema
- een visualisatie

Elke representatie drukt dezelfde onderliggende inhoud uit, maar op een andere manier.

### Kenmerken ⭐
Een representatie:
- is afgeleid van betekenis, niet andersom
- bestaat altijd in een representatievorm
- is concreet en observeerbaar
- kan worden vertaald naar andere representaties
- kan verouderen of wijzigen zonder dat de betekenis verandert

### Wat het niet is ❌
- Niet de betekenis zelf
- Niet het besluit of de norm
- Niet per definitie het artefact
- Niet de waarheid, maar een uitdrukking daarvan

Een representatie toont betekenis, maar definieert haar niet.

### Relatie tussen betekenis, representatie en representatievorm 🔄

Canoniek onderscheid:

- **Betekenis** – datgene wat inhoudelijk geldt of bedoeld is
- **Representatie** – de concrete uitdrukking van die betekenis
- **Representatievorm** – de manier waarop die representatie is vastgelegd

In relatie:

> Betekenis → wordt uitgedrukt in → representatie → heeft een → representatievorm

### Voorbeelden 💡
- Een architectuurbesluit (betekenis)
  → vastgelegd als een ADR (representatie)
  → geschreven in Markdown (representatievorm)

- Een logisch datamodel (betekenis/structuur)
  → vastgelegd als een ER-diagram (representatie)
  → weergegeven als afbeelding of XML (representatievorm)

### Relatie tot **mandarin-agents** 🤝

**Inhoudelijke **mandarin-agents****
- Werken op betekenis en creëren of wijzigen representaties.

**Representatieomvormende **mandarin-agents****
- Werken uitsluitend op representaties en hun representatievormen, zonder begrip van betekenis.

Een representatieomvormende **mandarin-agent** verandert de uitdrukking, niet de inhoud.

### Canonieke zin (kort) 🧭

Een representatie is de concrete uitdrukking van betekenis; zij maakt betekenis zichtbaar zonder haar te bepalen.

---

## Representatiestatus

### Definitie 📝
**Representatiestatus** is het meta-concept dat vastlegt of een **representatie** geldt als bron van betekenis, dan wel is afgeleid van een andere representatie, zonder de onderliggende betekenis zelf te wijzigen.

De representatiestatus zegt niets over de inhoud, maar alles over de positie van een representatie in de keten van afleiding.

### Categorieën binnen representatiestatus 💫

#### 1. Bronrepresentatie

##### Definitie 📝
Een **bronrepresentatie** is een representatie die geldt als het primaire vastleggingspunt van betekenis binnen een context.

Dit is de representatie:
- waar betekenis formeel aan wordt ontleend
- die leidend is bij interpretatie
- die niet afhankelijk is van een andere representatie voor haar geldigheid

##### Kenmerken ⭐
Een bronrepresentatie:
- is autoritatief binnen haar domein of scope
- fungeert als referentie voor afgeleide representaties
- kan door mensen worden vastgesteld, beoordeeld of gewijzigd
- heeft wijzigingen die doorwerken naar afgeleiden
- is vaak expliciet aangewezen (door governance of afspraak)

##### Wat een bronrepresentatie niet is ❌
- Geen “eerste bestand” per se
- Geen technisch origineel
- Geen onveranderlijke waarheid

Een bronrepresentatie is leidend bij verschil van interpretatie, niet per definitie ouder of technischer.

---

## Change Log

| Datum      | Versie | Wijziging                                                           | Auteur     |
|------------|--------|---------------------------------------------------------------------|------------|
| 2026-02-01 | 1.5.0  | Bedrijfs-artefact hernoemd naar Richtinggevend artefact; toegevoegd: Realiserend artefact en Afgeleid artefact als aanvullende ordeningsconcepten | Constitutioneel Auteur  |
| 2026-02-01 | 1.4.0  | Toegevoegd: meta-concept Representatiestatus met categorie Bronrepresentatie | Constitutioneel Auteur  |
| 2026-02-01 | 1.3.0  | Toegevoegd: meta-concept Representatie als concrete uitdrukking van betekenis in een representatievorm | Constitutioneel Auteur  |
| 2026-02-01 | 1.2.0  | Toegevoegd: meta-concept Representatievorm als onderscheid tussen betekenis en vorm van artefacten | Constitutioneel Auteur  |
| 2026-02-01 | 1.1.0  | Toegevoegd: meta-concept Artefactclassificatie als ordeningskader voor Mandarin-artefacten en hun typen | Constitutioneel Auteur  |
| 2026-02-01 | 1.0.0  | Initiële versie — **ordenings-concepten** afgesplitst van concepten-en-architectonische-grondslagen.md v1.6.0; bevat classificatie-concepten (mandarin-agent-classificatie, As, 4 assen) en artefact-structuur (Mandarin-artefact met specialisaties) | Constitutioneel Auteur  |

---

**Einde document**

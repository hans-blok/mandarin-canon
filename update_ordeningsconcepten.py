import re
from pathlib import Path

file_path = Path(r'c:\git\mandarin-canon\grondslagen\.algemeen\mandarin-ordeningsconcepten.md')
content = file_path.read_text(encoding='utf-8')

# 1. Table at the top
content = content.replace(
    '| Vormingsfase \ Betekeniseffect | Duidend | Structurerend | Bindend | Beschrijvend |',
    '| Vormingsfase \ Betekeniseffect | Interpreterend | Structurerend | Vastleggend | Registrerend |'
)
content = content.replace(
    '| Verkenning                     | 🟢      | 🟢       | 🔴      | 🟢           |',
    '| Verkenning                     | 🟢             | 🟢            | 🔴          | 🟢           |'
)
content = content.replace(
    '| Ordening                       | 🟢      | 🟢       | 🔴      | 🟢           |',
    '| Ordening                       | 🟢             | 🟢            | 🔴          | 🟢           |'
)
content = content.replace(
    '| Vastlegging                    | 🔴      | 🟢       | 🟢      | 🔴           |',
    '| Vastlegging                    | 🔴             | 🟢            | 🟢          | 🔴           |'
)
content = content.replace(
    '| Toetsing                       | 🟢      | 🔴       | 🔴      | 🟢           |',
    '| Toetsing                       | 🟢             | 🔴            | 🔴          | 🟢           |'
)
content = content.replace(
    '| Verantwoording                 | 🔴      | 🔴       | 🔴      | 🟢           |',
    '| Verantwoording                 | 🔴             | 🔴            | 🔴          | 🟢           |'
)

# 2. Inhoudsopgave
content = content.replace(
    '- [Bindend artefact](#bindend-artefact) — Artefact dat normen, regels of direct uitvoerbaar gedrag vastlegt',
    '- [Vastleggend artefact](#vastleggend-artefact) — Artefact dat normen, regels of direct uitvoerbaar gedrag vastlegt'
)
content = content.replace(
    '- [Duidend artefact](#duidend-artefact) — Artefact dat betekenis, interpretatie of oordeel geeft',
    '- [Interpreterend artefact](#interpreterend-artefact) — Artefact dat betekenis, interpretatie of oordeel geeft'
)
content = content.replace(
    '- [Beschrijvend artefact](#beschrijvend-artefact) — Artefact dat inzicht en uitleg biedt',
    '- [Registrerend artefact](#registrerend-artefact) — Artefact dat inzicht en uitleg biedt'
)

# 3. Voorbeelden
content = content.replace(
    '- Een **mandarin-agent** kan beschrijvend zijn (betekeniseffect), in de beschrijven-fase acteren (vormingsfase), en inhoudelijk zijn (werking)',
    '- Een **mandarin-agent** kan registrerend zijn (betekeniseffect), in de beschrijven-fase acteren (vormingsfase), en inhoudelijk zijn (werking)'
)
content = content.replace(
    '- Een **mandarin-agent** kan bindend, in de vastleggings-fase, en inhoudelijk zijn',
    '- Een **mandarin-agent** kan vastleggend, in de vastleggings-fase, en inhoudelijk zijn'
)

# 4. Betekeniseffect Kenmerken
content = content.replace(
    '- Vijf categorieën: Geen betekenis (Nul-positie), Beschrijvend, Duidend, Structurerend, Bindend',
    '- Vijf categorieën: Geen betekenis (Nul-positie), Registrerend, Interpreterend, Structurerend, Vastleggend'
)

# 5. Categorieën section
old_categories = '''**1. Beschrijvend**
- Legt vast wat is
- Achteraf: beschrijven bestaande werkelijkheid
- Wijzigen geen bindende of structurerende artefacten
- Voorbeelden: Verslagen, Overzichten, Uitlegdocumentatie

**2. Duidend**
- Geeft betekenis, interpretatie of oordeel
- Beoordelen kwaliteit, samenhang en risico's
- Leggen oordeel vast, geen besluit
- Voorbeelden: Review-mandarin-agents, Samenhangbeoordeling

**3. Structurerend**
- Structureert intentie zonder die te fixeren
- Maken impliciete samenhang, relaties en architectuur expliciet
- Instantiëren een samenhangend architectuurmodel over lagen en aspecten binnen de gestelde kaders
- Voorbeelden: ArchiMate-modelleur, Domein-modelleur

**4. Bindend**
- Legt betekenis vast als geldend binnen de workspace
- Hebben uitvoerbare of door tooling direct interpreteerbare impact, of stellen harde kaders
- Bepalen *wat als werk bestaat* of *hoe het systeem mag bestaan*
- Voorbeelden: Programmacode, Gherkin-requirements, Logisch datamodel, Deployment-configurator'''

new_categories = '''**1. Interpreterend**
- **Definitie**: Geeft betekenis, interpretatie of oordeel aan bestaande structuren, voorstellen of resultaten.
- **Kenmerken**: Voegt duiding of beoordeling toe, is niet bindend, sluit interpretatie niet af.
- **Voorbeelden van rollen**: Architectuurbeoordelaar, Risico-analist, Hypotheseformuleerder, Samenhangduider, Kwaliteitsreviewer.

**2. Structurerend**
- **Definitie**: Structureert intentie en samenhang zonder deze bindend vast te leggen.
- **Kenmerken**: Maakt relaties expliciet, brengt ordening aan, laat interpretatie open.
- **Voorbeelden van rollen**: Themastructureerder, Backlog-architect, Domeinmodelleur (conceptueel), Capability-ontwerper, Procesontwerper (conceptueel).

**3. Vastleggend**
- **Definitie**: Legt betekenis vast als geldend binnen de workspace. Maakt interpretatie bindend.
- **Kenmerken**: Sluit interpretatie, creëert normerende of realiserende artefacten, heeft formele of uitvoerende status.
- **Voorbeelden van rollen**: Requirementspecificator, API-contractbeheerder, Datamodelbeheerder, Configuratiebeheerder, Architectuurprincipesteller.

**4. Registrerend**
- **Definitie**: Legt vast wat is, zonder interpretatie of normatieve toevoeging.
- **Kenmerken**: Geen oordeel, geen normering, geen wijziging van betekenis.
- **Voorbeelden van rollen**: Testrapporteur, Logboekbeheerder, Release-documentalist, Auditverslaglegger, API-documentatiegenerator.'''

content = content.replace(old_categories, new_categories)

# 6. Werking Categorieën
content = content.replace(
    '- Omvat alle categorieën van het betekeniseffect (Beschrijvend, Duidend, Structurerend, Bindend)',
    '- Omvat alle categorieën van het betekeniseffect (Registrerend, Interpreterend, Structurerend, Vastleggend)'
)

# 7. Vormingsfase Kenmerken
content = content.replace(
    '- Geldt voor alle inhoudelijke categorieën (beschrijvend, duidend, structurerend, bindend)',
    '- Geldt voor alle inhoudelijke categorieën (registrerend, interpreterend, structurerend, vastleggend)'
)

# 8. Vormingsfase Voorbeeldmatrix
old_matrix = '''|Betekenis effect        | Vormingsfase       | Voorbeeld                              |
|------------------------|--------------------|----------------------------------------|
| Duidend                | Verkenning         | Opstellen hypothese voor verandering   |
| Structurerend               | Verkenning         | Opstellen hypothese voor verandering   |
| Beschrijvend           | Verantwoording     | Vastleggen van systeemwerking          |
| Structurerend               | Ordening           | Modelleren van applicatie-view         |
| Bindend                | Vastlegging        | Schrijven code, opstellen Gherkin-requiremts voor automatisch testen   |
| Duidend                | Toetsing           | Beoordelen van codekwaliteit           |'''

new_matrix = '''|Betekenis effect        | Vormingsfase       | Voorbeeld                              |
|------------------------|--------------------|----------------------------------------|
| Interpreterend         | Verkenning         | Opstellen hypothese voor verandering   |
| Structurerend          | Verkenning         | Opstellen hypothese voor verandering   |
| Registrerend           | Verantwoording     | Vastleggen van systeemwerking          |
| Structurerend          | Ordening           | Modelleren van applicatie-view         |
| Vastleggend            | Vastlegging        | Schrijven code, opstellen Gherkin-requiremts voor automatisch testen   |
| Interpreterend         | Toetsing           | Beoordelen van codekwaliteit           |'''

content = content.replace(old_matrix, new_matrix)

# 9. Artefact-functie-as
content = content.replace(
    '**Leidende vraag:** *Welke bindende, structurerende, duidende of beschrijvende functie heeft dit artefact in de workspace?*',
    '**Leidende vraag:** *Welke vastleggende, structurerende, interpreterende of registrerende functie heeft dit artefact in de workspace?*'
)

# 10. Artefact-functie-as Posities
old_posities = '''**1. Bindend artefact**
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

**3. Duidend artefact**
- Geeft betekenis, interpretatie of oordeel
- Beoordeelt kwaliteit, samenhang en risico's
- Legt een oordeel vast, geen besluit
- Voorbeelden: review-rapporten, compliance-checks, kwaliteitsmetingen

**4. Beschrijvend artefact**
- Legt vast wat is
- Maakt bestaande of voorgenomen werkelijkheid inzichtelijk
- Legt analyse, structuur of samenhang vast zonder zelf bindend of structurerend te zijn
- Voorbeelden: modellen, analyses, overzichten, documentatie, handleidingen'''

new_posities = '''**1. Vastleggend artefact**
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
- Voorbeelden: modellen, analyses, overzichten, documentatie, handleidingen'''

content = content.replace(old_posities, new_posities)

# 11. Artefact-functie-as Voorbeelden
old_voorbeelden = '''### Voorbeelden
- Een **application-charter** of themabeschrijving staat als **richtinggevend artefact** (dus bindend binnen een specifieke workspace)
- Een ArchiMate-model of domeinmodel met coherente structuur staat als **structurerend artefact**
- Een logisch datamodel dat direct systeemgedrag bepaalt of programmacode staat als **bindend artefact**
- Een architectuurdiagram, analysemodel, API-referentie of gebruikershandleiding staat als **beschrijvend artefact**
- Een testrapport of review-bevinding staat als **duidend artefact**'''

new_voorbeelden = '''### Voorbeelden
- Een **application-charter** of themabeschrijving staat als **richtinggevend artefact** (dus vastleggend binnen een specifieke workspace)
- Een ArchiMate-model of domeinmodel met coherente structuur staat als **structurerend artefact**
- Een logisch datamodel dat direct systeemgedrag bepaalt of programmacode staat als **vastleggend artefact**
- Een architectuurdiagram, analysemodel, API-referentie of gebruikershandleiding staat als **registrerend artefact**
- Een testrapport of review-bevinding staat als **interpreterend artefact**'''

content = content.replace(old_voorbeelden, new_voorbeelden)

# 12. Artefact-functie-as Toelichting
old_toelichting = '''De **artefact-functie-as** maakt zichtbaar *wat* een artefact doet in de workspace: of het kaders schept en gedrag realiseert (bindend), structuur expliciteert (structurerend), oordeelt (duidend) of inzicht geeft en vastlegt (beschrijvend). Deze as werkt samen met de **representatie-as**: dezelfde functie kan in verschillende representaties bestaan zonder dat de positie op de **artefact-functie-as** verandert.

De posities op de **artefact-functie-as** corresponderen direct met de ordeningsconcepten **bindend artefact**, **structurerend artefact**, **duidend artefact** en **beschrijvend artefact**. **Artefactclassificatie** gebruikt deze as expliciet om artefacten te positioneren naar hun functie, los van vorm, tooling en proces.'''

new_toelichting = '''De **artefact-functie-as** maakt zichtbaar *wat* een artefact doet in de workspace: of het kaders schept en gedrag realiseert (vastleggend), structuur expliciteert (structurerend), oordeelt (interpreterend) of inzicht geeft en vastlegt (registrerend). Deze as werkt samen met de **representatie-as**: dezelfde functie kan in verschillende representaties bestaan zonder dat de positie op de **artefact-functie-as** verandert.

De posities op de **artefact-functie-as** corresponderen direct met de ordeningsconcepten **vastleggend artefact**, **structurerend artefact**, **interpreterend artefact** en **registrerend artefact**. **Artefactclassificatie** gebruikt deze as expliciet om artefacten te positioneren naar hun functie, los van vorm, tooling en proces.'''

content = content.replace(old_toelichting, new_toelichting)

# 13. Artefactclassificatie Definitie
content = content.replace(
    '- een **artefact-functie-as** (bindend, structurerend, duidend, beschrijvend), en',
    '- een **artefact-functie-as** (vastleggend, structurerend, interpreterend, registrerend), en'
)

# 14. Artefactclassificatie Kenmerken
content = content.replace(
    '- Gebruikt op de **artefact-functie-as** posities als: **bindend artefact** (met specialisatie **richtinggevend artefact**), **structurerend artefact**, **duidend artefact** en **beschrijvend artefact**',
    '- Gebruikt op de **artefact-functie-as** posities als: **vastleggend artefact** (met specialisatie **richtinggevend artefact**), **structurerend artefact**, **interpreterend artefact** en **registrerend artefact**'
)

# 15. Artefactclassificatie Voorbeelden
old_art_voorbeelden = '''### Voorbeelden
- Een requirements-specificatie of thema-beschrijving wordt geclassificeerd als **richtinggevend artefact** (bindend binnen een workspace), vaak tekstueel
- Een **ArchiMate-model** of domeinmodel met coherente architectuurstructuur wordt geclassificeerd als **structurerend artefact** in een diagram- of model-gebaseerde representatie
- Een logisch datamodel dat direct systeemgedrag realiseert of programmacode wordt geclassificeerd als **bindend artefact** in een programma code of machine taal representatie (bijv. DDL, model-XML)
- Een architectuurdiagram, ad-hoc analysemodel of gegenereerde documentatie wordt geclassificeerd als **beschrijvend artefact**, vaak met een afgeleide afleidingspositie
- Een testrapport of review-bevinding wordt geclassificeerd als **duidend artefact**'''

new_art_voorbeelden = '''### Voorbeelden
- Een requirements-specificatie of thema-beschrijving wordt geclassificeerd als **richtinggevend artefact** (vastleggend binnen een workspace), vaak tekstueel
- Een **ArchiMate-model** of domeinmodel met coherente architectuurstructuur wordt geclassificeerd als **structurerend artefact** in een diagram- of model-gebaseerde representatie
- Een logisch datamodel dat direct systeemgedrag realiseert of programmacode wordt geclassificeerd als **vastleggend artefact** in een programma code of machine taal representatie (bijv. DDL, model-XML)
- Een architectuurdiagram, ad-hoc analysemodel of gegenereerde documentatie wordt geclassificeerd als **registrerend artefact**, vaak met een afgeleide afleidingspositie
- Een testrapport of review-bevinding wordt geclassificeerd als **interpreterend artefact**'''

content = content.replace(old_art_voorbeelden, new_art_voorbeelden)

# 16. Artefactclassificatie Toelichting
old_art_toelichting = '''**Artefactclassificatie** vormt de meta-laag boven op de concrete definities van **Mandarin-artefact**, **bindend artefact**, **richtinggevend artefact**, **structurerend artefact**, **duidend artefact**, **beschrijvend artefact**, **representatie** en **afleidingspositie**. Zij legt vast *langs welke assen* artefacten worden geordend en welke posities op die assen canoniek zijn.

Samengevat:
- de **artefact-functie-as** positioneert artefacten op basis van hun functie binnen de workspace. Met deze functie krijgt het artefact betekenis.
- de **representatie-as** maakt zichtbaar *hoe* die betekenis wordt uitgedrukt (tekst, diagram, programma code, machine taal, â€¦).
- de **afleidingspositie** geeft aan of deze representatie de leidende bron is, of is afgeleid van een andere representatie.

Door deze classificatie wordt helder welke artefacten bindend en prescriptief zijn, welke artefacten structuur of inzicht bieden, en hoe al deze artefacten in verschillende representaties kunnen bestaan zonder dat hun rol verandert. Dit maakt het mogelijk om werk en governance scherp van elkaar te scheiden, tooling verwisselbaar te houden en de betekenis van elk artefacttype vast en toetsbaar te maken.'''

new_art_toelichting = '''**Artefactclassificatie** vormt de meta-laag boven op de concrete definities van **Mandarin-artefact**, **vastleggend artefact**, **richtinggevend artefact**, **structurerend artefact**, **interpreterend artefact**, **registrerend artefact**, **representatie** en **afleidingspositie**. Zij legt vast *langs welke assen* artefacten worden geordend en welke posities op die assen canoniek zijn.

Samengevat:
- de **artefact-functie-as** positioneert artefacten op basis van hun functie binnen de workspace. Met deze functie krijgt het artefact betekenis.
- de **representatie-as** maakt zichtbaar *hoe* die betekenis wordt uitgedrukt (tekst, diagram, programma code, machine taal, â€¦).
- de **afleidingspositie** geeft aan of deze representatie de leidende bron is, of is afgeleid van een andere representatie.

Door deze classificatie wordt helder welke artefacten vastleggend en prescriptief zijn, welke artefacten structuur of inzicht bieden, en hoe al deze artefacten in verschillende representaties kunnen bestaan zonder dat hun rol verandert. Dit maakt het mogelijk om werk en governance scherp van elkaar te scheiden, tooling verwisselbaar te houden en de betekenis van elk artefacttype vast en toetsbaar te maken.'''

content = content.replace(old_art_toelichting, new_art_toelichting)

# 17. Bindend artefact -> Vastleggend artefact
old_bindend = '''## Bindend artefact

### Definitie
Een **bindend artefact** is een **Mandarin-artefact** dat expliciete normen, regels, principes, standaarden of direct uitvoerbaar gedrag vastlegt die geldend zijn voor een specifiek domein binnen de workspace.

### Kenmerken
- Legt betekenis vast als geldend binnen de workspace
- Is prescriptief (schrijft voor wat moet) of direct uitvoerbaar
- Is leidend voor ontwerp, implementatie en evaluatie
- Vormt de hoogste autoriteit binnen zijn scope
- Is versieerbaar en traceerbaar
- Wordt niet afgeleid uit andere artefacten
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
- Realiserend artefact

### Analogieën 
- Vergelijkbaar met wetgeving, standaarden (zoals ISO), policies
- In enterprise architectuur: principles, standards, guidelines
- In softwareontwikkeling: coding standards, architectural decision records (bindende variant), source code, infrastructure-as-code

### Toelichting  
**Bindende artefacten** hebben de hoogste autoriteit en zijn geldend. Zij vormen het fundament waarop alle andere artefacten voortbouwen, of ze realiseren direct het gedrag van het systeem. Bindende artefacten zijn primair (niet afgeleid) en stabiel in de tijd.'''

new_bindend = '''## Vastleggend artefact

### Definitie
Een **vastleggend artefact** is een **Mandarin-artefact** dat expliciete normen, regels, principes, standaarden of direct uitvoerbaar gedrag vastlegt die geldend zijn voor een specifiek domein binnen de workspace.

### Kenmerken
- Legt betekenis vast als geldend binnen de workspace
- Is prescriptief (schrijft voor wat moet) of direct uitvoerbaar
- Is leidend voor ontwerp, implementatie en evaluatie
- Vormt de hoogste autoriteit binnen zijn scope
- Is versieerbaar en traceerbaar
- Wordt niet afgeleid uit andere artefacten
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
- Realiserend artefact
- Bindend artefact

### Analogieën 
- Vergelijkbaar met wetgeving, standaarden (zoals ISO), policies
- In enterprise architectuur: principles, standards, guidelines
- In softwareontwikkeling: coding standards, architectural decision records (vastleggende variant), source code, infrastructure-as-code

### Toelichting  
**Vastleggende artefacten** hebben de hoogste autoriteit en zijn geldend. Zij vormen het fundament waarop alle andere artefacten voortbouwen, of ze realiseren direct het gedrag van het systeem. Vastleggende artefacten zijn primair (niet afgeleid) en stabiel in de tijd.'''

content = content.replace(old_bindend, new_bindend)

# 18. Structurerend artefact
content = content.replace(
    'Zij verschillen van **beschrijvende artefacten** door hun focus op structurele coherentie en metamodel-conformiteit, en van **bindende artefacten** omdat zij structuur representeren maar niet direct uitvoeren of fixeren.',
    'Zij verschillen van **registrerende artefacten** door hun focus op structurele coherentie en metamodel-conformiteit, en van **vastleggende artefacten** omdat zij structuur representeren maar niet direct uitvoeren of fixeren.'
)

# 19. Duidend artefact -> Interpreterend artefact
old_duidend = '''## Duidend artefact

### Definitie
Een **duidend artefact** is een **Mandarin-artefact** dat betekenis, interpretatie of een oordeel geeft over andere artefacten of systemen.

### Kenmerken
- Beoordeelt kwaliteit, samenhang en risico's
- Legt een oordeel vast, geen besluit
- Is evaluatief van aard
- Kan gegenereerd zijn uit geautomatiseerde checks of handmatige reviews

### Wat het niet is
- Geen bindend artefact (legt geen norm of intentie vast)
- Geen puur beschrijvend artefact (het bevat een oordeel of interpretatie)
- Geen structurerend artefact

### Voorbeelden
- Formuleringshypothese voor een verandering
- Testrapporten
- Review-bevindingen
- Compliance-checks
- Kwaliteitsmetingen
- Security-audits

### Synoniemen
- Evaluerend artefact
- Beoordelings-artefact

### Analogieën 
- In softwareontwikkeling: test results, linting reports, code review comments
- In kwaliteitszorg: audit reports, inspectierapporten

### Toelichting  
**Duidende artefacten** vormen de feedbackloop binnen de workspace. Zij toetsen of de gerealiseerde of ontworpen artefacten voldoen aan de gestelde kaders en leveren de interpretatie die nodig is voor verdere besluitvorming.'''

new_duidend = '''## Interpreterend artefact

### Definitie
Een **interpreterend artefact** is een **Mandarin-artefact** dat betekenis, interpretatie of een oordeel geeft over andere artefacten of systemen.

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
- Evaluerend artefact
- Beoordelings-artefact
- Duidend artefact

### Analogieën 
- In softwareontwikkeling: test results, linting reports, code review comments
- In kwaliteitszorg: audit reports, inspectierapporten

### Toelichting  
**Interpreterende artefacten** vormen de feedbackloop binnen de workspace. Zij toetsen of de gerealiseerde of ontworpen artefacten voldoen aan de gestelde kaders en leveren de interpretatie die nodig is voor verdere besluitvorming.'''

content = content.replace(old_duidend, new_duidend)

# 20. Beschrijvend artefact -> Registrerend artefact
old_beschrijvend = '''## Beschrijvend artefact

### Definitie
Een **beschrijvend artefact** is een **Mandarin-artefact** dat inzicht, uitleg of overzicht biedt over bestaande structuren, besluiten of situaties, zonder zelf bindend of structurerend te zijn.

### Kenmerken
- Biedt inzicht en uitleg
- Is descriptief (beschrijft wat is)
- Is niet bindend of prescriptief
- Kan afgeleid zijn uit andere artefacten
- Ondersteunt begripsvorming en communicatie

### Wat het niet is
- Geen bindend artefact (schrijft niets voor)
- Geen richtinggevend artefact (geen bindende output van vormingsfase)
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
**Beschrijvende artefacten** helpen mensen de workspace te begrijpen. Zij zijn vaak afgeleid uit bindende of richtinggevende artefacten. Beschrijvende artefacten zijn ondersteunend en niet bindend.'''

new_beschrijvend = '''## Registrerend artefact

### Definitie
Een **registrerend artefact** is een **Mandarin-artefact** dat inzicht, uitleg of overzicht biedt over bestaande structuren, besluiten of situaties, zonder zelf vastleggend of structurerend te zijn.

### Kenmerken
- Biedt inzicht en uitleg
- Is descriptief (beschrijft wat is)
- Is niet vastleggend of prescriptief
- Kan afgeleid zijn uit andere artefacten
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
- Beschrijvend artefact

### Analogieën 
- Vergelijkbaar met white papers, explanatory documents, vision documents
- In enterprise architectuur: viewpoints, perspectives
- In softwareontwikkeling: architectural decision records (registrerende variant), design rationale

### Toelichting  
**Registrerende artefacten** helpen mensen de workspace te begrijpen. Zij zijn vaak afgeleid uit vastleggende of richtinggevende artefacten. Registrerende artefacten zijn ondersteunend en niet vastleggend.'''

content = content.replace(old_beschrijvend, new_beschrijvend)

file_path.write_text(content, encoding='utf-8')
print('Done')

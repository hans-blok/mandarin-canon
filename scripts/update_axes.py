import re

file_path = r'c:\git\mandarin-canon\grondslagen\aeo\mandarin-ordeningsconcepten.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update TOC
content = content.replace('- [Betekenis-as](#betekenis-as) — Effect op betekenis\n- [Inzet-as](#inzet-as) — Context van gebruik\n- [Vorm-as](#vorm-as) — Betekenis of representatie\n- [Werkingsas](#werkingsas) — Inhoud of voorwaarden\n- [Epistemische as](#epistemische-as) — Kennisbronnen en herleidbaarheid',
                          '- [Betekeniseffect](#betekeniseffect) — Effect op betekenis\n- [Werking](#werking) — Inhoud, representatie of voorwaarden\n- [Interventieniveau](#interventieniveau) — Systeemniveau van ingreep\n- [Epistemische houding](#epistemische-houding) — Kennisbronnen en herleidbaarheid')

# 2. Update Mandarin-agent-classificatie section
content = content.replace('Bestaat uit 5 orthogonale assen:\n  1. **Betekenis-as** — effect op betekenis\n  2. **Inzet-as** — context van gebruik\n  3. **Vorm-as** — betekenis of representatie\n  4. **Werkingsas** — inhoud of voorwaarden\n  5. **Epistemische as** — kennisbronnen en herleidbaarheid',
                          'Bestaat uit 4 orthogonale assen:\n  1. **Betekeniseffect** — effect op betekenis\n  2. **Interventieniveau** — systeemniveau van ingreep\n  3. **Werking** — inhoud, representatie of voorwaarden\n  4. **Epistemische houding** — kennisbronnen en herleidbaarheid')

content = content.replace('Een **mandarin-agent** kan beschrijvend zijn (betekenis-as), value-stream-specifiek (inzet-as), vormvast (vorm-as) en inhoudelijk (werkingsas)',
                          'Een **mandarin-agent** kan beschrijvend zijn (betekeniseffect), op werk-niveau acteren (interventieniveau), en inhoudelijk zijn (werking)')
content = content.replace('Een **mandarin-agent** kan structuur-normerend, value-stream-specifiek, vormvast en inhoudelijk zijn',
                          'Een **mandarin-agent** kan normerend, op architectuur-niveau, en inhoudelijk zijn')
content = content.replace('Een **mandarin-agent** kan conditioneel zijn (werkingsas), value-stream-overstijgend (inzet-as)',
                          'Een **mandarin-agent** kan conditioneel zijn (werking), op ecosysteem-niveau (interventieniveau)')

content = content.replace('werkingsas en betekenis-as', 'werking en betekeniseffect')

# 3. Rename Betekenis-as to Betekeniseffect
content = content.replace('## Betekenis-as', '## Betekeniseffect')
content = content.replace('De **betekenis-as** is', 'Het **betekeniseffect** is')
content = content.replace('Onafhankelijk van andere assen (Inzet, Vorm, Werkingsas, Epistemische as)', 'Onafhankelijk van andere assen (Interventieniveau, Werking, Epistemische houding)')
content = content.replace('De **betekenis-as** is de primaire as', 'Het **betekeniseffect** is de primaire as')

# Update categories of Betekeniseffect based on image: beschrijvend | realiserend | evaluerend | normerend
# The current text has 6 categories. I will adjust them to match the 4 from the image.
old_betekenis_categories = """### Categorieën 

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

**3. Architectuur-structurerende **mandarin-agents****
- Instantiëren een samenhangend architectuurmodel over lagen en aspecten binnen de gestelde kaders
- Creëren coherente architectuurmodellen volgens metamodellen
- Maken architectonische structuur expliciet en beredeneerbaar
- Werken binnen normatieve kaders en richtlijnen
- Voorbeelden: ArchiMate-modelleur, C4-modelleur, Enterprise architectuur-**mandarin-agent**

**4. Structuur-normerende **mandarin-agents** (vooraf)**
- Normeren vooraf de structuur en indeling van toekomstig werk
- Beschrijven vooruit
- Normeren *wat als werk bestaat*
- Value-stream-gebonden
- Geen uitvoering, geen ecosysteemregels
- Voorbeelden: Thema-vormende **mandarin-agents**, Feature-beschrijvende **mandarin-agents**

**5. Curator-mandarin-agents**
- Beschrijvende **mandarin-agents** die expliciet oordeel of duiding vastleggen
- Maken overzichten
- Beoordelen kwaliteit, samenhang en risico's
- Leggen oordeel vast, geen besluit
- Escaleren i.p.v. corrigeren
- Voorbeelden: Review-mandarin-agents, Samenhangbeoordeling

**6. Ecosysteem-normerende **mandarin-agents****
- Vaststellen of wijzigen van regels, kaders en constituerende afspraken van het **mandarin-agent**-ecosysteem
- Meta-niveau
- Zeldzaam en zwaar
- Workspace- en value-stream-overstijgend
- Bepalen *hoe het systeem mag bestaan*
- Voorbeelden: Constitutie-**mandarin-agents**, Doctrine-**mandarin-agents**, Charter-**mandarin-agents**"""

new_betekenis_categories = """### Categorieën 

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
- Voorbeelden: Thema-vormende **mandarin-agents**, Constitutie-**mandarin-agents**"""

content = content.replace(old_betekenis_categories, new_betekenis_categories)
content = content.replace('Zes categorieën: Beschrijvend, Structuurrealiserend, Architectuur-structurerend, Structuur-normerend, Curator, Ecosysteem-normerend',
                          'Vier categorieën: Beschrijvend, Realiserend, Evaluerend, Normerend')

# 4. Remove Inzet-as and Vorm-as
# Find the start of Inzet-as and the start of Werkingsas
inzet_start = content.find('## Inzet-as')
werkingsas_start = content.find('## Werkingsas')
if inzet_start != -1 and werkingsas_start != -1:
    content = content[:inzet_start] + content[werkingsas_start:]

# 5. Rename Werkingsas to Werking and add Representatie-omvormend
content = content.replace('## Werkingsas', '## Werking')
content = content.replace('De **werkingsas** is', 'De **werking** is')
content = content.replace('Onafhankelijk van andere assen (Betekenis-as, Inzet, Vorm, Epistemische as)', 'Onafhankelijk van andere assen (Betekeniseffect, Interventieniveau, Epistemische houding)')
content = content.replace('Twee categorieën: Inhoudelijk, Conditioneel', 'Drie categorieën: Inhoudelijk, Representatie-omvormend, Conditioneel')

old_werking_categories = """### Categorieën

**1. Inhoudelijke **mandarin-agents****
- Werken direct op betekenisvolle artefacten
- Omvat alle categorieën van de betekenis-as:
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
  - **Engineering Steward** — codekwaliteit, veiligheid, onderhoudbaarheid"""

new_werking_categories = """### Categorieën

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
  - **Engineering Steward** — codekwaliteit, veiligheid, onderhoudbaarheid"""

content = content.replace(old_werking_categories, new_werking_categories)
content = content.replace('De **werkingsas** maakt cruciaal onderscheid', 'De **werking** maakt cruciaal onderscheid')

# 6. Update Interventieniveau
content = content.replace('orthogonaal aan de betekenis-as', 'orthogonaal aan het betekeniseffect')
content = content.replace('dat beschrijft de betekenis-as', 'dat beschrijft het betekeniseffect')
content = content.replace('dat is de betekenis-as', 'dat is het betekeniseffect')
content = content.replace('gecombineerd worden met de betekenis-as', 'gecombineerd worden met het betekeniseffect')

# 7. Rename Epistemische as to Epistemische houding
content = content.replace('## Epistemische as', '## Epistemische houding')
content = content.replace('De **epistemische as** is', 'De **epistemische houding** is')
content = content.replace('Onafhankelijk van andere assen (Betekenis-as, Inzet, Vorm, Werkingsas)', 'Onafhankelijk van andere assen (Betekeniseffect, Interventieniveau, Werking)')
content = content.replace('De **epistemische as** maakt expliciet', 'De **epistemische houding** maakt expliciet')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Update complete.")

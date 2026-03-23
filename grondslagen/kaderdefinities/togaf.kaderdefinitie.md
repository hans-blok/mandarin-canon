---
type: grondslag
subtype: kaderdefinitie
naam: TOGAF (The Open Group Architecture Framework)
versie: 2.0.0
status: actief
externe-grondslag: TOGAF 9.2 (The Open Group)
---

# Kaderdefinitie — TOGAF (The Open Group Architecture Framework)

## 0. Positie van dit document

Dit document is de **kaderdefinitie** van TOGAF binnen het Mandarin-ecosysteem.

### Wat dit document is

Een kaderdefinitie is de **normatieve controlelaag** tussen externe kennis en het operationele handelen van **mandarin-agents**. Zij bepaalt:

- welke delen van de externe grondslag **toegestaan** zijn binnen Mandarin
- welke **interpretatie** geldt
- welke toepassingen **uitgesloten** zijn
- welke **Mandarin-concepten** leidend zijn boven externe terminologie

### Wat dit document niet is

Dit document is **niet de bron** van TOGAF-kennis. Een LLM-gebaseerde agent beschikt reeds over algemene TOGAF-kennis uit zijn trainingsdata. De kaderdefinitie:

- **vervangt** die kennis niet
- **verrijkt** die kennis niet
- maar **filtert en begrenst** die kennis voor gebruik binnen Mandarin

### Operationeel model

```
LLM-basiskennis (TOGAF) → [kaderdefinitie als filter] → toegestane toepassing binnen Mandarin
```

De agent mag zijn bestaande TOGAF-kennis **alleen toepassen** voor zover die past binnen de scope, interpretatie en beperkingen van deze kaderdefinitie. Kennis die buiten de kaderdefinitie valt, is **niet toegestaan** als basis voor output binnen het Mandarin-ecosysteem.

### Praktische consequentie

- De agent hoeft geen externe bronnen te raadplegen
- De agent past bestaande kennis toe binnen de grenzen van dit document
- De kaderdefinitie is leidend; waar LLM-kennis afwijkt, geldt de kaderdefinitie

---

## 1. Doel

TOGAF wordt binnen het Mandarin-ecosysteem gebruikt als **geïnternaliseerd ordeningskader voor het gestructureerd ontwerpen, beschrijven en evolueren van enterprise-architecturen**.

Het kader biedt:

- een gefaseerde aanpak (ADM)
- een scheiding in architectuurdomeinen
- een set van consistente artefacttypen

TOGAF wordt **niet als volledig framework overgenomen**, maar als **selectief geïnterpreteerde grondslag**.

---

## 2. Scope binnen Mandarin

### Wel toepassen voor:

- het structureren van architectuurtrajecten
- het ordenen van analyse naar ontwerp en roadmap
- het onderscheiden van architectuurdomeinen:
  - business
  - data
  - applicatie
  - technologie
- het expliciteren van samenhang tussen deze domeinen

### Niet toepassen voor:

- governance-structuren van organisaties (boards, committees)
- formele compliance-processen
- volledige documentatie-eisen van TOGAF
- certificeringsgerichte implementaties

---

## 3. Kernconcepten (Mandarin-selectie)

### 3.1 ADM (Architecture Development Method)

Binnen Mandarin gebruiken we een vereenvoudigde interpretatie:

| Fase | Mandarin-betekenis |
|------|-------------------|
| A — Architecture Vision | Probleemdefinitie en richting |
| B — Business Architecture | Capabilities en bedrijfsstructuur |
| C — Information Systems | Data + applicatie-structuur |
| D — Technology Architecture | Technologische inrichting |
| E/F — Opportunities & Migration | Roadmap en transitie |

Fases G en H (governance, change management) worden **niet expliciet gemodelleerd**, maar impliciet behandeld via curator-rollen.

---

### 3.2 Architectuurdomeinen

TOGAF-domeinen worden als volgt geïnterpreteerd:

- **Business** → capabilities, processen, waardecreatie
- **Data** → informatiestructuur en begrippen
- **Applicatie** → systemen en logische functies
- **Technologie** → infrastructuur en platformen

---

### 3.3 Artefacttypen

Binnen Mandarin worden deze artefacttypen gebruikt:

- architectuurvisie
- capability map
- domeinarchitecturen
- integrale architectuurbeschrijving
- transitie-roadmap

Deze worden als **Mandarin-artefacten** behandeld.

---

## 4. Canonieke interpretatie

TOGAF wordt binnen Mandarin geïnterpreteerd volgens de volgende principes:

### Principe 1 — Structuur boven volledigheid
We gebruiken TOGAF als **ordeningskader**, niet als checklist.

### Principe 2 — Agents voeren fases uit
Elke ADM-fase wordt uitgevoerd door één of meerdere gespecialiseerde rollen.

### Principe 3 — Artefacten zijn leidend
Niet de fase zelf, maar het **opgeleverde artefact** is het primaire resultaat.

### Principe 4 — Kaderbron, geen waarheid
TOGAF is een **kaderbron**, geen absolute waarheid.  
Andere grondslagen kunnen aanvullend of vervangend zijn.

---

## 5. Toegestane toepassingen

- opstellen van enterprise-architecturen
- structureren van complexe veranderopgaven
- ontwerpen van capability-gebaseerde modellen
- ontwikkelen van transitie-roadmaps
- analyseren van samenhang tussen domeinen

---

## 6. Niet-toegestane toepassingen

- mechanisch volgen van alle ADM-stappen
- produceren van TOGAF-conforme documentatie zonder doel
- gebruiken als vervanging voor inhoudelijke analyse
- afdwingen van terminologie buiten Mandarin-concepten

---

## 7. Relatie tot agent-ecosysteem

**Mandarin-agents gebruiken uitsluitend deze kaderdefinitie** — niet de externe TOGAF-documentatie.

Deze kaderdefinitie is van toepassing binnen de value stream **Architectuur- en Oplossingsontwerp (AOD)**.

Typische rollen die deze kaderdefinitie toepassen:

- architectuurverkenner (Architecture Explorer)
- capability-analist (Capability Analyst)
- domeinarchitecten (Domain Architects)
- roadmap-vormer (Roadmap Designer)
- architectuur-curator (Architecture Curator)

Agents passen de kaders uit dit document toe als **geïnternaliseerde structuur**, niet als instructieset vanuit de externe bron.

---

## 8. Externe grondslag en controlelaag

### 8.1 Externe grondslag

| Eigenschap | Waarde |
|---|---|
| Naam | TOGAF 9.2 |
| Uitgever | The Open Group |
| Herkomst | Extern |
| Status externe bron | Ruwe, niet-gecontroleerde kennis voor Mandarin |

De externe grondslag heeft **geen normatieve status** binnen Mandarin. Agents mogen de externe bron niet rechtstreeks raadplegen als basis voor handelen.

### 8.2 Status van deze kaderdefinitie

| Eigenschap | Waarde |
|---|---|
| Type | Kaderdefinitie |
| Status | Actief — gecanoniseerd |
| Autoriteit | Enige toegestane basis voor TOGAF-gebruik binnen Mandarin |
| Beheerd als | Grondslag-artefact binnen mandarin-canon |

### 8.3 Controlelaag

Dit document vormt de **expliciete controlelaag** tussen de externe TOGAF-kennis en het operationele handelen van **mandarin-agents**:

```
Externe grondslag (TOGAF) → [kaderdefinitie als controlelaag] → mandarin-agents
```

Zonder deze kaderdefinitie mag een agent TOGAF-kennis **niet** gebruiken als basis voor output, governance of ontwerp.

---

## 9. Samenvattende stelling

> TOGAF is binnen Mandarin geen methode die gevolgd wordt en geen externe bron die agents zelf raadplegen. Het is een **geïnternaliseerd ordeningskader**, vastgelegd in deze kaderdefinitie, dat door agents wordt toegepast om architectuurartefacten consistent en overdraagbaar te maken.

## 10. Operationele interpretatie binnen Mandarin

Deze kaderdefinitie wordt door agents toegepast volgens de volgende regels:

### 10.1 Fase-naar-artefact mapping

Agents werken niet met fases als doel, maar met artefacten:

- Architecture Vision → architectuurvisie-document
- Business Architecture → capability map
- Information Systems → data- en applicatiemodellen
- Technology Architecture → technologie-overzicht
- Migration → roadmap

### 10.2 Volgorde is situationeel

Agents doorlopen niet verplicht alle fases lineair.  
De volgorde wordt bepaald door:

- de vraagstelling
- beschikbare werkbronnen
- de gevraagde output

### 10.3 Detailniveau

Agents leveren:

- **voldoende detail voor besluitvorming**
- maar vermijden:
  - volledige TOGAF-documentatie
  - overmatige uitwerking zonder doel

### 10.4 Geen nieuwe concepten introduceren

Agents gebruiken:

- Mandarin-concepten (leidend)
- TOGAF alleen als structuur

Niet toegestaan:

- introduceren van TOGAF-terminologie die niet in Mandarin is gedefinieerd

### 10.5 Synthese over domeinen

Agents moeten expliciet:

- samenhang tonen tussen:
  - business
  - data
  - applicatie
  - technologie

Geen losse domeinbeschrijvingen zonder integratie.

### 10.6 Output is leidend

De kwaliteit van toepassing wordt beoordeeld op:

- helderheid van artefact
- consistentie met canon
- bruikbaarheid voor vervolgstappen

## 11. Typische toepassing door agents

Voorbeeld:

- Architectuurverkenner:
  - gebruikt fase A
  - levert architectuurvisie

- Capability-analist:
  - gebruikt fase B
  - levert capability map

- Roadmap-vormer:
  - gebruikt E/F
  - levert roadmap

---

## Change Log

| Datum | Versie | Wijziging | Auteur |
|---|---|---|---|
| 2026-03-23 | 2.0.0 | Herzien als kaderdefinitie conform nieuw concept; sectie 0 (positie) en sectie 8 (controlelaag) toegevoegd; frontmatter en samenvattende stelling bijgewerkt | Concept-Curator |
| 2026-03-23 | 1.0.0 | Initiële versie | Concept-Curator |
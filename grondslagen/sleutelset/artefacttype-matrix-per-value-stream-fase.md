---
type: sleutelset
naam: Artefacttype-matrix per Value Stream Fase
versie: 2.2.0
digest: tbd0
status: vers
---
# Artefacttype-matrix per Value Stream Fase

---

## Herkomstverantwoording

Dit normatief artefact is afgeleid op basis van de volgende geraadpleegde bronnen:

**Geraadpleegde bronnen**:
- `constitutie.md` (versie 2.3.0, als normatief kader voor value stream begrip)
- `mandarin-domeinconcepten.md` (versie 2.13.0, voor definitie van artefact-type)
- `togaf.kaderdefinitie.md` (versie 2.0.0, als kaderbron voor AOD-fasering)
- `temp/artefact-type-overzicht.md` (gegenereerd 2026-04-15, als bron voor artefacttype-id-toekenning)

**Toelichting**:
Dit document legt vast welke artefacttypen binnen het Mandarin-ecosysteem worden onderkend, inclusief hun unieke artefacttype-id. Per value stream fase wordt een matrix gepresenteerd die aangeeft welke artefacttypen in die fase kunnen worden geproduceerd.

---

## 1. Inleiding

### 1.1 — Doel van dit document

Dit document beschrijft de canonieke set van **artefacttypen** die binnen het Mandarin-ecosysteem worden onderkend, met hun unieke **artefacttype-id**. Per **value stream fase** wordt een matrix gepresenteerd die de relatie tussen fasen en artefacttypen expliciet maakt.

### 1.2 — Structuur

- **Sectie 2**: Overzicht van alle artefacttypen met hun id en toelichting
- **Secties 3–8**: Matrices per value stream fase

---

## 2. Artefacttypen

De onderstaande tabel definieert alle canoniek erkende artefacttypen binnen het Mandarin-ecosysteem.

| Artefacttype-id | Artefacttype | Producerende agent | Korte toelichting |
|---|---|---|---|
| 001 | agent-boundary | aeo.01.capability-architect | Boundary-document dat de identiteit, scope en charter-grenzen van een agent vastlegt |
| 002 | ecosysteem-agent-prompt-contracten | aeo.02.agent-curator | Overzicht van alle prompt-contracten van agents in het ecosysteem |
| 003 | ecosysteem-overzicht | aeo.02.agent-curator | Overzichtsartefact van het volledige agent-ecosysteem (structuur, agents, relaties) |
| 004 | validatierapport | aeo.02.agent-curator | Rapport van validatie-uitkomsten voor agent- of ecosysteemkwaliteit |
| 005 | agent-prompt | aeo.02.agent-engineer | Prompt-instructies voor een agent-intent, gegenereerd door agent-engineer |
| 006 | agent-charter | aeo.02.agent-ontwerper | Legitimatieverklaring die een agent integreert in het ecosysteem |
| 007 | agent-contract-intent | aeo.02.agent-ontwerper | Contract dat één intent van een agent beschrijft (input, output, parameters) |
| 008 | agent-prompt | aeo.02.agent-ontwerper | Prompt-instructies voor een agent-intent, ontworpen door agent-ontwerper |
| 009 | agent-positioneringsbeschrijving | aeo.02.ecosysteem-beschrijver | Beschrijving van de positionering van één agent in het ecosysteem |
| 010 | ecosysteem-artefacten-beschrijving | aeo.02.ecosysteem-beschrijver | Beschrijving van artefacten in het agent-ecosysteem |
| 011 | ecosysteem-contracten-beschrijving | aeo.02.ecosysteem-beschrijver | Beschrijving van contracten in het agent-ecosysteem |
| 012 | ecosysteem-value-streams-agents-beschrijving | aeo.02.ecosysteem-beschrijver | Beschrijving van value streams en agents in het ecosysteem |
| 013 | handoff | aeo.03.handoff-steward | Overdrachtsbestand tussen agents bij keten-executie |
| 014 | actieve-structuur-architectuurartefact | aod.02.core-framework-architect | ArchiMate actieve structuur weergave (core-framework) |
| 015 | gedragslaag-architectuurartefact | aod.02.core-framework-architect | ArchiMate gedragslaag weergave (core-framework) |
| 016 | architectuur-totaalweergave | aod.02.core-framework-architect | ArchiMate totaalweergave van de architectuur |
| 017 | architectuurkeuze-document | aod.05.solution-architect | Onderbouwing van een architectuurkeuze (solution-architect) |
| 018 | mkdocs-configuratie | fnd.01.documentatie-omvormer | MkDocs YAML-configuratiebestand voor documentatie-publicatie |
| 019 | conceptdefinitie | fnd.02.concept-curator | Geformaliseerde definitie van een canoniek concept |
| 020 | hypothese | sfw.01.hypothese-vormer | Geformuleerde hypothese over een veranderbehoefte of -aanleiding |
| 021 | barker-validatierapport | sfw.03.logisch-modelleur | Validatierapport van logisch model conform Barker-notatie |
| 022 | logisch-model | sfw.03.logisch-modelleur | Logisch datamodel van een bedrijfsdomein |
| 023 | modelleringsbeslissing | sfw.03.logisch-modelleur | Vastgelegde beslissing over een modelleringskeuze |
| 024 | epic-structuur | sfw.02.thema-verwoorder | Gedefinieerde epics voor het product-backlog van een thema |
| 025 | thematische-scope | sfw.02.thema-verwoorder | Gedefinieerde thematische scope van een verandering |
| 026 | verbetervoorstellen | sfw.02.thema-verwoorder | Gedefinieerde verbetervoorstellen voor een thema |
| 027 | gedragsspecificatie | sfw.03.gedragsspecificator | Gedragsspecificatie van requirements in scenario-formaat |
| 028 | scenario-consistentie-validatierapport | sfw.03.gedragsspecificator | Validatierapport van scenario-consistentie |
| 029 | gherkin-specificatie | sfw.03.gedragsspecificator | Gherkin-specificatie van gedragsscenario's |

---

## 3. Artefacttype-matrix — FND (Foundation)

### FND.01 — Fundament

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| 018 | mkdocs-configuratie | Omvorming van documentatiestructuur naar MkDocs-publicatieformaat |

### FND.02 — Conceptuele grondslagen

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| 019 | conceptdefinitie | Formalisering en vastlegging van canonieke concepten als bouwstenen van het ecosysteem |

---

## 4. Artefacttype-matrix — AEO (Agent Ecosysteem Ontwikkeling)

### AEO.01 — Grondslagvorming

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| 001 | agent-boundary | Vaststellen van de identiteit en grenzen van een agent als basislegitimatie voor deelname aan het ecosysteem |

### AEO.02 — Ecosysteeminrichting

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| 002 | ecosysteem-agent-prompt-contracten | Geconsolideerd overzicht van alle prompt-contracten in het ecosysteem voor validatie en beheer |
| 003 | ecosysteem-overzicht | Beschrijving van de huidige staat van het ecosysteem: agents, relaties en structuur |
| 004 | validatierapport | Rapport van validatieresultaten voor één of meerdere agents of contracten |
| 005 | agent-prompt | Door agent-engineer gegenereerde prompt-instructies voor een specifieke intent |
| 006 | agent-charter | Ecosysteem-legitimatieverklaring van een agent: verantwoordelijkheid, grenzen en samenwerking |
| 007 | agent-contract-intent | Contractspecificatie van één intent: input, output, bronhouding en herkomstpositie |
| 008 | agent-prompt | Door agent-ontwerper opgestelde prompt-instructies voor een specifieke intent |
| 009 | agent-positioneringsbeschrijving | Beschrijving van hoe één agent zich positioneert ten opzichte van het ecosysteem |
| 010 | ecosysteem-artefacten-beschrijving | Overzicht en beschrijving van alle artefacten die in het ecosysteem worden geproduceerd |
| 011 | ecosysteem-contracten-beschrijving | Overzicht en beschrijving van alle agent-contracten in het ecosysteem |
| 012 | ecosysteem-value-streams-agents-beschrijving | Beschrijving van de relatie tussen value streams, fasen en agents |

### AEO.03 — Ecosysteemworkflow en -automatisering

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| 013 | handoff | Overdrachtsbestand dat context, besluiten en openstaande taken overdraagt aan een volgende agent |

---

## 5. Artefacttype-matrix — SFW (Softwareontwikkeling)

### SFW.01 — Veranderkenning

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| 020 | hypothese | Geformuleerde hypothese over een veranderbehoefte, -aanleiding of -trigger |

### SFW.02 — Werkvoorbereiding

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| 024 | epic-structuur | Gedefinieerde epics voor het product-backlog, afgeleid uit de thematische scope |
| 025 | thematische-scope | Gedefinieerde thematische scope van de verandering inclusief afbakening |
| 026 | verbetervoorstellen | Gedefinieerde verbetervoorstellen per thema voor het backlog |

### SFW.03 — Behoefte- en requirements analyse

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| 021 | barker-validatierapport | Validatierapport van het logisch model conform Barker-notatie |
| 022 | logisch-model | Logisch datamodel van het te realiseren bedrijfsdomein |
| 023 | modelleringsbeslissing | Vastgelegde beslissing over een specifieke modelleringskeuze en haar onderbouwing |
| 027 | gedragsspecificatie | Gedragsspecificatie van requirements in scenario-formaat (BDD) |
| 028 | scenario-consistentie-validatierapport | Validatierapport van consistentie tussen gedragsscenario's |
| 029 | gherkin-specificatie | Formele Gherkin-specificatie van gedragsscenario's voor testautomatisering |

### SFW.04 — Ontwerp

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| *[nog aan te vullen]* | | |

### SFW.05 — Realisatie

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| *[nog aan te vullen]* | | |

### SFW.06 — Validatie

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| *[nog aan te vullen]* | | |

### SFW.07 — Vrijgave

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| *[nog aan te vullen]* | | |

---

## 6. Artefacttype-matrix — AOD (Architectuur en Oplossingsontwerp)

### AOD.01 — Architectuurvisie

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| *[nog aan te vullen]* | | |

### AOD.02 — Bedrijfsarchitectuur

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| 014 | actieve-structuur-architectuurartefact | ArchiMate-weergave van actieve structuurelementen (applicaties, componenten, services) |
| 015 | gedragslaag-architectuurartefact | ArchiMate-weergave van gedragselementen (processen, functies, interacties) |
| 016 | architectuur-totaalweergave | Geïntegreerde ArchiMate-weergave van actieve structuur en gedrag in één view |

### AOD.03 — Informatie- en applicatiearchitectuur

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| *[nog aan te vullen]* | | |

### AOD.04 — Technische architectuur

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| *[nog aan te vullen]* | | |

### AOD.05 — Roadmap en transitie

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| 017 | architectuurkeuze-document | Onderbouwing van een architectuurkeuze met context, afwegingen en besluit |

---

## 7. Artefacttype-matrix — KNV (Kennisvastlegging)

### KNV.01 — Kennisverkenning

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| *[nog aan te vullen]* | | |

### KNV.02 — Structurering

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| *[nog aan te vullen]* | | |

### KNV.03 — Vastlegging

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| *[nog aan te vullen]* | | |

### KNV.04 — Publicatie en Onderhoud

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| *[nog aan te vullen]* | | |

---

## 8. Artefacttype-matrix — MIV (Markt- en Investeringsvorming)

### MIV.01 — Strategische intentie expliciteren

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| *[nog aan te vullen]* | | |

### MIV.02 — Waarde-hypotheses formuleren

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| *[nog aan te vullen]* | | |

### MIV.03 — Positioneringsrichtingen verkennen

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| *[nog aan te vullen]* | | |

### MIV.04 — Monetisatie-logica's scheiden

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| *[nog aan te vullen]* | | |

### MIV.05 — Investering en kostenrealiteit expliciet maken

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| *[nog aan te vullen]* | | |

### MIV.06 — Keuzeruimte structureren

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| *[nog aan te vullen]* | | |

### MIV.07 — Leveranciersselectie (hosting)

| Artefacttype-id | Artefacttype | Toelichting voor deze fase |
|---|---|---|
| *[nog aan te vullen]* | | |

---

## 9. Wijzigingshistorie

| Datum | Versie | Wijziging | Auteur |
|---|---|---|---|
| 2026-04-15 | 2.2.0 | Artefacten logisch-modelleur (021–023) verplaatst van SFW.02 naar SFW.03; producerende agent bijgewerkt naar `sfw.03.logisch-modelleur` | Hans Blok |
| 2026-04-15 | 2.1.0 | §2 gevuld met 29 artefacttypen (id's 001–029) op basis van `temp/artefact-type-overzicht.md`; matrices §3–§6 ingevuld; FND.02 toegevoegd op basis van fnd.02.concept-curator; foutief bijgevoegd value streams-document verwijderd | Hans Blok |
| 2026-04-15 | 2.0.0 | Herschrijving: document omgevormd naar artefacttype-matrix per value stream fase met artefacttype-id structuur | Hans Blok |
| 2026-04-12 | 1.8.0 | Toegevoegd: FND (Foundation) als fundament value stream | Hans Blok |
| 2026-03-23 | 1.7.0 | Herijking value stream AOD: fasen geconsolideerd van 9 naar 5 conform togaf.kaderdefinitie.md | Hans Blok |
| 2026-02-15 | 1.6.0 | Herziening value stream AOD | Constitutioneel Auteur |
| 2026-02-05 | 1.5.0 | Aanpassing: ONV vervangen door MIV | Constitutioneel Auteur |
| 2026-02-02 | 1.4.0 | Toegevoegd: value stream Ondernemingsvorming (ONV) | Constitutioneel Auteur |
| 2026-02-02 | 1.3.0 | Toegevoegd: drie-letterige codes per value stream | Constitutioneel Auteur |
| 2026-02-01 | 1.2.0 | Verduidelijking artefacttypes per value stream | Constitutioneel Auteur |
| 2026-01-31 | 1.1.0 | Verduidelijking agent-toekenning per agent-soort | Constitutioneel Auteur |
| 2026-01-31 | 1.0.0 | Initiële versie — canonieke vastlegging van value streams en fasen | Constitutioneel Auteur |

---

## 10. Relatie tot andere documenten

Dit document is normatief en dient als bron voor:
- **Agent-contracts**: Bij het opstellen van een agent-contract wordt het artefacttype-id als FK opgenomen
- **Templates**: Het template-id verwijst naar het artefacttype-id dat het template ondersteunt
- **Artefact-headers**: Het artefacttype-id is een verplicht veld in de YAML-header

Dit document verwijst naar:
- **mandarin-domeinconcepten.md** (v2.13.0) voor de definitie van "artefact-type"
- **constitutie.md** (v2.3.0) als hoogste normatieve bron
- **togaf.kaderdefinitie.md** (v2.0.0) als kaderbron voor de AOD value stream fasering

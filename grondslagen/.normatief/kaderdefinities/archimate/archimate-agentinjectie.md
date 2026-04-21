# Plan voor effectieve agentinjectie met ArchiMate-kennis

**Status**: implementatienotitie  
**Doel**: praktische richtlijn voor het voeden van agents met ArchiMate-kennis zonder onnodig promptvolume

---

## 1. Waarom een aparte injectiestrategie nodig is

ArchiMate-fouten ontstaan in de praktijk meestal niet door gebrek aan woorden, maar door verkeerde interpretatie van:

- het doel van een view;
- het onderscheid tussen service, component en interface;
- het onderscheid tussen `Serving`, `Realization`, `Assignment` en `Access`.

Een volledige kennisbron integraal in elke prompt opnemen is inefficiënt. Daarom is een taakgerichte injectiestrategie nodig.

---

## 2. Aanbevolen kennisbronnen

Gebruik voor agentinjectie primair:

1. `artefacten/kaderstelling/archimate-samenvatting-voor-llm.md`
2. `artefacten/kaderstelling/archimate-kennisindex.yaml`

Gebruik aanvullend, taakafhankelijk:

3. relevante repo-views en architectuurdocumenten;
4. externe verificatie alleen bij semantische twijfel.

---

## 3. Injectiepatroon per taaktype

### 3.1 View-interpretatie

Injecteer:

- viewpointregel;
- relevante elementtypen;
- relevante relatietypen;
- één repo-voorbeeld dat semantisch vergelijkbaar is.

Minimale set:

- `application-service`
- `application-component`
- `data-object`
- `serving`
- `realization`
- `access`

### 3.2 ARA- of architectuurtekstschrijven

Injecteer:

- viewpointbeschrijvingen voor context-, informatieflow-, applicatie- en roadmapviews;
- Common Ground-laagmapping;
- repo-voorbeelden van vergelijkbare architectuurpassages.

### 3.3 Review van bestaande views

Injecteer:

- anti-patterns uit de YAML-index;
- de LLM-regels;
- de relevante viewbeschrijving uit de repo.

Doel:

- foutdetectie op relatiekeuze;
- inconsistenties tussen tekst en diagram signaleren.

---

## 4. Promptopbouw

Aanbevolen opbouw voor agentcontext:

1. Taakdoel
2. Relevante repo-bestanden
3. Knowledge Context
4. Verwachte outputvorm

Voorbeeld van compacte Knowledge Context:

```markdown
## Knowledge Context: ArchiMate
- Viewpoint: applicatieview
- Kernregel 1: als een service een component bedient, gebruik Serving
- Kernregel 2: als een component een service implementeert, gebruik Realization
- Kernregel 3: als gedrag op een object werkt, gebruik Access
- Relevante elementen: Application service, Application component, Data object
- Relevante voorbeelden: kennisbank-kiss-huidig.md, open-product-doel.md
```

---

## 5. Aanbevolen selectielogica

Selecteer kennis niet op bestandsnaam alleen, maar op vraagtype:

| Vraagtype | Injecteer |
|---|---|
| "Leg deze view uit" | viewpoint + relaties + voorbeeldview |
| "Welke relatie klopt hier" | relatietypen + anti-patterns + vergelijkbaar voorbeeld |
| "Schrijf een ARA-viewbeschrijving" | viewpoint + laagmapping + repo-voorbeeld |
| "Controleer ArchiMate-correctheid" | YAML-heuristieken + relevante viewbestanden |

---

## 6. Aanbevolen implementatie in agentflow

Voor de huidige workspace zijn dit de logische invoerpunten:

### 6.1 Beleidslaag

`beleid-workspace.md` legt vast:

- welke ArchiMate-bronnen leidend zijn;
- in welke volgorde bronnen worden geraadpleegd;
- dat injectie selectief moet zijn.

### 6.2 Instruction generation

Wanneer een lokale of externe generator execution-bestanden assembleert, voeg dan een sectie toe:

`## Knowledge Context`

Deze sectie bevat:

- relevante ArchiMate-regels;
- relevante YAML-selecties;
- links naar semantische ankerbestanden in de repo.

### 6.3 Task- of parameterlaag

Voeg optioneel een parameter toe voor:

- viewpoint;
- relatievraagstuk;
- referentieview.

Daarmee kan de generator selectief injecteren in plaats van volledige bestanden mee te geven.

---

## 7. Minimale succescriteria

De aanpak is geslaagd als agents:

- minder vaak `Serving` en `Realization` verwisselen;
- minder vaak `Association` als default gebruiken;
- explicieter aangeven welk viewpoint zij hanteren;
- semantische ankers uit GGM, GEMMA of Common Ground beter betrekken;
- consistenter dezelfde redenering toepassen in viewbeschrijvingen.

---

## 8. Fasegewijze invoering

### Fase 1

- Markdown-samenvatting beschikbaar maken
- YAML-kennisindex beschikbaar maken
- beleid-workspace uitbreiden

### Fase 2

- instruction-generation uitbreiden met `Knowledge Context`
- taakgerichte selectie op viewpoint of relatietype

### Fase 3

- evalueren of graph-afleiding nodig is voor geavanceerde modelchecks
- eventueel Neo4j-seed of graph-export toevoegen als afgeleid hulpmiddel

---

## 9. Nu nog niet doen

- geen volledige externe standaarddocumentatie in prompts opnemen;
- geen graphdatabase als primaire kennisbron gebruiken;
- geen generieke regels forceren zonder repo-context;
- geen ArchiMate-regels los gebruiken van het doel van de view.
# Agent Doctrine — Intent Naming

**Doctrine-ID**: `AEO.DOC.002`  
**Versie**: 1.3.0  
**Value Stream**: Agent Ecosysteem ontwikkeling  

---

## Classificatie

**Agent-classificatie**: Ecosysteem-vastleggend, Value-stream-overstijgend, Vormvast, Conditioneel

*Voor uitleg van classificatie-assen zie [mandarin-ordeningsconcepten](../aeo/mandarin-ordeningsconcepten.md#mandarin-agent-classificatie)*

---

## 1. Doel en bestaansreden

Deze doctrine normeert **intent-naming** voor agents binnen het Mandarin-ecosysteem door een canoniek werkwoord te koppelen aan elke agent-classificatie.

Zij stelt kaders voor:

- de relatie tussen agent-classificatie en werkwoord;
- voorspelbaarheid in communicatie tussen agents;
- architectonische helderheid over agent-werking;
- ecosysteem-brede consistentie in naming.

Deze doctrine waarborgt dat de **naam van een intent de architectonische werking** reflecteert, niet het artefact-type.

---

## 2. Capability boundary

Deze doctrine normeert **intent-naming** door voor elke agent-classificatie exact één canoniek werkwoord vast te stellen, waarmee architectonische werking direct herkenbaar wordt in de naam van een intent.

---

## 3. Kernprincipes

### Principe 1 — Één Classificatie, Één Werkwoord

Elke **agent-classificatie** (op de werkingsas) heeft **exact één canoniek werkwoord** voor intent-naming.

Het werkwoord manifesteert:

- de architectonische werking van de agent;
- niet het type artefact dat wordt geproduceerd;
- niet het technische mechanisme.

De ontwerprichting is:

> classificatie → canoniek werkwoord → intent-naam

Niet:

> artefact-type → werkwoord

---

### Principe 2 — Werkwoord Volgt Werking

Het canonieke werkwoord reflecteert de **architectonische transformatie** die de agent uitvoert:

- **Registrerend**: `beschrijf` — Observatie → expliciete beschrijving
- **Structuur-vastleggend**: `definieer` — Chaos → gedefinieerde scope
- **Constituerend**: `constitueer` — Intentie → normatief kader
- **Structuurvastleggend**: `realiseer` — Ontwerp → werkende structuur
- **Curator**: `beoordeel` — Artefact → kwalitatief oordeel
- **Ecosysteem-vastleggend**: `stel vast` — Bestaande norm → gewijzigde norm
- **Conditioneel (validerend)**: `valideer` — Artefact + Norm → pass/fail
- **Conditioneel (ordenend)**: `orden` — Chaos → geordende structuur

Het werkwoord verbergt nooit de ware werking.

---

### Principe 3 — Naamgevingsconventie als Contract

Alle intents volgen het formaat:

```
{werkwoord}-{object}[-{context}]
```

Met de regels:

1. Werkwoord altijd in gebiedende wijs, kleine letters;
2. Object in kebab-case;
3. Context optioneel, voor verdere specificatie;
4. Geen lidwoorden ("de", "het");
5. Gebruik altijd het canonieke werkwoord voor de agent-classificatie.

Voorbeelden:
- ✅ `beschrijf-agent-contract`
- ✅ `realiseer-database-schema`
- ✅ `definieer-themas-werkvoorbereiding`
- ✅ `constitueer-doctrine`
- ✅ `beoordeel-consistentie-charter`
- ✅ `stel-vast-doctrine-wijziging`
- ✅ `valideer-tegen-doctrine`
- ✅ `orden-workspace`
- ✅ `realiseer-charter`

---

### Principe 4 — Representatie-omvorming Kent Drie Varianten

Agents met classificatie **Representatie-omvormend** hebben drie sub-varianten, elk met eigen werkwoord:

#### 4.1 Omzettend (vorm zonder betekeniswijziging)

**Canoniek werkwoord**: `zet om`

**Werking**: Vorm A → Vorm B (zelfde betekenis)

Intent-patroon: `zet-om-naar-{formaat}` of `zet-om-{bron}-naar-{doel}`

#### 4.2 Verdichtend (reductie, behoud kern)

**Canoniek werkwoord**: `vat samen`

**Werking**: Complex → beknopt (essentie behouden)

Intent-patroon: `vat-samen-{object}` of `vat-samen-in-{aantal}`

#### 4.3 Uitbreidend (explicitering)

**Canoniek werkwoord**: `licht toe`

**Werking**: Impliciet → expliciet (verheldering)

Intent-patroon: `licht-toe-{aspect}` of `licht-toe-aannames-{object}`

---

### Principe 5 — Kritische Verschillen Zijn Expliciet

Bepaalde werkwoorden lijken op elkaar maar hebben fundamenteel verschillende werking:

#### `beoordeel` vs `valideer`
- **beoordeel** (curator): Kwalitatief gradueel oordeel ("redelijk consistent")
- **valideer** (conditioneel): Binaire check ("voldoet", "voldoet niet")

#### `definieer` vs `stel vast`
- **definieer** (structuur-vastleggend): Bepaalt wat binnen scope bestaat
- **stel vast** (ecosysteem-vastleggend): Wijzigt governance-spelregels

#### `constitueer` vs `definieer`
- **constitueer** (constituerend): Schept het normatieve kader zelf (doctrine, constitutie, beleid)
- **definieer** (structuur-vastleggend): Bepaalt wat binnen een bestaand kader valt

#### `structureer` vs `definieer` vs `orden`
- **structureer** (structurerend): Brengt structuur aan in bestaande elementen (kan inhoud wijzigen)
- **definieer** (structuur-vastleggend): Bepaalt wat binnen scope bestaat (normering)
- **orden** (conditioneel): Rangschikt alleen (geen inhoudelijke wijziging)

#### `beschrijf` vs `documenteer`
- **beschrijf** (registrerend): Momentopname, observatie
- **documenteer** (documenterend): Duurzame kennisregistratie

#### `realiseer` vs `genereer`
- **realiseer** (vastleggend): Van specificatie naar concreet artefact
- **genereer` (afgeleid): Volledig berekend/afgeleid uit andere artefacten

Het ecosysteem handhaaft deze verschillen strikt.

---

### Principe 6 — Niet-Canonieke Werkwoorden Worden Geweigerd

Een intent met een niet-canoniek werkwoord wordt geweigerd tijdens contract-beschrijving.

Validatieregel:
```
IF intent_werkwoord NOT IN canonieke_werkwoorden_voor(agent_classificatie):
    STOP met foutmelding
    SUGGEREER: Canoniek werkwoord voor deze classificatie
    ESCALEER: Naar canon-curator bij onduidelijkheid
```

Geen uitzonderingen: elk werkwoord moet het canonieke werkwoord voor de classificatie zijn.

---

## 4. Canonieke Werkwoorden per Classificatie

| Classificatie | Canoniek Werkwoord |
|---------------|-----------------|
| Registrerend | `beschrijf` |
| Structuur-vastleggend | `definieer` |
| Constituerend | `constitueer` |
| Structurerend | `structureer` |
| Structuurvastleggend | `realiseer` |
| Curator | `beoordeel` |
| Ecosysteem-vastleggend | `stel vast` |
| Representatie-omvormend (omzettend) | `zet om` |
| Representatie-omvormend (verdichtend) | `vat samen` |
| Representatie-omvormend (uitbreidend) | `licht toe` |
| Vastleggend | `realiseer` |
| Conditioneel (validerend) | `valideer` |
| Conditioneel (ordenend) | `orden` |
| Documenterend | `documenteer` |
| Afgeleid | `genereer` |

---

## 5. Architectonische Werking per Werkwoord

### Inhoudelijke Agents (Werkings-as: Inhoudelijk)

#### `beschrijf` (Registrerend)
**Werking**: Legt vast wat is, zonder oordeel of transformatie  
**Effect**: Observatie → expliciete beschrijving

| Intent-patroon | Voorbeeld |
|----------------|-----------|
| `beschrijf-{object}` | `beschrijf-agent` |
| `beschrijf-{aspect}-{object}` | `beschrijf-structuur-document` |
| `beschrijf-{proces}` | `beschrijf-workflow` |

**Niet toegestaan**: `analyseer` (impliceert interpretatie), `documenteer` (te breed)

---

#### `definieer` (Structuur-vastleggend)
**Werking**: Bepaalt wat binnen scope bestaat, legt normering vast  
**Effect**: Chaos → gedefinieerde scope

| Intent-patroon | Voorbeeld |
|----------------|-----------|
| `definieer-{scope}` | `definieer-themas` |
| `definieer-{concept}` | `definieer-agent-contract` |
| `definieer-{grens}` | `definieer-capability-boundary` |

**Niet toegestaan**: `bepaal` (te zwak), `normeer` (zie ecosysteem-vastleggend)

---

#### `constitueer` (Constituerend)
**Werking**: Schept het normatieve kader zelf  
**Effect**: Intentie → normatief kader (doctrine, constitutie, beleid)

| Intent-patroon | Voorbeeld |
|----------------|-----------|
| `constitueer-{norm}` | `constitueer-doctrine` |
| `constitueer-{governance}` | `constitueer-constitutie` |
| `constitueer-{beleidskader}` | `constitueer-workspace-beleid` |

**Verschil met definieer**: `constitueer` schept het kader, `definieer` bepaalt wat binnen het kader valt

**Niet toegestaan**: `creëer` (te algemeen), `ontwerp` (te breed), `schrijf` (zie vastleggend)

---

#### `structureer` (Structurerend)
**Werking**: Brengt structuur aan in bestaande elementen of content  
**Effect**: Ongestructureerde elementen → gestructureerd geheel

| Intent-patroon | Voorbeeld |
|----------------|-----------||
| `structureer-{object}` | `structureer-artefacten` |
| `structureer-{content}` | `structureer-documenten` |
| `structureer-{verzameling}` | `structureer-workspace` |

**Verschil met orden**: `structureer` brengt structuur aan (kan inhoud wijzigen), `orden` rangschikt alleen (geen inhoudelijke wijziging)

**Verschil met definieer**: `definieer` bepaalt wat binnen scope valt, `structureer` organiseert wat al bestaat

**Niet toegestaan**: `organiseer` (te algemeen), `orden` (zie conditioneel)

---

#### `realiseer` (Structuurvastleggend)
**Werking**: Realiseert active structure (applicatielaag) - databases, code, API's  
**Effect**: Ontwerp/specificatie → werkende applicatie-structuur

| Intent-patroon | Voorbeeld |
|----------------|-----------|
| `realiseer-{structuur}` | `realiseer-database-schema` |
| `realiseer-{component}` | `realiseer-api-endpoint` |
| `realiseer-{laag}` | `realiseer-data-access-layer` |

**Context (ArchiMate)**: Realiseert de "Active Structure" - structurele elementen die gedrag mogelijk maken

**Niet toegestaan**: `structureer` (te abstract), `bouw` (te specifiek), `implementeer` (anglicisme)

---

#### `beoordeel` (Curator)
**Werking**: Geeft kwalitatief oordeel zonder te beslissen  
**Effect**: Artefact → oordeel over kwaliteit/consistentie

| Intent-patroon | Voorbeeld |
|----------------|-----------|
| `beoordeel-{kwaliteitskenmerk}` | `beoordeel-consistentie` |
| `beoordeel-{object}-op-{norm}` | `beoordeel-contract-op-doctrine` |
| `beoordeel-samenhang-{object}` | `beoordeel-samenhang-charter` |

**Niet toegestaan**: `evalueer` (te formeel), `reviewe` (anglicisme)

---

#### `stel vast` (Ecosysteem-vastleggend)
**Werking**: Wijzigt of stelt governance-spelregels vast  
**Effect**: Bestaande norm → gewijzigde/nieuwe norm

| Intent-patroon | Voorbeeld |
|----------------|-----------|
| `stel-vast-{governance}` | `stel-vast-doctrine-aanpassing` |
| `stel-vast-{besluit}` | `stel-vast-naming-conventie` |
| `stel-vast-of-{conditie}` | `stel-vast-of-migratie-nodig` |

**Niet toegestaan**: `bepaal` (te zwak), `besluit` (te definitief)

---

#### `zet om` (Representatie-omvormend: omzettend)
**Werking**: Vorm zonder betekeniswijziging  
**Effect**: Vorm A → Vorm B (zelfde betekenis)

| Intent-patroon | Voorbeeld |
|----------------|-----------|
| `zet-om-naar-{formaat}` | `zet-om-naar-archimate` |
| `zet-om-{bron}-naar-{doel}` | `zet-om-yaml-naar-json` |

**Niet toegestaan**: `converteer` (anglicisme), `transformeer` (te abstract)

---

#### `realiseer` (Vastleggend)
**Werking**: Van specificatie naar concreet artefact  
**Effect**: Specificatie → concreet artefact

| Intent-patroon | Voorbeeld |
|----------------|-----------|
| `realiseer-{artefact}` | `realiseer-prompt` |
| `realiseer-{tekst}` | `realiseer-charter` |
| `realiseer-{simpel}` | `realiseer-template` |
| `realiseer-{overzicht}` | `realiseer-overzicht` |
| `realiseer-{technisch}` | `realiseer-pipeline` |

**Niet toegestaan**: `schrijf`, `maak`, `genereer`, `creëer`, `bouw`, `produceer`, `fabriceer`

---

### Conditionele Agents (Werkings-as: Conditioneel)

#### `valideer` (Validerend)
**Werking**: Binaire check tegen vastgestelde norm  
**Effect**: Artefact + Norm → pass/fail

| Intent-patroon | Voorbeeld |
|----------------|-----------|
| `valideer-{object}` | `valideer-contract` |
| `valideer-tegen-{norm}` | `valideer-tegen-doctrine` |
| `valideer-{aspect}-{object}` | `valideer-consistentie-artefacten` |

**Niet toegestaan**: `check` (anglicisme), `controleer` (te algemeen), `toets` (te zwak)

---

#### `orden` (Ordenend)
**Werking**: Brengt bestaande elementen in logische volgorde  
**Effect**: Chaos → geordende structuur (zonder inhoud te wijzigen)

| Intent-patroon | Voorbeeld |
|----------------|-----------|
| `orden-{object}` | `orden-workspace` |
| `orden-{object}-op-{criterium}` | `orden-agents-op-classificatie` |

**Niet toegestaan**: `sorteer` (te mechanisch), `rangschik` (te literair)

---

### Overige Classificaties

#### `documenteer` (Documenterend)
**Werking**: Maakt duurzame kennisregistratie  
**Effect**: Impliciete kennis → expliciete documentatie

| Intent-patroon | Voorbeeld |
|----------------|-----------|
| `documenteer-{object}` | `documenteer-workspace` |
| `documenteer-{proces}` | `documenteer-workflow` |

---

#### `genereer` (Afgeleid)
**Werking**: Produceert afgeleid artefact uit andere artefacten  
**Effect**: Primaire artefacten → berekende/afgeleide output

| Intent-patroon | Voorbeeld |
|----------------|-----------|
| `genereer-{overzicht}` | `genereer-overzicht-agents` |
| `genereer-{index}` | `genereer-index-artefacten` |

---

## 6. Reikwijdte en grenzen

Deze doctrine:

- **Normeert** intent-naming voor alle agents binnen het Mandarin-ecosysteem;
- **Koppelt** canonieke werkwoorden aan agent-classificaties;
- **Handhaaft** consistentie door niet-canonieke werkwoorden te weigeren;
- **Faciliteert** architectonische helderheid door werking in naam te reflecteren.

Deze doctrine vervangt geen agent-classificatie, maar **ondersteuntIntent-naming als communicatie-contract**.

---

## 7. Traceerbaarheid

Deze doctrine geldt voor:

- alle agent-intents binnen het Mandarin-ecosysteem;
- alle nieuwe agents die contracts definiëren;
- alle bestaande agents bij herziening van hun contract.

Agents die deze doctrine incorporeren, dragen bij aan **voorspelbaarheid en herkenbaarheid** van architectonische werking.

---

## 8. Change Log

| Datum       | Versie | Wijziging                                                                 | Auteur |
|------------|--------|---------------------------------------------------------------------------|--------|
| 2026-02-15 | 1.3.0  | Werkwoord 'structureer' toegevoegd voor classificatie Structurerend | —      |
| 2026-02-14 | 1.2.0  | Werkwoord 'constitueer' toegevoegd voor scheppen van normatieve kaders | —      |
| 2026-02-14 | 1.1.0  | Synoniemen verwijderd: alleen canonieke werkwoorden toegestaan | —      |
| 2026-02-14 | 1.0.0  | Initiële doctrine: canonieke werkwoorden per agent-classificatie vastgesteld | —      |

---

### Canonieke essentie

> De naam van een intent is een architectonisch contract: het canonieke werkwoord maakt de werking direct herkenbaar, zonder verberging of ambiguïteit.

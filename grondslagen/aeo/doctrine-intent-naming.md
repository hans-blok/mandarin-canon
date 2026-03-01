
# Agent Doctrine — Intent Naming

**Doctrine-ID**: `AEO.DOC.002`  
**Versie**: 2.0.0  
**Value Stream**: Agent Ecosysteem ontwikkeling

---

## Classificatie

Deze doctrine volgt de vier orthogonale assen uit [mandarin-ecosysteem-ordeningsconcepten.md](../aeo/mandarin-ecosysteem-ordeningsconcepten.md):

- **Betekeniseffect**: bepaalt het type transformatie of effect van de intent
- **Vormingsfase**: positioneert de intent in het proces van verkenning tot operationalisatie
- **Werking**: bepaalt of de intent inhoudelijk, representatie-omvormend of conditioneel is
- **Bronhouding**: bepaalt de herleidbaarheid en kennisbasis van de intent

Intent-naming is primair gekoppeld aan de werking en het betekeniseffect van de agent.

---

## Doel en bestaansreden

Deze doctrine normeert **intent-naming** voor agents binnen het Mandarin-ecosysteem. Elke intent-naam maakt via een canoniek werkwoord direct duidelijk:
- het architectonisch effect (betekeniseffect)
- de aard van de interventie (werking)

Hiermee wordt voorspelbaarheid, consistentie en uitlegbaarheid in het ecosysteem geborgd.

---

## Kernprincipes

### 1. Eén werking, één canoniek werkwoord
Elke werking (en bijbehorend betekeniseffect) kent exact één canoniek werkwoord voor intent-naming. Dit werkwoord is verplicht leidend in de intent-naam.

### 2. Intent-naming volgt architectonische werking
Het canonieke werkwoord reflecteert de architectonische transformatie die de agent uitvoert. De intent-naam mag nooit het ware effect of de werking verhullen.

### 3. Naamgevingsconventie
Het formaat voor elke intent is:

    {werkwoord}-{object}[-{context}]

Regels:
1. Werkwoord altijd in gebiedende wijs, kleine letters
2. Object in kebab-case
3. Context optioneel, voor specificatie
4. Geen lidwoorden
5. Altijd het canonieke werkwoord voor de werking gebruiken

### 4. Kritische verschillen expliciet
Werkwoorden met verschillende architectonische werking mogen niet worden verward. Zie de toelichting en matrix in [mandarin-ecosysteem-ordeningsconcepten.md](../aeo/mandarin-ecosysteem-ordeningsconcepten.md).

### 5. Validatie
Een intent met een niet-canoniek werkwoord wordt geweigerd. Alleen de vastgestelde werkwoorden per werking/betekeniseffect zijn toegestaan.

---

## Canonieke werkwoorden per werking/betekeniseffect


Werking     | Bekeneniseffect                 | Canoniek werkwoord |
----------- |---------------------------------|--------------------|
Inhoudelijk | Beschrijvend                    | beschrijf          |
Inhoudelijk | Beschrijvend                    | maak-overzicht     |
Inhoudelijk | Structurerend                   | structureer        |
Inhoudelijk | Normerend                       | definieer          |
Inhoudelijk | Constituerend                   | constitueer        |
Inhoudelijk | Normerend                       | leg-vast           |
Inhoudelijk | Realiserend                     | realiseer          |
Inhoudelijk | Evaluerend                      | beoordeel          |
Conditioneel | Validerend                     | valideer           |
Conditoneel |  Rangschikkend                  | rangschik          |
representatie-omvormend | beschrijvend        | zet om / vat samen |

### werking representatie-omvormend

Zie voor de volledige matrix en toelichting de secties *Betekeniseffect* en *Werking* in [mandarin-ecosysteem-ordeningsconcepten.md](../aeo/mandarin-ecosysteem-ordeningsconcepten.md).

---

## Voorbeelden

**Correcte voorbeelden volgens doctrine:**

- `beschrijf-agent-contract`
- `realiseer-database-schema`
- `definieer-themas-werkvoorbereiding`
- `constitueer-doctrine`
- `beoordeel-consistentie-charter`
- `stel-vast-doctrine-wijziging`
- `valideer-tegen-doctrine`
- `rangschik-workspace`
- `realiseer-charter`
- `structureer-documenten`
- `documenteer-workflow`
- `genereer-index-artefacten`
- `zet-om-yaml-naar-json`

**Toelichting op de fout:**  
De fout ontstaat doordat `orden-workspace` wordt gebruikt, terwijl volgens de doctrine het canonieke werkwoord voor rangschikkende werking `rangschik` is. `Orden` is te algemeen en niet toegestaan voor deze werking; alleen vastgestelde canonieke werkwoorden per werking/betekeniseffect mogen worden gebruikt.

- `beschrijf-agent-contract`
- `realiseer-database-schema`
- `definieer-themas-werkvoorbereiding`
- `constitueer-doctrine`
- `beoordeel-consistentie-charter`
- `stel-vast-doctrine-wijziging`
- `valideer-tegen-doctrine`
- `orden-workspace`
- `realiseer-charter`
- `structureer-documenten`
- `documenteer-workflow`
- `genereer-index-artefacten`
- `zet-om-yaml-naar-json`

**Niet-toegestane voorbeelden (fout):**

- `analyseer-agent` (gebruik `beschrijf-agent`)
- `controleer-contract` (gebruik `valideer-contract`)
- `bouw-database` (gebruik `realiseer-database`)
- `maak-overzicht` (gebruik `genereer-overzicht` of `beschrijf-overzicht`)
- `organiseer-documenten` (gebruik `structureer-documenten`)
- `transformeer-bestand` (gebruik `zet-om-bestand`)
- `reviewe-charter` (gebruik `beoordeel-charter`)

- `beschrijf-agent-contract`
- `realiseer-database-schema`
- `definieer-themas-werkvoorbereiding`
- `constitueer-doctrine`
- `beoordeel-consistentie-charter`
- `stel-vast-doctrine-wijziging`
- `valideer-tegen-doctrine`
- `orden-workspace`
- `realiseer-charter`

---

## Reikwijdte en grenzen

Deze doctrine:
- Normeert intent-naming voor alle agents binnen het Mandarin-ecosysteem
- Koppelt canonieke werkwoorden aan werking en betekeniseffect
- Handhaaft consistentie door niet-canonieke werkwoorden te weigeren
- Faciliteert uitlegbaarheid en voorspelbaarheid van intent-werking

---

## Change Log

| Datum       | Versie | Wijziging                                                                 | Auteur |
|------------|--------|---------------------------------------------------------------------------|--------|
| 2026-03-01 | 2.0.0  | Volledig herschreven: structuur, assen en terminologie uit canon, koppeling intent-naming aan werking en betekeniseffect, validatie en matrix expliciet. | Constitutioneel Auteur |
| 2026-02-15 | 1.3.0  | Werkwoord 'structureer' toegevoegd voor classificatie Structurerend | —      |
| 2026-02-14 | 1.2.0  | Werkwoord 'constitueer' toegevoegd voor scheppen van normatieve kaders | —      |
| 2026-02-14 | 1.1.0  | Synoniemen verwijderd: alleen canonieke werkwoorden toegestaan | —      |
| 2026-02-14 | 1.0.0  | Initiële doctrine: canonieke werkwoorden per agent-classificatie vastgesteld | —      |

---

### Canonieke essentie

> De naam van een intent is een architectonisch contract: het canonieke werkwoord maakt de werking direct herkenbaar, zonder verberging of ambiguïteit.

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


#### `beschrijf` (Beschrijvend)
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

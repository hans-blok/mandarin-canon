---
type: doctrine
naam: Doctrine — Intent Naming
code: DINM
versie: 2.1.0
value-stream: aeo
digest: tbd0
status: vers
---
# Doctrine — Intent Naming

---

## Herkomstverantwoording

Dit normatief artefact is opgesteld op basis van de volgende bronnen:

**Geraadpleegde bronnen**:
- `mandarin-ecosysteem-ordeningsconcepten.md` — assen betekeniseffect, werking en vormingsfase; canonieke werkwoordmatrix (versie 1.9.0, gelezen op 2026-03-01)
- `doctrine.agent-charter-normering.md` — agent-classificatie, capability boundary en werkings-as (versie 2.4.0, gelezen op 2026-03-01)
- `mandarin-domeinconcepten.md` — concepten intent, agent-contract, werking (versie 2.13.0, gelezen op 2026-03-01)

**Opsteller**: Constitutioneel Auteur  
**Doel**: Normering van intent-naamgeving voor agents door canonieke werkwoorden te koppelen aan architectonische werking en betekeniseffect

---

## Classificatie

Deze doctrine positioneert zich als volgt op de vier orthogonale assen:

| Betekeniseffect | Vormingsfase | Werking | Bronhouding |
|---|---|---|---|
| normerend | ordening / vastlegging | conditioneel | canon-gebonden |

- **Betekeniseffect** — *normerend*: stelt canonieke werkwoorden vast als verplichte norm voor intent-naming
- **Vormingsfase** — *ordening / vastlegging*: formaliseert naamgevingsconventies als onderdeel van agent-contract-ontwerp
- **Werking** — *conditioneel*: stelt voorwaarden voor welke intent-namen geldig zijn; niet-canonieke werkwoorden worden geweigerd
- **Bronhouding** — *canon-gebonden*: canonieke werkwoorden zijn leidend en uitsluitend afkomstig uit de Mandarin-canon

---

## 1. Doel en scope

Deze doctrine normeert **intent-naming** voor agents binnen het Mandarin-ecosysteem. Elke intent-naam maakt via een canoniek werkwoord direct duidelijk:

- het architectonisch effect (betekeniseffect)
- de aard van de interventie (werking)

Zij borgt dat:

- intent-namen voorspelbaar, consistent en uitlegbaar zijn;
- het canonieke werkwoord de architectonische werking reflecteert;
- niet-canonieke werkwoorden worden geweigerd.

**Buiten scope**:
- Agent-classificatie zelf (dit is bepaald in agent-charters)
- Naamgeving van artefacten of bestanden
- Interne logica van agent-executie

---

## 2. Kernprincipes en naamgevingsconventie

### 2.1 — Eén werking, één canoniek werkwoord

Elke werking (en bijbehorend betekeniseffect) kent exact één canoniek werkwoord voor intent-naming. Dit werkwoord is verplicht leidend in de intent-naam.

### 2.2 — Intent-naming volgt architectonische werking

Het canonieke werkwoord reflecteert de architectonische transformatie die de agent uitvoert. De intent-naam mag nooit het ware effect of de werking verhullen.

### 2.3 — Naamgevingsconventie

Het formaat voor elke intent is:

```
{werkwoord}-{object}[-{context}]
```

Regels:
1. Werkwoord altijd in gebiedende wijs, kleine letters
2. Object in kebab-case
3. Context optioneel, voor specificatie
4. Geen lidwoorden
5. Altijd het canonieke werkwoord voor de werking gebruiken

### 2.4 — Kritische verschillen expliciet

Werkwoorden met verschillende architectonische werking mogen niet worden verward. Zie de toelichting en matrix in `mandarin-ecosysteem-ordeningsconcepten.md`.

### 2.5 — Validatie

Een intent met een niet-canoniek werkwoord wordt geweigerd. Alleen de vastgestelde werkwoorden per werking/betekeniseffect zijn toegestaan.

---

## 3. Canonieke werkwoorden per werking/betekeniseffect

| Werking | Betekeniseffect | Canoniek werkwoord |
|---|---|---|
| Inhoudelijk | Beschrijvend | `beschrijf` |
| Inhoudelijk | Beschrijvend | `maak-overzicht` |
| Inhoudelijk | Structurerend | `structureer` |
| Inhoudelijk | Normerend | `definieer` |
| Inhoudelijk | Constituerend | `constitueer` |
| Inhoudelijk | Normerend | `leg-vast` |
| Inhoudelijk | Realiserend | `realiseer` |
| Inhoudelijk | Evaluerend | `beoordeel` |
| Conditioneel | Validerend | `valideer` |
| Conditioneel | Rangschikkend | `orden` |
| Representatie-omvormend | Beschrijvend | `zet om` / `vat samen` |

---

## 4. Voorbeelden

**Correcte voorbeelden**:

- `beschrijf-agent-contract`
- `realiseer-database-schema`
- `definieer-themas-werkvoorbereiding`
- `constitueer-doctrine`
- `beoordeel-consistentie-charter`
- `leg-vast-doctrine-wijziging`
- `valideer-tegen-doctrine`
- `orden-workspace`
- `structureer-documenten`
- `zet-om-yaml-naar-json`

**Niet-toegestane voorbeelden**:

- `analyseer-agent` (gebruik `beschrijf-agent`)
- `controleer-contract` (gebruik `valideer-contract`)
- `bouw-database` (gebruik `realiseer-database`)
- `organiseer-documenten` (gebruik `structureer-documenten`)
- `transformeer-bestand` (gebruik `zet-om-bestand`)
- `reviewe-charter` (gebruik `beoordeel-charter`)

---

## 5. Architectonische werking per werkwoord

### 5.1 — `beschrijf` (Inhoudelijk / Beschrijvend)

**Werking**: Legt vast wat is, zonder oordeel of transformatie  
**Effect**: Observatie → expliciete beschrijving

| Intent-patroon | Voorbeeld |
|---|---|
| `beschrijf-{object}` | `beschrijf-agent` |
| `beschrijf-{aspect}-{object}` | `beschrijf-structuur-document` |

**Niet toegestaan**: `analyseer` (impliceert interpretatie), `documenteer` (te breed)

### 5.2 — `definieer` (Inhoudelijk / Normerend)

**Werking**: Bepaalt wat binnen scope bestaat, legt normering vast  
**Effect**: Chaos → gedefinieerde scope

| Intent-patroon | Voorbeeld |
|---|---|
| `definieer-{scope}` | `definieer-themas` |
| `definieer-{concept}` | `definieer-agent-contract` |

**Niet toegestaan**: `bepaal` (te zwak), `normeer`

### 5.3 — `constitueer` (Inhoudelijk / Constituerend)

**Werking**: Schept het normatieve kader zelf  
**Effect**: Intentie → normatief kader (doctrine, constitutie, beleid)

| Intent-patroon | Voorbeeld |
|---|---|
| `constitueer-{norm}` | `constitueer-doctrine` |
| `constitueer-{governance}` | `constitueer-constitutie` |

**Verschil met definieer**: `constitueer` schept het kader, `definieer` bepaalt wat binnen het kader valt

### 5.4 — `structureer` (Inhoudelijk / Structurerend)

**Werking**: Brengt structuur aan in bestaande elementen of content  
**Effect**: Ongestructureerde elementen → gestructureerd geheel

| Intent-patroon | Voorbeeld |
|---|---|
| `structureer-{object}` | `structureer-artefacten` |
| `structureer-{content}` | `structureer-documenten` |

**Niet toegestaan**: `organiseer` (te algemeen), `orden` (zie conditioneel)

### 5.5 — `realiseer` (Inhoudelijk / Realiserend)

**Werking**: Realiseert active structure (applicatielaag) of produceert concreet artefact  
**Effect**: Ontwerp/specificatie → werkende structuur of concreet artefact

| Intent-patroon | Voorbeeld |
|---|---|
| `realiseer-{structuur}` | `realiseer-database-schema` |
| `realiseer-{artefact}` | `realiseer-charter` |

**Niet toegestaan**: `bouw` (te specifiek), `implementeer` (anglicisme), `schrijf`, `maak`

### 5.6 — `beoordeel` (Inhoudelijk / Evaluerend)

**Werking**: Geeft kwalitatief oordeel zonder te beslissen  
**Effect**: Artefact → oordeel over kwaliteit/consistentie

| Intent-patroon | Voorbeeld |
|---|---|
| `beoordeel-{kwaliteitskenmerk}` | `beoordeel-consistentie` |
| `beoordeel-{object}-op-{norm}` | `beoordeel-contract-op-doctrine` |

**Niet toegestaan**: `evalueer` (te formeel), `reviewe` (anglicisme)

### 5.7 — `leg-vast` (Inhoudelijk / Normerend)

**Werking**: Wijzigt of stelt governance-spelregels vast  
**Effect**: Bestaande norm → gewijzigde/nieuwe norm

| Intent-patroon | Voorbeeld |
|---|---|
| `leg-vast-{governance}` | `leg-vast-doctrine-aanpassing` |
| `leg-vast-{besluit}` | `leg-vast-naming-conventie` |

### 5.8 — `valideer` (Conditioneel / Validerend)

**Werking**: Binaire check tegen vastgestelde norm  
**Effect**: Artefact + Norm → pass/fail

| Intent-patroon | Voorbeeld |
|---|---|
| `valideer-{object}` | `valideer-contract` |
| `valideer-tegen-{norm}` | `valideer-tegen-doctrine` |

**Niet toegestaan**: `check` (anglicisme), `controleer` (te algemeen)

### 5.9 — `orden` (Conditioneel / Rangschikkend)

**Werking**: Brengt bestaande elementen in logische volgorde  
**Effect**: Chaos → geordende structuur (zonder inhoud te wijzigen)

| Intent-patroon | Voorbeeld |
|---|---|
| `orden-{object}` | `orden-workspace` |
| `orden-{object}-op-{criterium}` | `orden-agents-op-classificatie` |

**Niet toegestaan**: `sorteer` (te mechanisch), `rangschik` (te literair)

### 5.10 — `zet om` / `vat samen` (Representatie-omvormend)

**Werking**: Vorm zonder betekeniswijziging  
**Effect**: Vorm A → Vorm B (zelfde betekenis)

| Intent-patroon | Voorbeeld |
|---|---|
| `zet-om-{bron}-naar-{doel}` | `zet-om-yaml-naar-json` |
| `vat-samen-{object}` | `vat-samen-rapport` |

**Niet toegestaan**: `converteer` (anglicisme), `transformeer` (te abstract)

---

## 6. Reikwijdte en grenzen

Deze doctrine:

- **Normeert** intent-naming voor alle agents binnen het Mandarin-ecosysteem;
- **Koppelt** canonieke werkwoorden aan werking en betekeniseffect;
- **Handhaaft** consistentie door niet-canonieke werkwoorden te weigeren;
- **Faciliteert** architectonische helderheid door werking in naam te reflecteren.

---

## 7. Relatie tot andere doctrines

| Doctrine | Relatie |
|---|---|
| `doctrine.agent-charter-normering.md` | Charters definiëren intents; intent-naming normeert de naamgeving van die intents |
| `mandarin-ecosysteem-ordeningsconcepten.md` | Bron van de orthogonale assen en canonieke werkwoordmatrix |

---

## Changelog

| Datum | Versie | Wijziging | Uitvoer door |
|---|---|---|---|
| 2026-04-15 | 2.1.0 | Herkomstverantwoording toegevoegd; naam gecorrigeerd naar `Doctrine —`; value-stream gecorrigeerd naar lowercase `aeo`; Classificatie herschreven als standaard tabel; sectiestructuur opgeschoond en genummerd; §7 Relatie tot andere doctrines toegevoegd; Canonieke essentie verwijderd; Change Log hernoemd naar Changelog | Hans Blok |
| 2026-03-01 | 2.0.0 | Volledig herschreven: structuur, assen en terminologie uit canon, koppeling intent-naming aan werking en betekeniseffect, validatie en matrix expliciet | Constitutioneel Auteur |
| 2026-02-15 | 1.3.0 | Werkwoord `structureer` toegevoegd voor classificatie Structurerend | — |
| 2026-02-14 | 1.2.0 | Werkwoord `constitueer` toegevoegd voor scheppen van normatieve kaders | — |
| 2026-02-14 | 1.1.0 | Synoniemen verwijderd: alleen canonieke werkwoorden toegestaan | — |
| 2026-02-14 | 1.0.0 | Initiële doctrine: canonieke werkwoorden per agent-classificatie vastgesteld | — |

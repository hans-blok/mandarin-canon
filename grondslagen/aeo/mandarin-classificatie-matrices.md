# Mandarin Agent Classificatie Matrices

Dit document bevat de combinatiematrices voor de vier orthogonale assen van de **mandarin-agent-classificatie**. 
De matrices tonen welke combinaties van as-posities architectonisch mogelijk en logisch zijn binnen het Mandarin-ecosysteem.

**Legenda:**
- 🟢 **Mogelijk**: Deze combinatie is logisch, toegestaan en komt voor in het ecosysteem.
- 🔴 **Niet mogelijk / Incompatibel**: Deze combinatie is architectonisch tegenstrijdig of betekenisloos.

> **Let op inzake Bronhouding:** De matrices tonen de architectonische positionering op de as *Bronhouding*. Deze positie wordt in de praktijk altijd geoperationaliseerd door een expliciet **Bronregime**, dat de concrete regels voor toegestane bronnen, interpretatie en herleidbaarheid vastlegt.

---

## 1. Betekeniseffect vs. Werking

| Betekeniseffect \ Werking | Inhoudelijk | Representatie-omvormend | Conditioneel |
| :--- | :---: | :---: | :---: |
| **Geen betekenis (Nul-positie)** | 🔴 | 🟢 | 🟢 |
| **Registrerend** | 🟢 | 🔴 | 🔴 |
| **Structurerend** | 🟢 | 🔴 | 🔴 |
| **Vastleggend** | 🟢 | 🔴 | 🔴 |
| **Interpreterend** | 🟢 | 🔴 | 🔴 |
| **Vastleggend** | 🟢 | 🔴 | 🔴 |

*Toelichting incompatibiliteiten:*
- **Geen betekenis (Nul-positie)** is incompatibel met **Inhoudelijk**, omdat inhoudelijke werking per definitie een betekeniseffect heeft.
- **Representatie-omvormend** is betekenis-blind. Het transformeert vorm, maar heeft geen betekeniseffect (Nul-positie).
- **Conditioneel** werkt op voorwaarden en hygiëne, en heeft geen betekeniseffect op inhoudelijke artefacten (Nul-positie).

---

## 2. Betekeniseffect vs. Interventieniveau

| Betekeniseffect \ Interventieniveau | Werk | Ontwerp | Architectuur | Ecosysteem |
| :--- | :---: | :---: | :---: | :---: |
| **Geen betekenis (Nul-positie)** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Registrerend** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Structurerend** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Vastleggend** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Interpreterend** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Vastleggend** | 🟢 | 🟢 | 🟢 | 🟢 |

*Alle combinaties zijn hier mogelijk. Een agent kan op elk niveau beschrijven, structureren, realiseren, evalueren, normeren, of voorwaarden bewaken zonder betekeniseffect.*

---

## 3. Betekeniseffect vs. Bronhouding

| Betekeniseffect \ Bronhouding | Input-gebonden | Canon-gebonden | Externe-bron gebonden | Exploratief |
| :--- | :---: | :---: | :---: | :---: |
| **Geen betekenis (Nul-positie)** | 🟢 | 🟢 | 🔴 | 🔴 |
| **Registrerend** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Structurerend** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Vastleggend** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Interpreterend** | 🔴 | 🟢 | 🟢 | 🟢 |
| **Vastleggend** | 🔴 | 🟢 | 🔴 | 🟢 |

*Toelichting incompatibiliteiten:*
- **Geen betekenis (Nul-positie) + Externe-bron/Exploratief**: Een agent zonder betekeniseffect (zoals een formatter of linter) mag geen externe bronnen raadplegen of exploratief genereren, omdat dit het risico op onbedoelde betekeniswijziging introduceert.
- **Interpreterend/Vastleggend + Input-gebonden**: Evalueren en normeren vereisen oordeelsvorming, interpretatie of autoriteit. Dit kan niet puur input-gebonden (input=output) zonder externe kennis of regels.
- **Vastleggend + Externe-bron gebonden**: Het puur ophalen van bestaande informatie (retrieval) kan geen nieuwe normen stellen; normeren vereist exploratieve synthese of canon-gebonden afleiding.

---

## 4. Werking vs. Interventieniveau

| Werking \ Interventieniveau | Werk | Ontwerp | Architectuur | Ecosysteem |
| :--- | :---: | :---: | :---: | :---: |
| **Inhoudelijk** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Representatie-omvormend** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Conditioneel** | 🟢 | 🔴 | 🔴 | 🟢 |

*Toelichting incompatibiliteiten:*
- **Conditioneel + Ontwerp/Architectuur**: Conditionele agents bewaken randvoorwaarden (zoals git, bestandsstructuur op ecosysteem- of werkniveau), maar ontwerpen of structureren geen architectuur.

---

## 5. Werking vs. Bronhouding

| Werking \ Bronhouding | Input-gebonden | Canon-gebonden | Externe-bron gebonden | Exploratief |
| :--- | :---: | :---: | :---: | :---: |
| **Inhoudelijk** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Representatie-omvormend** | 🟢 | 🔴 | 🔴 | 🔴 |
| **Conditioneel** | 🟢 | 🟢 | 🔴 | 🔴 |

*Toelichting incompatibiliteiten:*
- **Representatie-omvormend + Niet-input-gebonden**: Een pure vormtransformatie (bijv. Markdown naar XML) is per definitie input-gebonden en heeft geen canon, externe bronnen of exploratieve generatieve AI nodig (en mag dit ook niet gebruiken om hallucinaties te voorkomen).
- **Conditioneel + Externe-bron/Exploratief**: Hygiëne en voorwaarden (zoals linting, workspace checks) zijn input-gebonden of hooguit canon-gebonden (regels toepassen), maar vereisen geen exploratieve generatieve AI of open retrieval.

---

## 6. Interventieniveau vs. Bronhouding

| Interventieniveau \ Bronhouding | Input-gebonden | Canon-gebonden | Externe-bron gebonden | Exploratief |
| :--- | :---: | :---: | :---: | :---: |
| **Werk** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Ontwerp** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Architectuur** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Ecosysteem** | 🟢 | 🟢 | 🟢 | 🟢 |

*Alle combinaties zijn hier mogelijk. Op elk interventieniveau kan elke bronhouding worden aangenomen, afhankelijk van de specifieke taak van de agent.*

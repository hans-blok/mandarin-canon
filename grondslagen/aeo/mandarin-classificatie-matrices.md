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
| **Beschrijvend** | 🟢 | 🔴 | 🔴 |
| **Realiserend** | 🟢 | 🔴 | 🔴 |
| **Evaluerend** | 🟢 | 🔴 | 🔴 |
| **Normerend** | 🟢 | 🔴 | 🔴 |

*Toelichting incompatibiliteiten:*
- **Representatie-omvormend** is betekenis-blind. Het transformeert vorm, maar heeft geen betekeniseffect.
- **Conditioneel** werkt op voorwaarden en hygiëne, en heeft geen betekeniseffect op inhoudelijke artefacten.
*(Opmerking: Agents die niet Inhoudelijk zijn, scoren in de praktijk 'N.v.t.' op de as Betekeniseffect, wat hier als 🔴 is weergegeven voor de reguliere categorieën).*

---

## 2. Betekeniseffect vs. Interventieniveau

| Betekeniseffect \ Interventieniveau | Werk | Ontwerp | Architectuur | Ecosysteem |
| :--- | :---: | :---: | :---: | :---: |
| **Beschrijvend** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Realiserend** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Evaluerend** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Normerend** | 🟢 | 🟢 | 🟢 | 🟢 |

*Alle combinaties zijn hier mogelijk. Een agent kan op elk niveau beschrijven, realiseren, evalueren of normeren.*

---

## 3. Betekeniseffect vs. Bronhouding

| Betekeniseffect \ Bronhouding | Input-gebonden | Canon-gebonden | Externe-bron gebonden | Vrij |
| :--- | :---: | :---: | :---: | :---: |
| **Beschrijvend** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Realiserend** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Evaluerend** | 🔴 | 🟢 | 🟢 | 🟢 |
| **Normerend** | 🔴 | 🟢 | 🔴 | 🟢 |

*Toelichting incompatibiliteiten:*
- **Evaluerend/Normerend + Input-gebonden**: Evalueren en normeren vereisen oordeelsvorming, interpretatie of autoriteit. Dit kan niet puur input-gebonden (input=output) zonder externe kennis of regels.
- **Normerend + Externe-bron gebonden**: Het puur ophalen van bestaande informatie (retrieval) kan geen nieuwe normen stellen; normeren vereist vrije synthese of canon-gebonden afleiding.

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

| Werking \ Bronhouding | Input-gebonden | Canon-gebonden | Externe-bron gebonden | Vrij |
| :--- | :---: | :---: | :---: | :---: |
| **Inhoudelijk** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Representatie-omvormend** | 🟢 | 🔴 | 🔴 | 🔴 |
| **Conditioneel** | 🟢 | 🟢 | 🔴 | 🔴 |

*Toelichting incompatibiliteiten:*
- **Representatie-omvormend + Niet-input-gebonden**: Een pure vormtransformatie (bijv. Markdown naar XML) is per definitie input-gebonden en heeft geen canon, externe bronnen of vrije generatieve AI nodig (en mag dit ook niet gebruiken om hallucinaties te voorkomen).
- **Conditioneel + Externe-bron/Vrij**: Hygiëne en voorwaarden (zoals linting, workspace checks) zijn input-gebonden of hooguit canon-gebonden (regels toepassen), maar vereisen geen vrije generatieve AI of open retrieval.

---

## 6. Interventieniveau vs. Bronhouding

| Interventieniveau \ Bronhouding | Input-gebonden | Canon-gebonden | Externe-bron gebonden | Vrij |
| :--- | :---: | :---: | :---: | :---: |
| **Werk** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Ontwerp** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Architectuur** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Ecosysteem** | 🟢 | 🟢 | 🟢 | 🟢 |

*Alle combinaties zijn hier mogelijk. Op elk interventieniveau kan elke bronhouding worden aangenomen, afhankelijk van de specifieke taak van de agent.*

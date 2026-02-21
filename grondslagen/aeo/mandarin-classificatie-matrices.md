# Mandarin Agent Classificatie Matrices

Dit document bevat de combinatiematrices voor de vier orthogonale assen van de **mandarin-agent-classificatie**. 
De matrices tonen welke combinaties van as-posities architectonisch mogelijk en logisch zijn binnen het Mandarin-ecosysteem.

**Legenda:**
- 🟢 **Mogelijk**: Deze combinatie is logisch, toegestaan en komt voor in het ecosysteem.
- 🔴 **Niet mogelijk / Incompatibel**: Deze combinatie is architectonisch tegenstrijdig of betekenisloos.

---

## 1. Betekeniseffect vs. Werking

| Betekeniseffect \ Werking | Inhoudelijk | Representatie-omvormend | Conditioneel |
| :--- | :---: | :---: | :---: |
| **Beschrijvend** | 🟢 | 🟢 | 🟢 |
| **Realiserend** | 🟢 | 🔴 | 🔴 |
| **Evaluerend** | 🟢 | 🔴 | 🟢 |
| **Normerend** | 🟢 | 🔴 | 🟢 |

*Toelichting incompatibiliteiten:*
- **Representatie-omvormend** is betekenis-blind. Het kan alleen een vorm transformeren (beschrijvend), maar geen nieuwe betekenis realiseren, evalueren of normeren.
- **Conditioneel + Realiserend**: Conditionele agents bewaken randvoorwaarden en hygiëne, maar realiseren geen inhoudelijke domein-artefacten.

---

## 2. Betekeniseffect vs. Epistemische houding

| Betekeniseffect \ Epistemische houding | Deterministisch | Canon-gebonden | Retrieval-gebonden | Generatief |
| :--- | :---: | :---: | :---: | :---: |
| **Beschrijvend** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Realiserend** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Evaluerend** | 🔴 | 🟢 | 🟢 | 🟢 |
| **Normerend** | 🔴 | 🟢 | 🔴 | 🟢 |

*Toelichting incompatibiliteiten:*
- **Evaluerend/Normerend + Deterministisch**: Evalueren en normeren vereisen oordeelsvorming, interpretatie of autoriteit. Dit kan niet puur deterministisch (input=output) zonder externe kennis of regels.
- **Normerend + Retrieval-gebonden**: Het puur ophalen van bestaande informatie (retrieval) kan geen nieuwe normen stellen; normeren vereist generatieve synthese of canon-gebonden afleiding.

---

## 3. Werking vs. Epistemische houding

| Werking \ Epistemische houding | Deterministisch | Canon-gebonden | Retrieval-gebonden | Generatief |
| :--- | :---: | :---: | :---: | :---: |
| **Inhoudelijk** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Representatie-omvormend** | 🟢 | 🔴 | 🔴 | 🔴 |
| **Conditioneel** | 🟢 | 🟢 | 🔴 | 🔴 |

*Toelichting incompatibiliteiten:*
- **Representatie-omvormend + Niet-deterministisch**: Een pure vormtransformatie (bijv. Markdown naar XML) is per definitie deterministisch en heeft geen canon, retrieval of generatieve AI nodig (en mag dit ook niet gebruiken om hallucinaties te voorkomen).
- **Conditioneel + Retrieval/Generatief**: Hygiëne en voorwaarden (zoals linting, workspace checks) zijn deterministisch of hooguit canon-gebonden (regels toepassen), maar vereisen geen generatieve AI of open retrieval.

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

## 5. Betekeniseffect vs. Interventieniveau

| Betekeniseffect \ Interventieniveau | Werk | Ontwerp | Architectuur | Ecosysteem |
| :--- | :---: | :---: | :---: | :---: |
| **Beschrijvend** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Realiserend** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Evaluerend** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Normerend** | 🟢 | 🟢 | 🟢 | 🟢 |

*Alle combinaties zijn hier mogelijk. Een agent kan op elk niveau beschrijven, realiseren, evalueren of normeren.*

---

## 6. Interventieniveau vs. Epistemische houding

| Interventieniveau \ Epistemische houding | Deterministisch | Canon-gebonden | Retrieval-gebonden | Generatief |
| :--- | :---: | :---: | :---: | :---: |
| **Werk** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Ontwerp** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Architectuur** | 🟢 | 🟢 | 🟢 | 🟢 |
| **Ecosysteem** | 🟢 | 🟢 | 🟢 | 🟢 |

*Alle combinaties zijn hier mogelijk. Op elk interventieniveau kan elke epistemische houding worden aangenomen, afhankelijk van de specifieke taak van de agent.*

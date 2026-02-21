# Agent Doctrine — Agent Charter Normering

**Doctrine-ID**: `AEO.DOC.001`  
**Versie**: 2.2.0  
**Value Stream**: Agent Ecosysteem ontwikkeling 

---

## Classificatie

**Agent-classificatie**: Normerend (Betekeniseffect), Ecosysteem (Interventieniveau), Inhoudelijk (Werking), Canon-gebonden (Bronhouding)

*Voor uitleg van classificatie-assen zie [mandarin-ordeningsconcepten](../aeo/mandarin-ordeningsconcepten.md#mandarin-agent-classificatie)*

---

## 1. Doel en bestaansreden

Deze doctrine beschrijft **hoe het agent-ecosysteem zichzelf ordent** door gemeenschappelijke ontwerpprincipes voor agent-charters.

Zij stelt kaders voor:

- de architectuur van agent-identiteit;
- de relatie tussen verantwoordelijkheid en transparantie;
- de evolutie van het agent-ecosysteem;
- de integriteit van samenwerking tussen agents.

Deze doctrine normeert niet individuele agents, maar **het ontwerpdenken dat alle agent-charters ondersteunt**.

---

## 2. Capability boundary

Deze doctrine normeert het **ontwerpdenken voor agent-charters** door principes van expliciete identiteit, evolutionaire integriteit en transparante verantwoording te verankeren, zonder specifieke agent-gedragingen voor te schrijven.

---

## 3. Kernprincipes

### Principe 1 — Identiteit vóór Implementatie

Een agent-charter begint bij **expliciete identiteit**: wat de agent WEL is en wat hij NIET is.

Identiteit manifesteert zich in:

- een scherpe capability boundary;
- een extern observeerbaar contract;
- een consistente verantwoordelijkheid.

De ontwerprichting is:

> identiteit → contract → charter → realisatie

Niet:

> functie → rol

Een agent-charter legitimeert wat het ecosysteem van de agent mag verwachten.

---

### Principe 2 — Eenduidige Verantwoordelijkheid

Elke agent heeft **één expliciete verantwoordelijkheid**.

Verantwoordelijkheid kenmerkt zich door:

- scherpte: in één zin uit te leggen;
- volledigheid: wat WEL en wat NIET;
- duurzaamheid: onafhankelijk van implementatie.

Een agent zonder expliciete verantwoordelijkheid compromitteert het ecosysteem.

---

### Principe 3 — Charter als Ecosysteem-Integrator

Het charter integreert de agent in het ecosysteem door:

- identiteit te formaliseren;
- samenwerking te reguleren;
- evolutie mogelijk te maken.

Het charter volgt uit identiteit en contract.  
Het charter mag geen verantwoordelijkheid introduceren die niet extern observeerbaar is.

---

### Principe 4 — Scheiding van Wat en Hoe

- Contract = extern observeerbaar gedrag  
- Charter = ecosysteem-legitimatie  
- Implementatie = technische realisatie  

Verandering in implementatie mag nooit identiteit of contract compromitteren.

---

### Principe 5 — Evolutionaire Integriteit

Agents evolueren **zonder het ecosysteem te breken**.

Evolutie respecteert:

- **Contractstabiliteit**: bestaande verwachtingen blijven geldig;
- **Identiteitscoherentie**: de kern-verantwoordelijkheid blijft herkenbaar;
- **Transparante wijziging**: veranderingen zijn traceerbaar en begrijpelijk.

Evolutie gebeurt via semantische versioning conform conventie.

---

### Principe 6 — Ecosysteem-Cohesie

Fundamentele wijzigingen vereisen **ecosysteem-brede herbeoordeling**.

Identiteitswijziging vraagt om:

- expliciete impactanalyse op samenwerking;
- herbeoordeling van afhankelijke agents;
- transparantie naar het gehele ecosysteem.

Identiteitswijziging zonder ecosysteem-herbeoordeling compromitteert de integriteit.

---

### Principe 7 — Transparante Verantwoording

Elke agent is **verantwoordelijk voor zijn handelen** naar het ecosysteem toe.

Transparante verantwoording betekent:

- traceerbaarheid van beslissingen;
- observeerbaarheid van effecten;
- reproduceerbaarheid van resultaten.

Transparantie is een **constitutieve eigenschap** van agent-identiteit, geen optionele functionaliteit.

Een agent die zijn handelen niet transparant kan verantwoorden, handelt buiten zijn charter.

---

### Principe 8 — Architectonische Flexibiliteit

Het agent-ecosysteem is **evolueerbaar door ontwerp**.

Agents kunnen:

- hun identiteit verfijnen;
- hun verantwoordelijkheid herdefiniëren;
- hun samenwerking aanpassen.

Maar alleen binnen de kaders van:

- expliciete identiteitsherdefinitie;
- transparante ecosysteem-communicatie;
- architectonische coherentie.

---

### Principe 9 — Output-formaat Normering voor Inhoudelijke Agents

Agents die op de as **Werking de positie "Inhoudelijk"** hebben, leveren altijd een bestand als primair artefact.

Omdat deze agents betekenis begrijpen en vastleggen:

- Het **default formaat is Markdown**, tenzij expliciet anders gevraagd in de prompt;
- Alternatieve formaten (zoals YAML) worden alleen toegepast wanneer expliciet aangevraagd;
- De keuze voor het formaat wordt gedocumenteerd in de output.

Deze normering waarborgt:

- **Voorspelbaarheid**: ecosysteem-breed consistente output;
- **Flexibiliteit**: ruimte voor context-specifieke formatering;
- **Expliciete intentie**: formatwijziging vereist bewuste keuze.

---

## 4. Ontwerprichting

De creatie van een agent-charter volgt een architectonische discipline:

1. **Identiteit articuleren** — Wat is de unieke verantwoordelijkheid?  
2. **Grenzen expliciteren** — Wat wel en niet?  
3. **Contract formuleren** — Hoe observeerbaar?  
4. **Charter afleiden** — Hoe geïntegreerd in het ecosysteem?  
5. **Evolutie faciliteren** — Hoe duurzaam veranderbaar?  

---

## 5. Reikwijdte en grenzen

Deze doctrine:

- **Richt** het ontwerpdenken voor agent-charters;
- **Normeert** geen specifieke agent-implementaties;
- **Faciliteert** ecosysteem-coherentie zonder rigiditeit;
- **Ondersteunt** evolutie zonder chaos.

Deze doctrine vervangt geen individuele charter, maar **ondersteunt hun architectonische integriteit**.

---

## 6. Traceerbaarheid

Deze doctrine geldt voor:

- alle agent-charters binnen het Mandarin-ecosysteem;
- alle nieuwe agents die zich in het ecosysteem manifesteren;
- alle evolutie van bestaande agent-identiteiten.

Charters die deze doctrine incorporeren, dragen bij aan de **architectonische coherentie van het geheel**.

---

## Gerelateerde Doctrines

Deze doctrine wordt aangevuld door:

- **[doctrine-intent-naming.md](doctrine-intent-naming.md)**  
  Normeert de naming van agent-intents door canonieke werkwoorden te koppelen aan agent-classificaties. Agents met charters definiëren intents volgens deze naming-conventie.

---

## 7. Change Log

| Datum       | Versie | Wijziging                                                                 | Auteur |
|------------|--------|---------------------------------------------------------------------------|--------|
| 2026-02-21 | 2.2.0  | Classificatie en Principe 9 herschreven conform de 4 nieuwe orthogonale assen uit mandarin-ordeningsconcepten.md | Constitutioneel Auteur |
| 2026-02-13 | 2.1.0  | Principe 9 toegevoegd: output-formaat normering voor inhoudelijke agents | —      |
| 2026-02-12 | 2.0.0  | Fundamentele herziening: focus op ecosysteem-architectuur en -integriteit | —      |
| YYYY-MM-DD | 1.1.0  | Transparantie- en logplicht expliciet toegevoegd als kernprincipe        | —      |
| YYYY-MM-DD | 1.0.0  | Initiële doctrine met nadruk op Prompt First en versie-discipline         | —      |

---

### Canonieke essentie

> Een agent-charter draagt architectonische verantwoordelijkheid: het integreert identiteit, transparantie en evolutie in service van ecosysteem-coherentie.

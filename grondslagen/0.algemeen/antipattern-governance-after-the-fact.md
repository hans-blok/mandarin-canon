# Anti-pattern — Governance after the fact

**Status**: Canoniek (anti-pattern)  
**Type**: Verboden werkwijze / herkenningspatroon  
**Versie**: 1.0  
**Van toepassing op**: alle agents, runners en orkestratiecomponenten

---

## 1. Definitie

**Governance after the fact** is het patroon waarbij een agent of runner:

1. **eerst handelt** (zoekt, concludeert, genereert, wijzigt, voert uit),
2. en **pas daarna** governance raadpleegt of aanhaalt
   om het reeds uitgevoerde gedrag te rechtvaardigen of te corrigeren.

> Governance wordt dan gebruikt als *verhaal achteraf*, niet als *startvoorwaarde*.

Dit patroon maakt uitvoering **ongeldig**, ongeacht de kwaliteit van het eindresultaat.

---

## 2. Canonieke regel

> **Governance moet het startpunt van handelen zijn.**  
> Governance die pas achteraf wordt toegepast, is geen governance.

---

## 3. Signalen (hoe je dit herkent)

### Taal- en gedragsindicatoren
- “Je hebt gelijk, ik had eerst de constitutie moeten lezen…”
- “Het beleid regelt dit al, ik heb het per ongeluk genegeerd.”
- “Ik ben direct gaan zoeken in repo X in plaats van eerst canon Y te pullen.”
- “Het bestond niet” → later blijkt: “ik keek op de verkeerde plek.”

### Procesindicatoren
- er is geen **bootstrap-verklaring** vóór de eerste output;
- conclusies worden getrokken vóór value-stream-afbakening;
- er wordt gewerkt met lokale context of default aannames zonder canon-sync.

### Outputindicatoren
- output bevat verwijzingen naar governance zonder dat traceerbaar is dat die governance vooraf is toegepast;
- resultaten lijken plausibel, maar zijn niet herleidbaar naar een constitutionele start.

---

## 4. Waarom dit gevaarlijk is

Governance after the fact leidt structureel tot:
- **scope creep**: handelen buiten boundary zonder het te merken;
- **normselectie door toeval**: “welke regels heb ik toevallig gezien?”;
- **audit-falen**: je kunt niet aantonen dat regels vooraf zijn toegepast;
- **achteraf-rationalisatie**: correcte uitkomst op basis van fout proces;
- **schaal-inconsistentie**: bij groei wordt het onvoorspelbaar en onbestuurbaar.

Het probleem is niet dat de agent een fout maakt,
maar dat het systeem toestaat dat fouten **pas achteraf** worden gecorrigeerd.

---

## 5. Verboden gedrag (hard)

Het is verboden dat een agent of runner:
- een taak start zonder constitutionele bootstrapping;
- eerst zoekt/handelt en later pas de canon raadpleegt;
- governance gebruikt als justificatie na een conclusie;
- “corrigeert” zonder de eerdere output als ongeldig te markeren.

**Governance-herstel achteraf maakt de run niet geldig.**

---

## 6. Correct gedrag (wat moet er gebeuren)

Wanneer een agent merkt dat bootstrapping is overgeslagen:

1. **Stop** onmiddellijk met uitvoering.  
2. **Markeer alle reeds geproduceerde output als ongeldig** (discard).  
3. **Herstart** met constitutionele bootstrapping:
   - canon sync
   - constitutie lezen
   - value stream vaststellen
   - grondslagen afbakenen
   - bootstrap-verklaring vastleggen
4. **Escaleer** naar mens als:
   - er al wijzigingen zijn aangebracht met impact,
   - er onzekerheid is over toepasselijke value stream,
   - of er conflict is tussen grondslagen.

---

## 7. Minimale remedie-eis

Elke geldige run of taakuitvoering bevat:
- een bootstrap-verklaring vóór de eerste inhoudelijke stap,
- en traceerbaarheid naar constitutie en relevante grondslagen.

Zonder deze twee elementen is de uitvoering **niet auditbaar** en daarmee **ongeldig**.

---

## 8. Voorbeeld (typisch incident)

**Fout patroon**:
- Agent zoekt direct in `mandarin-agents`
- Concludeert: “norm bestaat niet”
- Zegt daarna: “ik had eerst canon moeten pullen”

**Correct patroon**:
- Orkestrator/agent: canon pull
- Leest constitutie
- Bepaalt value stream
- Leest grondslagen
- Pas daarna: zoekt naar norm → conclusie

---

## 9. Canoniek uitgangspunt

> **Een correct resultaat uit een fout proces is geen succes.**  
> In agentic systemen is procesdiscipline de basis van vertrouwen.

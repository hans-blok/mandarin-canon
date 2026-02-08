# Norm — Constitutionele Bootstrapping voor Agents en Runners

**Status**: Canoniek  
**Type**: Normatief (afdwingbaar)  
**Versie**: 1.0  
**Geldig vanaf**: YYYY-MM-DD  
**Van toepassing op**:  
- alle agents  
- alle runners  
- alle orkestratiecomponenten  
binnen het agent-ecosysteem

---

## 1. Doel van deze norm

Deze norm borgt dat **geen enkele agent of runner handelt zonder expliciete, aantoonbare toepassing van de constitutie**.

Zij voorkomt:
- handelen buiten governance,
- achteraf-rationalisatie van regels,
- en impliciete normselectie door agents.

> **Zonder constitutionele bootstrapping is elke handeling ongeldig.**

---

## 2. Definitie: Constitutionele bootstrapping

**Constitutionele bootstrapping** is het verplichte startproces waarbij een agent of runner:

1. de geldende constitutie raadpleegt;
2. zijn toepassingsbereik bepaalt;
3. expliciet verklaart onder welke grondslagen hij opereert;
4. pas daarna taken uitvoert.

Bootstrapping is **geen interpretatie**, maar een **entry condition**.

---

## 3. Verplichte startvolgorde (hard)

Elke agent, runner of orkestratiecomponent **MOET** bij aanvang de volgende stappen uitvoeren, in exact deze volgorde:

1. **Canon synchroniseren**  
   - Raadpleeg de centrale canon repository.
   - Synchroniseer deze (`git pull` of equivalent).
   - Indien dit niet lukt: **STOP**.

2. **Constitutie laden**  
   - Lees:  
     ```
     grondslagen/.algemeen/constitutie.md
     ```
   - Zonder succesvolle lezing: **STOP**.

3. **Value stream bepalen**  
   - Bepaal en declareer exact één primaire value stream.
   - Zonder expliciete value stream: **STOP**.

4. **Toepasselijke grondslagen afbakenen**  
   - Algemene grondslagen (`grondslagen/.algemeen/`)
   - Grondslagen van de gedeclareerde value stream
   - Geen andere grondslagen zijn toegestaan.

5. **Bootstrap-verklaring vastleggen**  
   - Leg vast (log/trace/output):
     - constitutieversie
     - value stream
     - set geraadpleegde grondslagen

Pas **na succesvolle afronding van alle stappen** mag uitvoering plaatsvinden.

---

## 4. Verplichte bootstrap-verklaring

Elke agent of runner **MOET** bij start een expliciete bootstrap-verklaring produceren.

Minimale inhoud:

- **Constitutie**: naam + versie/digest  
- **Value stream**: expliciet benoemd  
- **Grondslagenet**:
  - algemene grondslagen
  - value-stream-specifieke grondslagen
- **Datum/tijd bootstrapping**

Zonder bootstrap-verklaring is output **niet geldig**.

---

## 5. Verboden gedrag (anti-patterns)

Het is expliciet verboden dat een agent of runner:

- taken uitvoert vóór constitutionele bootstrapping;
- de constitutie pas achteraf raadpleegt;
- impliciet aannames doet over toepasselijke grondslagen;
- “corrigeert” nadat uitvoering is gestart;
- grondslagen uit andere value streams toepast zonder expliciete escalatie.

**Governance-herstel achteraf is ongeldig.**

---

## 6. Falen is correct gedrag

Wanneer constitutionele bootstrapping niet mogelijk is, geldt:

- stoppen is correct;
- escaleren is correct;
- niets doen is correct.

Doorgaan is **altijd fout**.

---

## 7. Relatie tot beleid en implementatie

- Deze norm **vervangt geen beleid**, maar **activeert** het.
- Beleidsdocumenten en grondslagen zijn **niet operationeel** zonder deze bootstrap.
- Implementatiedetails (scripts, tooling, prompts) vallen **buiten** deze norm, maar **moeten** haar afdwingen.

---

## 8. Canoniek uitgangspunt

> **Governance bestaat pas  
> wanneer zij het startpunt van handelen is.**

Constitutionele bootstrapping is daarom geen aanbeveling,  
maar een **voorwaarde voor bestaan** binnen het agent-ecosysteem.

# Norm — Deterministische Runners in Agentic Systemen

**Status**: Canoniek  
**Type**: Normatief  
**Versie**: 1.0  
**Geldig vanaf**: YYYY-MM-DD  
**Eigenaar**: Canon Architectuur  
**Scope**: Alle agentic systemen binnen dit ecosysteem

---

## 1. Doel en positie van deze norm

Deze norm beschrijft **wat een runner is**, **wat een runner niet is**, en **aan welke voorwaarden elke runner moet voldoen** om betrouwbaar, schaalbaar en bestuurbaar ingezet te kunnen worden in een agentic systeem.

Deze norm is **technologie-onafhankelijk**.  
Zij geldt ongeacht of runners zijn geïmplementeerd in Python, PowerShell, Bash, Go of een andere uitvoeringsvorm.

> **Deze norm is leidend boven individuele runner-implementaties.**  
> Code is altijd ondergeschikt aan dit document.

---

## 2. Definitie: Runner

Een **runner** is een **deterministische uitvoeringscomponent** die:

- een expliciet gedefinieerde capability uitvoert;
- wordt aangeroepen via één of meer **front doors (contracts)**;
- geen autonome intelligentie bevat;
- geen interpretatieve beslissingen neemt buiten zijn contract.

Een runner **denkt niet**, **redeneert niet**, en **improviseert niet**.  
Een runner **voert uit**.

---

## 3. Principe: Contract-first uitvoering

Elke runner bestaat uitsluitend bij de gratie van een expliciet contract.

Dit contract:
- definieert **wanneer** de runner mag starten;
- specificeert **welke inputs** geldig zijn;
- beschrijft **welke outputs** worden geproduceerd;
- bepaalt **wat succes en falen betekenen**.

> **Zonder contract bestaat een runner architectonisch niet.**

---

## 4. Front Doors als canoniek concept

### Definitie
Een **front door** is een formeel, observeerbaar en afdwingbaar aanroepmechanisme van een runner.

Voorbeelden:
- CLI-parameters
- configuratiebestanden
- API-calls
- events of schedules

### Normen
Elke front door:
- valideert input vóór uitvoering;
- faalt expliciet bij ongeldige input;
- produceert voorspelbare exit-codes;
- laat geen impliciete aannames toe.

Front doors **vervangen** impliciete scripts en handmatige aanroepen.

---

## 5. Determinisme als harde eis

Elke runner moet deterministisch zijn.

Dat betekent:
- dezelfde geldige input → hetzelfde resultaat;
- geen verborgen afhankelijkheden;
- geen niet-geregistreerde externe invloeden.

Indien determinisme niet haalbaar is:
- moet dit expliciet worden vastgelegd;
- en moet de runner escaleren in plaats van “best effort” gedrag vertonen.

---

## 6. Idempotency en herhaalbaarheid

Runners moeten herhaalbaar zijn zonder ongewenste neveneffecten.

Elke runner:
- definieert expliciet hoe herhaalde uitvoering wordt afgehandeld;
- documenteert zijn idempotency-strategie;
- voorkomt stille duplicatie of datacorruptie.

---

## 7. Input Quality Gates

Een runner **mag niet starten** tenzij:

- alle verplichte inputs aanwezig zijn;
- inputformaten valide zijn;
- referenties en paden bestaan;
- aannames expliciet zijn en beperkt blijven (maximaal 3).

Input-validatie is geen optimalisatie, maar een **verplichting**.

---

## 8. Output Quality Gates

Een runner is alleen succesvol wanneer:

- alle verwachte outputs zijn geproduceerd;
- outputs intern consistent zijn;
- outputs traceerbaar zijn naar input en run-id;
- waarschuwingen expliciet zijn vastgelegd.

“Half werk” of “gedeeltelijk succes” is geen geldige eindstatus.

---

## 9. Observability en traceerbaarheid

Elke run moet minimaal vastleggen:

- een unieke run-id;
- start- en eindtijd;
- input-fingerprint (zonder gevoelige data);
- output-referenties;
- expliciete warnings en errors.

> Wat niet traceerbaar is, is niet bestuurbaar.

---

## 10. Falen, stoppen en escaleren

Runners:
- stoppen expliciet bij fouten;
- maskeren geen problemen;
- escaleren wanneer regels of grenzen worden overschreden.

Escalatie is geen fout, maar een **kwaliteitsmechanisme**.

---

## 11. Scheiding van rollen

Binnen een agentic systeem geldt strikt:

- **Agents**: interpreteren, beslissen, adviseren.
- **Runners**: voeren deterministisch uit.
- **Orkestratie**: bepaalt volgorde en samenhang.

Een runner bevat nooit:
- businesslogica;
- strategische afwegingen;
- adaptief gedrag.

---

## 12. Anti-patterns (verboden)

Een runner mag nooit:

- impliciete aannames maken;
- stil falen;
- outputs produceren zonder trace;
- scope uitbreiden zonder nieuw contract;
- afhankelijk zijn van niet-gedocumenteerde context.

---

## 13. Canoniek uitgangspunt

> **Stabiele agentic systemen ontstaan niet door slimme code,  
> maar door expliciete grenzen.**

Deze norm borgt die grenzen.

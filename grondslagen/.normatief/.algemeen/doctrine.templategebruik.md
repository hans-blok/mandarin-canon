---
type: doctrine
naam: Doctrine — Templategebruik en Structuurborging
code: DTPL
versie: 1.1.0
digest: tbd0
status: vers
---
# Doctrine — Templategebruik en Structuurborging

---

## Herkomstverantwoording

Dit normatief artefact is opgesteld op basis van de volgende bronnen:

**Geraadpleegde bronnen**:
- mandarin-domeinconcepten.md — concept Template en relatie met prompt en artefactstructuur (gelezen op 2026-04-08)
- doctrine-agent-charter-normering.md — bestaande contractstructuur met `template` als output-eigenschap (gelezen op 2026-04-08)
- mandarin.ecosysteem-coordinator.aggregeer-tasks.prompt.md — voorbeeld van prompt-frontmatter zonder template-verwijzing (gelezen op 2026-04-08)
- mandarin.ecosysteem-coordinator.genereer-instructies.prompt.md — voorbeeld van prompt-frontmatter zonder template-verwijzing (gelezen op 2026-04-08)
- Gebruikersinvoer over borging van structuur, leesbaarheid en opname van template in contract en prompt-YAML (ontvangen op 2026-04-08)

**Opsteller**: Constitutioneel Auteur  
**Doel**: Normeren hoe templates expliciet worden vastgelegd en gespiegeld tussen agent-contract en prompt-YAML

---

## Classificatie

Deze doctrine positioneert zich als volgt op de vier orthogonale assen:

| Betekeniseffect | Vormingsfase | Werking | Bronhouding |
|---|---|---|---|
| normerend | ordening / vastlegging | procedureel | canon-gebonden |

- **Betekeniseffect** — *normerend*: stelt expliciete normen voor het gebruik van templates in agent-contracten en prompt-YAML
- **Vormingsfase** — *ordening / vastlegging*: formaliseert de templatekeuze als verplicht onderdeel van het contract en de promptassemblage
- **Werking** — *procedureel*: schrijft voor hoe templates worden vastgelegd, gespiegeld en gevalideerd
- **Bronhouding** — *canon-gebonden*: baseert zich uitsluitend op canonieke agent-contracten en prompt-YAML-conventies

---

## 1. Doel en scope

Deze doctrine normeert het gebruik van **templates** als middel om:

1. structuur van output te standaardiseren;
2. leesbaarheid van artefacten te borgen;
3. intent-uitvoering voorspelbaar en toetsbaar te maken;
4. de relatie tussen **agent-contract** en prompt-YAML expliciet te houden.

De doctrine geldt voor alle intents waarvoor een mandarin-agent een artefact, document, configuratie of ander gestructureerd resultaat oplevert.

---

## 2. Normatieve uitgangspunten

### 2.1 — Template als structuurdrager

Een **template** legt de vereiste secties, volgorde en minimale vorm van output vast.

Een template:
- borgt vorm en leesbaarheid;
- ondersteunt consistente uitvoering;
- is geen vervanging van het **agent-contract**;
- is geen bron van normatieve waarheid over intent of governance.

### 2.2 — Contract is bron van waarheid

Het **agent-contract** is de normatieve bron die bepaalt welk template van toepassing is op de uitvoering van een intent.

De prompt-YAML neemt deze informatie over voor uitvoerbaarheid, maar mag die niet zelfstandig herdefiniëren.

### 2.3 — Explicietheid boven implicatie

Templategebruik mag nooit impliciet blijven.

Indien een template van toepassing is, wordt deze expliciet genoemd.
Indien geen template van toepassing is, wordt dat eveneens expliciet vastgelegd met `template: ~`.

---

## 3. Normering in agent-contracten

### 3.1 — Verplichte vastlegging

Elk **agent-contract** legt per output vast welk template van toepassing is.

**Contract-structuur:**

```yaml
intent: <intent-naam>
output:
  - type: <artefact-type>
    herkomstpositie: initierend | voortbouwend
    template: <template-pad> | ~
```

### 3.2 — Betekenis van de waarde

| Waarde | Betekenis |
|--------|-----------|
| `<template-pad>` | De output moet de structuur volgen van het aangewezen template |
| `~` | Er geldt geen afzonderlijk template; vorm volgt direct uit contract en formaat-eisen |

### 3.3 — Ontwerpregel

De template-verwijzing in het contract is:
- verplicht;
- eenduidig;
- relatief ten opzichte van de workspace waar het template wordt beheerd;
- onderdeel van de contractuele toetsbaarheid van de intent.

### 3.4 — Voorbeelden

```yaml
# Voorbeeld: document met expliciet template
intent: definieer-concept
output:
  - type: concept-definitie
    herkomstpositie: initierend
    template: templates/concept.template.md
```

```yaml
# Voorbeeld: configuratie zonder apart template
intent: aggregeer-tasks
output:
  - type: tasks-configuratie
    herkomstpositie: initierend
    template: ~
```

---

## 4. Normering in prompt-YAML

### 4.1 — Verplichte spiegeling

De prompt-YAML bevat eveneens een `template`-eigenschap.

Deze eigenschap spiegelt de contractuele template-keuze zodat tijdens uitvoering direct zichtbaar is welke structuur verwacht wordt.

**Prompt-frontmatter:**

```yaml
---
agent: mandarin.<agent>
intent: <intent>
template: <template-pad> | ~
bronhouding: <bronhouding>
versie: <versie>
value_stream_fase: <vs.fase>
---
```

### 4.2 — Afgeleide status

De `template`-eigenschap in prompt-YAML is afgeleid van het **agent-contract**.

Daarom geldt:
- contract eerst;
- prompt-YAML daarna;
- bij mismatch heeft het contract voorrang;
- een mismatch is een validatiefout.

### 4.3 — Doel van opname in prompt-YAML

Opname van het template in prompt-YAML dient om:
- de agent direct te informeren over de beoogde structuur;
- prompt-assemblage controleerbaar te maken;
- debugging en validatie te vereenvoudigen;
- ambiguiteit tussen intent en outputvorm te voorkomen.

---

## 5. Consistentieregels

Een intent-definitie is alleen consistent als aan alle onderstaande voorwaarden is voldaan:

1. het **agent-contract** bevat voor elke output een `template`-eigenschap;
2. de prompt-YAML bevat een `template`-eigenschap;
3. de waarde in prompt-YAML is gelijk aan de contractuele waarde voor de primaire output van de intent;
4. het aangewezen template-pad bestaat, tenzij de waarde `~` is;
5. de runner of validator behandelt een mismatch als fout of escalatiepunt, niet als stil herstel.

---

## 6. Runner- en validatiegedrag

### 6.1 — Runner

De runner of prompt-assembler:
- leest het template primair uit het **agent-contract**;
- controleert of prompt-YAML dezelfde waarde bevat;
- logt een afwijking expliciet;
- mag geen alternatieve template afleiden uit documentinhoud of bestandsnaam alleen.

### 6.2 — Validator

Een validator of curator controleert minimaal:
- aanwezigheid van `template` in contract;
- aanwezigheid van `template` in prompt-YAML;
- gelijkheid tussen beide waarden;
- bestaan van het referenced template-bestand wanneer geen `~` is opgegeven.

---

## 7. Grenzen en uitzonderingen

### 7.1 — Wanneer `template: ~` is toegestaan

`template: ~` is toegestaan wanneer:
- het resultaat primair machine-configuratie is;
- het contract de volledige vorm al voldoende specificeert;
- er geen herbruikbare documentstructuur nodig is;
- introductie van een apart template geen extra helderheid oplevert.

### 7.2 — Wat niet is toegestaan

Niet toegestaan is:
- een intent uitvoeren op basis van een impliciet template;
- een prompt-YAML met een andere template dan het contract;
- een template-pad gebruiken dat niet bestaat zonder expliciete `~`;
- templatekeuze verbergen in vrije tekst buiten contract of frontmatter.

---

## 8. Verantwoordelijkheden

| Verantwoordelijkheid | Rol |
|----------------------|-----|
| Vastleggen van template in agent-contract | Contract-auteur |
| Spiegeling van template in prompt-YAML | Prompt-auteur / agent-engineer |
| Controle op consistentie tussen contract en prompt | Runner / Agent-curator |
| Beheer van template-bestanden | Workspace-beheerder / canon-curator |

---

## 9. Slotbepaling

Een template is binnen Mandarin geen cosmetische voorkeur,
maar een expliciet stuurmiddel voor vormvastheid.

Wanneer een intent output oplevert,
moet zichtbaar zijn welke structuur geldt,
waar die structuur is vastgelegd
en hoe prompt en contract elkaar daarin exact volgen.

Zonder expliciete templatebinding
ontstaat variatie zonder legitimatie.

---

## Changelog

| Datum | Versie | Wijziging | Uitvoer door |
|---|---|---|---|
| 2026-04-15 | 1.1.0 | Classificatie toegevoegd; subsectiekoppen voorzien van em-dash; Wijzigingslog hernoemd naar Changelog | Hans Blok |
| 2026-04-08 | 1.0.0 | Eerste versie: templategebruik genormeerd in agent-contract en prompt-YAML | Constitutioneel Auteur |
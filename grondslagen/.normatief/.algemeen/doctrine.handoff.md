---
type: doctrine
naam: Doctrine — Handoff en Overdrachtsdiscipline
code: DHND
versie: 1.3.0
digest: tbd0
status: vers
---
# Doctrine — Handoff en Overdrachtsdiscipline

---

## Herkomstverantwoording

Dit normatief artefact is opgesteld op basis van de volgende bronnen:

**Geraadpleegde bronnen**:
- `mandarin-domeinconcepten.md` — concepten handoff, handoff-identificatie, execution-identificatie, execution-bestand (versie 2.11.0, gelezen op 2026-04-06)
- `doctrine.traceability.md` — §5 Relatie tot handoff-discipline, §6 execution-identiteit (versie 1.2.0, gelezen op 2026-04-06)
- `constitutie.md` — Artikel 5 §3 Herkomstverantwoording (versie 2.6.0, gelezen op 2026-04-06)
- `doctrine.bronhouding-en-exploratie.md` — structurele bronlaad-verantwoordelijkheid (gelezen op 2026-04-06)

**Opsteller**: Hans Blok  
**Doel**: Normering van handoff-creatie, overdrachtsdiscipline en handoff-bestand als canoniek artefacttype binnen het Mandarin-ecosysteem

---

## Classificatie

Deze doctrine positioneert zich als volgt op de vier orthogonale assen:

| Betekeniseffect | Vormingsfase | Werking | Bronhouding |
|---|---|---|---|
| normerend | ordening / vastlegging | procedureel | canon-gebonden |

- **Betekeniseffect** — *normerend*: stelt expliciete normen voor handoff-creatie en overdrachtsdiscipline
- **Vormingsfase** — *ordening / vastlegging*: structureert en formaliseert het overdrachtsproces tussen agents
- **Werking** — *procedureel*: schrijft een procedure voor voor handoff-aanmaak, escalatie en validatie
- **Bronhouding** — *canon-gebonden*: baseert zich uitsluitend op canonieke bronnen en traceability-discipline

---

## 1. Doel en scope

Deze doctrine normeert de **handoff** als expliciete overdrachtsgebeurtenis in een meervoudige agent-keten. Zij definieert:

1. De **handoff-identificatie** als unieke, door de runner gegenereerde identifier per overdrachtsgebeurtenis
2. Het **handoff-bestand** als canoniek artefact dat de ontvangende agent voorziet van voldoende context om rechtmatig te handelen
3. **Escalatie** als bijzondere variant van handoff, waarbij expliciete menselijke tussenkomst wordt gevraagd
4. De **relatie** tot de traceability-doctrine en de bronhouding-doctrine

Een handoff is de **horizontale** tegenhanger van de herkomstcode: waar de herkomstcode de verticale keten (initierend → voortbouwend) identificeert, identificeert de handoff één horizontale overdracht (agent → agent).

**Buiten scope**:
- Interne stappen binnen één agent-executie
- Automatische synchronisatie of artefact-doorgifte zonder expliciete overdrachtsintentie
- Versie- en conflictbeheer van onderliggende artefacten

---

## 2. Handoff-identificatie

### 2.1 — Definitie

Een **handoff-identificatie** is de unieke identifier van een specifieke handoff-gebeurtenis. Zij identificeert de overdracht als zelfstandige gebeurtenis, los van de `execution_code` van de betrokken executies.

### 2.2 — Formaat-conventie

```
Format:  hf-JJMM.NNNN
         │  │  │  └─── 4-cijferig volgnummer (0001–9999), per maand oplopend
         │  │  └───── Maand (01-12)
         │  └─────── Jaar (laatste 2 cijfers)
         └─────────── Vaste prefix die het artefacttype identificeert
```

**Voorbeelden**:
- `hf-2604.0001` — April 2026, eerste handoff
- `hf-2604.0002` — April 2026, tweede handoff
- `hf-2603.0017` — Maart 2026, zeventiende handoff

Het volgnummer wordt **per kalendermaand** opnieuw gestart bij `0001`. De `hf-` prefix onderscheidt de handoff-identificatie van de herkomstcode (`JJMM.XXXX`) en van de `execution_code`. Beide mogen nooit verwisseld worden.

### 2.3 — Generatie van het volgnummer

Het volgnummer wordt oplopend toegekend door de runner:

```
volgnummer = volgende_vrije_nummer(maand=JJMM, register=handoff-register)
handoff_id = "hf-" + JJMM + "." + volgnummer.zfill(4)
```

De runner houdt een **handoff-register** bij per workspace of per kalendermaand. Een eenmaal uitgegeven volgnummer wordt niet hergebruikt, ook niet bij verwijdering van het bijbehorende handoff-bestand.

**Kenmerken**:
- **Numeriek**: uitsluitend cijfers 0–9
- **Nul-gepaddeerd**: altijd 4 posities (`0001`, niet `1`)
- **Monotoon oplopend**: nooit teruggezet binnen dezelfde maand

### 2.4 — Generatie-verantwoordelijkheid

De **runner** is als enige verantwoordelijk voor het genereren van de handoff-identificatie.

- De runner genereert de handoff-id op het moment van handoff-creatie
- Agents genereren **geen** handoff-identificaties
- De gegenereerde handoff-id wordt opgenomen in het handoff-bestand

---

## 3. Handoff-bestand

### 3.1 — Definitie

Een **handoff-bestand** is een canoniek artefact dat de overdragende agent aanmaakt aan het einde van een executie, met als doel de ontvangende agent te voorzien van voldoende context, besluiten en openstaande punten om rechtmatig en informatiegedragen te kunnen handelen.

Het handoff-bestand kijkt **vooruit**: het bereidt de ontvanger voor.  
Het execution-trace-bestand kijkt **achteruit**: het legt de provenance van de afgeronde executie vast.

Beide artefacten zijn complementair en vervangen elkaar niet.

### 3.2 — Bestandsnaam-conventie

```
{handoff_id}.handoff.md
```

**Voorbeeld**: `hf-2604.0001.handoff.md`

Het bestand wordt opgeslagen in de map die is aangewezen door de workspace-doctrine van de uitvoerende workspace.

Wanneer de workspace-doctrine met **execution-bundels** werkt, geldt als normatieve locatie:

```text
executions/{execution_code}.{overdragende-agent}.{intent}/handoffs/{handoff_id}.handoff.md
```

De handoff hoort dus bij de producerende execution-bundel en niet in een generieke, losstaande handoff-map op workspace-niveau.

### 3.3 — Minimale inhoud

Een geldig handoff-bestand bevat minimaal de volgende velden:

```yaml
handoff_id: hf-JJMM.NNNN
execution_code: exec-JJMM.XXXX   # verwijzing naar opleverende executie
overdragende-agent: <agent-id>
ontvangende-agent: <agent-id>
overdracht-datum: JJJJ-MM-DD
samenvatting-context: |
  <wat de overdragende agent heeft uitgevoerd en opgeleverd>
genomen-beslissingen:
  - <beslissing 1>
  - <beslissing 2>
gesignaleerde-ambiguiteiten:
  - <ambiguïteit 1 — ter beoordeling aan ontvanger>
openstaande-taken:
  - <taak 1>
  - <taak 2>
human_in_the_loop: false        # true indien escalatie vereist (zie §4)
overdrachtsnota: |
  <vrije tekst met instructie of context voor de ontvanger>
```

**Verplichte velden**: `handoff_id`, `execution_code`, `overdragende-agent`, `ontvangende-agent`, `overdracht-datum`, `samenvatting-context`, `human_in_the_loop`.

**Conditioneel verplicht**: `escalatie-reden` is verplicht wanneer `human_in_the_loop: true`.

### 3.4 — Onderscheid van execution-trace-bestand

| Aspect | Handoff-bestand | Execution-trace-bestand |
|--------|-----------------|------------------------|
| **Richting** | Vooruit (naar ontvanger) | Achteruit (provenance) |
| **Doel** | Ontvanger informeren | Audit en traceerbaarheid |
| **Aangemaakt door** | Runner namens overdragende agent | Runner namens afgeronde executie |
| **Sleutel** | `handoff_id` | `execution_code` + `execution_digest` |
| **Levensduur** | Geldig tot ontvanger heeft gehandeld | Permanent archiefrecord |
| **Inhoud** | Besluiten, ambiguiteiten, taken, escalatie | Bronverwijzingen, opnamevorm, segment-id's |

Beide artefacten mogen naar elkaar verwijzen, maar zijn zelfstandige eenheden.

---

## 4. Escalatie als bijzondere handoff-variant

### 4.1 — Definitie

**Escalatie** is een bijzondere variant van handoff waarbij de overdrachtsrichting niet van agent naar agent loopt, maar van agent naar mens. Escalatie treedt op wanneer een agent een situatie tegenkomt die buiten zijn charter, bevoegdheid of beslissingscapaciteit valt.

### 4.2 — Escalatie-indicatie

Een handoff-bestand met `human_in_the_loop: true` bevat aanvullend:

```yaml
human_in_the_loop: true
escalatie-reden: |
  <beschrijving van de situatie die escalatie vereist>
escalatie-urgentie: laag | normaal | hoog
```

### 4.3 — Verplichtingen bij escalatie

Wanneer een agent escaleert:

1. **Stopt** de agent met verdere uitvoering op het geëscaleerde onderdeel
2. **Legt** de agent alle tot dan toe genomen beslissingen vast in `genomen-beslissingen`
3. **Beschrijft** de agent precies welke informatie of beslissing van de mens wordt verwacht
4. **Opent** de agent geen nieuwe uitvoering op het geëscaleerde onderdeel zonder expliciete vrijgave

Stilzwijgende doorzetting na een gesignaleerde escalatie is verboden.

---

## 5. Relatie tot andere doctrines

| Doctrine | Relatie |
|---|---|
| `doctrine.traceability.md` | Complementair: handoff-id is horizontaal, herkomstcode is verticaal; runner genereert beide |
| `doctrine.bronhouding-en-exploratie.md` | Handoff-bestand is een canon-artefact en valt onder herkomstverantwoordingsverplichting |
| `doctrine.agent-charter-normering.md` | Escalatie vereist dat de agent zijn charter-grenzen erkent |
| `doctrine.retrieval-en-contextselectie.md` | Handoff-bestand is input-context voor de ontvangende agent bij retrieval |

---

## 6. Runner-logica

De runner implementeert de handoff-discipline als volgt:

```
EINDE EXECUTIE:

IF handoff is vereist:
    handoff_id = genereer_handoff_id(maand=JJMM, register=handoff-register)
    bestandsnaam = handoff_id + ".handoff.md"
    schrijf handoff-bestand(
        handoff_id = handoff_id,
        execution_code = execution_code,
        overdragende-agent = sender_agent,
        ontvangende-agent = receiving_agent,
        ...
    )
    plaats bestand in execution-bundel/handoffs/
    registreer handoff_id in execution-trace-bestand

IF human_in_the_loop == true:
    STOP verdere uitvoering op geëscaleerd onderdeel
    wacht op vrijgave van mens
```

De runner mag de handoff-id **nooit** overnemen van een eerdere executie. Elke handoff-gebeurtenis vereist een nieuw gegenereerde handoff-identificatie.

---

## 7. Validatie en governance

### 7.1 — Geldigheidsvereisten

Een handoff-bestand is geldig wanneer:

1. `handoff_id` aanwezig is en voldoet aan het `hf-JJMM.NNNN` formaat
2. `execution_code` verwijst naar een aantoonbaar bestaand execution-bestand
3. Alle verplichte velden zijn ingevuld
4. Bij `human_in_the_loop: true` is `escalatie-reden` aanwezig

### 7.2 — Verbod op retroactieve creatie

Handoff-bestanden mogen **niet retroactief** worden aangemaakt voor overdrachten die al hebben plaatsgevonden zonder expliciete vastlegging. Retroactieve handoff-bestanden zijn canoniek ongeldig en mogen niet als legitimiteitsbron worden gebruikt.

### 7.3 — Wijzigingsbeheer

Een handoff-bestand is na uitgifte onveranderlijk. Correcties worden verwerkt via een nieuw handoff-bestand met een nieuwe handoff-identificatie, waarbij het gecorrigeerde bestand expliciet verwijst naar het vorige.

---

## Changelog

| Datum | Versie | Wijziging | Uitvoer door |
|---|---|---|---|
| 2026-04-15 | 1.3.0 | Classificatie toegevoegd; subsectiekoppen voorzien van em-dash (###  N.M — Naam); §5 Relatie tot andere doctrines herschreven als standaard tabel; hernoemd naar `doctrine.handoff.md` | Hans Blok |
| 2026-04-12 | 1.2.0 | Hernoemd conform TDM: `handoff-identificatie` → `handoff_id`, `execution-identificatie` → `execution_code`, `escalatie-indicatie` → `human_in_the_loop` | Hans Blok |
| 2026-04-08 | 1.1.0 | Verduidelijkt: opslaglocatie van handoff-bestanden binnen `handoffs/` van de producerende execution-bundel | Hans Blok |
| 2026-04-06 | 1.0.0 | Initiële versie: handoff-identificatie formaat, handoff-bestand minimale inhoud, escalatie als subsectie, relaties tot traceability en bronhouding | Hans Blok |

---
type: doctrine
naam: Doctrine — Handoff en Overdrachtsdiscipline
versie: 1.0.0
digest: tbd0
status: vers
---
# Doctrine — Handoff en Overdrachtsdiscipline


---

## Herkomstverantwoording

Dit normatief artefact is opgesteld op basis van de volgende bronnen:

**Geraadpleegde bronnen**:
- mandarin-domeinconcepten.md — concepten handoff, handoff-identificatie, execution-identificatie, execution-bestand (versie 2.11.0, gelezen op 2026-04-06)
- doctrine-traceability.md — §5 Relatie tot handoff-discipline, §6 execution-identiteit (versie 1.2.0, gelezen op 2026-04-06)
- constitutie.md — Artikel 5 §3 Herkomstverantwoording (versie 2.6.0, gelezen op 2026-04-06)
- doctrine-bronhouding-en-exploratie.md — structurele bronlaad-verantwoordelijkheid (gelezen op 2026-04-06)

**Opsteller**: Hans Blok
**Doel**: Normering van handoff-creatie, overdrachtsdiscipline en handoff-bestand als canoniek artefacttype binnen het Mandarin-ecosysteem

---

## 1. Doel en scope

Deze doctrine normeert de **handoff** als expliciete overdrachtsgebeurtenis in een meervoudige agent-keten. Zij definieert:

1. De **handoff-identificatie** als unieke, door de runner gegenereerde identifier per overdrachtsgebeurtenis
2. Het **handoff-bestand** als canoniek artefact dat de ontvangende agent voorziet van voldoende context om rechtmatig te handelen
3. **Escalatie** als bijzondere variant van handoff, waarbij expliciete menselijke tussenkomst wordt gevraagd
4. De **relatie** tot de traceability-doctrine en de bronhouding-doctrine

Een handoff is de **horizontale** tegenhanger van de herkomstcode: waar de herkomstcode de verticale keten (initiërend → voortbouwend) identificeert, identificeert de handoff één horizontale overdracht (agent → agent).

**Buiten scope**:
- Interne stappen binnen één agent-executie
- Automatische synchronisatie of artefact-doorgifte zonder expliciete overdrachtsintentie
- Versie- en conflictbeheer van onderliggende artefacten

---

## 2. Handoff-identificatie

### 2.1 Definitie

Een **handoff-identificatie** is de unieke identifier van een specifieke handoff-gebeurtenis. Zij identificeert de overdracht als zelfstandige gebeurtenis, los van de execution-identificatie van de betrokken executies.

### 2.2 Formaat-conventie

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

Het volgnummer wordt **per kalendermaand** opnieuw gestart bij `0001`. De `hf-` prefix onderscheidt de handoff-identificatie van de herkomstcode (`JJMM.XXXX`) en van de execution-identificatie. Beide mogen nooit verwisseld worden.

### 2.3 Generatie van het volgnummer

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

### 2.4 Generatie-verantwoordelijkheid

De **runner** is als enige verantwoordelijk voor het genereren van de handoff-identificatie.

- De runner genereert de handoff-id op het moment van handoff-creatie
- Agents genereren **geen** handoff-identificaties
- De gegenereerde handoff-id wordt opgenomen in het handoff-bestand

---

## 3. Handoff-bestand

### 3.1 Definitie

Een **handoff-bestand** is een canoniek artefact dat de overdragende agent aanmaakt aan het einde van een executie, met als doel de ontvangende agent te voorzien van voldoende context, besluiten en openstaande punten om rechtmatig en informatiegedragen te kunnen handelen.

Het handoff-bestand kijkt **vooruit**: het bereidt de ontvanger voor.  
Het execution-trace-bestand kijkt **achteruit**: het legt de provenance van de afgeronde executie vast.

Beide artefacten zijn complementair en vervangen elkaar niet.

### 3.2 Bestandsnaam-conventie

```
{handoff-identificatie}.handoff.md
```

**Voorbeeld**: `hf-2604.0001.handoff.md`

Het bestand wordt opgeslagen in de map die is aangewezen door de workspace-doctrine van de uitvoerende workspace.

### 3.3 Minimale inhoud

Een geldig handoff-bestand bevat minimaal de volgende velden:

```yaml
handoff-identificatie: hf-JJMM.NNNN
execution-identificatie: exec-JJMM.XXXX   # verwijzing naar opleverende executie
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
escalatie-indicatie: false        # true indien escalatie vereist (zie §4)
overdrachtsnota: |
  <vrije tekst met instructie of context voor de ontvanger>
```

**Verplichte velden**: `handoff-identificatie`, `execution-identificatie`, `overdragende-agent`, `ontvangende-agent`, `overdracht-datum`, `samenvatting-context`, `escalatie-indicatie`.

**Conditioneel verplicht**: `escalatie-reden` is verplicht wanneer `escalatie-indicatie: true`.

### 3.4 Onderscheid van execution-trace-bestand

| Aspect | Handoff-bestand | Execution-trace-bestand |
|--------|-----------------|------------------------|
| **Richting** | Vooruit (naar ontvanger) | Achteruit (provenance) |
| **Doel** | Ontvanger informeren | Audit en traceerbaarheid |
| **Aangemaakt door** | Runner namens overdragende agent | Runner namens afgeronde executie |
| **Sleutel** | handoff-identificatie | execution-identificatie + execution-digest |
| **Levensduur** | Geldig tot ontvanger heeft gehandeld | Permanent archiefrecord |
| **Inhoud** | Besluiten, ambiguiteiten, taken, escalatie | Bronverwijzingen, opnamevorm, segment-id's |

Beide artefacten mogen naar elkaar verwijzen, maar zijn zelfstandige eenheden.

---

## 4. Escalatie als bijzondere handoff-variant

### 4.1 Definitie

**Escalatie** is een bijzondere variant van handoff waarbij de overdrachtsrichting niet van agent naar agent loopt, maar van agent naar mens. Escalatie treedt op wanneer een agent een situatie tegenkomt die buiten zijn charter, bevoegdheid of beslissingscapaciteit valt.

### 4.2 Escalatie-indicatie

Een handoff-bestand met `escalatie-indicatie: true` bevat aanvullend:

```yaml
escalatie-indicatie: true
escalatie-reden: |
  <beschrijving van de situatie die escalatie vereist>
escalatie-urgentie: laag | normaal | hoog
```

### 4.3 Verplichtingen bij escalatie

Wanneer een agent escaleert:

1. **Stopt** de agent met verdere uitvoering op het geëscaleerde onderdeel
2. **Legt** de agent alle tot dan toe genomen beslissingen vast in `genomen-beslissingen`
3. **Beschrijft** de agent precies welke informatie of beslissing van de mens wordt verwacht
4. **Opent** de agent geen nieuwe uitvoering op het geëscaleerde onderdeel zonder expliciete vrijgave

Stilzwijgende doorzetting na een gesignaleerde escalatie is verboden.

---

## 5. Relatie tot andere doctrines

### 5.1 Traceability-doctrine

De handoff-discipline is complementair aan de traceability-doctrine (zie ook doctrine-traceability.md §5):

| Aspect | Handoff-discipline | Traceability-discipline |
|--------|-------------------|------------------------|
| **ID-type** | handoff-identificatie | herkomstcode |
| **Scope** | Eén overdrachtsgebeurtenis | Volledige artefact-keten |
| **Richting** | Horizontaal (agent → agent) | Verticaal (initiërend → voortbouwend) |
| **Doel** | Legitimiteit van handeling | Herleidbaarheid van oorsprong |

Een artefact kan en mag zowel een **handoff-identificatie** als een **herkomstcode** bevatten. Het zijn orthogonale identifiers.

### 5.2 Bronhouding-doctrine

De bronhouding-doctrine regelt welke bronnen een agent in zijn execution-bestand opneemt. Het handoff-bestand is geen execution-bestand en valt daarom buiten de directe werkingssfeer van de bronhouding-discipline. Het handoff-bestand is echter wel een canon-artefact en moeten voldoen aan de herkomstverantwoordingsverplichting (zie Artikel 5 §3 van de constitutie).

### 5.3 Header-integratie

De herkomstcode — gegenereerd of geërfd conform de traceability-doctrine — wordt ook opgenomen in de Herkomst-sectie van het handoff-bestand:

```markdown
## Herkomst

- Herkomstcode: 2604.Ab3K
- Herkomstpositie: voortbouwend
- Initiërend artefact: <pad naar initiërend artefact>
- Gegenereerd door: <agent-id>
- Datum: 2026-04-06
- Handoff-referentie: hf-2604.0001
```

---

## 6. Runner-logica

De runner implementeert de handoff-discipline als volgt:

```
EINDE EXECUTIE:

IF handoff is vereist:
    handoff_id = genereer_handoff_id(maand=JJMM, register=handoff-register)
    bestandsnaam = handoff_id + ".handoff.md"
    schrijf handoff-bestand(
        handoff-identificatie = handoff_id,
        execution-identificatie = execution_id,
        overdragende-agent = sender_agent,
        ontvangende-agent = receiving_agent,
        ...
    )
    registreer handoff_id in execution-trace-bestand

IF escalatie-indicatie == true:
    STOP verdere uitvoering op geëscaleerd onderdeel
    wacht op vrijgave van mens
```

De runner mag de handoff-id **nooit** overnemen van een eerdere executie. Elke handoff-gebeurtenis vereist een nieuw gegenereerde handoff-identificatie.

---

## 7. Validatie en governance

### 7.1 Geldigheidsvereisten

Een handoff-bestand is geldig wanneer:

1. `handoff-identificatie` aanwezig is en voldoet aan het `hf-JJMM.NNNN` formaat
2. `execution-identificatie` verwijst naar een aantoonbaar bestaand execution-bestand
3. Alle verplichte velden zijn ingevuld
4. Bij `escalatie-indicatie: true` is `escalatie-reden` aanwezig

### 7.2 Verbod op retroactieve creatie

Handoff-bestanden mogen **niet retroactief** worden aangemaakt voor overdrachten die al hebben plaatsgevonden zonder expliciete vastlegging. Retroactieve handoff-bestanden zijn canoniek ongeldig en mogen niet als legitimiteitsbron worden gebruikt.

### 7.3 Wijzigingsbeheer

Een handoff-bestand is na uitgifte onveranderlijk. Correcties worden verwerkt via een nieuw handoff-bestand met een nieuwe handoff-identificatie, waarbij het gecorrigeerde bestand expliciet verwijst naar het vorige.

### 7.4 Versiebeheer

Dit document volgt het versiebeheerschema van de Mandarin-canon. Wijzigingen worden vastgelegd in het changelog hieronder.

---

## Changelog

| Datum | Versie | Wijziging | Uitvoer door |
|-------|--------|-----------|--------------|
| 2026-04-06 | 1.0.0 | Initiële versie: handoff-identificatie formaat, handoff-bestand minimale inhoud, escalatie als subsectie, relaties tot traceability en bronhouding | Hans Blok |

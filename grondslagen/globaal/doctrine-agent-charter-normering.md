# Doctrine — Agent-charter normering

**Type**: Doctrine  
**Repository**: mandarin-canon  
**Identifier**: mandarin-canon.doctrine.agent-charter-normering  
**Version**: 2.4.0  
**Status**: Active  
**Last Updated**: 2026-02-06  
**Owner**: Hans Blok

---

## Herkomstverantwoording

Deze doctrine is opgesteld door Constitutioneel Auteur op 1 februari 2026 als herijkte norm voor agent-charters binnen het Mandarin-ecosysteem, op basis van de vernieuwde conceptuele en ordenende grondslagen.

**Geraadpleegde bronnen**:
- grondslagen/globaal/constitutie.md (gelezen op 2026-02-01)
- grondslagen/globaal/axioma-van-gezag.md (gelezen op 2026-02-01)
- grondslagen/globaal/workspace-doctrine.md (gelezen op 2026-02-01)
- grondslagen/globaal/mandarin-ordeningsconcepten.md (versie 1.5.0, gelezen op 2026-02-01)
- grondslagen/globaal/mandarin-domeinconcepten.md (versie 2.3.0, gelezen op 2026-02-01)
- grondslagen/globaal/conceptuele-grondslagen.md (versie 1.0.0, gelezen op 2026-02-01)
- templates/agent.charter.template.md (gelezen op 2026-02-01)
- templates/type agents.md (gelezen op 2026-02-01)

**Datum**: 2026-02-01  
**Doel**: Vastleggen van normatieve regels voor inhoud, structuur, herkomst en gebruik van **agent-charters** als governance-artefacten, zodat **mandarin-agents** voorspelbaar, toetsbaar en binnen hun mandaat opereren.

**Ontwerpkeuze**: Deze doctrine maakt expliciet gebruik van de vernieuwde concepten uit mandarin-domeinconcepten (zoals **mandarin-agent**, **agent-charter**, **agent-contract**, **Template**, **Prompt**) en van de artefactclassificatie uit mandarin-ordeningsconcepten (met **Governance-artefact**, **Richtinggevend artefact**, **Realiserend artefact**, **Afgeleid artefact**). Agent-charters worden daarin gepositioneerd als **governance-artefacten** en maken gebruik van gestandaardiseerde **templates**.

**Normatief fundament**: Deze doctrine werkt de constitutie, het axioma van gezag en de workspace-doctrine uit voor het specifieke domein van **agent-charters** en is bindend voor alle **mandarin-agents** en mensen die agent-charters opstellen of wijzigen.

---

## Inhoudsopgave

1. [Doel en reikwijdte](#1-doel-en-reikwijdte)  
2. [Conceptuele positionering](#2-conceptuele-positionering)  
3. [Agent-charter als governance-artefact](#3-agent-charter-als-governance-artefact)  
4. [Structuur en Template-verplichting](#4-structuur-en-template-verplichting)  
5. [Minimale inhoud van een agent-charter](#5-minimale-inhoud-van-een-agent-charter)  
6. [Relatie met agent-contract en capabilities](#6-relatie-met-agent-contract-en-capabilities)  
7. [Relatie met Templates en value-stream-specifieke agents](#7-relatie-met-templates-en-value-stream-specifieke-agents)  
8. [Relatie met Prompts](#8-relatie-met-prompts)  
9. [Herkomst, versiebeheer en legitimiteit](#9-herkomst-versiebeheer-en-legitimiteit)  
10. [Normen voor agent-initialisatie en gebruik](#10-normen-voor-agent-initialisatie-en-gebruik)  
11. [Locatie en workspace-afspraken](#11-locatie-en-workspace-afspraken)  
12. [Change Log](#12-change-log)

---

## 1. Doel en reikwijdte

### Definitie
Deze doctrine beschrijft de **normen** voor het opstellen, onderhouden en gebruiken van **agent-charters** binnen het Mandarin-ecosysteem.

### Reikwijdte
- Geldt voor **alle mandarin-agents** die in een canonieke workspace worden beheerd.
- Geldt voor mensen en agents die agent-charters schrijven, reviewen of publiceren.
- Geldt voor alle workspaces waarin agent-charters worden vastgelegd als **Mandarin-artefact**.

---

## 2. Conceptuele positionering

1. Een **mandarin-agent** (mandarin-domeinconcepten) ontleent zijn legitimiteit aan een combinatie van:
   - een **agent-charter** (governance en bestaansrecht), en
   - een of meer **agent-contracten** (formele interface en capabilities).
2. Een **agent-charter** is een **governance-artefact** (mandarin-ordeningsconcepten):
   - specialisatie van **normerend artefact**;
   - operationeel in de value stream "mandarin-agent Ecosysteem Ontwikkeling" (value stream 0).
3. Een **Template** (mandarin-domeinconcepten) wordt gebruikt om de vorm van een **agent-charter** te standaardiseren; de normatieve inhoud blijft in het artefact zelf.

---

## 3. Agent-charter als governance-artefact

1. **Norm 3.1 — Governance-artefact**  
   Elk agent-charter **is** een **governance-artefact** en moet voldoen aan de kenmerken van een normerend artefact:
   - bindend en prescriptief binnen de scope van de agent,
   - versieerbaar en traceerbaar,
   - operationeel in maximaal één value stream fase binnen value stream 0.

2. **Norm 3.2 — Uniek per mandarin-agent**  
   Elke **mandarin-agent** heeft **exact één** primair agent-charter.

3. **Norm 3.3 — Canonieke waarheid**  
   Bij conflict tussen documenten over missie, scope of bevoegdheid van een agent is het **agent-charter** leidend boven beschrijvende of documenterende artefacten.

---

## 4. Structuur en Template-verplichting

1. **Norm 4.1 — Verplicht gebruik van agent-charter-template**  
   Elk nieuw of gewijzigd agent-charter **moet** gebaseerd zijn op het template in `templates/agent.charter.template.md`.

2. **Norm 4.2 — Inhoud boven vorm**  
   Het template bepaalt de **representatievorm** en structuur (secties, koppen, volgorde). De normatieve inhoud (missie, scope, beslisrechten) ligt vast in het agent-charter als **Mandarin-artefact**, niet in het template zelf.

3. **Norm 4.3 — Uitbreiding toegestaan, reductie niet**  
   - Secties uit het standaardtemplate mogen worden uitgebreid of gespecificeerd.
   - Verwijderen van verplichte secties of betekenisvolle velden is niet toegestaan zonder canonieke wijziging van het template en deze doctrine.

---

## 5. Minimale inhoud van een agent-charter

Een geldig agent-charter bevat minimaal de volgende elementen (overeenkomstig het template):

1. **Identificatieblok**  
   - Repository, Agent Identifier, Status, Owner (en optioneel aanvullende metadata zoals tags of classificaties).  
   - Versiebeheer van het charter gebeurt **niet** via een versieveld in het bestand, maar via git (zie Norm 9.1).

2. **Purpose (Missie en waarde)**  
   - Heldere, beknopte mission statement.
   - Primaire doelen (Primary Objectives).

3. **Scope & Boundaries**  
   - Expliciete beschrijving van wat de agent **wel** doet (in scope).
   - Expliciete beschrijving van wat de agent **niet** doet (out of scope).
   - Relatie met **agent-boundary** uit mandarin-domeinconcepten.

4. **Authority & Decision Rights**  
   - Duidelijke kwalificatie van beslisbevoegdheid.
   - Afspraken over aannames en escalatie.

5. **Fase- en kwaliteitsafspraken**  
   - Expliciete koppeling aan value streams en **value stream fasen** waarbinnen de agent actief is.
   - Kwaliteitsprincipes en quality gates die gelden voor de outputs.

6. **Inputs & Outputs**  
   - Lijst van verwachte inputs (met type, bron, verplichtheid, beschrijving).
   - Lijst van geleverde outputs (met type, doel, conditie, beschrijving).

**Norm 5.1 — Onvolledigheid**  
Een agent-charter dat één of meer van bovenstaande onderdelen mist, wordt als **onvolledig** beschouwd en mag niet gebruikt worden voor het initialiseren of herinitialiseren van een **mandarin-agent**.

---

## 6. Relatie met agent-contract en capabilities

1. **Norm 6.1 — Charter vóór contract**  
   Een **agent-contract** mag pas canoniek worden gemaakt als er een geldig, vastgesteld agent-charter bestaat.

2. **Norm 6.2 — Capabilities in contract, niet in charter**  
   - **Agent-capabilities** worden formeel gedefinieerd in het **agent-contract**, niet in het agent-charter.
   - Het agent-charter mag capabilities benoemen op beschrijvend niveau (bijv. "deze agent ondersteunt vertaal-capabilities"), maar de canonieke definitie ligt in het contract.

3. **Norm 6.3 — Conflictoplossing**  
   - Bij conflict over **wat** een agent mag (scope/mandaat) is het **agent-charter** leidend.
   - Bij conflict over **hoe** een capability wordt aangeroepen (input/output, policies) is het **agent-contract** leidend.

---

## 7. Relatie met Templates en value-stream-specifieke agents

1. **Norm 7.1 — Template als domeinconcept**  
   Een **Template** is een herbruikbare, gestructureerde opzet voor artefacten en prompts (mandarin-domeinconcepten). Templates zijn geen normerende artefacten, maar ondersteunen het consistent invullen van normerende en andere artefacten.

2. **Norm 7.2 — Verplicht gebruik door value-stream-specifieke agents**  
   **Mandarin-agents** die op de **inzet-as** als *value-stream-specifiek* zijn geclassificeerd, **moeten** voor hun primaire artefacten gebruikmaken van door het ecosysteem goedgekeurde templates.

3. **Norm 7.3 — Template-beheer**  
   - Templates voor agent-charters, fase-charters en aanverwante governance-artefacten worden centraal beheerd in `templates/` binnen de relevante workspace.
   - Wijzigingen aan deze templates vereisen een normatieve wijziging (publicatie) en moeten worden afgestemd met deze doctrine.

---

## 8. Relatie met Prompts

1. **Norm 8.1 — Geen gelijkstelling van prompt en charter**  
   Een **prompt** (mandarin-domeinconcepten) is een concrete, contextuele uitdrukking van een aanroep naar een **mandarin-agent**, maar is **geen** agent-charter en **geen** vervanging daarvoor.

2. **Norm 8.2 — Begripsverwarring voorkomen**  
   - In documentatie, agent-charters en agent-contracten wordt de term **prompt** uitsluitend gebruikt volgens de canonieke definitie in mandarin-domeinconcepten.
   - Historische verwijzingen naar "prompt" als synoniem voor capability of charter worden actief uitgefaseerd.

3. **Norm 8.3 — Tooling-specifieke prompts**  
   - Bestanden in `.github/` van de vorm `{agent-naam}.prompt` voeden VS Code Copilot, maar zijn in de canon **geen** prompts in de zin van het domeinconcept;
   - zij worden gezien als tooling-specifieke **representaties** van aanroepen, afgeleid van agent-contract en agent-charter.

---

## 9. Herkomst, versiebeheer en legitimiteit

1. **Norm 9.1 — Versiebeheer (verwijzing Constitutie)**  
   - Voor versiebeheer en traceerbaarheid van agent-charters geldt rechtstreeks **Artikel 4, punt 3** van de Constitutie Mandarin (versiebeheer via git).  
   - Deze doctrine voegt geen aanvullend intern versieveld toe aan agent-charters; zij volgen de constitutionele regel dat bestanden geen verplicht intern versieveld nodig hebben en dat nieuwe versies de vorige inhoud op hetzelfde bestandspad **overschrijven**.

2. **Norm 9.2 — Herkomstverantwoording**  
   - Nieuwe of ingrijpend herziene agent-charters bevatten een korte herkomstverantwoording (verwijzing naar constitutie, doctrines, templates en relevante besluiten).

3. **Norm 9.3 — Legitimiteit**  
   - Een **mandarin-agent** is pas legitiem als:
     - er een geldig, vastgesteld agent-charter is;
     - het charter in de juiste workspace is gepubliceerd;
     - eventuele aanvullende governance-artefacten (bijv. fase-charters) zijn afgestemd.

---

## 10. Normen voor agent-initialisatie en gebruik

1. **Norm 10.1 — Initialisatievolgorde**  
   Bij het creëren van een nieuwe **mandarin-agent** wordt de volgende volgorde aangehouden:
   1. Opstellen en vaststellen van het **agent-charter** (op basis van het template).
   2. Opstellen van het eerste **agent-contract** (capabilities en policies).
   3. Configuratie van tooling-specifieke representaties (prompts, scripts, instellingen).

2. **Norm 10.2 — Gebruik zonder charter**  
   Een agent zonder geldig agent-charter mag niet operationeel worden gebruikt binnen een canonieke workspace.

3. **Norm 10.3 — Evaluatie en herziening**  
   - Bij significante wijziging van scope, beslisbevoegdheid of value stream-inbedding wordt het agent-charter herzien **vóór** aanpassing van contracten of implementatie.

4. **Norm 10.4 — Logging bij handmatige initialisatie**  
   - Wanneer een **mandarin-agent** handmatig wordt geïnitieerd (dus niet via een geautomatiseerde pipeline of runner), schrijft deze initialisatie een logbestand weg.  
   - De bestandsnaam volgt het patroon: `yyyyddmm.HHmm <agent-naam>.log` (jaar, dag, maand, 24-uurs tijd zonder dubbele punt, gevolgd door een spatie en de canonieke agent-naam).  
   - De inhoud van het logbestand bevat ten minste een expliciete opsomming van:  
     - welke bestanden zijn **gelezen** (met pad), en  
     - welke bestanden zijn **aangepast** (met pad).  
   - Deze norm geldt voor **alle mandarin-agents**, ongeacht value stream of rol, tenzij een hogere norm anders voorschrijft.

5. **Norm 10.5 — Output van inhoudelijke agents**  
    - **Mandarin-agents** die op de **werkingsas** als *inhoudelijk* zijn gepositioneerd, produceren hun primaire output als bestand in de betreffende workspace.  
    - Wanneer deze primaire output de status heeft van **normerend artefact** (bijvoorbeeld governance-artefact of bedrijfs-artefact volgens mandarin-ordeningsconcepten), wordt deze **altijd** vastgelegd als Markdown-bestand (`.md`).  
    - Andere bestandsformaten (bijlagen, diagrammen, datasets) zijn toegestaan als **afgeleide artefacten**, maar vervangen nooit het normerende Markdown-artefact.

---

## 11. Locatie en workspace-afspraken

1. **Norm 11.1 — Locatie van agent-charters**  
   - Agent-charters worden opgeslagen op een door workspace-doctrine voorgeschreven locatie, doorgaans in een `artefacten/`- of `governance/`-subfolder van de betreffende workspace.

2. **Norm 11.2 — Templates in templates/**  
   - Alle templates (inclusief agent-charter-templates, fase-charter-templates en document-templates) worden opgeslagen in de `templates/`-folder van de workspace, conform workspace-doctrine.

3. **Norm 11.3 — Publicatie en toegang**  
   - Agent-charters zijn leesbaar voor alle agents en mensen die afhankelijk zijn van de betreffende **mandarin-agent**.

---

## 12. Change Log

| Datum      | Versie | Wijziging                                                                                                   | Auteur                |
|------------|--------|-------------------------------------------------------------------------------------------------------------|-----------------------|
| 2026-02-06 | 2.4.0  | Norm 9.1 aangepast tot verwijzing naar constitutie (Artikel 4, punt 3) als bron voor versiebeheer via git | Constitutioneel Auteur |
| 2026-02-06 | 2.3.0  | Aangepast versiebeheer: agent-charters hebben geen intern versieveld meer; versie en historie lopen via git (Norm 5 en 9) | Constitutioneel Auteur |
| 2026-02-06 | 2.2.0  | Toegevoegd: norm 10.5 over outputbestanden van inhoudelijke agents en verplichte Markdown-vorm voor normerende artefacten | Constitutioneel Auteur |
| 2026-02-06 | 2.1.0  | Toegevoegd: norm 10.4 over verplichte logging van gelezen en aangepaste bestanden bij handmatige initialisatie van alle mandarin-agents | Constitutioneel Auteur |
| 2026-02-01 | 2.0.0  | Herijkte doctrine op basis van vernieuwde conceptuele en ordeningsgrondslagen; expliciete integratie van Template- en Prompt-concepten | Constitutioneel Auteur |

---

**Einde document**

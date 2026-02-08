## Herkomstverantwoording

Deze doctrine-aanvulling is opgesteld door Constitutioneel Auteur op basis van inconsistenties tussen canon en feitelijk gedrag van agents in de mandarin-agents workspace.

**Geraadpleegde bronnen**:
- grondslagen/globaal/constitutie.md (versie 1.3.0, gelezen op 2026-02-06)
- grondslagen/globaal/workspace-doctrine.md (versie 1.4.0, gelezen op 2026-02-06)
- beleid-mandarin-agents (value stream: agent-enablement, gelezen op 2026-02-06)
- mandarin-agents/agent-charters en agent-contracten met verwijzingen naar `docs/resultaten/` (analyse uitgevoerd op 2026-02-06)

**Toelichting structuur**:
Deze doctrine-aanvulling maakt de "eigen structuur" van de mandarin-agents workspace expliciet. Zij concretiseert:
- waar agents in mandarin-agents hun output moeten opslaan;
- hoe bestandsnamen worden gevormd (zonder datum-versionering);
- hoe overschrijven en logging werken in relatie tot de constitutie.
De regels sluiten aan op de bestaande workspace-doctrine en de constitutie, maar gelden alleen voor de mandarin-agents workspace.

---

## 1. Doel en reikwijdte

1. Deze doctrine legt de output-structuur vast voor de **mandarin-agents workspace**.
2. De scope is beperkt tot agents die in deze workspace leven, met name:
   - **agent-enablement** en **agent-ecosysteem** agents (value stream Agent Ecosysteem Ontwikkeling / agent-enablement);
   - foundational agents die in mandarin-agents worden beheerd.
3. Voor andere workspaces blijft de bestaande workspace-doctrine leidend.

---

## 2. Positionering ten opzichte van constitutie en workspace-doctrine

1. De constitutie (versie 1.3.0) Artikel 4.3 bepaalt dat:
   - versiebeheer via **git** loopt;
   - bestanden geen intern versieveld hoeven te hebben;
   - nieuwe versies de vorige inhoud op hetzelfde bestandspad **overschrijven**.
2. De workspace-doctrine (versie 1.4.0, sectie 5.1) bepaalt voor normale workspaces dat agent-resultaten naar `artefacten/{agent-naam}/` gaan.
3. Voor mandarin-agents en mandarin-canon is in de workspace-doctrine een uitzondering gemaakt ("eigen structuur"). Deze doctrine vult die uitzondering nu expliciet in voor **mandarin-agents**.

---

## 3. Locatie-principe voor output in mandarin-agents

**Norm 3.1 — Hoofdregel: artefacten-folder per agent**  
1. Alle agents in de mandarin-agents workspace schrijven hun **primaire output** naar de `artefacten/`-folder, niet naar `docs/resultaten/`.
2. De subfolder is afhankelijk van het type agent:
   - **Value stream-agents**: `artefacten/{value-stream-code}.{fase-code}.{agent-naam}/`  
     Voorbeeld: `artefacten/sfw.01.hypothese-vormer/`.
   - **Foundational agents**: `artefacten/fnd.{nn}.{agent-naam}/`  
     Voorbeeld: `artefacten/fnd.01.workspace-steward/`.
   - **Agent-enablement / AEO-agents**: `artefacten/aeo.{nn}.{agent-naam}/`  
     Voorbeeld: `artefacten/aeo.01.agent-curator/`.
3. Binnen deze folder bepaalt het agent-charter de verdere substructuur, zolang deze in lijn is met de bestandsnaam-principes in deze doctrine.

**Norm 3.2 — Rol van `docs/` in mandarin-agents**  
1. De folder `docs/` in mandarin-agents is **niet** de primaire locatie voor agent-output.  
2. Publicatie- of documentatiebestanden die vanuit mandarin-agents naar buiten worden gedeeld (bijvoorbeeld README-achtige uitleg of gepubliceerde overzichten) **mogen** in `docs/` staan, maar zijn dan afgeleide publicaties van de canonieke artefacten in `artefacten/`.
3. Nieuwe agents in mandarin-agents verwijzen in hun charters en contracts **niet** langer naar `docs/resultaten/` als outputlocatie voor primaire artefacten.

---

## 4. Bestandsnaam-principe — geen datum-versionering

**Norm 4.1 — Geen datum in bestandsnamen als versie**  
1. Bestandsnamen in `artefacten/...` bevatten **geen** datum-suffix als versie-indicator.  
   - Toegestaan voorbeeld: `artefacten/sfw.01.hypothese-vormer/hypothese-mandarin.md`  
   - Niet toegestaan: `artefacten/sfw.01.hypothese-vormer/hypothese-mandarin-2026-02-06.md`.
2. Patronen als `*-v2.md`, `*-final.md`, `*-definitief.md` en `*-<datum>.md` als versie-aanduiding zijn **niet toegestaan**.
3. Een datum in de inhoud van het document (bijvoorbeeld in een kopje of metadata in het bestand) **is wel toegestaan**, zolang dit geen versiebeheer vervangt maar enkel context geeft.

**Norm 4.2 — Versiebeheer via git (verwijzing constitutie)**  
1. Versiebeheer van alle artefacten in mandarin-agents volgt direct **Artikel 4.3** van de constitutie:
   - git-commits vormen de versiehistorie;
   - bestanden hoeven geen intern versieveld te hebben;
   - nieuwe versies overschrijven de vorige inhoud op hetzelfde bestandspad.
2. Agent-charters en agent-contracten in mandarin-agents leggen deze werkwijze vast in hun secties over versiebeheer en change log (indien aanwezig), maar voegen geen alternatieve versie-mechanismen toe.

---

## 5. Overschrijf-principe

**Norm 5.1 — Eén canoniek pad per artefact**  
1. Voor elk type artefact dat een agent in mandarin-agents produceert, is er **één** canoniek bestandspad in `artefacten/...`.
2. Nieuwe inhoud voor dat artefact wordt telkens naar **datzelfde** bestand geschreven.

**Norm 5.2 — Geen kopieën met andere namen**  
1. Agents maken geen structurele kopieën van hetzelfde artefact onder andere bestandsnamen (bijvoorbeeld `*-v2.md`, `*-oud.md`, `*-backup.md`).  
2. Tijdelijke hulpbestanden (bijvoorbeeld in `temp/`) zijn toegestaan, maar worden niet als canonieke artefacten beschouwd en worden opgeschoond volgens de geldende runner- en workspace-afspraken.

---

## 6. Logging bij handmatige initialisatie

**Norm 6.1 — Logbestand per handmatige start**  
1. Wanneer een agent in de mandarin-agents workspace **handmatig** wordt gestart (dus niet via een geautomatiseerde pipeline of orchestrator), schrijft deze initialisatie een logbestand weg in de `logs/`-folder van de workspace.
2. De bestandsnaam volgt het bestaande patroon uit de agent-charter-doctrine:  
   `logs/yyyyddmm.HHmm {agent-naam}.log`
3. Het logbestand bevat minimaal:
   - welke bestanden zijn **gelezen** (met pad);
   - welke bestanden zijn **aangepast** (met pad);
   - welke bestanden zijn **aangemaakt** (met pad).
4. Deze norm concretiseert voor mandarin-agents de algemene logging-norm uit de doctrine agent-charter normering.

---

## 7. Transitie-instructies

**Norm 7.1 — Wijziging van charters en agent-contracten**  
1. Agent Smeder (of opvolgende enablement-agent) is verantwoordelijk voor het **bijwerken** van agent-charters en agent-contracten in mandarin-agents zodat:
   - outputlocaties verwijzen naar `artefacten/...` volgens Norm 3.1;
   - datum- en versie-suffixen uit bestandsnamen worden verwijderd;
   - verwijzingen naar `docs/resultaten/` worden vervangen door verwijzingen naar de juiste `artefacten/`-paden, behalve waar expliciet sprake is van publicatie.

**Norm 7.2 — Historische bestanden in `docs/resultaten/`**  
1. Bestaande bestanden in `docs/resultaten/` blijven voorlopig **ongewijzigd** als historisch archief.
2. Indien nodig kan een korte README in de betreffende `docs/resultaten/{agent}/`-map worden toegevoegd die verwijst naar de nieuwe canonieke locatie in `artefacten/...`.
3. Nieuwe output na inwerkingtreding van deze doctrine volgt **altijd** de nieuwe structuur in `artefacten/...`.

**Norm 7.3 — Inwerkingtreding**  
1. Deze doctrine treedt in werking op het moment van publicatie in de mandarin-canon repository.
2. Vanaf dat moment is het oude patroon `docs/resultaten/{agent}/{bestand}-<datum>.md` **niet langer toegestaan** voor nieuwe of bijgewerkte artefacten in mandarin-agents.

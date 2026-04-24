# Entoli-ecosysteem — workspaces

Overzicht van alle workspaces bij de migratie van Mandarin → Entoli op GitLab.

---

## Workspaces

### 1. entoli-agents
**Van:** `mandarin-agents`
**Naam:** behouden

Bevat agent-contracts, charters en intent-definities voor het Entoli agent-ecosysteem. Elke agent heeft hier zijn operationele opdracht gedefinieerd.

**Description:**
`Agent contracts, charters and intent definitions for the Entoli agent ecosystem`

**Topics:**
`entoli` `ai-agents` `agent-contracts` `multi-agent` `governance`

---

### 2. entoli-canon
**Van:** `mandarin-canon`
**Naam:** `entoli-canon` (voorstel — zie toelichting)

Centrale governance-workspace voor het Entoli-ecosysteem. Bevat constitutie, doctrines, ontologie, rulespeak en kaderdefinities. Staat boven alle value streams; geeft normen, geeft geen uitvoering.

> **Toelichting naamkeuze:** "canon" drukt gezag en canoniciteit uit — de workspace is de gezaghebbende bron. Alternatieven als `entoli-gov` of `entoli-norm` zijn minder specifiek. `entoli-canon` is aanbevolen.

**Description:**
`Governance workspace for the Entoli ecosystem — constitution, doctrines, ontology, rulespeak and framework definitions`

**Topics:**
`entoli` `governance` `canon` `ontology` `rulespeak` `doctrines`

---

### 3. entoli-arch
**Van:** `mandarin-architecture`
**Naam:** `entoli-arch` (inkorten en heroriënteren)

Beschrijft en verantwoordt de systeemarchitectuur van het Entoli-platform. Eerder beschrijvend en verantwoordend dan normatief — de normstelling ligt in `entoli-canon`. Bevat architectuurbesluiten, systeemoverzichten en technology choices.

> **Let op:** de huidige workspace is meer normerend dan bedoeld. Bij migratie ombuigen naar verantwoordende architectuurdocumentatie.

**Description:**
`Architecture documentation and system decisions for the Entoli platform`

**Topics:**
`entoli` `architecture` `adr` `system-design` `documentation`

---

### 4. entoli-run
**Van:** nog niet bestaand
**Naam:** `entoli-run` (nieuw)

Eigen runtime-implementatie vergelijkbaar met Azure AI Foundry. Bevat orkestratie, deployment-configuratie en uitvoeringsinfrastructuur voor agents. Dit is de operationele laag van het ecosysteem.

**Description:**
`Runtime orchestration and deployment infrastructure for Entoli agents`

**Topics:**
`entoli` `runtime` `orchestration` `ai-agents` `infrastructure` `deployment`

---

### 5. entoli-startup
**Van:** (nieuw of bestaand)
**Naam:** behouden

Beschrijft de ondernemingsvorming van Entoli. Bevat oprichtingsdocumenten, governance-keuzes op ondernemingsniveau en vroege beslissingen over structuur en aanpak.

**Description:**
`Company formation documents, governance choices and founding decisions for Entoli`

**Topics:**
`entoli` `startup` `company-formation` `governance`

---

### 6. entoli-scaffold
**Van:** `mandarin-init`
**Naam:** `entoli-scaffold` (voorstel — zie toelichting)

Referentie-workspace met templates, bootstrapmateriaal en voorbeeldstructuren voor nieuwe workspaces binnen het Entoli-ecosysteem — bijvoorbeeld voor een beleid-workspace of een nieuwe value stream. Geen uitvoerende workspace; uitsluitend hergebruikbare patronen.

> **Toelichting naamkeuze:** `scaffold` (steigerwerk) geeft precies aan wat deze workspace doet: een structuur bieden om iets nieuws op te bouwen. Alternatieven: `entoli-blueprint` (meer statisch), `entoli-template` (te smal), `entoli-ref` (te generiek).

**Description:**
`Reference workspace with templates and bootstrap structures for new Entoli workspaces`

**Topics:**
`entoli` `templates` `scaffold` `bootstrap` `starter-kit`

---

## Samenvatting naamkeuzes

| # | Huidige naam | Nieuwe naam | Status |
|---|---|---|---|
| 1 | mandarin-agents | **entoli-agents** | Behouden |
| 2 | mandarin-canon | **entoli-canon** | Hernoemd |
| 3 | mandarin-architecture | **entoli-arch** | Hernoemd + heroriënteren |
| 4 | — | **entoli-run** | Nieuw |
| 5 | — | **entoli-startup** | Behouden |
| 6 | mandarin-init | **entoli-scaffold** | Hernoemd |

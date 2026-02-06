![Mandarin Canon Logo](docs/assets/mandarin-logo-m.png)

# Mandarin Canon

**De gezaghebbende canon voor het ontwerpen en besturen van het Mandarin agent-ecosysteem.**

---

## Wat is Mandarin Canon?

De **mandarin-canon** workspace is de centrale governance-workspace en fungeert als de agent-ecosysteem constitutie. Deze workspace staat boven de value streams en is zelf geen value stream.

### Doel

Deze workspace bevat:
- **Constitutie**: De bron van alle regels voor het agent-ecosysteem
- **Gedragscode**: Leidende principes voor alle agents en werkprocessen
- **Doctrines**: Richtlijnen per domein en value stream
- **Stage-charters**: Gestandaardiseerde fase-charters (A t/m G en U)
- **Templates**: Sjablonen voor charters, fase-charters en beleid
- **Normering**: Kwaliteitseisen en standaarden voor agent-charters

---

## Structuur

```
mandarin-canon/
├── .github/                 # Prompts en agent-contracts
│   ├── agents/              # Agent contract bestanden
│   └── prompts/             # Agent prompt bestanden
├── artefacten/              # Agent-resultaten per agent
│   ├── canon-curator/       # Rapporten, voorstellen, validaties
│   ├── moeder/              # Agent boundaries, analyses
│   └── {agent-naam}/        # Output van andere agents
├── charters-agents/         # Agent charters
├── docs/                    # Documentatie en publicaties
│   └── assets/              # Afbeeldingen en resources
├── grondslagen/             # Normatieve artefacten
│   ├── globaal/             # Constitutie, workspace-doctrine, etc.
│   ├── it-development/      # IT Development doctrines
│   └── value-streams/       # Value stream specifieke doctrines
├── logs/                    # Log bestanden
├── scripts/                 # Ondersteunende scripts en runners
│   └── runners/             # Agent runner scripts
├── temp/                    # Tijdelijke bestanden
├── templates/               # Sjablonen voor charters, etc.
├── beleid-mandarin-canon.md # Workspace-specifiek beleid
└── README.md                # Dit bestand
```

**Let op**: Alleen **Publisher** en **Presentatie-architect** mogen schrijven naar `docs/`. Alle andere agents schrijven naar `artefacten/{agent-naam}/` conform workspace-doctrine v1.4.0.

---

## Beleid

Het volledige beleid voor deze workspace staat in [beleid-mandarin-canon.md](beleid-mandarin-canon.md).

### Kernpunten

- **Taal**: Nederlands (B1-niveau)
- **Scope**: Governance, doctrines, stage-charters en templates
- **Niet in scope**: Individuele agent-charters (horen in agent-services workspaces), applicatiecode, project-specifieke afspraken
- **Doctrine**: Workspace-doctrine, doctrine-it-development, doctrine/value-streams

---

## Agent Werking

In deze workspace zijn twee typen agents primair actief:
1. **Workspace-steward**: Beheert governance, beleid en documentatie
2. **Schrijvende agents**: Stellen doctrines, beleid en normering op

Deze agents vallen onder de agent-ecosysteem constitutie en niet onder een specifieke value stream.

### Belangrijke regels voor agents

- Lees eerst de constitutie en gedragscode voordat je taken uitvoert
- Agent-charters en prompts komen uit de centrale agent-services repositories
- Voer `git pull` uit voordat je je charter leest
- Geen `git push` door agents (alleen handmatige commits)
- Artefacten worden geschreven in de centrale `artefacten/` folder

---

## Kwaliteitsnormen

- Alle documenten zijn in het Nederlands op B1-niveau
- Verwijzingen naar doctrines via `artefacten/0-governance/doctrine/*.md`
- Traceerbare afspraken naar relevante doctrines en value streams
- Wijzigingen worden vastgelegd in changelog of document header

---

## Changelog

| Datum | Versie | Wijziging | Auteur |
|-------|--------|-----------|--------|
| 2026-01-23 | 1.0.0 | Initiële creatie van README.md voor mandarin-canon workspace | Workspace-steward |

---

## Contact

Deze workspace wordt beheerd volgens de principes in de gedragscode en workspace-doctrine.

Voor vragen of wijzigingsvoorstellen: raadpleeg eerst de governance documenten in deze workspace.

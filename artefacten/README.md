# Artefacten

Deze folder bevat alle resultaten van agents, georganiseerd per agent.

Conform workspace-doctrine v1.4.0 schrijven alle agents (behalve Publisher en Presentatie-architect) hun output naar `artefacten/{agent-naam}/`.

## Structuur

```
artefacten/
├── canon-curator/       # Rapporten, voorstellen, validaties
├── moeder/              # Agent boundaries, analyses
├── layout-optimizer/    # Layout rapporten en geoptimaliseerde diagrammen
└── {agent-naam}/        # Output van andere agents
```

## Uitzonderingen

**Publisher** en **Presentatie-architect** zijn de enige agents die hun output in `docs/` plaatsen:
- Publisher: content bedoeld voor publicatie naar buiten
- Presentatie-architect: presentatie-assets en styling

Deze scheiding waarborgt traceerbaarheid en consistente structuur.

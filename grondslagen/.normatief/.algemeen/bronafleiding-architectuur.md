# Bronafleiding-architectuur

Dit document beschrijft de architectuur van bronafleiding: hoe normatieve bronnen worden getransformeerd en samengesteld tot execution files voor LLM-agents.

## Relevante bestanden

| Artefact | Locatie |
|----------|---------|
| Doctrine-bestanden | [doctrine.bronhouding-en-exploratie.md](doctrine.bronhouding-en-exploratie.md), [doctrine.traceability.md](doctrine.traceability.md), [doctrine.handoff.md](doctrine.handoff.md) |
| Ontologie (TTL) | [ontologie.ttl](ontologie.ttl) |
| Ontologie (compact) | [ontologie.compact.md](ontologie.compact.md) |
| Graph-schema | [graph/mandarin-schema.cypher](graph/mandarin-schema.cypher) |
| Graph-model | [graph/mandarin-model.md](graph/mandarin-model.md) |

## Flowchart

```mermaid
flowchart TD
    D[doctrine.md<br/>Normatieve bron] --> R[rules.md<br/>RuleSpeak-afleiding]
    D --> M[ontologie.compact.md<br/>LLM-projectie]

    T[ontologie.ttl<br/>Canonieke semantiek] --> M
    T --> G[graph-schema / graph-bestand<br/>Technische representatie]

    R --> EC[EC bronassemblage]
    M --> EC
    G --> EC
    D --> EC

    EC --> E[execution file<br/>samengesteld bronpakket]
    E --> A[doelagent / LLM-executie]

    T -. validatie / mapping .-> G
    T -. semantische bron .-> R
    D -. normatieve herkomst .-> T
```

## Flow - links rechts

```mermaid
flowchart LR
    D[doctrine.md] --> T[ontologie.ttl]
    D --> R[rules.md]
    T --> M[ontologie.compact.md]
    T --> G[graph-schema]
    M --> E[execution file]
    R --> E
    G --> E
    D --> E
```
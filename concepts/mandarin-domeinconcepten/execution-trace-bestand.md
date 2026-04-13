* mandarin-domeinconcepten.md (versie 2.10.0, gelezen 2026-04-06)
* doctrine-traceability.md (versie 1.2.0, gelezen 2026-04-06)
* 2f0b.concept-curator.definieer-concept.md (voorbeeld, gelezen 2026-04-06)

# Concept — execution-trace-bestand

---

## Definitie 📝

Een **execution-trace-bestand** is het aparte traceerbaarheidsartefact dat naast een **execution-bestand** bestaat en per opgenomen bron of segment vastlegt welke herkomst, opnamevorm en reden van opname voor die executie gelden.

Het execution-trace-bestand is de audit- en linkdrager van een executie. Waar het execution-bestand de uitvoeringscontext bevat, bevat het execution-trace-bestand de verantwoording van de daarin opgenomen bronnen.

## Kenmerken ⭐

- Is een zelfstandig **Mandarin-artefact** naast het execution-bestand
- Bevat minimaal `execution_id` en `execution_digest`
- Bevat bij voorkeur ook `execution_identificatie`
- Legt per bron of segment de herkomst en opnamevorm vast
- Ondersteunt volledige opname, fragment-opname en samenvatting
- Maakt audit, kruisverwijzing en latere controle op opnamebeslissingen mogelijk

## Verplichte velden per bron of segment

- `bronpad`
- `type`
- `digest` of `versie`
- `reden_van_opname`
- `opnamevorm` met waarden `volledig`, `fragment`, `samenvatting`

Bij `opnamevorm = fragment` wordt minimaal een heading-gebaseerde segment-identificatie vastgelegd, met optioneel bereik of andere canonieke segmentverwijzing.

## Wat het niet is ❌

- Geen vervanging van het **execution-bestand**
- Geen bronpakket zelf
- Geen los auditlog zonder koppeling naar een concrete executie
- Geen runlog van toolingstappen zonder bronverantwoording

## Relaties ➰

| Gerelateerd concept | Relatie |
| ------------------- | ------- |
| **Execution-bestand** | hoort bij precies één execution-bestand |
| **Bronpakket** | legt de herkomst vast van onderdelen die in het bronpakket zijn opgenomen |
| **Bronassemblage** | verantwoordt keuzes die tijdens assemblage zijn gemaakt |
| **Traceerbaarheid** | concrete drager van traceability op bron- en segmentniveau |
| **Artefact-type** | classificeert execution-trace-bestand als eigen artefactsoort naast execution-bestand |

## Traceerbaarheid

- Vastgesteld door: **concept-curator** (fnd.02.concept-curator)
- Laatst gewijzigd: 2026-04-09
- Bronnen: mandarin-domeinconcepten.md, doctrine-traceability.md, memo-sleutels-identificaties-en-loose-coupling.md

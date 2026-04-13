* mandarin-domeinconcepten.md (versie 2.10.0, gelezen 2026-04-06)
* doctrine-traceability.md (versie 1.2.0, gelezen 2026-04-06)
* 2f0b.concept-curator.definieer-concept.md (voorbeeld, gelezen 2026-04-06)

# Concept — execution-bestand

---

## Definitie 📝

Een **execution-bestand** is het technische artefact waarin de runner een concrete agent-executie vastlegt als een uitvoerbaar en traceerbaar geheel. Het bevat de execution-identiteit, de opdracht, de parameters, de bronhouding, de uitvoeringsmodus en de samengestelde grondslagen waarmee de agent moet werken.

Een execution-bestand is de runner-taal voor een executie: waar **bronpakket** het semantische bronnengeheel benoemt dat het LLM bereikt, benoemt **execution-bestand** de technische representatie waarin dat bronnengeheel samen met de uitvoeringscontext wordt verpakt.

## Minimale execution-identiteit

- `execution_id`
- `execution_identificatie`
- `execution_digest`
- `agent`
- `intent`
- `timestamp`
- `value_stream_fase`
- `bronhouding`
- `modus`

## Kenmerken ⭐

- Is een technisch **Mandarin-artefact** dat door de runner wordt gegenereerd
- Legt precies één concrete executie vast
- Neemt het **bronpakket** op, maar is breder dan dat pakket
- Maakt de executie reproduceerbaar, controleerbaar en auditbaar
- Functioneert als overdrachtsvorm tussen runner en agent of LLM
- Gebruikt `timestamp` als expliciete ordenings- en auditsleutel
- Gebruikt `agent` als execution-contextnaam voor de uitvoerende actor
- Wordt canoniek opgeslagen in `executions/`

## Wat het niet is ❌

- Geen synoniem voor **bronpakket**
- Geen **execution-trace-bestand**
- Geen **agent-contract**
- Geen **agent-charter**
- Geen louter technisch logbestand

## Relaties ➰

| Gerelateerd concept | Relatie |
| ------------------- | ------- |
| **Bronpakket** | semantisch bronnengeheel dat technisch in het execution-bestand wordt opgenomen |
| **Broninjectie** | het execution-bestand legt de uitkomst van broninjectie technisch vast |
| **Bronassemblage** | levert de inhoud die in het execution-bestand terechtkomt |
| **Execution-trace-bestand** | apart artefact dat de herkomst en opnamevorm per bron of segment vastlegt |
| **Runner** | genereert en beheert het execution-bestand |
| **Artefact-type** | classificeert execution-bestand als zelfstandig soort artefact |

## Traceerbaarheid

- Vastgesteld door: **concept-curator** (fnd.02.concept-curator)
- Laatst gewijzigd: 2026-04-09
- Bronnen: mandarin-domeinconcepten.md, doctrine-traceability.md, 2f0b.concept-curator.definieer-concept.md, memo-sleutels-identificaties-en-loose-coupling.md

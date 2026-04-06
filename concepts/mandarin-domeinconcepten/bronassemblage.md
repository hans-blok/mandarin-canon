* broninjectie.md (concept, gelezen 2026-04-06)
* doctrine-bronhouding-en-exploratie.md (versie 1.0.0)

# Concept — bronassemblage

---

## Definitie 📝

**Bronassemblage** is de handeling waarmee de runner de voor een agent-executie relevante kader- en werkbronnen selecteert, ordent en samenvoegt tot één geheel dat aan het LLM wordt aangeboden.

## Kenmerken ⭐

* Is een *proces*, geen product — het resultaat van bronassemblage is het **bronpakket**
* Wordt uitgevoerd door de **runner** tijdens de preflight-fase van een executie
* Staat onder toezicht van het geldende **bronregime**: de bronhouding bepaalt welke bronnen geselecteerd mogen worden
* Is *deterministisch* bij gelijke input: dezelfde bronhouding, dezelfde bronnen en dezelfde parameters leiden tot dezelfde assemblage
* Omvat selectie (welke bronnen), ordening (in welke volgorde) en samenvoeging (tot welk formaat)

## Wat het niet is ❌

* **Geen bronpakket** — bronassemblage is de handeling; het bronpakket is het resultaat
* **Geen bronhouding** — bronhouding bepaalt wat *mag*; bronassemblage voert die norm *uit*
* **Geen bronrol** — bronrol labelt individuele artefacten; bronassemblage combineert ze
* **Geen LLM-activiteit** — het LLM ontvangt het resultaat maar voert de assemblage niet uit

## Voorbeelden 💡

* De runner leest het agent-contract, bepaalt de benodigde kaderbronnen (constitutie, beleid, doctrines, charter, contract) en werkbronnen (parameters), en assembleert deze tot één samenhangend prompt-document
* Bij een verweef-concepten-executie selecteert de runner het conceptbestand als werkbron en de relevante domeinconcepten als referentiebronnen, en voegt deze samen

## Relaties ➰

| Gerelateerd concept          | Relatie                                                        |
| ---------------------------- | -------------------------------------------------------------- |
| **Bronpakket**               | resultaat van bronassemblage                                   |
| **Broninjectie**             | overkoepelend concept dat zowel assemblage als pakket omvat    |
| **Bronhouding / Bronregime** | normatief kader dat de assemblage stuurt                        |
| **Kaderbron**                | type bron dat tijdens assemblage wordt geselecteerd             |
| **Werkbron**                 | type bron dat tijdens assemblage wordt geselecteerd             |
| **Runner (preflight)**       | verantwoordelijke actor die de assemblage uitvoert              |

## Traceerbaarheid

* Vastgesteld door: **concept-curator** (fnd.02.concept-curator)
* Execution ID: 2f0b
* Laatst gewijzigd: 2026-04-06
* Bronnen: broninjectie.md (concept), gebruikersinvoer

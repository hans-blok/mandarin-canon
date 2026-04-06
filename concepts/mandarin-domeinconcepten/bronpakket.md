* broninjectie.md (concept, gelezen 2026-04-06)
* doctrine-bronhouding-en-exploratie.md (versie 1.0.0)

# Concept — bronpakket

---

## Definitie 📝

**Bronpakket** is het samengestelde geheel van expliciete bronnen zoals het het LLM bereikt op het moment van een agent-executie.

## Kenmerken ⭐

* Is een *product*, geen proces — het is het resultaat van **bronassemblage**
* Bevat uitsluitend expliciet gespecificeerde **kaderbronnen** en **werkbronnen**; impliciete modelkennis maakt er geen deel van uit
* Is tijdgebonden: elke executie kent precies één bronpakket op het moment van aanroep
* Vormt de volledige context waarop het LLM tijdens de executie mag redeneren
* Is herleidbaar: de inhoud van het bronpakket bepaalt welke claims de output mag bevatten (*geen bron in → geen claim in output*)

## Wat het niet is ❌

* **Geen bronassemblage** — bronassemblage is de handeling die het bronpakket creëert
* **Geen bronhouding** — bronhouding bepaalt wat in het pakket *mag*; het bronpakket is wat er daadwerkelijk *in zit*
* **Geen intern geheugen** van het LLM — het is extrinsieke, per executie samengestelde input
* **Geen permanente cache** — elke executie kan en vaak moet een nieuw bronpakket hebben

## Voorbeelden 💡

* Het in een execution-bestand opgenomen bronnenblok met constitutie, doctrines, charter, contract en parameters vormt het bronpakket voor die executie
* Bij een definieer-concept-executie bestaat het bronpakket uit: de parameters (term, definitie, domein) als werkmateriaal en de grondslagen (constitutie, beleid, doctrines) als kader-input
* Twee executies met dezelfde agent maar verschillende werkbronnen hebben verschillende bronpakketten

## Relaties ➰

| Gerelateerd concept          | Relatie                                                        |
| ---------------------------- | -------------------------------------------------------------- |
| **Bronassemblage**           | handeling die het bronpakket produceert                        |
| **Broninjectie**             | overkoepelend concept dat zowel assemblage als pakket omvat    |
| **Execution-bestand**        | technische drager waarin het bronpakket kan zijn opgenomen     |
| **Kaderbron**                | individueel artefact dat als kader-input in het pakket zit     |
| **Werkbron**                 | individueel artefact dat als werkmateriaal in het pakket zit   |
| **Bronhouding / Bronregime** | normatief kader dat bepaalt wat in het pakket mag              |
| **Runner (preflight)**       | actor die het bronpakket assembleert en aan het LLM levert     |

## Traceerbaarheid

* Vastgesteld door: **concept-curator** (fnd.02.concept-curator)
* Execution ID: 2f0b
* Laatst gewijzigd: 2026-04-06
* Bronnen: broninjectie.md (concept), gebruikersinvoer

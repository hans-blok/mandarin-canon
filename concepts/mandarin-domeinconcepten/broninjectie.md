* conceptuele-grondslagen.md (versie 1.1.0, datum 2026-02-21)
* doctrine-bronhouding-en-exploratie.md (versie 1.0.0, datum 2026-??-??)
* bronassemblage.md (concept, datum 2026-04-06)
* bronpakket.md (concept, datum 2026-04-06)

# Concept — Broninjectie

---

## Definitie 📝

**Broninjectie** is het overkoepelende concept voor het beschikbaar maken van expliciete bronnen aan een LLM ten behoeve van een agent-executie. Het omvat twee deelconcepten:

* **Bronassemblage** — de *handeling*: het selecteren, ordenen en samenvoegen van bronnen door de runner
* **Bronpakket** — het *resultaat*: het samengestelde geheel van bronnen zoals het het LLM bereikt

> **Kort:** broninjectie = bronassemblage (handeling) + bronpakket (resultaat).

## Kenmerken ⭐

* Overkoepelt proces én product: zonder assemblage geen pakket, zonder pakket geen context voor het LLM
* Wordt per executie uitgevoerd door de **runner**, onder toezicht van het geldende **bronregime**
* Omvat uitsluitend expliciete **kaderbronnen** en **werkbronnen**; impliciete modelkennis valt erbuiten
* Stuurt de kwaliteit, reproduceerbaarheid en herleidbaarheid van de output: *geen bron in → geen claim in output*
* Is tijdgebonden: elke executie kent precies één broninjectie

## Wat het niet is ❌

* **Geen intern geheugen** van het LLM — het is extrinsieke, per executie samengestelde input
* **Geen bronhouding** — het bronregime bepaalt wat erin *mag*; broninjectie is wat er daadwerkelijk *in zit* en hoe het er *in komt*
* **Geen losse bronrol** — bronrollen labelen individuele artefacten; broninjectie is het geheel
* **Geen synoniem voor bronassemblage of bronpakket** — het is de eenheid van beide

## Voorbeelden 💡

* De runner voert bronassemblage uit (selecteert constitutie, doctrines, charter, contract, parameters) en produceert een bronpakket dat als systeem-prompt aan het LLM wordt meegegeven — samen is dat de broninjectie
* Bij een definieer-concept-executie omvat de broninjectie de assemblage van parameters (term, definitie, domein) met kaderbronnen, en het resulterende bronpakket dat het LLM ontvangt

## Relaties ➰

| Gerelateerd concept          | Relatie                                                           |
| ---------------------------- | ----------------------------------------------------------------- |
| **Bronassemblage**           | deelconcept: de handeling binnen broninjectie                     |
| **Bronpakket**               | deelconcept: het resultaat binnen broninjectie                    |
| **Bronrol**                  | labelt individuele artefacten die via broninjectie worden gebundeld |
| **Kaderbron**                | type bron dat via bronassemblage in het bronpakket terechtkomt    |
| **Werkbron**                 | type bron dat via bronassemblage in het bronpakket terechtkomt    |
| **Bronregime / Bronhouding** | normatief kader dat de bronassemblage stuurt                      |
| **Runner (preflight)**       | actor die de broninjectie uitvoert                                |

## Traceerbaarheid

* Vastgesteld door: **concept-curator** (fnd.02.concept-curator)
* Execution ID: 2f0b
* Laatst gewijzigd: 2026-04-06
* Bronnen: zie lijst bovenaan

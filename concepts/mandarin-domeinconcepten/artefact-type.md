* mandarin-domeinconcepten.md (versie 2.10.0, geraadpleegd 2026-04-09)
* doctrine-traceability.md (versie 1.4.0, geraadpleegd 2026-04-09)
* memo-sleutels-identificaties-en-loose-coupling.md (werkdocument, geraadpleegd 2026-04-09)

# Concept - artefact-type

---

## Definitie 📝

Een **artefact-type** is de expliciete classificatiesleutel die aanduidt tot welke soort een Mandarin-artefact behoort. Het benoemt de klasse van een artefact, niet de individuele identiteit van dat artefact.

## Kenmerken ⭐

- Classificeert output als soort, bijvoorbeeld doctrine, concept, execution-bestand of takenconfiguratie
- Is een metadata-sleutel en geen vervanging van een identifier
- Kan worden gebruikt voor verwerking, validatie en routing
- Voorkomt dat classificatie impliciet moet worden afgeleid uit bestandsnaam of mapstructuur
- Kan als input dienen voor afleidings- en hashlogica zonder zelf een keten- of execution-id te zijn

## Wat het niet is ❌

- Geen **herkomstcode**
- Geen **execution_identificatie**
- Geen uniek individueel artefact-adres
- Geen bestandsformaat op zichzelf

## Relaties ➰

| Gerelateerd concept | Relatie |
| ------------------- | ------- |
| **Herkomstcode** | het artefact-type kan input zijn voor afleiding, maar identificeert niet de keten |
| **Execution-bestand** | een execution-bestand is zelf een mogelijk artefact-type |
| **Execution-trace-bestand** | een execution-trace-bestand is een apart artefact-type naast het execution-bestand |
| **Template** | het artefact-type zegt wat iets is; template zegt welke vorm het moet volgen |

## Toelichting 💬

Het expliciet vastleggen van **artefact-type** voorkomt semantische overbelasting van paden en bestandsnamen. Waar een identifier aangeeft *welk individueel object* bedoeld wordt, geeft artefact-type aan *tot welke klasse* dat object behoort. Die scheiding ondersteunt loose coupling tussen classificatie, opslag en traceability.

## Traceerbaarheid

- Vastgesteld door: GitHub Copilot
- Laatst gewijzigd: 2026-04-09
- Bronnen: mandarin-domeinconcepten.md, doctrine-traceability.md, memo-sleutels-identificaties-en-loose-coupling.md
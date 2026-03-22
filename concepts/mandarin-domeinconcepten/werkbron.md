# Concept — werkbron

---

## Definitie 📝
Een **werkbron** is een positie op de as **bronrol** die aangeeft dat een artefact binnen een agent-executie wordt ingelezen om te bewerken, analyseren of verwerken als het materiaal waarop de agent zijn intent toepast.

## Kenmerken ⭐
- Is het materiaal waarop de agent actief handelt
- Kan worden gelezen, geanalyseerd, gevalideerd of getransformeerd
- Bepaalt de inhoudelijke scope van de executie
- Typische artefacten in deze rol: bestaande concepten, artefact-bestanden, inputlijsten

## Wat het niet is ❌
- Geen vaste eigenschap van het artefact — het is een rol *in* een executie
- Geen kaderbron die mandaat of kennis levert
- Geen output van de executie (al kan de bewerking van een werkbron tot output leiden)

## Voorbeelden 💡
- Een bestaand concept-bestand als werkbron bij een valideer-concept-coherentie-executie
- Een lijst van domeinconcepten als werkbron bij een rapporteer-concept-status-executie
- Een artefact dat moet worden verrijkt als werkbron bij een verweef-concepten-executie

## Relatie tot andere concepten
- **Bronrol**: werkbron is één van de twee posities op deze as
- **Kaderbron**: de complementaire positie op dezelfde as

## Traceerbaarheid
- Vastgesteld door: concept-curator (fnd.02.concept-curator)
- Execution ID: e99b
- Laatst gewijzigd: 2026-03-22
- Bron(nen): gebruikersinvoer, concept-curator.charter.md

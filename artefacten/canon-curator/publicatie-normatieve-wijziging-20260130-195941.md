# Publicatie Rapport — Normatieve Wijziging

**Datum**: 2026-01-30  
**Tijd**: 19:59 CET  
**Agent**: Canon Curator  
**Type wijziging**: Normatieve uitbreiding  
**Impact**: Hoog — Alle agents

---

## Herkomstverantwoording

Dit publicatie rapport is gegenereerd door Canon Curator op 2026-01-30 ter documentatie van een normatieve wijziging aan doctrine-agent-charter-normering.md.

**Geraadpleegde bronnen**:
- doctrine-agent-charter-normering.md (versie 1.3.1, gelezen op 2026-01-30 19:55 CET)
- Gebruikersinstructie ontvangen op 2026-01-30 (exacte tijd niet beschikbaar)
- Constitutie Mandarin (versie 1.2.1, referentie)
- workspace-doctrine.md (versie 1.4.0, referentie)

---

## Samenvatting

Een nieuwe norm is toegevoegd aan doctrine-agent-charter-normering.md (versie 1.3.2) die verplicht dat:
1. Elke agent aan het **begin** van zijn interactie alle **gelezen bestanden** opsommet met klikbare links
2. Elke agent aan het **einde** van zijn interactie alle **gewijzigde bestanden** opsommet met klikbare links

Deze norm vergroot transparantie en traceerbaarheid in agent-interacties.

---

## Details van de Wijziging

### Gewijzigd Document
- [grondslagen/globaal/doctrine-agent-charter-normering.md](grondslagen/globaal/doctrine-agent-charter-normering.md)

### Versiewijziging
- **Van**: 1.3.1
- **Naar**: 1.3.2
- **Type**: PATCH (nieuwe norm, non-breaking)

### Toegevoegde Inhoud

**Nieuwe sectie**: 12.2.5 "Norm: Agent Communicatie — Gelezen en Gewijzigde Bestanden"

**Kernprincipe**:
> Elke agent-interactie begint met transparantie over gelezen bronnen en eindigt met transparantie over gewijzigde bestanden.

**Verplichte structuur**:

1. **Begin van agent-interactie**: Lijst met gelezen bestanden
   - Formaat: `**Gelezen bestanden:**` gevolgd door bulletlijst met Markdown-links
   - Workspace-relative paden
   - Voorbeeld: `- [grondslagen/globaal/constitutie.md](grondslagen/globaal/constitutie.md)`

2. **Einde van agent-interactie**: Lijst met gewijzigde bestanden
   - Formaat: `**Gewijzigde bestanden:**` gevolgd door bulletlijst met Markdown-links
   - Nieuwe bestanden krijgen prefix "✨ (nieuw)"
   - Workspace-relative paden
   - Indien geen wijzigingen: vermeld "Geen"

**Uitzondering**:
- Norm geldt niet voor interne tooling-operaties (grep_search, list_dir)
- Norm geldt wel voor alle deliverables en normatieve wijzigingen

**Normatief fundament**:
- Constitutie Artikel 2 (Transparantie in automatisering)
- Constitutie Artikel 4 (Wijzigingsbeheer en traceerbaarheid)
- Workspace-doctrine kernprincipe 3 (Traceerbaarheid)

---

## Impact Analyse

### Scope
- **Alle agents** in het Mandarin ecosysteem
- **Alle workspace-interacties** die deliverables opleveren
- **Alle normatieve wijzigingen**

### Impactniveau: **Hoog**

Deze wijziging heeft brede impact omdat:
1. Alle agents hun communicatie-structuur moeten aanpassen
2. Alle prompts moeten worden bijgewerkt om deze norm af te dwingen
3. Gebruikers krijgen nieuwe, standaard output-structuur

### Benodigde Vervolgacties

1. **Agent-prompts bijwerken**:
   - Alle prompts in `.github/prompts/` moeten instructies krijgen om gelezen/gewijzigde bestanden te tonen
   - Priority: Hoog

2. **Agent-charters reviewen**:
   - Elk charter moet verwijzen naar deze nieuwe norm in sectie "Inputs & Outputs"
   - Priority: Medium

3. **Documentatie bijwerken**:
   - README's en handleidingen moeten nieuwe output-formaat reflecteren
   - Priority: Laag

---

## Validatie

### Conformiteit Check

✅ **Structurele validatie**:
- Nieuwe sectie 12.2.5 toegevoegd na sectie 12.2.4 (workspace state logging)
- Genummerde secties correct bijgewerkt
- Alle verwijzingen naar andere secties kloppen

✅ **Inhoudelijke validatie**:
- Norm is consistent met bestaande Herkomstverantwoording-norm (sectie 12.2)
- Geen conflict met Constitutie of workspace-doctrine
- Duidelijke voorbeelden en formaat-specificaties

✅ **Change Log bijgewerkt**:
- Nieuwe entry toegevoegd voor versie 1.3.2
- Datum, versie, wijziging en auteur correct vastgelegd

✅ **Herkomstverantwoording bijgewerkt**:
- Nieuwe Herkomstverantwoording sectie geschreven
- Geraadpleegde bronnen gedocumenteerd
- Gebruikersinstructie geciteerd

---

## Publicatie Status

**Status**: ✅ Gepubliceerd  
**Datum publicatie**: 2026-01-30  
**Tijd publicatie**: 19:59 CET  
**Gepubliceerd door**: Canon Curator (agent)

**Wijziging actief**: Ja, met onmiddellijke werking  
**Backward compatible**: Ja (agents die deze norm nog niet volgen, blijven functioneren maar zijn niet conform)

---

## Traceerbaarheid

### Oorsprong Wijziging
- **Type**: Gebruikersinstructie
- **Ontvangen**: 2026-01-30
- **Inhoud**: "Elke agent begint met bulletsgewijs opsommen welke bestanden hij heeft gelezen. Hij eindigt met bulletsgewijs opsommen welke bestanden zijn gewijzigd. Dit met een klikbaar linkje naar het bestand."

### Uitgevoerde Handelingen
1. Nieuwe norm sectie 12.2.5 toegevoegd aan doctrine-agent-charter-normering.md
2. Versienummer verhoogd van 1.3.1 naar 1.3.2
3. Last Updated datum bijgewerkt naar 2026-01-30
4. Herkomstverantwoording sectie volledig herschreven
5. Change Log bijgewerkt met nieuwe entry
6. Dit publicatie rapport gegenereerd

### Gewijzigde Bestanden
- [grondslagen/globaal/doctrine-agent-charter-normering.md](grondslagen/globaal/doctrine-agent-charter-normering.md)

---

## Aanbevelingen

### Korte Termijn (Week 1-2)
1. Update alle agent-prompts in `.github/prompts/` met instructies voor gelezen/gewijzigde bestanden
2. Test nieuwe communicatie-structuur met 2-3 pilot agents
3. Verzamel feedback van gebruikers

### Middellange Termijn (Week 3-4)
1. Review alle agent-charters voor verwijzing naar nieuwe norm
2. Update templates voor agent-charters
3. Schrijf voorbeelden en best practices

### Lange Termijn (Maand 2+)
1. Evalueer adoptie-rate van nieuwe norm
2. Overweeg tooling-ondersteuning voor automatische link-generatie
3. Monitor impact op gebruikerservaring

---

## Afsluitende Opmerkingen

Deze normatieve wijziging versterkt de transparantie en traceerbaarheid die kernwaarden zijn van het Mandarin ecosysteem. Door expliciete communicatie over gelezen en gewijzigde bestanden kunnen gebruikers:
- Direct navigeren naar relevante bronnen
- Wijzigingen onmiddellijk verifiëren
- Beter begrijpen wat agents doen

De norm is consistent met bestaande governance-principes en vergroot het vertrouwen in agent-interacties.

---

**Einde rapport**

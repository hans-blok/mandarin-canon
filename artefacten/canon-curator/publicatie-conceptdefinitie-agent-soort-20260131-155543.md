# Publicatierapport — Toevoeging Conceptdefinitie Agent-soort

**Type**: Publicatierapport Normatieve Wijziging  
**Datum**: 2026-01-31  
**Timestamp**: 20260131-155543  
**Agent**: canon-curator  
**Status**: Gepubliceerd

---

## Samenvatting

Toevoeging van de conceptdefinitie **Agent-soort** aan het document [concepten-en-architectonische-grondslagen.md](../../grondslagen/globaal/concepten-en-architectonische-grondslagen.md). Dit concept was impliciet aanwezig (gebruikt in inhoudsopgave en relatie-tabel) maar ontbrak als expliciete definitie.

**Versie-update**: 1.0.0 → 1.1.0 (MINOR: nieuwe conceptdefinitie)

---

## Aanleiding

Het concept "agent-soort" werd gebruikt in:
- Inhoudsopgave (sectie "Agent-Soorten")
- Relatie-tabel "value stream ↔ agent-soort"
- Verwijzingen in andere conceptdefinities (adviserende agent, uitvoerende agent, beheeragent)

Zonder expliciete definitie ontbrak de conceptuele onderbouwing voor deze classificatie, wat inconsistent is met het doel van het conceptendocument: alle fundamentele concepten expliciet definiëren.

---

## Wijziging

### Toegevoegd

**Nieuw concept**: Agent-soort (sectie toegevoegd na Agent-boundary)

**Definitie**:  
Een **agent-soort** is een expliciete classificatie van **mandarin-agents** op basis van het type output dat zij leveren en de structurele impact die zij veroorzaken binnen het **Mandarin-ecosysteem**.

**Kenmerken**:
- Is een taxonomische indeling van agents
- Onderscheidt agents op basis van output-type en impact
- Bepaalt welke governanceregels van toepassing zijn
- Maakt duidelijk welke rol een agent speelt in het ecosysteem
- Is leidend voor contractontwerp en template-vereisten

**Voorbeelden**:
- Adviserende agent — levert alleen informatie
- Uitvoerende agent — levert artefacten (met sub-typen)
- Beheeragent — beheert workspace en runtime

**Synoniemen**: Agent-type, Agent-classificatie, Agent-categorie

**Analogieën**: Actor-type in enterprise architectuur, service type in software engineering

**Toelichting**: Legt uit hoe agent-soort governance-impact heeft (template-vereisten, normen) en relatie met agent-charter.

### Bijgewerkt

**Inhoudsopgave**: Link naar [Agent-soort](#agent-soort) toegevoegd onder "Agent-Gerelateerde Concepten"

**Metadata**: Versie 1.0.0 → 1.1.0

**Change Log**: Entry toegevoegd voor versie 1.1.0

---

## Impact

### Conceptueel
- **Compleetheid**: Vult lacune in conceptendocument
- **Consistentie**: Maakt impliciete classificatie expliciet
- **Traceerbaarheid**: Biedt referentiepunt voor agent-charters en governanceregels

### Operationeel
- **Agent-charters**: Kunnen nu verwijzen naar gedefinieerd concept "agent-soort"
- **Doctrine-agent-charter-normering**: Kan agent-soort gebruiken om normen te differentiëren
- **Governance-uitvoerende agents**: Hebben nu volledige conceptuele basis bij activatie

### Documentatie
- [concepten-en-architectonische-grondslagen.md](../../grondslagen/globaal/concepten-en-architectonische-grondslagen.md): v1.0.0 → v1.1.0
- Inhoudsopgave: uitgebreid met Agent-soort link
- Change Log: entry toegevoegd

---

## Validatie

✅ **Structuur**: Volgt standaard emoji-structuur (📝 ⭐ ❌ 💡 🏷️ 🔄 💬)  
✅ **Consistentie**: Terminologie consistent met bestaande concepten  
✅ **Compleetheid**: Alle verplichte secties aanwezig (Definitie, Kenmerken, Wat het niet is, Voorbeelden, Synoniemen, Analogieën, Toelichting)  
✅ **Relaties**: Gekoppeld aan bestaande concepten (Mandarin-agent, Agent-charter, Adviserende agent, Uitvoerende agent, Beheeragent)  
✅ **Inhoudsopgave**: Link toegevoegd en functioneel  
✅ **Metadata**: Versie en datum bijgewerkt  
✅ **Change Log**: Entry toegevoegd voor v1.1.0  

---

## Aanbevelingen

### Vervolgacties
1. **Doctrine-agent-charter-normering**: Overweeg expliciete verwijzing naar Agent-soort bij normen die agent-soort-specifiek zijn (bijv. template-vereiste voor uitvoerende agents)
2. **Agent-charters**: Overweeg toevoeging van expliciete "Agent-soort:" field in charter metadata
3. **Relatie-tabel**: Huidige tabel "value stream ↔ agent-soort" is nu volledig onderbouwd

### Governance
- Dit is een MINOR update (nieuwe definitie, geen breaking change)
- Document blijft status "Active"
- Geen impact op bestaande agent-implementaties
- Conceptuele basis is nu compleet voor alle agent-gerelateerde concepten

---

## Herkomstverantwoording

**Uitgevoerd door**: canon-curator  
**Op verzoek van**: Hans Blok  
**Datum uitvoering**: 2026-01-31  
**Publicatietijd**: 15:55:43  

**Grondslag**: 
- Charter canon-curator: [canon-curator.charter.md](../../charters-agents/canon-curator.charter.md)
- Werkwijze: Publiceer normatieve wijziging (sectie "Bij publicatie normatieve wijzigingen")

**Legitimiteit**:
- Canon-curator is bevoegd tot publicatie van normatieve wijzigingen conform charter
- Wijziging betreft toevoeging van conceptdefinitie (binnen scope)
- Geen normatieve inhoud gewijzigd, alleen toegevoegd

---

**Einde rapport**

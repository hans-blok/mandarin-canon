# Norm — Verplichte Bootstrap-Header in Agent Output

**Status**: Canoniek  
**Type**: Normatief (geldig/ongeldig criterium)  
**Versie**: 1.0  
**Geldig vanaf**: YYYY-MM-DD  
**Van toepassing op**:  
- alle agents  
- alle runners  
- alle door agents gegenereerde rapportages, wijzigingen en artefacten  

---

## 1. Doel van deze norm

Deze norm borgt dat **elke agent-output herleidbaar, auditbaar en constitutioneel gelegitimeerd** is.

Zij voorkomt dat:
- technisch correcte output wordt geaccepteerd zonder geldige start;
- governance impliciet of achteraf wordt toegepast;
- resultaten loskomen van hun normatieve context.

> **Output zonder expliciete legitimiteit is ongeldig.**

---

## 2. Kernregel (hard)

Elke agent-output **MOET** beginnen met een expliciete **Bootstrap-Header**.

Ontbreekt deze header, of is zij onvolledig, dan is de output:
- **ongeldig**, en
- **niet toegestaan voor gebruik, publicatie of besluitvorming**.

---

## 3. Verplichte Bootstrap-Header (minimale inhoud)

Elke Bootstrap-Header bevat minimaal:

### 3.1 Constitutie
- **Pad** naar de constitutie:
- **Versie, commit-hash of digest** van de gelezen constitutie

### 3.2 Value stream
- Exact **één** gedeclareerde value stream  
- Deze value stream is passend bij de uitgevoerde handeling

### 3.3 Geraadpleegde grondslagen
- Algemene grondslagen (`grondslagen/.algemeen/`)
- Grondslagen van de gedeclareerde value stream
- Geen andere grondslagen

### 3.4 Tijdstip en identiteit
- Datum/tijd van bootstrapping
- Identiteit van agent / runner / component

---

## 4. Vorm (format-neutraal)

De Bootstrap-Header:
- staat **bovenaan** de output;
- is **duidelijk gescheiden** van de inhoud;
- mag Markdown, JSON, YAML of tekstueel zijn;
- maar is altijd **machine- en mensleesbaar**.

Voorbeeld (illustratief):

```text
Bootstrap-Header
- Constitutie: grondslagen/.algemeen/constitutie.md
- Constitutie versie: <commit-hash>
- Value stream: Agent-ecosysteemontwikkeling
- Geraadpleegde grondslagen:
- grondslagen/.algemeen/*
- grondslagen/agent-ecosysteemontwikkeling/*
- Agent: <naam/id>
- Timestamp: <ISO-8601>

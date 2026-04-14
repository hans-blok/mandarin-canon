// ============================================================
// Mandarin Ecosysteem — Voorbeeldqueries
// ============================================================
// Gebruik na uitvoering van mandarin-schema.cypher
// en mandarin-seed.cypher.
// Label- en relatietypeconventies: zie mandarin-model.md
// ============================================================


// ============================================================
// Q1 — Alle artefacten met hun herkomstcode en positie
// ============================================================
// Geeft een overzicht van alle artefacten en de keten waaruit
// ze voortkomen. Nuttig voor audit en traceerbaarheid.

MATCH (art:MandarinArtefact)-[:BEHOORT_TOT]->(hk:HerkomstKeten)
RETURN art.artefactId     AS artefactId,
       art.herkomstpositie AS positie,
       hk.herkomstCode     AS herkomstCode,
       art.tijdstip        AS tijdstip
ORDER BY hk.herkomstCode, art.herkomstpositie;
ldm-mandarin.md

// ============================================================
// Q2 — Volledige voortbouwketen voor een herkomstcode
// ============================================================
// Geeft alle artefacten die tot dezelfde herkomst-ketenldm-mandarin.md
// behoren, inclusief het initierende artefact.
// Vervang '2604.Aa1B' door de gewenste herkomstcode.

MATCH (hk:HerkomstKeten {herkomstCode: '2604.Aa1B'})
      <-[:BEHOORT_TOT]-(art:MandarinArtefact)
OPTIONAL MATCH (art)-[:GEGENEREERD_DOOR]->(agent:MandarinAgent)
OPTIONAL MATCH (art)-[:IS_VAN_TYPE]->(at:ArtefactType)
RETURN hk.herkomstCode     AS keten,
       art.artefactId       AS artefactId,
       art.herkomstpositie  AS positie,
       at.artefactTypeNaam  AS type,
       agent.agentId        AS gegenereerdDoor,
       art.tijdstip         AS tijdstip
ORDER BY art.herkomstpositie DESC, art.tijdstip;


// ============================================================
// Q3 — Alle handoffs voortgekomen uit een executie
// ============================================================
// Geeft handoffs geproduceerd door een specifieke executie,
// inclusief de adresserende agent.
// Vervang 'exec-2604.0001' door de gewenste executiecode.

MATCH (hf:Handoff)-[:VLOEIT_VOORT_UIT]->(exec:Execution {executieCode: 'exec-2604.0001'})
OPTIONAL MATCH (hf)-[:ADRESSEERT]->(naarAgent:MandarinAgent)
RETURN hf.handoffId              AS handoffId,
       hf.menselijkeInterventie  AS escalatie,
       hf.tijdstip                AS tijdstip,
       naarAgent.agentId          AS naarAgent,
       hf.inhoudBoodschap         AS boodschap;


// ============================================================
// Q4 — Alle bronnen gebruikt door een executie
// ============================================================
// Splitst kaderbronnen en werkbronnen per executie.
// Vervang 'exec-2604.0001' door de gewenste executiecode.

MATCH (exec:Execution {executieCode: 'exec-2604.0001'})
OPTIONAL MATCH (exec)-[:RAADPLEEGT_ALS_KADER]->(kb:KaderBron)
OPTIONAL MATCH (exec)-[:RAADPLEEGT_ALS_WERK]->(wb:WerkBron)
RETURN exec.executieCode             AS executieCode,
       collect(DISTINCT kb.kaderBronId) AS kaderbronnen,
       collect(DISTINCT wb.werkBronId)  AS werkbronnen;


// ============================================================
// Q5 — Alle agents in een value stream fase
// ============================================================
// Geeft alle agents die gehuisvest zijn in een bepaalde fase.
// Vervang 'aeo.02' door de gewenste fasecode.

MATCH (fase:ValueStreamFase {faseCode: 'aeo.02'})-[:HUISVEST]->(agent:MandarinAgent)
OPTIONAL MATCH (agent)-[:VALT_ONDER]->(br:Bronregime)
RETURN fase.faseCode       AS fase,
       agent.agentId        AS agentId,
       agent.agentNaam      AS agentNaam,
       agent.versie         AS versie,
       br.regimeId          AS bronregime;


// ============================================================
// Q6 — Alle artefacten gerealiseerd door een intent
// ============================================================
// Traceer alle artefacten die zijn geproduceerd via een
// bepaalde intent, via de execution-keten.
// Vervang de intentId door de gewenste waarde.

MATCH (intent:Intent {intentId: 'aeo.02.agent-ontwerper.definieer-agent-charter'})
      <-[:VOERT_UIT]-(exec:Execution)
      -[:PRODUCEERT]->(art:MandarinArtefact)
OPTIONAL MATCH (art)-[:IS_VAN_TYPE]->(at:ArtefactType)
RETURN intent.intentId      AS intentId,
       exec.executieCode     AS executieCode,
       art.artefactId        AS artefactId,
       at.artefactTypeNaam   AS artefactType,
       art.herkomstpositie   AS positie,
       art.tijdstip          AS tijdstip
ORDER BY art.tijdstip;


// ============================================================
// Q7 — Alle escalaties (human-in-the-loop handoffs)
// ============================================================
// Geeft alle handoffs waarbij menselijke tussenkomst vereist
// is, inclusief de producerende agent.

MATCH (hf:Handoff {menselijkeInterventie: true})
OPTIONAL MATCH (hf)-[:VLOEIT_VOORT_UIT]->(exec:Execution)
               -[:UITGEVOERD_DOOR]->(agent:MandarinAgent)
RETURN hf.handoffId             AS handoffId,
       agent.agentId             AS vanAgent,
       hf.tijdstip               AS tijdstip,
       hf.inhoudBoodschap        AS boodschap
ORDER BY hf.tijdstip DESC;


// ============================================================
// Q8 — Traceerbaarheidspad van artefact terug naar agent
// ============================================================
// Geeft de volledige traceerbaarheidsketen van een artefact
// terug tot de producerende agent, intent en execution.
// Vervang 'art-2604.0001' door het gewenste artefactId.

MATCH (art:MandarinArtefact {artefactId: 'art-2604.0001'})
OPTIONAL MATCH (art)<-[:PRODUCEERT]-(exec:Execution)
OPTIONAL MATCH (exec)-[:UITGEVOERD_DOOR]->(agent:MandarinAgent)
OPTIONAL MATCH (exec)-[:VOERT_UIT]->(intent:Intent)
OPTIONAL MATCH (art)-[:BEHOORT_TOT]->(hk:HerkomstKeten)
OPTIONAL MATCH (art)-[:IS_VAN_TYPE]->(at:ArtefactType)
RETURN art.artefactId         AS artefactId,
       at.artefactTypeNaam    AS artefactType,
       hk.herkomstCode        AS herkomstCode,
       art.herkomstpositie    AS herkomstpositie,
       exec.executieCode      AS executieCode,
       intent.intentId        AS intentId,
       agent.agentId          AS agentId;


// ============================================================
// Q9 — Overzicht van het volledige ecosysteem per value stream
// ============================================================
// Geeft per value stream alle fasen, agents en hun intents.

MATCH (vs:ValueStream)-[:OMVAT]->(fase:ValueStreamFase)
OPTIONAL MATCH (fase)-[:HUISVEST]->(agent:MandarinAgent)
OPTIONAL MATCH (agent)-[:DEFINIEERT]->(intent:Intent)
RETURN vs.waardestroomCode    AS valueStream,
       fase.faseCode           AS fase,
       agent.agentId           AS agentId,
       collect(intent.intentId) AS intents
ORDER BY vs.waardestroomCode, fase.faseCode;


// ============================================================
// Q10 — Initierende artefacten per herkomst-keten
// ============================================================
// Geeft het startpunt (initierend artefact) van elke
// herkomst-keten via de deferred GESTART_DOOR-relatie.

MATCH (hk:HerkomstKeten)-[:GESTART_DOOR]->(initierend:MandarinArtefact)
OPTIONAL MATCH (initierend)-[:IS_VAN_TYPE]->(at:ArtefactType)
OPTIONAL MATCH (initierend)-[:GEGENEREERD_DOOR]->(agent:MandarinAgent)
RETURN hk.herkomstCode         AS herkomstCode,
       initierend.artefactId   AS initiërendArtefact,
       at.artefactTypeNaam     AS type,
       agent.agentId           AS gegenereerdDoor
ORDER BY hk.herkomstCode;

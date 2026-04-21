// ============================================================
// Mandarin Ecosystem - Example Queries
// ============================================================
// Use after running mandarin-schema.cypher
// and mandarin-seed.cypher.
// Label and relationship-type conventions: see mandarin-model.md
// ============================================================


// ============================================================
// Q1 - All artifacts with their provenance code and position
// ============================================================
// Gives an overview of all artifacts and the chain from which
// they originate. Useful for audit and traceability.

MATCH (art:MandarinArtefact)-[:BEHOORT_TOT]->(hk:HerkomstKeten)
RETURN art.artefactId     AS artefactId,
       art.herkomstpositie AS positie,
       hk.herkomstCode     AS herkomstCode,
       art.tijdstip        AS tijdstip
ORDER BY hk.herkomstCode, art.herkomstpositie;
// ============================================================
// Q2 - Full continuation chain for a provenance code
// ============================================================
// Gives all artifacts that belong to the same provenance chain,
// including the initiating artifact.
// Replace '2604.Aa1B' with the desired provenance code.

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
// Q3 - All handoffs resulting from an execution
// ============================================================
// Gives handoffs produced by a specific execution,
// including the addressed agent.
// Replace 'exec-2604.0001' with the desired execution code.

MATCH (hf:Handoff)-[:VLOEIT_VOORT_UIT]->(exec:Execution {executieCode: 'exec-2604.0001'})
OPTIONAL MATCH (hf)-[:ADRESSEERT]->(naarAgent:MandarinAgent)
RETURN hf.handoffId              AS handoffId,
       hf.menselijkeInterventie  AS escalatie,
       hf.tijdstip                AS tijdstip,
       naarAgent.agentId          AS naarAgent,
       hf.inhoudBoodschap         AS boodschap;


// ============================================================
// Q4 - All sources used by an execution
// ============================================================
// Splits frame sources and work sources per execution.
// Replace 'exec-2604.0001' with the desired execution code.

MATCH (exec:Execution {executieCode: 'exec-2604.0001'})
OPTIONAL MATCH (exec)-[:RAADPLEEGT_ALS_KADER]->(kb:KaderBron)
OPTIONAL MATCH (exec)-[:RAADPLEEGT_ALS_WERK]->(wb:WerkBron)
RETURN exec.executieCode             AS executieCode,
       collect(DISTINCT kb.kaderBronId) AS kaderbronnen,
       collect(DISTINCT wb.werkBronId)  AS werkbronnen;


// ============================================================
// Q5 - All agents in a value stream phase
// ============================================================
// Gives all agents housed in a particular phase.
// Replace 'aeo.02' with the desired phase code.

MATCH (fase:ValueStreamFase {faseCode: 'aeo.02'})-[:HUISVEST]->(agent:MandarinAgent)
OPTIONAL MATCH (agent)-[:VALT_ONDER]->(br:Bronregime)
RETURN fase.faseCode       AS fase,
       agent.agentId        AS agentId,
       agent.agentNaam      AS agentNaam,
       agent.versie         AS versie,
       br.regimeId          AS bronregime;


// ============================================================
// Q6 - All artifacts realized by an intent
// ============================================================
// Trace all artifacts produced through a
// particular intent via the execution chain.
// Replace the intentId with the desired value.

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
// Q7 - All escalations (human-in-the-loop handoffs)
// ============================================================
// Gives all handoffs for which human intervention is required,
// including the producing agent.

MATCH (hf:Handoff {menselijkeInterventie: true})
OPTIONAL MATCH (hf)-[:VLOEIT_VOORT_UIT]->(exec:Execution)
               -[:UITGEVOERD_DOOR]->(agent:MandarinAgent)
RETURN hf.handoffId             AS handoffId,
       agent.agentId             AS vanAgent,
       hf.tijdstip               AS tijdstip,
       hf.inhoudBoodschap        AS boodschap
ORDER BY hf.tijdstip DESC;


// ============================================================
// Q8 - Artifact traceability path back to the agent
// ============================================================
// Gives the full traceability chain of an artifact
// back to the producing agent, intent, and execution.
// Replace 'art-2604.0001' with the desired artifactId.

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
// Q9 - Overview of the full ecosystem per value stream
// ============================================================
// Gives, per value stream, all phases, agents, and their intents.

MATCH (vs:ValueStream)-[:OMVAT]->(fase:ValueStreamFase)
OPTIONAL MATCH (fase)-[:HUISVEST]->(agent:MandarinAgent)
OPTIONAL MATCH (agent)-[:DEFINIEERT]->(intent:Intent)
RETURN vs.waardestroomCode    AS valueStream,
       fase.faseCode           AS fase,
       agent.agentId           AS agentId,
       collect(intent.intentId) AS intents
ORDER BY vs.waardestroomCode, fase.faseCode;


// ============================================================
// Q10 - Initiating artifacts per provenance chain
// ============================================================
// Gives the starting point (initiating artifact) of each
// provenance chain through the deferred GESTART_DOOR relationship.

MATCH (hk:HerkomstKeten)-[:GESTART_DOOR]->(initierend:MandarinArtefact)
OPTIONAL MATCH (initierend)-[:IS_VAN_TYPE]->(at:ArtefactType)
OPTIONAL MATCH (initierend)-[:GEGENEREERD_DOOR]->(agent:MandarinAgent)
RETURN hk.herkomstCode         AS herkomstCode,
       initierend.artefactId   AS initiërendArtefact,
       at.artefactTypeNaam     AS type,
       agent.agentId           AS gegenereerdDoor
ORDER BY hk.herkomstCode;

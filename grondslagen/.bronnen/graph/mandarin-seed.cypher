// ============================================================
// Mandarin Ecosystem - Seed Data
// ============================================================
// Minimal representative instances per entity class:
//   MandarinAgent, ValueStream, ValueStreamFase,
//   Intent, Execution, MandarinArtefact,
//   KaderBron, WerkBron, Bronregime,
//   HerkomstKeten, Handoff, Workspace,
//   ArtefactType, Template, OrchestratieRun
//
// Closed source stance: instances are derived from
//   mandarin-value-streams-en-fasen.md v1.8.0
//   doctrine-traceability.md v1.6.0
//   doctrine-handoff.md v1.2.0
// ============================================================


// ============================================================
// SOURCE REGIMES
// Four canonical positions on the source-stance axis
// Source: doctrine-bronhouding-en-exploratie.md v1.0.0
// ============================================================

MERGE (brInput:Bronregime {regimeId: 'input-gebonden'})
  SET brInput.beschrijving = 'The source is supplied as input for the execution; the agent works only with what is supplied';

MERGE (brCanon:Bronregime {regimeId: 'canon-gebonden'})
  SET brCanon.beschrijving = 'The source is canonical; the agent consults only sources recorded in the canon';

MERGE (brExtern:Bronregime {regimeId: 'externe-bron-gebonden'})
  SET brExtern.beschrijving = 'The source is outside the canon but has been explicitly designated and verified';

MERGE (brExploratief:Bronregime {regimeId: 'exploratief'})
  SET brExploratief.beschrijving = 'The agent may consult sources independently; the result is not canonical';


// ============================================================
// WORKSPACE
// Source: mandarin-domeinconcepten.md v2.13.0
// ============================================================

MERGE (ws:Workspace {workspaceId: 'ws-mandarin-canon'})
  SET ws.workspaceNaam = 'Mandarin Canon Workspace';


// ============================================================
// VALUE STREAMS
// Source: mandarin-value-streams-en-fasen.md v1.8.0
// ============================================================

MERGE (fnd:ValueStream {waardestroomCode: 'fnd'})
  SET fnd.waardestroomNaam = 'Fundament',
    fnd.inhoudBeschrijving = 'Canonical basis, doctrines, constitution, and foundations of the Mandarin ecosystem';

MERGE (aeo:ValueStream {waardestroomCode: 'aeo'})
  SET aeo.waardestroomNaam = 'Agent Ecosystem Setup',
    aeo.inhoudBeschrijving = 'Design and standardization of the agent ecosystem';

MERGE (sfw:ValueStream {waardestroomCode: 'sfw'})
  SET sfw.waardestroomNaam = 'Software Workflow',
    sfw.inhoudBeschrijving = 'Software development by agents within the ecosystem';

MERGE (aod:ValueStream {waardestroomCode: 'aod'})
  SET aod.waardestroomNaam = 'Agent Development',
    aod.inhoudBeschrijving = 'Development and refinement of individual agents';

MERGE (knv:ValueStream {waardestroomCode: 'knv'})
  SET knv.waardestroomNaam = 'Knowledge Processing',
    knv.inhoudBeschrijving = 'Knowledge acquisition, processing, and safeguarding';

MERGE (miv:ValueStream {waardestroomCode: 'miv'})
  SET miv.waardestroomNaam = 'Model Integration and Validation',
    miv.inhoudBeschrijving = 'Integration, validation, and quality assurance of models';


// ============================================================
// VALUE STREAM PHASES
// Source: mandarin-value-streams-en-fasen.md v1.8.0
// ============================================================

// Foundation
MERGE (fnd01:ValueStreamFase {faseCode: 'fnd.01'})
  SET fnd01.waardestroomNaam = 'Foundation - Foundations',
      fnd01.inhoudBeschrijving = 'Canonical foundations, doctrines, and constitution';

// AEO
MERGE (aeo01:ValueStreamFase {faseCode: 'aeo.01'})
    SET aeo01.waardestroomNaam = 'AEO - Orientation',
      aeo01.inhoudBeschrijving = 'Orientation on the ecosystem and the initial design';

MERGE (aeo02:ValueStreamFase {faseCode: 'aeo.02'})
    SET aeo02.waardestroomNaam = 'AEO - Design',
      aeo02.inhoudBeschrijving = 'Design of agents, intents, and charters';

MERGE (aeo03:ValueStreamFase {faseCode: 'aeo.03'})
    SET aeo03.waardestroomNaam = 'AEO - Refinement',
      aeo03.inhoudBeschrijving = 'Refinement and standardization of the agent ecosystem';

// VALUE STREAM -> VALUE STREAM PHASE
MERGE (fnd)-[:OMVAT]->(fnd01);
MERGE (aeo)-[:OMVAT]->(aeo01);
MERGE (aeo)-[:OMVAT]->(aeo02);
MERGE (aeo)-[:OMVAT]->(aeo03);


// ============================================================
// AGENTS
// Source: doctrine-agent-charter-normering.md v2.4.0
// ============================================================

MERGE (agOntwerper:MandarinAgent {agentId: 'aeo.02.agent-ontwerper'})
  SET agOntwerper.agentNaam  = 'Agent Designer',
      agOntwerper.versie      = '1.0.0',
      agOntwerper.bronhouding = 'canon-gebonden',
      agOntwerper.inhoudCharter = 'Designs agent charters and defines the identity and responsibility of agents within the Mandarin ecosystem.';

MERGE (agCurator:MandarinAgent {agentId: 'fnd.01.agent-curator'})
  SET agCurator.agentNaam   = 'Agent Curator',
      agCurator.versie       = '1.0.0',
      agCurator.bronhouding  = 'canon-gebonden',
      agCurator.inhoudCharter = 'Manages and validates the canonical foundations of the Mandarin ecosystem.';

// VALUE STREAM PHASE -> AGENT
MERGE (aeo02)-[:HUISVEST]->(agOntwerper);
MERGE (fnd01)-[:HUISVEST]->(agCurator);

// AGENT -> SOURCE REGIME
MERGE (agOntwerper)-[:VALT_ONDER]->(brCanon);
MERGE (agCurator)-[:VALT_ONDER]->(brCanon);


// ============================================================
// ARTIFACT TYPES AND TEMPLATES
// Source: ldm-mandarin.md v1.4.0, templates/yaml-header.template.md
// ============================================================

MERGE (atCharter:ArtefactType {artefactTypeId: '001'})
  SET atCharter.artefactTypeNaam  = 'Agent Charter',
      atCharter.artefactFunctie   = 'structurerend',
      atCharter.inhoudBeschrijving = 'Canonical charter of a Mandarin agent; records identity, responsibility, and capability boundary';

MERGE (atLdm:ArtefactType {artefactTypeId: '002'})
    SET atLdm.artefactTypeNaam   = 'Logical Data Model',
      atLdm.artefactFunctie    = 'vastleggend',
      atLdm.inhoudBeschrijving = 'Logical data model in 3NF';

MERGE (atDoctrine:ArtefactType {artefactTypeId: '003'})
  SET atDoctrine.artefactTypeNaam  = 'Doctrine',
      atDoctrine.artefactFunctie   = 'structurerend',
      atDoctrine.inhoudBeschrijving = 'Normative artifact that records behavioral rules';

MERGE (atHandoff:ArtefactType {artefactTypeId: '004'})
    SET atHandoff.artefactTypeNaam  = 'Handoff File',
      atHandoff.artefactFunctie   = 'registrerend',
      atHandoff.inhoudBeschrijving = 'Transfer document from agent to agent or agent to human';

// Template
MERGE (tplYaml:Template {templateId: '002'})
    SET tplYaml.templateNaam  = 'YAML Header Template - Mandarin Artifacts',
      tplYaml.inhoudTekst   = 'See templates/yaml-header.template.md';

// ARTIFACT TYPE -> TEMPLATE
MERGE (atCharter)-[:GEBRUIKT]->(tplYaml);


// ============================================================
// INTENTS
// ============================================================

MERGE (intDefinieer:Intent {intentId: 'aeo.02.agent-ontwerper.definieer-agent-charter'})
    SET intDefinieer.intentNaam    = 'Define Agent Charter',
      intDefinieer.inhoudContract = 'The agent designer defines a complete agent charter in accordance with doctrine-agent-charter-normering.md and stores it as a canonical artifact.';

MERGE (intValideer:Intent {intentId: 'fnd.01.agent-curator.valideer-canoniek-artefact'})
    SET intValideer.intentNaam    = 'Validate Canonical Artifact',
      intValideer.inhoudContract = 'The agent curator validates whether a submitted artifact meets the canonical requirements (YAML header, traceability, provenance code).';

// AGENT -> INTENT
MERGE (agOntwerper)-[:DEFINIEERT]->(intDefinieer);
MERGE (agCurator)-[:DEFINIEERT]->(intValideer);

// INTENT -> ARTIFACT TYPE
MERGE (intDefinieer)-[:PRODUCEERT_TYPE]->(atCharter);
MERGE (intValideer)-[:PRODUCEERT_TYPE]->(atDoctrine);


// ============================================================
// ORCHESTRATION RUN
// ============================================================

MERGE (run1:OrchestratieRun {orchestratieRunId: 'run-2604.0001'})
  SET run1.starttijdstip = datetime('2026-04-13T09:00:00Z'),
      run1.status        = 'completed',
      run1.inhouddoel    = 'Create an agent charter for the Agent Designer within AEO phase 02';


// ============================================================
// FRAME SOURCES AND WORK SOURCES
// ============================================================

MERGE (kb1:KaderBron {kaderBronId: 'kb-doctrine-agent-charter-normering'})
  SET kb1.headerDigest    = 'bef0',
      kb1.werkelijkeDigest = 'bef0';

MERGE (kb2:KaderBron {kaderBronId: 'kb-mandarin-domeinconcepten'})
  SET kb2.headerDigest    = 'tbd0',
      kb2.werkelijkeDigest = 'tbd0';

MERGE (wb1:WerkBron {werkBronId: 'wb-ldm-mandarin-v1.4.0'})
  SET wb1.headerDigest    = 'tbd0',
      wb1.werkelijkeDigest = 'tbd0';


// ============================================================
// PROVENANCE CHAIN
// ============================================================

MERGE (hk1:HerkomstKeten {herkomstCode: '2604.Aa1B'})
  SET hk1.oorsprong_tijdstip = datetime('2026-04-13T09:30:00Z');


// ============================================================
// EXECUTION
// ============================================================

MERGE (exec1:Execution {executieId: '2604.0001'})
  SET exec1.executieCode             = 'exec-2604.0001',
      exec1.executieDigest           = 'ab12cd34',
      exec1.bronhouding              = 'canon-gebonden',
      exec1.modus                    = 'tool-ondersteund',
      exec1.tijdstip                 = datetime('2026-04-13T09:30:00Z'),
      exec1.inhoudPromptInstructies  = 'Define an agent charter for the Agent Designer in accordance with doctrine-agent-charter-normering.md.';

// ORCHESTRATION RUN -> EXECUTION
MERGE (run1)-[:ORKESTREERT]->(exec1);

// EXECUTION -> AGENT / INTENT / SOURCE REGIME
MERGE (exec1)-[:UITGEVOERD_DOOR]->(agOntwerper);
MERGE (exec1)-[:VOERT_UIT]->(intDefinieer);
MERGE (exec1)-[:VALT_ONDER]->(brCanon);

// EXECUTION -> SOURCES
MERGE (exec1)-[:RAADPLEEGT_ALS_KADER]->(kb1);
MERGE (exec1)-[:RAADPLEEGT_ALS_KADER]->(kb2);
MERGE (exec1)-[:RAADPLEEGT_ALS_WERK]->(wb1);

// WORK SOURCE -> EXECUTION (originated_in)
MERGE (wb1)-[:ONTSTAAN_IN]->(exec1);


// ============================================================
// ARTIFACT
// ============================================================

MERGE (art1:MandarinArtefact {artefactId: 'art-2604.0001'})
  SET art1.herkomstpositie = 'initierend',
      art1.executieId      = '2604.0001',
      art1.tijdstip        = datetime('2026-04-13T10:00:00Z'),
      art1.inhoudTekst     = 'Agent Charter - Agent Designer v1.0.0';

// EXECUTION -> ARTIFACT (1:1 - N8 in LDM)
MERGE (exec1)-[:PRODUCEERT]->(art1);

// ARTIFACT -> ARTIFACT TYPE / AGENT / PROVENANCE CHAIN
MERGE (art1)-[:IS_VAN_TYPE]->(atCharter);
MERGE (art1)-[:GEGENEREERD_DOOR]->(agOntwerper);
MERGE (art1)-[:BEHOORT_TOT]->(hk1);

// FRAME SOURCE -> ARTIFACT (refers to canonical frame artifact)
MERGE (kb1)-[:VERWIJST_NAAR]->(art1);

// PROVENANCE CHAIN -> INITIATING ARTIFACT (deferred constraint - K6/K7)
MERGE (hk1)-[:GESTART_DOOR {deferred: true}]->(art1);


// ============================================================
// HANDOFF
// ============================================================

MERGE (hf1:Handoff {handoffId: 'hf-2604.0001'})
  SET hf1.menselijkeInterventie = false,
      hf1.tijdstip              = datetime('2026-04-13T10:05:00Z'),
      hf1.inhoudBoodschap       = 'Agent Charter art-2604.0001 is ready. Transfer to Agent Curator for canonical validation.';

// HANDOFF -> EXECUTION / AGENT
MERGE (hf1)-[:VLOEIT_VOORT_UIT]->(exec1);
MERGE (hf1)-[:ADRESSEERT]->(agCurator);

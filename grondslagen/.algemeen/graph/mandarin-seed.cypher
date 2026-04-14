// ============================================================
// Mandarin Ecosysteem — Seed Data
// ============================================================
// Minimale representatieve instanties per entiteitsklasse:
//   MandarinAgent, ValueStream, ValueStreamFase,
//   Intent, Execution, MandarinArtefact,
//   KaderBron, WerkBron, Bronregime,
//   HerkomstKeten, Handoff, Workspace,
//   ArtefactType, Template, OrchestratieRun
//
// Gesloten bronhouding: instanties zijn afgeleid van
//   mandarin-value-streams-en-fasen.md v1.8.0
//   doctrine-traceability.md v1.6.0
//   doctrine-handoff.md v1.2.0
// ============================================================


// ============================================================
// BRONREGIMES
// Vier canonieke posities van de bronhouding-as
// Bron: doctrine-bronhouding-en-exploratie.md v1.0.0
// ============================================================

MERGE (brInput:Bronregime {regimeId: 'input-gebonden'})
  SET brInput.beschrijving = 'Bron is aangeleverd als input voor de executie; de agent werkt uitsluitend met wat aangeleverd is';

MERGE (brCanon:Bronregime {regimeId: 'canon-gebonden'})
  SET brCanon.beschrijving = 'Bron is canoniek; de agent raadpleegt uitsluitend bronnen die in de canon zijn vastgelegd';

MERGE (brExtern:Bronregime {regimeId: 'externe-bron-gebonden'})
  SET brExtern.beschrijving = 'Bron bevindt zich buiten de canon maar is expliciet aangewezen en gecontroleerd';

MERGE (brExploratief:Bronregime {regimeId: 'exploratief'})
  SET brExploratief.beschrijving = 'De agent mag zelfstandig bronnen raadplegen; resultaat is niet canoniek';


// ============================================================
// WORKSPACE
// Bron: mandarin-domeinconcepten.md v2.13.0
// ============================================================

MERGE (ws:Workspace {workspaceId: 'ws-mandarin-canon'})
  SET ws.workspaceNaam = 'Mandarin Canon Workspace';


// ============================================================
// VALUE STREAMS
// Bron: mandarin-value-streams-en-fasen.md v1.8.0
// ============================================================

MERGE (fnd:ValueStream {waardestroomCode: 'fnd'})
  SET fnd.waardestroomNaam = 'Fundament',
      fnd.inhoudBeschrijving = 'Canonieke basis, doctrines, constitutie en grondslagen van het Mandarin-ecosysteem';

MERGE (aeo:ValueStream {waardestroomCode: 'aeo'})
  SET aeo.waardestroomNaam = 'Agent Ecosysteem Opzet',
      aeo.inhoudBeschrijving = 'Ontwerp en normering van het agent-ecosysteem';

MERGE (sfw:ValueStream {waardestroomCode: 'sfw'})
  SET sfw.waardestroomNaam = 'Software Werkstroom',
      sfw.inhoudBeschrijving = 'Softwareontwikkeling door agents binnen het ecosysteem';

MERGE (aod:ValueStream {waardestroomCode: 'aod'})
  SET aod.waardestroomNaam = 'Agent Ontwikkeling',
      aod.inhoudBeschrijving = 'Ontwikkeling en verfijning van individuele agents';

MERGE (knv:ValueStream {waardestroomCode: 'knv'})
  SET knv.waardestroomNaam = 'Kennisverwerking',
      knv.inhoudBeschrijving = 'Kennisverwerving, -verwerking en -borging';

MERGE (miv:ValueStream {waardestroomCode: 'miv'})
  SET miv.waardestroomNaam = 'Model Integratie en Validatie',
      miv.inhoudBeschrijving = 'Integratie, validatie en kwaliteitsborging van modellen';


// ============================================================
// VALUE STREAM FASEN
// Bron: mandarin-value-streams-en-fasen.md v1.8.0
// ============================================================

// Fundament
MERGE (fnd01:ValueStreamFase {faseCode: 'fnd.01'})
  SET fnd01.waardestroomNaam = 'Fundament — Grondslagen',
      fnd01.inhoudBeschrijving = 'Canonieke grondslagen, doctrines en constitutie';

// AEO
MERGE (aeo01:ValueStreamFase {faseCode: 'aeo.01'})
  SET aeo01.waardestroomNaam = 'AEO — Oriëntatie',
      aeo01.inhoudBeschrijving = 'Oriëntatie op het ecosysteem en het initiele ontwerp';

MERGE (aeo02:ValueStreamFase {faseCode: 'aeo.02'})
  SET aeo02.waardestroomNaam = 'AEO — Ontwerp',
      aeo02.inhoudBeschrijving = 'Ontwerp van agents, intents en charters';

MERGE (aeo03:ValueStreamFase {faseCode: 'aeo.03'})
  SET aeo03.waardestroomNaam = 'AEO — Verfijning',
      aeo03.inhoudBeschrijving = 'Verfijning en normering van het agent-ecosysteem';

// VALUE STREAM → VALUE STREAM FASE
MERGE (fnd)-[:OMVAT]->(fnd01);
MERGE (aeo)-[:OMVAT]->(aeo01);
MERGE (aeo)-[:OMVAT]->(aeo02);
MERGE (aeo)-[:OMVAT]->(aeo03);


// ============================================================
// AGENTS
// Bron: doctrine-agent-charter-normering.md v2.4.0
// ============================================================

MERGE (agOntwerper:MandarinAgent {agentId: 'aeo.02.agent-ontwerper'})
  SET agOntwerper.agentNaam  = 'Agent Ontwerper',
      agOntwerper.versie      = '1.0.0',
      agOntwerper.bronhouding = 'canon-gebonden',
      agOntwerper.inhoudCharter = 'Ontwerpt agent-charters en definieert de identiteit en verantwoordelijkheid van agents binnen het Mandarin-ecosysteem.';

MERGE (agCurator:MandarinAgent {agentId: 'fnd.01.agent-curator'})
  SET agCurator.agentNaam   = 'Agent Curator',
      agCurator.versie       = '1.0.0',
      agCurator.bronhouding  = 'canon-gebonden',
      agCurator.inhoudCharter = 'Beheert en valideert de canonieke grondslagen van het Mandarin-ecosysteem.';

// VALUE STREAM FASE → AGENT
MERGE (aeo02)-[:HUISVEST]->(agOntwerper);
MERGE (fnd01)-[:HUISVEST]->(agCurator);

// AGENT → BRONREGIME
MERGE (agOntwerper)-[:VALT_ONDER]->(brCanon);
MERGE (agCurator)-[:VALT_ONDER]->(brCanon);


// ============================================================
// ARTEFACT TYPES EN TEMPLATES
// Bron: ldm-mandarin.md v1.4.0, templates/yaml-header.template.md
// ============================================================

MERGE (atCharter:ArtefactType {artefactTypeId: '001'})
  SET atCharter.artefactTypeNaam  = 'Agent Charter',
      atCharter.artefactFunctie   = 'structurerend',
      atCharter.inhoudBeschrijving = 'Canoniek charter van een Mandarin-agent; legt identiteit, verantwoordelijkheid en capability boundary vast';

MERGE (atLdm:ArtefactType {artefactTypeId: '002'})
  SET atLdm.artefactTypeNaam   = 'Logisch Datamodel',
      atLdm.artefactFunctie    = 'vastleggend',
      atLdm.inhoudBeschrijving = 'Logisch datamodel in 3NF';

MERGE (atDoctrine:ArtefactType {artefactTypeId: '003'})
  SET atDoctrine.artefactTypeNaam  = 'Doctrine',
      atDoctrine.artefactFunctie   = 'structurerend',
      atDoctrine.inhoudBeschrijving = 'Normatief artefact dat gedragsregels vastlegt';

MERGE (atHandoff:ArtefactType {artefactTypeId: '004'})
  SET atHandoff.artefactTypeNaam  = 'Handoff Bestand',
      atHandoff.artefactFunctie   = 'registrerend',
      atHandoff.inhoudBeschrijving = 'Overdrachtsdocument van agent naar agent of agent naar mens';

// Template
MERGE (tplYaml:Template {templateId: '002'})
  SET tplYaml.templateNaam  = 'YAML Header Template — Mandarin Artefacten',
      tplYaml.inhoudTekst   = 'Zie templates/yaml-header.template.md';

// ARTEFACT TYPE → TEMPLATE
MERGE (atCharter)-[:GEBRUIKT]->(tplYaml);


// ============================================================
// INTENTS
// ============================================================

MERGE (intDefinieer:Intent {intentId: 'aeo.02.agent-ontwerper.definieer-agent-charter'})
  SET intDefinieer.intentNaam    = 'Definieer Agent Charter',
      intDefinieer.inhoudContract = 'De agent-ontwerper definieert een volledig agent-charter conform doctrine-agent-charter-normering.md en slaat het op als canoniek artefact.';

MERGE (intValideer:Intent {intentId: 'fnd.01.agent-curator.valideer-canoniek-artefact'})
  SET intValideer.intentNaam    = 'Valideer Canoniek Artefact',
      intValideer.inhoudContract = 'De agent-curator valideert of een aangeboden artefact voldoet aan de canonieke eisen (YAML-header, traceability, herkomstcode).';

// AGENT → INTENT
MERGE (agOntwerper)-[:DEFINIEERT]->(intDefinieer);
MERGE (agCurator)-[:DEFINIEERT]->(intValideer);

// INTENT → ARTEFACT TYPE
MERGE (intDefinieer)-[:PRODUCEERT_TYPE]->(atCharter);
MERGE (intValideer)-[:PRODUCEERT_TYPE]->(atDoctrine);


// ============================================================
// ORCHESTRATIE RUN
// ============================================================

MERGE (run1:OrchestratieRun {orchestratieRunId: 'run-2604.0001'})
  SET run1.starttijdstip = datetime('2026-04-13T09:00:00Z'),
      run1.status        = 'voltooid',
      run1.inhouddoel    = 'Aanmaken van een agent-charter voor de Agent Ontwerper binnen AEO fase 02';


// ============================================================
// KADER- EN WERKBRONNEN
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
// HERKOMST KETEN
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
      exec1.inhoudPromptInstructies  = 'Definieer een agent-charter voor de Agent Ontwerper conform doctrine-agent-charter-normering.md.';

// ORCHESTRATIE RUN → EXECUTION
MERGE (run1)-[:ORKESTREERT]->(exec1);

// EXECUTION → AGENT / INTENT / BRONREGIME
MERGE (exec1)-[:UITGEVOERD_DOOR]->(agOntwerper);
MERGE (exec1)-[:VOERT_UIT]->(intDefinieer);
MERGE (exec1)-[:VALT_ONDER]->(brCanon);

// EXECUTION → BRONNEN
MERGE (exec1)-[:RAADPLEEGT_ALS_KADER]->(kb1);
MERGE (exec1)-[:RAADPLEEGT_ALS_KADER]->(kb2);
MERGE (exec1)-[:RAADPLEEGT_ALS_WERK]->(wb1);

// WERKBRON → EXECUTION (entstaan_in)
MERGE (wb1)-[:ONTSTAAN_IN]->(exec1);


// ============================================================
// ARTEFACT
// ============================================================

MERGE (art1:MandarinArtefact {artefactId: 'art-2604.0001'})
  SET art1.herkomstpositie = 'initierend',
      art1.executieId      = '2604.0001',
      art1.tijdstip        = datetime('2026-04-13T10:00:00Z'),
      art1.inhoudTekst     = 'Agent Charter — Agent Ontwerper v1.0.0';

// EXECUTION → ARTEFACT (1:1 — N8 in LDM)
MERGE (exec1)-[:PRODUCEERT]->(art1);

// ARTEFACT → ARTEFACT TYPE / AGENT / HERKOMST KETEN
MERGE (art1)-[:IS_VAN_TYPE]->(atCharter);
MERGE (art1)-[:GEGENEREERD_DOOR]->(agOntwerper);
MERGE (art1)-[:BEHOORT_TOT]->(hk1);

// KADERBRON → ARTEFACT (verwijst naar canoniek kaderartefact)
MERGE (kb1)-[:VERWIJST_NAAR]->(art1);

// HERKOMST KETEN → INITIËEREND ARTEFACT (deferred constraint — K6/K7)
MERGE (hk1)-[:GESTART_DOOR {deferred: true}]->(art1);


// ============================================================
// HANDOFF
// ============================================================

MERGE (hf1:Handoff {handoffId: 'hf-2604.0001'})
  SET hf1.menselijkeInterventie = false,
      hf1.tijdstip              = datetime('2026-04-13T10:05:00Z'),
      hf1.inhoudBoodschap       = 'Agent Charter art-2604.0001 is gereed. Overdracht aan Agent Curator voor canonieke validatie.';

// HANDOFF → EXECUTION / AGENT
MERGE (hf1)-[:VLOEIT_VOORT_UIT]->(exec1);
MERGE (hf1)-[:ADRESSEERT]->(agCurator);

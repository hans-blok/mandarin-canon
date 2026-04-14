// ============================================================
// Mandarin Ecosysteem — Neo4j Schema
// ============================================================
// Bron: ldm-mandarin.md v1.4.0 (3NF, Barker-methode)
// Ontwerp-keuzes: zie mandarin-model.md
// Gesloten bronhouding: alle bronnen aanwezig in de workspace
// ============================================================


// ============================================================
// CONSTRAINTS — uniciteit op PK-velden
// ============================================================

// MandarinAgent
CREATE CONSTRAINT agent_id_unique IF NOT EXISTS
  FOR (n:MandarinAgent) REQUIRE n.agentId IS UNIQUE;

// ValueStream
CREATE CONSTRAINT value_stream_code_unique IF NOT EXISTS
  FOR (n:ValueStream) REQUIRE n.waardestroomCode IS UNIQUE;

// ValueStreamFase
CREATE CONSTRAINT value_stream_fase_code_unique IF NOT EXISTS
  FOR (n:ValueStreamFase) REQUIRE n.faseCode IS UNIQUE;

// Intent
CREATE CONSTRAINT intent_id_unique IF NOT EXISTS
  FOR (n:Intent) REQUIRE n.intentId IS UNIQUE;

// InvoerParameter
CREATE CONSTRAINT invoer_parameter_id_unique IF NOT EXISTS
  FOR (n:InvoerParameter) REQUIRE n.parameterId IS UNIQUE;

// OrchestratieRun
CREATE CONSTRAINT orchestratie_run_id_unique IF NOT EXISTS
  FOR (n:OrchestratieRun) REQUIRE n.orchestratieRunId IS UNIQUE;

// Execution — twee constraints: PK en UK
CREATE CONSTRAINT execution_id_unique IF NOT EXISTS
  FOR (n:Execution) REQUIRE n.executieId IS UNIQUE;

CREATE CONSTRAINT execution_code_unique IF NOT EXISTS
  FOR (n:Execution) REQUIRE n.executieCode IS UNIQUE;

// MandarinArtefact — twee constraints: PK en UK (executieId is FK+UK)
CREATE CONSTRAINT artefact_id_unique IF NOT EXISTS
  FOR (n:MandarinArtefact) REQUIRE n.artefactId IS UNIQUE;

CREATE CONSTRAINT artefact_executie_id_unique IF NOT EXISTS
  FOR (n:MandarinArtefact) REQUIRE n.executieId IS UNIQUE;

// ArtefactType
CREATE CONSTRAINT artefact_type_id_unique IF NOT EXISTS
  FOR (n:ArtefactType) REQUIRE n.artefactTypeId IS UNIQUE;

// Template
CREATE CONSTRAINT template_id_unique IF NOT EXISTS
  FOR (n:Template) REQUIRE n.templateId IS UNIQUE;

// HerkomstKeten
CREATE CONSTRAINT herkomst_code_unique IF NOT EXISTS
  FOR (n:HerkomstKeten) REQUIRE n.herkomstCode IS UNIQUE;

// KaderBron
CREATE CONSTRAINT kader_bron_id_unique IF NOT EXISTS
  FOR (n:KaderBron) REQUIRE n.kaderBronId IS UNIQUE;

// WerkBron
CREATE CONSTRAINT werk_bron_id_unique IF NOT EXISTS
  FOR (n:WerkBron) REQUIRE n.werkBronId IS UNIQUE;

// Handoff
CREATE CONSTRAINT handoff_id_unique IF NOT EXISTS
  FOR (n:Handoff) REQUIRE n.handoffId IS UNIQUE;

// Bronregime (extensienode — K4 in mandarin-model.md)
CREATE CONSTRAINT bronregime_id_unique IF NOT EXISTS
  FOR (n:Bronregime) REQUIRE n.regimeId IS UNIQUE;

// Workspace (extensienode — K5 in mandarin-model.md)
CREATE CONSTRAINT workspace_id_unique IF NOT EXISTS
  FOR (n:Workspace) REQUIRE n.workspaceId IS UNIQUE;


// ============================================================
// INDEXES — frequent bevraagde velden
// ============================================================

// Agents op status en bronhouding
CREATE INDEX agent_status_idx IF NOT EXISTS
  FOR (n:MandarinAgent) ON (n.status);

CREATE INDEX agent_bronhouding_idx IF NOT EXISTS
  FOR (n:MandarinAgent) ON (n.bronhouding);

// Executions op tijdstip, modus en bronhouding
CREATE INDEX execution_tijdstip_idx IF NOT EXISTS
  FOR (n:Execution) ON (n.tijdstip);

CREATE INDEX execution_modus_idx IF NOT EXISTS
  FOR (n:Execution) ON (n.modus);

CREATE INDEX execution_bronhouding_idx IF NOT EXISTS
  FOR (n:Execution) ON (n.bronhouding);

// Artefacten op herkomstpositie en tijdstip
CREATE INDEX artefact_herkomstpositie_idx IF NOT EXISTS
  FOR (n:MandarinArtefact) ON (n.herkomstpositie);

CREATE INDEX artefact_tijdstip_idx IF NOT EXISTS
  FOR (n:MandarinArtefact) ON (n.tijdstip);

// Handoffs op tijdstip en menselijkeInterventie (escalatie-filter)
CREATE INDEX handoff_tijdstip_idx IF NOT EXISTS
  FOR (n:Handoff) ON (n.tijdstip);

CREATE INDEX handoff_menselijke_interventie_idx IF NOT EXISTS
  FOR (n:Handoff) ON (n.menselijkeInterventie);

// ArtefactType op artefactFunctie
CREATE INDEX artefact_type_functie_idx IF NOT EXISTS
  FOR (n:ArtefactType) ON (n.artefactFunctie);

// OrchestratieRun op status
CREATE INDEX orchestratie_run_status_idx IF NOT EXISTS
  FOR (n:OrchestratieRun) ON (n.status);


// ============================================================
// VERWACHTE LABELS, RELATIETYPES EN EIGENSCHAPPEN
// (documentatie — geen DDL, voor validatie en tooling)
// ============================================================

// Labels:
//   MandarinAgent, ValueStream, ValueStreamFase,
//   Intent, InvoerParameter, OrchestratieRun,
//   Execution, MandarinArtefact, ArtefactType,
//   BeschrijvendArtefactType (multi-label op ArtefactType — K2),
//   Template, HerkomstKeten, KaderBron, WerkBron,
//   Handoff, Bronregime, Workspace

// Relatietypes:
//   OMVAT, HUISVEST, HEEFT_SUBTYPE, GEBRUIKT,
//   DEFINIEERT, VEREIST, PRODUCEERT_TYPE,
//   ORKESTREERT, UITGEVOERD_DOOR, VOERT_UIT, PRODUCEERT,
//   RAADPLEEGT_ALS_KADER, RAADPLEEGT_ALS_WERK,
//   IS_VAN_TYPE, GEGENEREERD_DOOR, BEHOORT_TOT,
//   GESTART_DOOR, VERWIJST_NAAR, ONTSTAAN_IN,
//   VLOEIT_VOORT_UIT, ADRESSEERT, VALT_ONDER

// Relatie-eigenschappen:
//   GESTART_DOOR { deferred: Boolean }
//     — zie N6 in ldm-mandarin.md en K6/K7 in mandarin-model.md

---
type: ontologie
naam: Mandarin Ecosystem Ontology (compact)
versie: 2.0.0
status: vers
afleidingspositie: afgeleid
bron: ontologie.ttl v1.0.0
---

# Mandarin Ecosystem Ontology (compact)

> Derived LLM injection source. Primary source: `ontologie.ttl`.  
> When `ontologie.ttl` changes, this file must be regenerated.  
> Use for standard agent executions. Inject `ontologie.ttl` for graph-structuring or ontology-validation tasks.

---

## Language Rule

Within the ecosystem, only the canonical terms from this document are used. Synonyms are forbidden in governance artifacts, charters, doctrines, and agent contracts.

---

## Meta Concepts

```yaml
concept_id: mandarin.mandarin-concept
term_nl: mandarin-concept
term_en: mandarin-concept
definitie_nl: Expliciet gedefinieerd, samenhangend en herbruikbaar bouwblok dat een fundamenteel begrip, structuur of mechanisme beschrijft.
definition_en: Explicitly defined, coherent, and reusable building block describing a fundamental notion, structure, or mechanism.
kenmerken_nl: onderdeel van de canon; geen tijdelijke afspraak; herbruikbaar als referentie
features_en: part of the canon; not a temporary agreement; reusable as reference
```

```yaml
concept_id: mandarin.actieve-structuur
term_nl: actieve structuur
term_en: active structure
definitie_nl: Functioneel element dat zelfstandig of in samenwerking taken uitvoert, interactie aangaat en output produceert.
definition_en: Functional element that independently or collaboratively executes tasks, engages in interaction, and produces output.
kenmerken_nl: expliciete rol of functie; in staat tot handelen; toetsbaar op gedrag en output
features_en: explicit role or function; capable of action; testable on behavior and output
relaties:
  - subklasse-van → Mandarin-concept
  - voorbeelden zijn → Mandarin-agent, Workspace, Value stream
```

```yaml
concept_id: mandarin.mandarin-ecosysteem
term_nl: mandarin-ecosysteem
term_en: mandarin-ecosystem
definitie_nl: Overkoepelende, samenhangende verzameling van alle Mandarin-concepten, actieve structuren, artefacten, governance-mechanismen en hun onderlinge relaties.
definition_en: Overarching, coherent collection of all Mandarin concepts, active structures, artifacts, governance mechanisms, and their interrelationships.
kenmerken_nl: adaptief en uitbreidbaar; waarborgt expliciete contracten en governance; zelfregistrerend
features_en: adaptive and extensible; ensures explicit contracts and governance; self-registering
```

---

## Agent and Governance

```yaml
concept_id: mandarin.mandarin-agent
term_nl: mandarin-agent
term_en: mandarin-agent
definitie_nl: Expliciet gedefinieerde, autonome software-entiteit die op basis van een formeel agent-charter en agent-contract specifieke taken uitvoert en Mandarin-artefacten produceert.
definition_en: Explicitly defined, autonomous software entity that executes specific tasks and produces Mandarin artifacts based on a formal agent charter and agent contract.
kenmerken_nl: heeft charter en contract; opereert binnen expliciete boundary; voert één of meer capabilities uit; herbruikbaar en vervangbaar
features_en: has charter and contract; operates within explicit boundary; executes one or more capabilities; reusable and replaceable
relaties:
  - heeft → Agent-charter (verplicht, min. 1)
  - heeft → Agent-boundary (verplicht, precies 1)
  - heeft → Agent-contract
  - voert-uit → Agent-capability
  - produceert → Mandarin-artefact
  - valt-onder → Bronregime
```

```yaml
concept_id: mandarin.agent-boundary
term_nl: agent-boundary
term_en: agent-boundary
definitie_nl: Expliciet vastgelegde servicegrens waarbinnen een Mandarin-agent zijn interne werking organiseert; buiten deze grens is interactie uitsluitend mogelijk via formele agent-contracten.
definition_en: Explicitly defined service boundary within which a Mandarin agent organizes its internal operation; beyond this boundary, interaction is only possible through formal agent contracts.
kenmerken_nl: scheidt interne werking van externe interactie; verplichte eerste stap in agent-ontwerp
features_en: separates internal operation from external interaction; mandatory first step in agent design
relaties:
  - begrenst → Mandarin-agent
```

```yaml
concept_id: mandarin.agent-charter
term_nl: agent-charter
term_en: agent-charter
definitie_nl: Formeel document dat de missie, verantwoordelijkheden, grenzen en governance van een specifieke Mandarin-agent vastlegt.
definition_en: Formal document that establishes the mission, responsibilities, boundaries, and governance of a specific Mandarin agent.
kenmerken_nl: legt missie en bestaansrecht vast; versieerbaar en vastleggend; basis voor het agent-contract
features_en: establishes mission and purpose; versionable and binding; basis for the agent contract
relaties:
  - legt-vast → Mandarin-agent missie
```

```yaml
concept_id: mandarin.agent-capability
term_nl: agent-capability
term_en: agent-capability
definitie_nl: Expliciet aanroepbare functie van een Mandarin-agent, vastgelegd in een agent-contract. Één capability = één intent.
definition_en: Explicitly invocable function of a Mandarin agent, specified in an agent contract. One capability = one intent.
kenmerken_nl: aanroepbaar (uitvoerbaar); vastgelegd in contract; één-op-één met een intent
features_en: invocable (executable); specified in contract; one-to-one with an intent
relaties:
  - vastgelegd-in → Agent-contract
  - uitgevoerd-door → Mandarin-agent
```

```yaml
concept_id: mandarin.agent-contract
term_nl: agent-contract
term_en: agent-contract
definitie_nl: Formele specificatie van de intent van een Mandarin-agent, de verwachte input, te produceren output en geldende beleidsregels.
definition_en: Formal specification of a Mandarin agent's intent, expected input, output to be produced, and applicable policy rules.
kenmerken_nl: definieert input/output-afspraken; bevat herkomstpositie van output; geen interne implementatiedetails
features_en: defines input/output agreements; contains provenance position of output; no internal implementation details
relaties:
  - definieert → Agent-capability
  - basis-voor → Execution-bestand
```

```yaml
concept_id: mandarin.mandarin-capability
term_nl: mandarin-capability
term_en: mandarin-capability
definitie_nl: Duurzaam, herbruikbaar vermogen van het Mandarin-ecosysteem om een bepaald type waarde te realiseren, onafhankelijk van specifieke agents of tooling.
definition_en: Durable, reusable capacity of the Mandarin ecosystem to realize a specific type of value, independent of specific agents or tooling.
kenmerken_nl: stabiel in de tijd; niet aan één agent gekoppeld; inzetbaar in meerdere value stream fasen
features_en: stable over time; not tied to a single agent; deployable in multiple value stream phases
```

```yaml
concept_id: mandarin.prompt
term_nl: prompt
term_en: prompt
definitie_nl: Concrete, tekstuele of gestructureerde uitdrukking van een aanroep of instructie aan een Mandarin-agent; geen canoniek onderdeel van het agent-contract.
definition_en: Concrete, textual or structured expression of an invocation or instruction to a Mandarin agent; not a canonical part of the agent contract.
kenmerken_nl: tijdelijk en situationeel; tooling- en implementatiegebonden; representatie van beoogde aanroep, geen formele capability-definitie
features_en: temporary and situational; tooling- and implementation-bound; representation of intended invocation, not a formal capability definition
relaties:
  - gericht-aan → Mandarin-agent
```

---

## Handoff and Transfer

```yaml
concept_id: mandarin.handoff
term_nl: handoff
term_en: handoff
definitie_nl: Expliciete, traceerbare overdracht van taak, context en verantwoordelijkheid van de ene Mandarin-agent naar de andere, als discrete gebeurtenis in een meervoudige agent-keten.
definition_en: Explicit, traceable transfer of task, context, and responsibility from one Mandarin agent to another, as a discrete event in a multi-agent chain.
kenmerken_nl: expliciete overdrachtsgebeurtenis; horizontale koppeling in multi-agent keten; traceerbaar via handoff-identificatie; ontkoppelt producerende en ontvangende agent
features_en: explicit transfer event; horizontal coupling in multi-agent chain; traceable via handoff identification; decouples producing and receiving agent
relaties:
  - heeft → Handoff-identificatie (verplicht, precies 1)
  - vloeit-voort-uit → Execution-bestand
  - adresseert → Mandarin-agent (ontvanger)
```

```yaml
concept_id: mandarin.handoff-identificatie
term_nl: handoff-identificatie
term_en: handoff-identification
definitie_nl: Unieke identifier van een specifieke handoff-gebeurtenis. Formaat: hf-JJMM.NNNN.
definition_en: Unique identifier of a specific handoff event. Format: hf-YYMM.NNNN.
kenmerken_nl: gegenereerd door de runner; stabiel per handoff-gebeurtenis; per kalendermaand oplopend volgnummer; nooit hergebruikt
features_en: generated by the runner; stable per handoff event; incrementing sequence number per calendar month; never reused
relaties:
  - identificeert → Handoff
```

```yaml
concept_id: mandarin.handoff-bestand
term_nl: handoff-bestand
term_en: handoff-file
definitie_nl: Canoniek artefact aangemaakt door de overdragende agent aan het einde van een executie, gericht op het informeren van de ontvangende agent (vooruitkijkend).
definition_en: Canonical artifact created by the transferring agent at the end of an execution, aimed at informing the receiving agent (forward-looking).
kenmerken_nl: kijkt vooruit (naar ontvanger); onveranderlijk na uitgifte; bevat human_in_the_loop-indicatie; complement van execution-trace-bestand
features_en: looks forward (to receiver); immutable after issuance; contains human_in_the_loop indication; complement of execution-trace-file
relaties:
  - sleutel → Handoff-identificatie
  - verwijst-naar → Execution-bestand (via execution_code)
```

---

## Artifacts

```yaml
concept_id: mandarin.mandarin-artefact
term_nl: mandarin-artefact
term_en: mandarin-artifact
definitie_nl: Duurzame, expliciete en overdraagbare vastlegging van resultaat of besluitvorming die binnen een value stream fase waarde representeert.
definition_en: Durable, explicit, and transferable recording of result or decision-making that represents value within a value stream phase.
kenmerken_nl: duurzaam; expliciet (leesbaar, inspecteerbaar); overdraagbaar; heeft herkomstpositie (initierend of voortbouwend)
features_en: durable; explicit (readable, inspectable); transferable; has provenance position (initiating or continuing)
relaties:
  - behoort-tot → Herkomst-keten
  - is-van-type → Artefacttype
  - gegenereerd-door → Mandarin-agent
```

```yaml
concept_id: mandarin.governance-artefact
term_nl: governance-artefact
term_en: governance-artifact
definitie_nl: Specialisatie van vastleggend artefact voor het ecosysteem als geheel; ontstaat uitsluitend in value stream 0 (AEO).
definition_en: Specialization of binding artifact for the ecosystem as a whole; originates exclusively in value stream 0 (AEO).
kenmerken_nl: ecosysteem- en value-stream-overstijgend; prescriptief; vastleggend van kaders en regels
features_en: transcends ecosystem and value stream; prescriptive; binding for frameworks and rules
relaties:
  - subklasse-van → Mandarin-artefact
```

```yaml
concept_id: mandarin.richtinggevend-artefact
term_nl: richtinggevend artefact
term_en: directive-artifact
definitie_nl: Specialisatie van vastleggend artefact dat richting geeft aan een value stream fase in waarde value streams 1-n.
definition_en: Specialization of binding artifact that provides direction to a value stream phase in value streams 1-n.
kenmerken_nl: inhoudelijke keuzes en gewenste resultaten; primair artefact (niet afgeleid); input voor volgende fasen
features_en: substantive choices and desired outcomes; primary artifact (not derived); input for subsequent phases
relaties:
  - subklasse-van → Mandarin-artefact
```

```yaml
concept_id: mandarin.structurerend-artefact
term_nl: structurerend artefact
term_en: structuring-artifact
definitie_nl: Mandarin-artefact dat een coherent geheel van architectuurelementen en hun onderlinge relaties representeert, geordend volgens een metamodel.
definition_en: Mandarin artifact that represents a coherent whole of architectural elements and their interrelationships, ordered according to a metamodel.
kenmerken_nl: metamodel-conform; maakt structuur expliciet en beredeneerbaar; coherent en intern consistent
features_en: metamodel-compliant; makes structure explicit and reasoned; coherent and internally consistent
relaties:
  - subklasse-van → Mandarin-artefact
```

```yaml
concept_id: mandarin.registrerend-artefact
term_nl: registrerend artefact
term_en: recording-artifact
definitie_nl: Mandarin-artefact dat bestaande of voorgenomen werkelijkheid inzichtelijk maakt zonder zelf vastleggend of realiserend te zijn.
definition_en: Mandarin artifact that makes existing or intended reality visible without being binding or realizing itself.
kenmerken_nl: beschrijvend of evaluerend; geen normatieve kracht; analyses, overzichten, documentatie
features_en: descriptive or evaluative; no normative force; analyses, overviews, documentation
relaties:
  - subklasse-van → Mandarin-artefact
```

```yaml
concept_id: mandarin.template
term_nl: template
term_en: template
definitie_nl: Herbruikbare, gestructureerde opzet voor een Mandarin-artefact of prompt die minimale inhoud en secties voorschrijft.
definition_en: Reusable, structured layout for a Mandarin artifact or prompt that prescribes minimum content and sections.
kenmerken_nl: legt structuur en verplichte onderdelen vast; beheerd in templates/-folder; geen vervanging van het onderliggende artefact
features_en: defines structure and mandatory components; managed in templates/ folder; not a replacement for the underlying artifact
relaties:
  - gebruikt-door → Artefacttype
  - toegepast-door → Mandarin-agent
```

---

## Value Streams and Workspace

```yaml
concept_id: mandarin.value-stream
term_nl: value stream
term_en: value stream
definitie_nl: Expliciet gedefinieerde keten van waarde-creërende stappen die samen leiden tot een herkenbaar resultaat.
definition_en: Explicitly defined chain of value-creating steps that together lead to a recognizable result.
kenmerken_nl: definieert stappen, geen taken; artefact-gericht; agent-agnostisch maar agent-sturend
features_en: defines steps, not tasks; artifact-oriented; agent-agnostic but agent-directing
relaties:
  - omvat → Value stream fase (1..n)
```

```yaml
concept_id: mandarin.value-stream-fase
term_nl: value stream fase
term_en: value stream phase
definitie_nl: Logisch afgebakende, waarde-creërende eenheid binnen een value stream, zichtbaar via expliciete artefacttypen en kwaliteitscriteria.
definition_en: Logically bounded, value-creating unit within a value stream, visible through explicit artifact types and quality criteria.
kenmerken_nl: waardemoment, geen activiteit; beschrijft wat, niet hoe; vormt context voor werkende agents
features_en: value moment, not activity; describes what, not how; forms context for working agents
relaties:
  - deel-van → Value stream
  - huisvest → Mandarin-agent
```

```yaml
concept_id: mandarin.workspace
term_nl: workspace
term_en: workspace
definitie_nl: Afgebakende werkomgeving ingericht om één of meer value stream fasen uit te werken, met bijbehorende artefacten, governance en ondersteunende agents.
definition_en: Bounded work environment set up to develop one or more value stream phases, with associated artifacts, governance, and supporting agents.
kenmerken_nl: activeert agents; contextualiseert werk tot specifieke fasen; kan meerdere fasen ondersteunen
features_en: activates agents; contextualizes work to specific phases; can support multiple phases
relaties:
  - ondersteunt → Value stream fase
```

---

## Sources and Execution

```yaml
concept_id: mandarin.bronrol
term_nl: bronrol
term_en: source-role
definitie_nl: Relationele eigenschap die beschrijft hoe een artefact wordt gebruikt binnen een concrete agent-executie; niet intrinsiek maar context-gebonden.
definition_en: Relational property that describes how an artifact is used within a concrete agent execution; not intrinsic but context-bound.
kenmerken_nl: ontstaat pas in executiecontext; zelfde artefact kan in verschillende executies andere bronrollen vervullen; twee posities: kaderbron en werkbron
features_en: only arises in execution context; same artifact can fulfill different source roles in different executions; two positions: frame source and work source
relaties:
  - posities → Kaderbron, Werkbron
```

```yaml
concept_id: mandarin.kaderbron
term_nl: kaderbron
term_en: frame-source
definitie_nl: Positie op de as bronrol: artefact dat kader, mandaat en kennis levert waarop de Mandarin-agent zijn handelen legitimeert. Wordt niet bewerkt tijdens de executie.
definition_en: Position on the source-role axis: artifact that provides framework, mandate, and knowledge on which the Mandarin agent legitimizes its actions. Not modified during execution.
kenmerken_nl: levert normatieve en kennisbasis; typisch: charters, canon, doctrines, beleidsdocumenten
features_en: provides normative and knowledge base; typically: charters, canon, doctrines, policy documents
relaties:
  - subklasse-van → Bronrol
  - verwijst-naar → Mandarin-artefact
```

```yaml
concept_id: mandarin.werkbron
term_nl: werkbron
term_en: work-source
definitie_nl: Positie op de as bronrol: artefact dat wordt ingelezen om te bewerken, analyseren of verwerken als het materiaal waarop de agent zijn intent toepast.
definition_en: Position on the source-role axis: artifact that is read in to be edited, analyzed, or processed as the material on which the agent applies its intent.
kenmerken_nl: inhoudelijke scope van de executie; kan worden gelezen, geanalyseerd, gevalideerd of getransformeerd
features_en: substantive scope of the execution; can be read, analyzed, validated, or transformed
relaties:
  - subklasse-van → Bronrol
  - verwijst-naar → Mandarin-artefact
```

```yaml
concept_id: mandarin.bronregime
term_nl: bronregime
term_en: source-regime
definitie_nl: Expliciet vastgelegd stelsel van toegestane kennisbronnen en afleidingsregels waarbinnen een Mandarin-agent betekenis mag vormen of artefacten mag produceren.
definition_en: Explicitly defined system of permitted knowledge sources and derivation rules within which a Mandarin agent may form meaning or produce artifacts.
kenmerken_nl: bepaalt welke bronnen geldig en uitgesloten zijn; reguleert determinisme vs. probabilisme; operationaliseert de bronhouding-as
features_en: determines which sources are valid and excluded; regulates determinism vs. probabilism; operationalizes the source-stance axis
relaties:
  - geldt-voor → Mandarin-agent
  - geldt-voor → Execution-bestand
```

```yaml
concept_id: mandarin.broninjectie
term_nl: broninjectie
term_en: source-injection
definitie_nl: Overkoepelend concept voor het beschikbaar maken van expliciete bronnen aan een LLM ten behoeve van een agent-executie.
definition_en: Overarching concept for making explicit sources available to an LLM for the purpose of an agent execution.
kenmerken_nl: omvat bronassemblage (handeling) en bronpakket (product); tijdgebonden per executie; onder toezicht van bronregime
features_en: includes source assembly (action) and source package (product); time-bound per execution; under supervision of source regime
relaties:
  - omvat → Bronassemblage
  - omvat → Bronpakket
```

```yaml
concept_id: mandarin.bronassemblage
term_nl: bronassemblage
term_en: source-assembly
definitie_nl: Handeling waarmee de runner relevante kaderbronnen en werkbronnen selecteert, ordent en samenvoegt tot één geheel dat aan het LLM wordt aangeboden.
definition_en: Action by which the runner selects, orders, and merges relevant frame sources and work sources into one whole that is offered to the LLM.
kenmerken_nl: een proces, geen product; uitgevoerd door de runner; deterministisch bij gelijke input
features_en: a process, not a product; executed by the runner; deterministic with equal input
relaties:
  - deel-van → Broninjectie
  - produceert → Bronpakket
  - stuurt → Kaderbron, Werkbron
```

```yaml
concept_id: mandarin.bronpakket
term_nl: bronpakket
term_en: source-package
definitie_nl: Samengesteld geheel van expliciete bronnen zoals het LLM dit bereikt op het moment van een agent-executie; resultaat van bronassemblage.
definition_en: Composite whole of explicit sources as it reaches the LLM at the moment of an agent execution; result of source assembly.
kenmerken_nl: een product, geen proces; begrenst welke claims de output mag bevatten; herleidbaar
features_en: a product, not a process; limits which claims the output may contain; traceable
relaties:
  - deel-van → Broninjectie
  - bevat → Kaderbron, Werkbron
```

```yaml
concept_id: mandarin.execution-bestand
term_nl: execution-bestand
term_en: execution-file
definitie_nl: Technisch artefact waarin de runner een concrete agent-executie vastlegt als één uitvoerbaar en traceerbaar geheel.
definition_en: Technical artifact in which the runner records a concrete agent execution as one executable and traceable whole.
kenmerken_nl: bevat execution-identiteit, opdracht, parameters, bronpakket; opgeslagen in executions/; breder dan bronpakket alleen
features_en: contains execution identity, assignment, parameters, source package; stored in executions/; broader than source package alone
relaties:
  - heeft → Execution-code (verplicht, precies 1)
  - heeft → Execution-digest (verplicht, precies 1)
  - heeft → Execution-trace-bestand (verplicht, min. 1)
  - raadpleegt-als-kader → Kaderbron
  - raadpleegt-als-werk → Werkbron
```

```yaml
concept_id: mandarin.execution-trace-bestand
term_nl: execution-trace-bestand
term_en: execution-trace-file
definitie_nl: Apart traceerbaarheidsartefact naast het execution-bestand dat per opgenomen bron of segment de herkomst, opnamevorm en reden van opname vastlegt.
definition_en: Separate traceability artifact alongside the execution file that records, per included source or segment, the provenance, inclusion form, and reason for inclusion.
kenmerken_nl: zelfstandig artefact; audit- en linkdrager; gekoppeld via execution_id en execution_digest
features_en: standalone artifact; audit and link carrier; coupled via execution_id and execution_digest
relaties:
  - hoort-bij → Execution-bestand (precies 1)
```

```yaml
concept_id: mandarin.execution-digest
term_nl: execution-digest
term_en: execution-digest
definitie_nl: Inhoudsgebonden hash (SHA-256) van een execution-bestand die de integriteit aantoonbaar maakt.
definition_en: Content-bound hash (SHA-256) of an execution file that demonstrably establishes integrity.
kenmerken_nl: verandert bij inhoudswijziging; integriteitsanker in execution-trace-bestand; geen stabiel adres
features_en: changes on content modification; integrity anchor in execution-trace-file; not a stable address
relaties:
  - integriteitsanker-van → Execution-bestand
```

```yaml
concept_id: mandarin.execution-code
term_nl: execution-code
term_en: execution-code
definitie_nl: Stabiel, persistent adres waarmee een specifieke agent-executie wordt aangewezen, ongeacht latere wijzigingen in het execution-bestand. Formaat: exec-JJMM.XXXX.
definition_en: Stable, persistent address by which a specific agent execution is designated, regardless of later changes to the execution file. Format: exec-YYMM.XXXX.
kenmerken_nl: verandert nooit na aanmaak; primaire verwijzingseenheid vanuit andere artefacten en ketens
features_en: never changes after creation; primary reference unit from other artifacts and chains
relaties:
  - adresseert → Execution-bestand
```

```yaml
concept_id: mandarin.externe-grondslag
term_nl: externe grondslag
term_en: external-foundation
definitie_nl: Bron van buiten het Mandarin-ecosysteem die een bruikbaar denkkader biedt; heeft geen normatieve status totdat selectie en kadering hebben plaatsgevonden.
definition_en: Source from outside the Mandarin ecosystem that offers a usable conceptual framework; has no normative status until selection and framing have taken place.
kenmerken_nl: ruwe, niet-gecontroleerde kennis; nooit rechtstreeks door agents te raadplegen; toegang alleen via kaderdefinitie
features_en: raw, uncontrolled knowledge; never directly consultable by agents; access only via frame definition
relaties:
  - grondstof-voor → Kaderdefinitie
```

```yaml
concept_id: mandarin.kaderdefinitie
term_nl: kaderdefinitie
term_en: frame-definition
definitie_nl: Geïnternaliseerde, gecontroleerde versie van een externe grondslag die de Mandarin-interpretatie, scope en beperkingen expliciet vastlegt.
definition_en: Internalized, controlled version of an external foundation that explicitly establishes the Mandarin interpretation, scope, and limitations.
kenmerken_nl: afgeleid van één externe grondslag; enige toegestane basis voor agent-gebruik van externe kennis; versieerbaar en traceerbaar
features_en: derived from one external foundation; only permitted basis for agent use of external knowledge; versionable and traceable
relaties:
  - afgeleid-van → Externe grondslag
```

---

## Provenance Chain

```yaml
concept_id: mandarin.herkomst-keten
term_nl: herkomst-keten
term_en: provenance-chain
definitie_nl: Reeks van initierende en voortbouwende artefacten verbonden aan dezelfde herkomstcode; borgt traceerbaarheid naar de oorsprong.
definition_en: Series of initiating and continuing artifacts connected to the same provenance code; ensures traceability to the origin.
kenmerken_nl: identificeerbaar via herkomstcode (formaat: JJMM.XXXX); gestart door initierend artefact; alle voortbouwende artefacten erven de code
features_en: identifiable via provenance code (format: YYMM.XXXX); started by initiating artifact; all continuing artifacts inherit the code
relaties:
  - gestart-door → Mandarin-artefact (initierend)
  - omvat → Mandarin-artefact (voortbouwend)
```

---

## Classification Axes (Ordering Concepts)

```yaml
concept_id: mandarin.mandarin-agent-classificatie
term_nl: mandarin-agent-classificatie
term_en: mandarin-agent-classification
definitie_nl: Expliciet positioneren van een Mandarin-agent langs vier orthogonale assen: betekeniseffect, vormingsfase, werking en bronhouding.
definition_en: Explicitly positioning a Mandarin agent along four orthogonal axes: meaning effect, formation phase, operation, and source stance.
kenmerken_nl: geen enkelvoudig label; agent neemt posities in op alle vier assen; assen zijn onafhankelijk van elkaar
features_en: no single label; agent takes positions on all four axes; axes are independent of each other
relaties:
  - bestaat-uit → Betekeniseffect, Werking, Vormingsfase, Bronhouding
```

```yaml
concept_id: mandarin.curator-agent
term_nl: curator-agent
term_en: curator-agent
definitie_nl: Mandarin-agent met classificatieprofiel: evaluerend (betekeniseffect), canon-gebonden (bronhouding), inhoudelijk (werking), toetsing (vormingsfase).
definition_en: Mandarin agent with classification profile: evaluating (meaning effect), canon-bound (source stance), substantive (operation), testing (formation phase).
kenmerken_nl: beoordeelt en bewaakt kwaliteit; canon-gebonden; werkt op betekenisvolle artefacten
features_en: assesses and guards quality; canon-bound; operates on meaningful artifacts
relaties:
  - subklasse-van → Mandarin-agent
  - heeft-profiel → evaluerend, canon-gebonden, inhoudelijk, toetsing
```

```yaml
concept_id: mandarin.betekeniseffect
term_nl: betekeniseffect
term_en: meaning-effect
definitie_nl: Classificatie-as die het effect van een Mandarin-agent op de betekenis van het werk beschrijft.
definition_en: Classification axis that describes the effect of a Mandarin agent on the meaning of the work.
posities_nl: vastleggend | normerend | beschrijvend | structurerend | realiserend | evaluerend | (nul: geen effect)
positions_en: binding | normative | descriptive | structuring | realizing | evaluating | (null: no effect)
```

```yaml
concept_id: mandarin.werking
term_nl: werking
term_en: operation
definitie_nl: Classificatie-as die beschrijft of een agent intervenieert in de inhoud, de vorm of de voorwaarden.
definition_en: Classification axis that describes whether an agent intervenes in the content, the form, or the conditions.
posities_nl: inhoudelijk | representatie-omvormend | conditioneel
positions_en: substantive | representation-transforming | conditional
```

```yaml
concept_id: mandarin.vormingsfase
term_nl: vormingsfase
term_en: formation-phase
definitie_nl: Classificatie-as die beschrijft in welke fase een interventie plaatsvindt.
definition_en: Classification axis that describes in which phase an intervention takes place.
posities_nl: verkenning | ordening | vastlegging | realisatie | toetsing | operationalisatie
positions_en: exploration | ordering | recording | realization | testing | operationalization
```

```yaml
concept_id: mandarin.bronhouding
term_nl: bronhouding
term_en: source-stance
definitie_nl: Classificatie-as die de toegestane bronruimte van een agent bepaalt.
definition_en: Classification axis that determines the permitted source space of an agent.
posities_nl: input-gebonden | canon-gebonden | workspace-gebonden | externe-bron-gebonden | exploratief
positions_en: input-bound | canon-bound | workspace-bound | external-source-bound | explorative
```

```yaml
concept_id: mandarin.herkomstpositie
term_nl: herkomstpositie
term_en: provenance-position
definitie_nl: Ordeningsconcept dat de positie van een Mandarin-artefact in de creatie-keten vastlegt.
definition_en: Ordering concept that establishes the position of a Mandarin artifact in the creation chain.
posities_nl:
  - initierend — bron-artefact dat een unieke herkomstcode genereert
  - voortbouwend — artefact dat de herkomstcode erft van het initierende artefact
positions_en:
  - initiating — source artifact that generates a unique provenance code
  - continuing — artifact that inherits the provenance code from the initiating artifact
```

```yaml
concept_id: mandarin.artefacttoestand
term_nl: artefacttoestand
term_en: artifact-state
definitie_nl: Dynamische operationele eigenschap die aangeeft of een artefact actueel is (digest-status).
definition_en: Dynamic operational property that indicates whether an artifact is current (digest status).
posities_nl:
  - vers — digest klopt; artefact is actueel
  - muf — kleine afwijking; geen impact op afleidingsketen; geen cascade
  - rot — functionele wijziging; downstream regeneratie vereist
positions_en:
  - fresh — digest matches; artifact is current
  - stale — minor deviation; no impact on derivation chain; no cascade
  - rotten — functional change; downstream regeneration required
```

```yaml
concept_id: mandarin.afleidingspositie
term_nl: afleidingspositie
term_en: derivation-position
definitie_nl: Metaconcept dat vastlegt of een representatie leidend (primair vastleggingspunt) of afgeleid (mechanisch gegenereerd) is.
definition_en: Metaconcept that establishes whether a representation is leading (primary recording point) or derived (mechanically generated).
posities_nl: leidend | afgeleid
positions_en: leading | derived
```

```yaml
concept_id: mandarin.representatie
term_nl: representatie
term_en: representation
definitie_nl: Specifieke vorm waarin een artefact of betekenis wordt vastgelegd, weergegeven of uitgewisseld; bepaalt hoe, niet wat.
definition_en: Specific form in which an artifact or meaning is recorded, displayed, or exchanged; determines how, not what.
vormen_nl: tekst (Markdown, JSON, YAML) | diagram (ArchiMate, UML) | programmacode | machinetaal
forms_en: text (Markdown, JSON, YAML) | diagram (ArchiMate, UML) | program code | machine language
```

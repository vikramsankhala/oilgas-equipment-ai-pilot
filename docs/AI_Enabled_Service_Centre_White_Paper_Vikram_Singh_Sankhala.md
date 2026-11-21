# Table of Contents

# AI-ENABLED SERVICE-CENTRE EXCELLENCE

## From Equipment Telemetry to Reliability, Repair Turnaround, Quality and Financial Performance

**A practical, auditable operating framework for compression and
rotating-equipment service centres**

**Vikram Singh Sankhala**  
Former AI Solutions Architect, SAP · Assistant Professor, MPSTME / NMIMS
University  
B.Tech (Honours), IIT Kharagpur · MBA, IIM Calcutta · FRM (GARP)

**Industry white paper \| Research and implementation framework \|
November 2026**

**Companion research demonstration:**
<https://github.com/vikramsankhala/oilgas-equipment-ai-pilot>

**Scope and integrity statement.** This paper develops a proposed
service-centre transformation framework, grounded in an existing
open-source, read-only anomaly-screening demonstration. No actual
Siemens Energy deployment, service-centre benchmark, production
predictive-maintenance system, certified safety function, measured
financial saving, or customer outcome is claimed. Illustrative figures
and workflows are decision aids requiring site-specific validation. The
author is not presenting an operational repair-management system as
already implemented.

# Executive summary

Compression and other rotating-equipment service centres are complex
industrial businesses. They must manage customer urgency and technical
risk while coordinating field assessment, inspection, repair
engineering, spare parts, machining, assembly, testing, quality release,
logistics and commercial closure. Their results are measured not only in
repair quality but also in safe execution, predictable turnaround,
cost-to-serve, first-time-right performance, repeat failures, working
capital and customer trust.

This paper proposes an integrated **AI-enabled Service-Centre
Performance System (ASPS)** with five related pillars:

1.  **Reliability intelligence** — convert equipment telemetry and
    documented failures into engineer-reviewed condition insights.

2.  **Turnaround and capacity intelligence** — expose queue times,
    bottlenecks, critical-path risk and schedule feasibility.

3.  **Quality and continuous improvement** — strengthen traceability,
    inspection evidence, non-conformance analysis and corrective-action
    effectiveness.

4.  **Digital workflow orchestration** — connect approved information
    from service management, ERP, engineering, quality and maintenance
    systems through governed interfaces.

5.  **Economic and governance intelligence** — quantify cost-to-serve,
    margin leakage, rework, working capital, investment choices and the
    value of improvements.

A small working pilot already demonstrates the first, deliberately
limited capability: local ingestion and auditing of authorised
historical rotating-equipment sensor CSV files, per-asset Isolation
Forest anomaly screening, interactive inspection and engineer-facing CSV
exports. It does **not** diagnose faults or predict remaining useful
life. The remaining four pillars are **architectural proposals**, not
delivered modules. The proper next step is a carefully controlled
discovery and retrospective evaluation with real service-centre data and
domain experts. \[1–3\]

# 1. The service-centre management problem

A rotating-equipment repair is a project and a safety-sensitive
engineered process, not just a maintenance work order. Scope may change
after strip-down; long-lead parts may dominate the critical path;
inspection and balancing resources are shared across jobs; technical
concessions require formal approval; and a compressed schedule can
create costly rework. Compression service also involves asset-specific
OEM instructions, contractual acceptance criteria and applicable
engineering standards.

The managerial challenge is to connect three operating views that often
remain separated:

- **Equipment view:** condition, operating modes, fault history,
  inspection results, design limits and test evidence.

- **Work-execution view:** job routing, planned versus actual activity
  durations, available skills, supplier commitments, non-conformances
  and customer approvals.

- **Business view:** quoted versus actual cost, capacity utilisation,
  recoverability, warranty exposure, cash conversion and contribution
  margin.

AI may help synthesise these views, but authoritative engineering
decisions must remain with appropriately qualified personnel. The safest
initial automation target is *decision support*, not autonomous
operation.

# 2. Reference architecture: five connected intelligence layers

- **1. Reliability** — Typical inputs: Vibration, bearing temperature,
  pressures, power, operating modes, maintenance records; Analytical
  function: Data validation; statistical screening; later mode-aware
  condition assessment; Reviewed output / user: Engineer-reviewed
  equipment investigation list

- **2. Service operations** — Typical inputs: Work orders, planned
  tasks, milestones, crew hours, test bays, purchase orders; Analytical
  function: Delay attribution, bottleneck analysis, forecast of delivery
  risk; Reviewed output / user: Repair-project manager and operations
  leader

- **3. Quality** — Typical inputs: Inspection/test records, defect
  codes, concessions, NCRs, CAPA actions, calibration; Analytical
  function: Non-conformance clustering, completeness checks, recurrence
  review; Reviewed output / user: Quality and repair engineering

- **4. Workflow orchestration** — Typical inputs: Approved ERP/CMMS/EAM
  APIs, documents, messages, service procedures; Analytical function:
  Governed retrieval, task drafting, escalation suggestions and approval
  routing; Reviewed output / user: Service teams, supply chain and
  customers

- **5. Finance & governance** — Typical inputs: Estimates, actual job
  costs, invoices, inventory, warranty, controls and audit logs;
  Analytical function: Margin bridge, economic benefit measurement,
  risk/approval monitoring; Reviewed output / user: Service-centre head,
  finance and leadership

**Architectural rule:** each analytical conclusion must trace to an
identifiable source, timestamp, asset/job, model version, decision owner
and approval status. Read-only access is the default. No AI agent should
change protection-system settings, release a repaired machine, authorise
a concession or post irreversible transactions without explicitly
authorised human controls.

## 2.1 Data foundation and identifiers

A deployable design needs a common identifier strategy: asset_id,
customer_id, service_job_id, work_order_id, inspection_id, part_id,
nonconformance_id, supplier_order_id and event_time. Establish reference
data for machine class, plant, duty, service category, failure mode,
repair route and customer contractual milestone. Preserve source-native
identifiers, units, time zones and revision histories; merge records
only through documented mappings.

Recommended ingestion zones: **raw immutable evidence → validated
analytical tables → approved metrics and features → governed read-only
dashboards → human-confirmed actions**. Integrations should use
authorised APIs or controlled batch extracts with identity, role
permissions and logging. A dashboard cannot remedy inaccurate timestamps
or inconsistent definitions of “repair completion”.

# 3. AI-driven condition monitoring and reliability analytics

## 3.1 What exists today in the author's pilot

The public research demonstration is built with **Python, Streamlit,
pandas, scikit-learn and Plotly**. It accepts historical CSV records
containing timestamp, asset identifier and numerical sensors; tests
asset eligibility and data completeness; fits an Isolation Forest model
to each suitable asset; shows unusual readings on trend charts; and
exports machine-readable investigation evidence. Its included example is
**synthetic**, not a field-validated dataset. The method can identify
*statistical outliers* without failure labels, but an outlier may be a
normal startup, load change, calibration artefact or sensor defect.
\[1–3\]

The prototype does not implement a live historian connection,
OPC-UA/SCADA/PLC integration, confirmed defect diagnosis,
time-to-failure, remaining useful life, alarm logic or automatic
intervention. It fits and evaluates on uploaded historical records, so
the results are exploratory rather than an unbiased future-performance
estimate.

## 3.2 Path from screening to validated reliability support

1.  **Segment the duty envelope:** separate steady-state, startup,
    shutdown, load changes, overhaul and maintenance modes using
    approved operational labels.

2.  **Establish signal integrity:** verify calibration, sensor
    placement, units, sampling, missing-data mechanisms and per-asset
    history.

3.  **Review anomalous periods:** compare model flags against
    maintenance logs, condition reports, operator notes and pre-defined
    engineering judgement criteria.

4.  **Benchmark against existing practices:** compare to approved
    limits, engineering thresholds and condition-monitoring rules,
    rather than evaluating the model in isolation.

5.  **Measure prospective usefulness:** freeze the algorithm and
    thresholds before a chronological holdout; report review workload,
    false investigation burden, missed known events and uncertainty.

6.  **Consider advanced methods only if warranted:** operating-mode
    models, multivariate temporal features, vibration spectra,
    supervised failure classification and physics-informed constraints.

The published ISO condition-monitoring guideline is **ISO 17359:2018**;
it describes general procedures for condition-monitoring programmes.
This is distinct from a 2025 regional adoption of the 2018 text.
Applicable measurement and machinery-specific standards must be
identified by qualified engineers. \[4\]

## 3.3 Non-negotiable evidence hierarchy

**Unusual sensor value ≠ defect ≠ imminent failure ≠ maintenance
instruction.** The decision chain is: *data finding → engineer
verification → corroborating records/tests → technical disposition →
authorised work instruction.* A screening result should display
uncertainty, source quality and alternative explanations.

# 4. Service-centre KPI, cost and turnaround intelligence

Dashboards are useful only when metrics have precise definitions,
timestamps, ownership and escalation rules. A proposed operating
scorecard should separate customer-facing, shop-floor, quality and
financial outcomes.

## 4.1 Core performance dictionary

- **End-to-end repair turnaround** — Recommended definition:
  Customer-agreed completion date/time minus authorised job
  start/acceptance timestamp; Practical caution: State whether waiting
  for customer approval and logistics are included

- **Shop execution cycle** — Recommended definition: Quality-release
  timestamp minus actual shop-entry timestamp; Practical caution: Do not
  confuse with customer lead time

- **On-time delivery (OTD)** — Recommended definition: Jobs accepted by
  customer on/before committed date ÷ jobs due in period; Practical
  caution: Version commitments; prevent retroactive rebaselining

- **Schedule adherence** — Recommended definition: Planned milestones
  completed on time ÷ milestones due; Practical caution: Define
  treatment of formally approved change orders

- **First-pass yield** — Recommended definition: Jobs completing
  required inspections/tests without rework ÷ jobs inspected/tested;
  Practical caution: Define job-level vs operation-level denominator

- **Rework hours share** — Recommended definition: Rework labour hours ÷
  total direct labour hours; Practical caution: Separate customer scope
  changes from repair-caused rework

- **Non-conformance closure time** — Recommended definition: Closure
  timestamp minus NCR opening timestamp; Practical caution:
  Safety-critical findings cannot be gamed by premature closure

- **WIP ageing** — Recommended definition: Days from shop-entry to
  reporting date for open jobs; Practical caution: Display percentile
  distribution and blocked-job reasons

- **Critical resource utilisation** — Recommended definition: Actual
  productive use ÷ practical available capacity; Practical caution:
  Account for planned maintenance, calibration and capability

- **Quote-to-actual cost variance** — Recommended definition: Actual
  cost minus approved baseline estimate; Practical caution: Bridge scope
  changes, inflation, productivity and scrap

- **Contribution by service job** — Recommended definition: Recognised
  job revenue minus attributable variable/direct costs; Practical
  caution: Separate allocated overhead and contractual provisions

- **Cash conversion** — Recommended definition: Days from
  milestone/invoice eligibility to customer receipt; Practical caution:
  Distinguish billing delays from customer payment delays

Each metric requires *versioned data definitions*, quality checks and an
auditable calculation owner. Use trend/percentile distributions rather
than reporting only averages: one late critical compressor can dominate
customer impact despite an attractive average cycle time.

## 4.2 Turnaround analysis

Represent each job as a precedence network: incoming inspection →
disassembly → dimensional inspection/NDT → engineering disposition →
parts availability → repair/machining → balancing/assembly → performance
test → QA release → shipping. The duration of the critical path, rather
than the sum of all task times, determines the earliest possible
completion.

Proposed analytics include: route-specific cycle-time distributions;
queue times by bottleneck work centre; due-date risk from parts lead
times; technician skill-coverage constraints; supplier promised-date
slippage; and how many jobs share the same testing bay. Engineers and
project managers should verify all route constraints before schedule
optimisation.

For each delay, use reason codes such as **technical scope**,
**materials**, **capacity**, **customer decision**, **quality rework**,
**documentation** and **logistics**. This allows Pareto analysis without
blaming individuals for systemic causes.

## 4.3 Cost-to-serve and prioritisation

A useful job-level cost model is:

**Total repair cost = direct labour + parts/materials + subcontracting +
test/consumables + logistics + rework + job-specific overhead + warranty
provisions.**

**Actual-versus-quoted bridge = scope effect + material price effect +
usage/scrap effect + labour-rate effect + productivity effect + rework
effect + other reconciled residual.**

Finance should reconcile the bridge to the general ledger, approved
change orders and contractual revenue recognition. The output should
identify manageable drivers; it should not automatically recommend
reducing necessary inspection, balancing or safety testing.

# 5. Data-driven quality management and continuous improvement

A quality system for rotating-equipment repair must protect safety,
contractual requirements, technical traceability and calibration
integrity. Relevant standards and practices may include ISO 9001, ISO
14001, ISO 45001, asset management ISO 55001:2024 and machine-specific
API documents such as API 617 (centrifugal/axial compressors) and API
618 (reciprocating compressors), **where the contract and equipment
require them**. The exact editions and applicable contractual clauses
need to be checked for each engagement. A standards reference is not
evidence of certification or compliance. \[5–8\]

## 5.1 A governed non-conformance-to-improvement loop

**Detection:** a dimensional tolerance, balancing result, material
trace, performance test or document check fails a specified criterion.
**Containment:** quarantine the affected component/job and suspend
release as appropriate. **Engineering disposition:** authorised
acceptance, repair, rework or rejection under the governing procedure.
**Root-cause analysis:** use 5-Why, fault tree or cause-and-effect
analysis with evidence rather than purely AI-generated narratives.
**Corrective action:** name owner, deadline, effectiveness test and
closure authority. **Prevention:** update route instructions, supplier
controls, training or inspections.

AI can assist with document completeness, defect-code normalisation,
retrieval of similar cases and drafting proposed CAPA summaries, subject
to human review. It must not independently approve non-conformances,
sign certificates or create misleading evidence.

## 5.2 Quality analytics measures

Track NCR incidence per comparable repair class, severity-weighted open
findings, recurrent causes, first-pass acceptance, calibration
compliance, supplier defect rate, rework hours and CAPA effectiveness at
30/60/90 days. Normalize rates for work type and repair complexity.
Avoid ranking teams solely by number of reported NCRs: this can penalise
better detection.

# 6. Digitally orchestrated maintenance and service workflows

The proposed digital layer connects—not replaces—existing ERP, CMMS/EAM,
service project management, document control, inventory, quality and
customer systems. A phased implementation can begin with **read-only
integration** and a single service-job dashboard before introducing
governed workflow actions.

## 6.1 Example event-driven workflow (proposed, not deployed)

A new customer service job is accepted. The authorised system publishes
a ServiceJobAccepted event. A workflow service resolves its equipment
record and required documents; creates a reviewable work-package draft;
checks capacity and materials availability via approved tools;
identifies missing documents; and routes the package to an
engineer/project manager. A separate quality gate prevents a release
recommendation unless required inspection evidence exists. Formal
sign-off remains with competent personnel.

An AI agent may *draft* a supplier follow-up or summarise delays, but
the actual purchase, concession, schedule commitment and customer
notification require permissions, validation and approval appropriate to
their risk.

## 6.2 Integration and security controls

Use API contracts, least-privilege roles, service identities, secrets
vaulting, audit trails, input validation, human approval gates and
prompt-injection-resistant retrieval boundaries. Industrial data should
remain in an approved environment. Do not expose direct SQL, unreviewed
external tools or plant-control write-back to language-model agents.
Separate development, testing and production; independently review model
changes and rollback procedures.

# 7. Financial performance, governance and decision support

A service-centre transformation should be evaluated as an investment
with verified baseline costs, incremental cash flows and explicit
counterfactuals—not headline percentages borrowed from other plants.

## 7.1 Economics of a proposed improvement

Let: **J** = eligible repairs per year; **Δh** = verified rework hours
saved per repair; **c_h** = fully loaded avoidable cost per labour hour;
**Δd** = validated reduction in avoidable delay days; **c_d** =
avoidable contractual/expediting cost per day; **B_w** = annual
recoverable working-capital benefit; **C_run** = incremental annual
running cost.

**Illustrative annual operating benefit = J × Δh × c_h + Δd × c_d +
other evidenced recurring savings − C_run.**

Working-capital release should be separately shown as cash-flow impact,
not counted as recurring P&L savings. Capacity gains generate additional
contribution only if validated customer demand and feasible throughput
exist. Avoid double-counting reduced rework both as labour saving and as
extra capacity revenue.

**NPV = − initial investment + Σ (incremental after-tax free cash flow
in year t / (1 + discount rate)^t).** Include integration, licensing,
cybersecurity, training, process change, data cleaning and recurring
model governance costs. Report base/downside/upside cases and
decision-gate thresholds. No project ROI is yet measured for the
author's pilot.

## 7.2 Illustrative example — not a forecast

Suppose a centre processes **120 qualifying repair jobs annually** and
independently verifies that a new workflow eliminates **3 avoidable
rework hours per job** at an *avoidable* cost of **₹1,200/hour**. The
labour saving would be **₹432,000 per year (₹4.32 lakh)** before
recurring costs and taxes. If software and governance cost ₹3 lakh
annually, the net annual operating benefit from *this one component*
would be ₹1.32 lakh. These are fictional inputs demonstrating
calculation, not actual customer or Siemens Energy performance. Benefits
from reduced delays or better inventory must be estimated and reported
separately, net of any costs.

## 7.3 Decision rights and governance

- **Flag unusual telemetry** — AI contribution: Rank and document
  unusual readings; Required human authority:
  Reliability/condition-monitoring engineer

- **Change maintenance plan** — AI contribution: Supply reviewed
  evidence and alternative hypotheses; Required human authority: Asset
  owner / authorised maintenance engineer

- **Alter repair scope or technical concession** — AI contribution:
  Assemble documents and impact summary; Required human authority:
  Repair engineering and authorised quality function

- **Move promised delivery date** — AI contribution: Quantify schedule
  scenarios and contractual impacts; Required human authority: Service
  project manager and customer-facing owner

- **Issue purchase/order or approve expenditure** — AI contribution:
  Draft request, validate fields, route for approval; Required human
  authority: Delegated finance/procurement approver

- **Release repaired equipment** — AI contribution: Check documentation
  for completeness; Required human authority: Qualified
  inspection/testing/release authority

# 8. Implementation roadmap and scientific validation

The proposed roadmap uses reversible, measurable stages rather than a
“big bang” AI rollout.

- **A. Discovery** — Suggested duration: Weeks 1–2; Main work: Identify
  asset/job types; define baseline KPIs, data permissions, safety
  boundaries, owners; Evidence gate: Signed scope, data dictionary,
  metric definitions

- **B. Data audit** — Suggested duration: Weeks 3–4; Main work: Trace
  3–10 representative assets/jobs across telemetry, work orders, costs
  and quality records; Evidence gate: Acceptable completeness, timestamp
  and join quality

- **C. Retrospective pilot** — Suggested duration: Weeks 5–8; Main work:
  Run existing anomaly tool locally; build independent KPI extracts and
  delay Pareto; engineer review; Evidence gate: Review workload and
  relevance; reproducible KPI calculations

- **D. Controlled business case** — Suggested duration: Weeks 9–10; Main
  work: Estimate intervention costs, benefits, baseline variation and
  control group/holdout; Evidence gate: Finance-approved assumptions,
  safety review and stop criteria

- **E. Read-only shadow dashboard** — Suggested duration: Weeks 11–12,
  only if approved; Main work: Demonstrate integrated visibility without
  operational control or financial write-back; Evidence gate:
  Monitoring, security, owners and rollout approval

- **F. Expansion** — Suggested duration: Subsequent, conditional; Main
  work: Add forecast models, governed workflows, quality modules and
  continuous improvement; Evidence gate: Independent validation and
  signed operational acceptance

*Durations are planning illustrations, not delivery commitments. Access
to approved data and service engineers determines the achievable scope.*

## 8.1 Evaluation questions

- Does the source data correctly identify assets, operating modes, jobs,
  milestones, rework and customer commitments?

- Are the anomaly flags useful to engineers **after** comparing with
  their present inspection and monitoring process?

- Can the same KPI numbers be reproduced independently from source
  records and financial ledgers?

- Which delays are controllable, and what happens to bottleneck
  utilisation if throughput increases?

- Does the proposal reduce total cost without weakening safety tests,
  traceability or service quality?

- Would the projected benefits remain positive under lower demand,
  slower adoption and model degradation?

## 8.2 What constitutes success

Success means an independently reproducible improvement in one or more
*pre-specified* customer, quality, operational or economic measures,
with no unacceptable deterioration in safety, compliance or customer
outcomes. A compelling dashboard or an anomaly plot alone is not
success. A rigorous pilot must have frozen acceptance criteria, matched
before/after baselines or suitable comparators, uncertainty estimates
and evidence that outcomes were not selected after seeing the results.

# 9. Risks, controls and boundaries

- **A statistical outlier is mistaken for a defect** — Mitigation:
  Warning labels; corroboration with engineering evidence; never infer
  RUL from Isolation Forest

- **Different operating modes create false positives** — Mitigation:
  Mode labels, stratified review, chronological holdout

- **Asset/job records mismatch** — Mitigation: Controlled ID mapping,
  revision tracking, reconciliation samples

- **KPI improvements are manipulated** — Mitigation: Frozen data
  dictionary, independently auditable timestamps and exclusions

- **AI-generated procedure is inaccurate** — Mitigation: Source
  citations, read-only retrieval, engineer approval and version control

- **Confidential plant/customer data leak** — Mitigation: Approved local
  processing, access controls, no public data commits or plaintext
  credentials

- **Savings are counted twice** — Mitigation: Signed finance benefit
  register and cost/revenue reconciliation

- **AI automates a safety/quality release** — Mitigation: Blocked
  write-back and qualified human authority

- **ISO/API compliance is incorrectly claimed** — Mitigation:
  Contract-specific standards register and independent evidence audit

# 10. Collaboration proposition

This paper invites a service-centre or rotating-equipment operator to
conduct a bounded, confidential proof of value. The partner supplies
approved, historical data, domain expertise and decision authority. The
author can contribute AI architecture, Python implementation,
data-quality analysis, model evaluation, dashboard prototypes and
economic analysis. Any additional engineering, controls integration or
quality-system claims require the partner's designated experts, formal
scope and independent acceptance.

**Proposed first deliverables:** (i) an asset/job data-readiness report;
(ii) a KPI glossary and baseline dashboard; (iii) local
anomaly-screening outputs reviewed by engineers; (iv) a repair
turnaround bottleneck and rework Pareto; (v) a finance-reviewed
investment case; and (vi) a go/no-go decision with measurable next-stage
criteria.

**Public demonstration:**
<https://github.com/vikramsankhala/oilgas-equipment-ai-pilot>  
**Suggested collaboration:** enterprise AI and reliability engineering,
operations, quality, procurement and finance; client data remain within
client-approved custody.

# References and source notes

1.  Sankhala, V. S. (2026). *From Telemetry to Engineering Insight: An
    accessible AI anomaly-detection pilot for rotating equipment across
    oil & gas operations.* Author's uploaded eight-page research white
    paper; supplied companion files.

2.  Sankhala, V. S. (2026). *AI Anomaly Detection for Oil & Gas
    Equipment: Technical Summary & Implementation Protocol.* Author's
    uploaded two-page summary.

3.  Sankhala, V. S. (2026). *Oil & Gas Equipment AI Pilot.* Public
    README and source repository.
    <https://github.com/vikramsankhala/oilgas-equipment-ai-pilot>

4.  ISO. *ISO 17359:2018 — Condition monitoring and diagnostics of
    machines — General guidelines.*
    <https://www.iso.org/standard/71194.html> (official ISO edition
    verified November 2026).

5.  ISO. *ISO 55001:2024 — Asset management — Asset management system —
    Requirements.* <https://www.iso.org/standard/83054.html>

6.  ISO. *Quality, environmental and occupational health and safety
    management systems* (current editions and applicability should be
    confirmed): <https://www.iso.org/management-system-standards.html>

7.  American Petroleum Institute. Standards relevant to compressors and
    rotating equipment include API 617 and API 618; select the
    contractual edition and confirm precise scope with repair
    engineering. API reference overview: <https://www.api.org/>

8.  NIST. *Artificial Intelligence Risk Management Framework (AI RMF
    1.0)* (2023).
    <https://www.nist.gov/itl/ai-risk-management-framework>

9.  Liu, F. T., Ting, K. M., and Zhou, Z.-H. (2008). “Isolation Forest.”
    IEEE ICDM. <https://doi.org/10.1109/ICDM.2008.17>

10. Liu, F. T., Ting, K. M., and Zhou, Z.-H. (2012). “Isolation-Based
    Anomaly Detection.” ACM TKDD.
    <https://doi.org/10.1145/2133360.2133363>

*This document is independent research and an implementation proposal.
It does not represent endorsement, certification, customer deployment,
or affiliation with Siemens Energy. Company and client-specific facts
have not been inferred.*
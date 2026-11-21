# AI-Enabled Service-Centre Excellence

**From Equipment Telemetry to Reliability, Repair Turnaround, Quality and Financial Performance**

**Author:** Vikram Singh Sankhala  
**Date:** November 2026  
**Status:** Independent industrial AI research and proposed service-centre transformation framework. Not a production system or certified repair, safety or condition-monitoring solution.

## Purpose

A rotating-equipment service centre must coordinate repair engineering, shop-floor capacity, inspection, spare parts, quality, customer commitments, costs and technical integrity. AI can improve the accessibility and quality of decision support across these areas, provided source data are reliable and engineering decisions stay with competent, authorised people.

This strategy paper expands the [existing local rotating-equipment anomaly-screening demonstration](../README.md) into a **proposed** five-pillar operating architecture:

1. **Reliability intelligence:** validate and review sensor observations with appropriate engineering context.
2. **Service operations:** monitor turnaround, work-in-process, critical-path delays, labour and test-bay capacity.
3. **Repair quality:** strengthen inspection traceability, first-pass yield, rework and non-conformance investigation.
4. **Workflow orchestration:** integrate approved enterprise data and deliver read-only, reviewable recommendations.
5. **Finance and governance:** track actual cost-to-serve, project margin, working capital, investment returns, accountability and controls.

The five pillars beyond historical anomaly screening are **not** currently implemented in this repository. The accompanying full Word/PDF white paper elaborates the proposed designs, KPI framework, sample calculations, evaluation method and reference material.

## What the existing implementation actually does

The public Streamlit application uses Python, pandas, scikit-learn and Plotly. An authorised user loads a CSV containing `timestamp`, `asset_id` and at least one varying numeric sensor. The code audits validity and eligibility, performs per-asset Isolation Forest statistical outlier screening, displays time-series plots and exports reviewable CSV evidence. It is **read-only and local**: no historian, SCADA, PLC, OPC-UA or maintenance control integration; no failure classification, remaining useful life estimate, certified alarm, automated shutdown or verified savings. Its supplied data are synthetic. Fitting and scoring on the same uploaded observations is exploratory and is not a prospective performance test.

**Safety principle:** an outlier is not proof of a fault. A qualified reliability engineer must corroborate findings with operating modes, history, calibrated measurements, inspections and engineering requirements.

## Proposed KPI dictionary

| KPI | Proposed definition | Important qualification |
|---|---|---|
| Customer turnaround | Accepted completion minus documented service-job start | Track contractual pauses and customer holds |
| Shop execution cycle | QA release minus physical shop entry | Not the same as customer lead time |
| On-time delivery | Jobs completed within approved commitment / jobs due | Prevent retroactive commitment changes |
| First-pass yield | Jobs accepted without rework / jobs tested | Comparable repair classes only |
| Rework burden | Rework hours / total direct hours | Exclude approved scope additions |
| Work-in-process aging | Reporting date minus shop entry for open jobs | Stratify by blocked reason |
| Quote-to-actual variance | Actual incurred cost minus approved quote baseline | Bridge material, labour, scrap, scope and productivity |
| Job contribution | Recognised revenue minus attributable direct / variable cost | Reconcile to finance ledgers |
| NCR closure time | Closed at minus opened at | Do not reward premature closure |
| Operating capacity | Productive hours / practical available hours | Account for setup, calibration and planned downtime |

Each measure must have an owner, versioned formula, source systems, definition of valid exclusions, and independent reconciliation.

## Proposed analytical and workflow sequence

```text
Authorised historian / CMMS / ERP / quality / finance extracts
   -> data validation and asset-job identity mapping
   -> approved metric calculations and historical anomaly screening
   -> engineer-validated reliability findings + repair delay analysis
   -> reviewed quality and rework hypotheses
   -> finance-reconciled investment case
   -> approval-controlled service process improvements
```

The first useful project is **retrospective and read-only**. Suggested tasks include reviewing 3–10 representative assets or jobs, auditing their timestamps and joins, demonstrating anomaly screening locally, calculating baseline KPIs, identifying delay causes and comparing results with actual engineering and commercial evidence.

## Financial logic

Illustrative annual operating benefit can be expressed as:

```text
(eligible jobs × verified avoidable rework hours per job × avoidable hourly cost)
+ verified avoidable delay cost savings
+ other separately evidenced recurring improvements
- annual implementation and governance running cost
```

Working-capital release is a cash-flow effect, not recurring profit. Added capacity should earn financial credit only where demand and throughput are verified. Do not double-count the same rework improvement as both labour saving and incremental sales.

**Purely illustrative figures:** 120 jobs × 3 hours × ₹1,200 per avoidable hour = ₹4.32 lakh annual gross benefit. Less ₹3 lakh hypothetical annual running costs leaves ₹1.32 lakh operating benefit before tax and investment costs. These numbers are not actual service-centre performance or an expected ROI.

## Governance and technical boundaries

- All model results require authorised human engineering review.
- There is no automated safety action, release-to-service, change to machine protection settings, concession approval or financial posting.
- Apply least privilege, governed APIs, local data custody, audit logging, credential protection and independent change management.
- Keep source provenance, timestamps, identifier mappings and exception logs.
- Review applicable editions and contractual requirements of standards such as ISO 17359:2018, ISO 55001:2024, ISO 9001, ISO 14001, ISO 45001 and compressor-specific API standards. References to standards do not establish certification.

## Staged evaluation proposition

**Weeks 1–2:** discovery, accountable stakeholders, business problem, data dictionary, safety boundary, frozen success metrics.  
**Weeks 3–4:** data readiness, historical integrity and representative service-job traces.  
**Weeks 5–8:** local anomaly demonstration, engineering review, KPI baseline and delay Pareto.  
**Weeks 9–10:** finance-reviewed benefit and cost assumptions; documented go/no-go gate.  
**Weeks 11–12, conditional:** client-approved read-only integrated dashboard in a secure environment.  
**Later expansion:** independently validated quality, scheduling and workflow capabilities if evidence supports investment.

Dates are illustrative planning windows and not implementation commitments.

## References

- Sankhala, V. S. (2026), *From Telemetry to Engineering Insight: An accessible AI anomaly-detection pilot for rotating equipment across oil & gas operations*. Author's research white paper.
- Sankhala, V. S. (2026), *AI Anomaly Detection for Oil & Gas Equipment: Technical Summary & Implementation Protocol*. Author's technical summary.
- [ISO 17359:2018 — Condition monitoring and diagnostics of machines](https://www.iso.org/standard/71194.html). Note: the ISO edition is 2018; some regional adoptions use a 2025 designation.
- [ISO 55001:2024 — Asset management system requirements](https://www.iso.org/standard/83054.html).
- [ISO management-system standards](https://www.iso.org/management-system-standards.html).
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework).
- Liu, Ting & Zhou (2008), *Isolation Forest*, IEEE ICDM. https://doi.org/10.1109/ICDM.2008.17

**Author:** Vikram Singh Sankhala — IIT Kharagpur; IIM Calcutta; former AI Solutions Architect, SAP; Assistant Professor, NMIMS.

**Disclaimer:** Independent proposal only. No Siemens Energy affiliation, deployment, certified functionality, commercial savings or client implementation is implied.

# From Telemetry to Engineering Insight

**An accessible AI anomaly-detection pilot for rotating equipment across oil and gas operations**

**White paper by Vikram Singh Sankhala** · November 2026

**Repository:** https://github.com/vikramsankhala/oilgas-equipment-ai-pilot

> **Research demonstration only.** The software performs exploratory statistical anomaly detection on historical CSV telemetry. It is not a certified industrial monitoring, failure-prediction, safety, alarm or control product. No equipment reliability improvement, ROI, downtime reduction or model generalizability has yet been established.

## Executive perspective

Oil and gas operators collect a wide range of measurements from pumps, compressors, motors and auxiliary equipment. Turning historical telemetry into reliable engineering insights is difficult when fault labels are sparse and operating conditions vary. I developed this open-source demonstration to provide a testable, transparent first step: ingest approved historical readings locally, audit data quality, flag statistically unusual observations and let qualified engineers decide whether further investigation is warranted.

The pilot offers a concrete way for a company to evaluate a computational workflow on its own data *without sharing its raw equipment history with me or uploading it to GitHub*.

## The working pilot

| Implemented | Not implemented |
|---|---|
| CSV upload with `timestamp`, `asset_id` and numeric sensor columns | Connection to control systems, SCADA, PLC or live historians |
| Duplicate/timestamp validation and asset-level coverage audit | Automated safety alarms or shutdowns |
| Per-asset unsupervised Isolation Forest | Failure probability or remaining useful life |
| Relative anomaly scores and flagged readings | Physical root-cause diagnosis |
| Streamlit/Plotly inspection and CSV export | Validated field performance, measured cost savings or ROI |
| Synthetic input and GitHub Actions tests | Certification or operational authorization |

The sample CSV contains **320 entirely synthetic readings for two equipment identifiers** with deliberately unusual-looking segments. These illustrate the user experience; they are not evidence of realistic failures.

## Computational method

The software uses pandas, scikit-learn, Streamlit and Plotly. Following timestamp and asset validation, each asset is scored independently using a standard Isolation Forest estimator. Isolation Forest separates rare observations with random decision-tree partitions, often isolating unusual points faster than typical ones. The configurable outlier proportion is a statistical assumption **not** a site failure rate.

A higher displayed score represents relative unusualness, **not a calibrated likelihood of a machine fault**. Anomalies may arise from startups, shutdowns, load variation, sensor error, maintenance states or actual equipment problems. Engineering review is essential.

One critical scientific limitation is that the current exploratory model is trained on uploaded observations and then scores those same observations. It must not be interpreted as a temporally independent estimate of real-time performance.

## A practical client-led evaluation

1. **Scope the study.** The client chooses approximately 3–10 suitable machines, a retrospective period, authorized users, data protections and outcome definitions.
2. **Prepare the data.** Check timestamps/timezones, units, asset identification, operating regimes, sensor changes, missing data and work-order provenance.
3. **Run locally.** Clone the repository to an approved workstation, install dependencies, verify unit tests and evaluate the synthetic CSV before importing approved plant telemetry.
4. **Review outputs.** Export scores, flags and the data-quality audit. Include both flagged and unflagged readings in engineer evaluation, ideally against labels defined independently of the model.
5. **Benchmark fairly.** Compare against facility threshold rules and assess review precision, false-alert burden per asset-day, coverage, sensitivity to operating modes and time spent interpreting results.
6. **Decide explicitly.** Continue, redesign or stop under predefined, mutually agreed criteria. No accuracy or savings targets should be asserted before evaluation.

Possible future research, only if the evidence warrants it, includes operating-mode segmentation, chronological holdouts, maintenance-event linkage, physics-informed temporal models, supervised failure prediction, interpretable diagnostics and prospective shadow-mode evaluation.

## Security and safe use

All company data should stay in an approved organization-controlled environment. Do not commit confidential telemetry, credentials, customer identifiers or analysis exports to a public repository. The demonstration includes no intentional outgoing telemetry upload or OT write-back, but local deployment, dependencies, network policies, retention and access controls must be assessed by the operator. No use in a safety-critical operating loop is authorized.

A research collaboration should define data rights, scope, responsibilities, review procedures, confidentiality, publications and any intellectual-property arrangement before proceeding.

## Potential collaborative work packages

- **WP1: Data readiness** — metadata, sensor quality and operations-context segmentation.
- **WP2: Retrospective benchmarking** — engineering adjudication and comparison with rule-based monitoring.
- **WP3: Model research** — mode-aware, temporal and physically constrained methods.
- **WP4: Interpretability** — investigation-ready evidence and carefully labelled hypotheses.
- **WP5: Shadow-mode research** — prospective observation only under approved governance.
- **WP6: Research dissemination** — reproducibility, technical workshops and mutually agreed publications.

I can contribute AI architecture, Python engineering, machine learning, mathematical modelling, experiment design and reproducibility infrastructure. Industrial partners supply operational context, engineering expertise, authorized data access and independent evaluation of the results.

## Getting started

Read the [User Manual](USER_MANUAL.md) and use the following commands on an approved local workstation with Python 3.11:

```powershell
git clone https://github.com/vikramsankhala/oilgas-equipment-ai-pilot.git
cd oilgas-equipment-ai-pilot
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
streamlit run app.py
```

Upload `data/sample_pump_telemetry.csv` first, then use your own authorized historical CSV.

## About the author

I am **Vikram Singh Sankhala**, a former AI Solutions Architect at SAP and an Assistant Professor at MPSTME, NMIMS University. My experience spans machine learning, deep learning, generative and agentic AI, AI systems architecture, mathematical modelling and Python software engineering. I hold a B.Tech (Honours) from IIT Kharagpur, an MBA from IIM Calcutta and the FRM qualification from GARP. I welcome evidence-based collaboration with oil and gas operators and research institutions.

## Technical references

1. Liu, F. T., Ting, K. M., and Zhou, Z.-H. (2008). *Isolation Forest*. IEEE ICDM. https://doi.org/10.1109/ICDM.2008.17
2. Liu, F. T., Ting, K. M., and Zhou, Z.-H. (2012). *Isolation-Based Anomaly Detection*. ACM TKDD. https://doi.org/10.1145/2133360.2133363
3. ISO 17359:2025. *Condition monitoring and diagnostics of machines — General guidelines*.
4. NIST. *Artificial Intelligence Risk Management Framework*. https://www.nist.gov/itl/ai-risk-management-framework

**This Markdown publication accompanies the more fully designed PDF/Word white paper available directly from the author.**

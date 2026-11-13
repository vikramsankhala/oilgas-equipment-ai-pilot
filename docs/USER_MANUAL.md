# User Manual | Oil & Gas Equipment AI Pilot

**Author:** Vikram Singh Sankhala. **Release:** research demo v0.1.

## Purpose

A local, read-only Streamlit application. It checks historical telemetry CSV files, fits per-asset Isolation Forest models, visualizes anomalous sensor readings and exports results. It is **not** a validated failure-prediction or industrial safety system.

## Installation

Python 3.11 or 3.12 is recommended, on an approved workstation.

Windows PowerShell:

```powershell
git clone https://github.com/vikramsankhala/oilgas-equipment-ai-pilot.git
cd oilgas-equipment-ai-pilot
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
streamlit run app.py
```

If activation is restricted, use `.\.venv\Scripts\python.exe -m pip install -r requirements.txt` and `.\.venv\Scripts\python.exe -m streamlit run app.py`. On Linux/macOS use `python3 -m venv .venv` then `source .venv/bin/activate`.

The browser normally opens at http://localhost:8501. Use only an approved secured local environment.

## Demonstration with synthetic data

1. Upload `data/sample_pump_telemetry.csv` from the repository.
2. Select available sensors; keep the assumed outlier fraction at 3%.
3. Review counts and data-quality audit; select a machine and measurement.
4. Inspect time-series trends and highlighted anomalous readings.
5. Export two CSV reports: anomaly scores/flags and data-quality audit.

Synthetic spikes are not real faults and do not validate reliability or maintenance savings.

## Upload your own data

Required: `timestamp`, `asset_id` and one or more numeric sensors. You can use your own sensor names. ISO 8601 timestamps with timezone are recommended. No duplicate pairs of equipment ID and timestamp; no mixed units or unrelated asset modes without preprocessing. At least 40 complete readings per asset and one varying sensor are required. Missing sensor readings are not imputed, and some observations may remain unscored.

Example:

```csv
timestamp,asset_id,vibration_mm_s,bearing_temp_c,pressure_bar,motor_current_a
2026-01-01T10:00:00Z,P-101,2.3,72.5,13.2,29.1
2026-01-01T10:15:00Z,P-101,2.4,72.8,13.1,29.0
```

Output fields: `anomaly_score` (relative unusualness, NOT failure probability); `is_anomaly` (binary statistical flag); `status` (scored, missing_sensor_values, insufficient_data).

## Recommended operator evaluation

1. Scope a historical cohort of 3–10 comparable pumps/compressors.
2. Agree telemetry provenance, units, timestamps, operating regimes and access controls.
3. Establish a reference set of engineering events/work orders before examining model flags.
4. Run the local pilot, export scores and assess engineer-labelled flagged *and unflagged* periods.
5. Measure review precision, false-alert burden per asset-day, data coverage and investigation time; stratify by operating mode.
6. Compare against existing monitoring rules and agree go/no-go criteria.

**Crucial limitation:** the model fits on all uploaded readings; evaluation on those same readings is not a temporally held-out estimate of operational performance. No failure prediction, downtime reduction or ROI is established.

## Security, safety and troubleshooting

Do not upload confidential telemetry to GitHub, share credentials, connect this pilot to SCADA/PLC systems, or make automated shutdown/maintenance decisions. The software has no intentional external upload of telemetry, but environment configuration and network egress must be checked under the site's IT/OT requirements.

Invalid timestamps/duplicate records cause errors. Short or constant sensor histories are unscored. Engineering reviews must consider startups, shutdowns, operating-regime changes, sensor faults and maintenance interventions.

## Collaboration

Possible separately scoped work: blinded engineer review, maintenance log linkage, operating-mode stratification, rolling train/test splits, supervised failure models, interpretability, privacy/security assessments and prospective shadow-mode evaluation. All require further validation and appropriate governance.

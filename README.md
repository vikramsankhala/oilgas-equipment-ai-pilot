# Oil & Gas Equipment AI Pilot

**Author:** Vikram Singh Sankhala  
**Status:** Research demonstration — not an operational safety system.

A **local, read-only Streamlit dashboard** for detecting unusual sensor measurements in pumps, compressors and other rotating equipment using unsupervised Isolation Forest. Operators can test with a synthetic CSV or their own **approved historical data** without connecting to plant control systems.

## AI-enabled service-centre excellence — complete white paper

**Author: Vikram Singh Sankhala · November 2026**

A client-facing research and transformation framework for compression and rotating-equipment service centres, covering **AI-driven condition monitoring, repair turnaround and service KPIs, cost optimisation, quality and non-conformance management, digital service workflows, financial governance and operational decision support**.

| Edition | GitHub publication |
| --- | --- |
| Complete white paper — **PDF** | [Read / download PDF](docs/AI_Enabled_Service_Centre_White_Paper_Vikram_Singh_Sankhala.pdf) |
| Complete white paper — **Word** | [Download editable DOCX](docs/AI_Enabled_Service_Centre_White_Paper_Vikram_Singh_Sankhala.docx) |
| Complete white paper — **Markdown** | [Read the full source paper](docs/AI_Enabled_Service_Centre_White_Paper_Vikram_Singh_Sankhala.md) |
| Technical strategy companion | [Service-centre AI strategy](docs/SERVICE_CENTER_AI_STRATEGY.md) |

The **full Markdown** edition is the publishing source; [GitHub Actions](.github/workflows/publish-service-centre-paper.yml) generates the corresponding Word and PDF editions in `docs/`. The generated editions are designed for distribution to prospective industrial partners, employers and reliability teams.

**Scope limitation:** the existing Streamlit pilot implements local, read-only statistical anomaly screening on historical telemetry. The service-centre KPI, repair turnaround, quality, financial and enterprise workflow modules discussed in the paper are **proposed future capabilities**, not demonstrated production functions. Neither safety certification nor verified industrial ROI is claimed.

## Five-minute quick start

For **Windows PowerShell** with Python 3.11:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
streamlit run app.py
```

For macOS/Linux: `python3 -m venv .venv && source .venv/bin/activate`, then install dependencies and run the same tests/app command.

Upload `data/sample_pump_telemetry.csv` into the dashboard. To use your data, provide a CSV with **timestamp**, **asset_id**, and at least one numeric sensor (e.g. `vibration_mm_s`, `bearing_temp_c`, `pressure_bar`, `motor_current_a`). Each asset needs at least 40 complete observations and at least one varying sensor.

Read the [client white paper](docs/WHITE_PAPER.md) and [full user manual](docs/USER_MANUAL.md) for the methodology, data preparation, evaluation, interpretation and security.

## Scope and limitations

- **Anomaly detection is not failure prediction.** Isolation Forest flags statistically unusual measurements; it does not estimate the probability of failure, remaining useful life or prescribe maintenance actions.
- The user-selected outlier proportion is a modelling assumption, not the actual failure rate.
- Models are fitted separately to each asset on the uploaded data; training on the evaluation period can bias operational performance estimates.
- **No SCADA / PLC / OPC-UA integration, automated alarms or control write-back.**
- Process sensitive datasets **locally** on an approved workstation. Never commit customer datasets, credentials or exported results.
- Before operational use, an independent engineering evaluation with maintenance records, holdout periods and site-specific safety governance is required.

## Files

- `app.py` — interactive Streamlit dashboard
- `src/core.py` — validation and Isolation Forest analysis
- `data/sample_pump_telemetry.csv` — synthetic example (no real equipment data)
- `tests/test_core.py` — unit tests
- `docs/USER_MANUAL.md` — operator instructions and evaluation protocol
- `.github/workflows/tests.yml` — GitHub Actions tests

## License

MIT. Research demo, provided without warranty.

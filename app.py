"""Streamlit dashboard for the read-only equipment anomaly detection pilot."""
import pandas as pd
import plotly.express as px
import streamlit as st
from src.core import analyze, DEFAULT_SENSORS

st.set_page_config(page_title="Oil & Gas | Equipment AI Pilot", layout="wide")
st.title("Equipment Health | AI Anomaly Detection Pilot")
st.caption("Local research demonstration • No control-system connection • No certified failure prediction")
st.info("Flagged measurements are statistical anomalies, not confirmed faults. Qualified engineers must interpret results using operating context and maintenance records.")

with st.sidebar:
    st.header("Input")
    file = st.file_uploader("Upload historical telemetry CSV", type="csv")
    contamination = st.slider("Assumed outlier fraction", 0.01, 0.15, 0.03, 0.01)
    st.markdown("Required columns: timestamp, asset_id; select at least one numeric sensor.")
    st.caption("For confidential data use an approved, secured local workstation; do not host this demo publicly.")

if file is None:
    st.write("Upload approved historical telemetry or try the synthetic sample.")
    with open("data/sample_pump_telemetry.csv", "rb") as f:
        st.download_button("Download synthetic example CSV", f.read(), "sample_pump_telemetry.csv")
    st.stop()

try:
    raw = pd.read_csv(file)
    available = [c for c in raw.columns if c not in ("timestamp", "asset_id")]
    selected = st.multiselect(
        "Select numeric sensor columns", available,
        default=[c for c in DEFAULT_SENSORS if c in available]
    )
    if not selected:
        st.warning("Select at least one numeric sensor.")
        st.stop()
    results, audit = analyze(raw, sensors=selected, contamination=contamination)
except Exception as exc:
    st.error(f"Unable to analyze dataset: {exc}")
    st.stop()

scored = results[results["status"] == "scored"]
col1, col2, col3 = st.columns(3)
col1.metric("Assets", results["asset_id"].nunique())
col2.metric("Scored readings", len(scored))
col3.metric("Statistical anomalies", int(scored["is_anomaly"].sum()))

st.subheader("Data quality and eligibility")
st.dataframe(audit, use_container_width=True)
asset = st.selectbox("Equipment", results["asset_id"].unique())
part = results[results["asset_id"] == asset].copy()
sensor = st.selectbox("Trend sensor", selected)
fig = px.line(part, x="timestamp", y=sensor, title=f"{asset} - {sensor}")
flagged = part[part["is_anomaly"]]
if not flagged.empty:
    fig.add_scatter(
        x=flagged["timestamp"], y=flagged[sensor], mode="markers",
        name="Statistical outliers", marker={"color": "red", "size": 9}
    )
st.plotly_chart(fig, use_container_width=True)
if part["anomaly_score"].notna().any():
    st.plotly_chart(px.line(
        part, x="timestamp", y="anomaly_score",
        title="Relative anomaly score (higher = more unusual)"
    ), use_container_width=True)
st.subheader("Results")
st.dataframe(part.tail(1000), use_container_width=True)
st.download_button(
    "Export scored CSV", results.to_csv(index=False).encode("utf-8"),
    "equipment_anomaly_results.csv", mime="text/csv"
)
st.download_button(
    "Export data-quality audit CSV", audit.to_csv(index=False).encode("utf-8"),
    "equipment_data_quality.csv", mime="text/csv"
)
st.caption("Isolation Forest is fitted separately to each asset on the uploaded records. Results do not measure failure probability, remaining useful life, or appropriate maintenance actions.")

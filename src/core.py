"""Read-only, per-asset Isolation Forest for historical equipment telemetry."""
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

REQUIRED = ["timestamp", "asset_id"]
DEFAULT_SENSORS = ["vibration_mm_s", "bearing_temp_c", "pressure_bar", "motor_current_a"]


def validate(df, sensors=None):
    if not set(REQUIRED).issubset(df.columns):
        raise ValueError("CSV requires timestamp and asset_id columns.")
    df = df.copy()
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce", utc=True)
    if df["timestamp"].isna().any():
        raise ValueError("Invalid timestamps; use ISO 8601 with timezone.")
    if df["asset_id"].isna().any() or (df["asset_id"].astype(str).str.strip() == "").any():
        raise ValueError("asset_id cannot be empty.")
    if df.duplicated(["asset_id", "timestamp"]).any():
        raise ValueError("Duplicate (asset_id, timestamp) readings. Resolve before upload.")
    if sensors is None:
        sensors = [s for s in DEFAULT_SENSORS if s in df.columns]
    if not sensors:
        raise ValueError("Select at least one numeric sensor.")
    for s in sensors:
        if s not in df.columns or s in REQUIRED:
            raise ValueError("Unknown or invalid sensor: " + str(s))
        df[s] = pd.to_numeric(df[s], errors="coerce").replace([np.inf, -np.inf], np.nan)
    return df.sort_values(["asset_id", "timestamp"]).reset_index(drop=True), sensors


def analyze(df, sensors=None, contamination=0.03, min_rows=40):
    if not 0 < contamination <= 0.2:
        raise ValueError("Assumed outlier fraction must be in (0, 0.2].")
    df, sensors = validate(df, sensors)
    results, audit = [], []
    for asset, g in df.groupby("asset_id", sort=True):
        g = g.copy()
        missing = g[sensors].isna().mean().to_dict()
        usable = [s for s in sensors if g[s].notna().sum() >= min_rows and g[s].nunique(dropna=True) > 1]
        audit.append({
            "asset_id": asset, "rows": len(g), "start": g["timestamp"].min(),
            "end": g["timestamp"].max(), "usable_sensors": ", ".join(usable),
            "max_missing_fraction": max(missing.values())
        })
        g["anomaly_score"] = np.nan
        g["is_anomaly"] = False
        g["status"] = "insufficient_data"
        if len(g) >= min_rows and usable:
            complete = g[usable].notna().all(axis=1)
            if complete.sum() >= min_rows:
                X = g.loc[complete, usable]
                model = IsolationForest(n_estimators=200, contamination=contamination, random_state=42)
                model.fit(X)
                # Score is relative unusualness, not probability of mechanical failure.
                g.loc[complete, "anomaly_score"] = -model.decision_function(X)
                g.loc[complete, "is_anomaly"] = model.predict(X) == -1
                g.loc[complete, "status"] = "scored"
                g.loc[~complete, "status"] = "missing_sensor_values"
        results.append(g)
    if not results:
        raise ValueError("Input dataset is empty.")
    return pd.concat(results, ignore_index=True), pd.DataFrame(audit)

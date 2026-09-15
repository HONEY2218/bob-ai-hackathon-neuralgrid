import os
import pandas as pd

# Absolute path configuration to avoid FileNotFoundError
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, 'data', 'grid_data.csv')

if not os.path.exists(csv_path):
    print("Error: grid_data.csv not found! Run train.py first.")
else:
    df = pd.read_csv(csv_path)

    print("=" * 50)
    print("1. SUBSTATION FAILURE BREAKDOWN")
    print("=" * 50)
    substation_summary = df.groupby('substation').agg(
        total_assets=('asset_id', 'count'),
        failures=('failure_label', lambda x: (x == 1).sum()),
        failure_rate=('failure_label', lambda x: (x == 1).mean() * 100)
    ).reset_index()
    print(substation_summary.to_string(index=False))

    print("\n" + "=" * 50)
    print("2. TELEMETRY COMPARISON (NORMAL vs FAILED)")
    print("=" * 50)
    telemetry_summary = df.groupby('failure_label').agg(
        avg_oil_temp=('oil_temp_c', 'mean'),
        avg_vibration=('vibration_mms', 'mean'),
        avg_gas_ppm=('gas_ppm', 'mean'),
        avg_wind_speed=('wind_speed_kmh', 'mean'),
        avg_customers=('customers_impacted', 'mean')
    ).reset_index()
    print(telemetry_summary.to_string(index=False))

    print("\n" + "=" * 50)
    print("3. TOP HIGH-IMPACT FAILED ASSETS")
    print("=" * 50)
    critical_assets = df[df['failure_label'] == 1].sort_values(by='customers_impacted', ascending=False)
    print(critical_assets[['asset_id', 'substation', 'customers_impacted', 'oil_temp_c', 'vibration_mms']].head(5).to_string(index=False))

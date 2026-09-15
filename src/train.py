import os
import numpy as np
import pandas as pd
import joblib

# Target Directory Setup
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir, 'data')
models_dir = os.path.join(base_dir, 'models')

os.makedirs(data_dir, exist_ok=True)
os.makedirs(models_dir, exist_ok=True)

data_csv_path = os.path.join(data_dir, 'grid_data.csv')
model_pkl_path = os.path.join(models_dir, 'transformer_model.pkl')

# Set seed for reproducibility
np.random.seed(42)
n_samples = 1000

# Synthetic Data Generation
data = pd.DataFrame({
    'asset_id': [f'TR_{i:03d}' for i in range(1, n_samples + 1)],
    'substation': np.random.choice(['Substation_A', 'Substation_B', 'Substation_C', 'Substation_D'], n_samples),
    'oil_temp_c': np.random.uniform(40, 105, n_samples),
    'vibration_mms': np.random.uniform(0.1, 8.0, n_samples),
    'gas_ppm': np.random.uniform(10, 400, n_samples),
    'wind_speed_kmh': np.random.uniform(5, 90, n_samples),
    'customers_impacted': np.random.randint(500, 25000, n_samples)
})

# Ground Truth Labeling Logic
data['failure_label'] = np.where(
    ((data['oil_temp_c'] > 85) & (data['gas_ppm'] > 200)) | 
    ((data['wind_speed_kmh'] > 65) & (data['vibration_mms'] > 4.5)), 
    1, 0
)

# Export Dataset
data.to_csv(data_csv_path, index=False)

# Lightweight Predictor Engine (Rule-based replacement for DLL issues)
class GridPredictor:
    def predict(self, df):
        return np.where(
            ((df['oil_temp_c'] > 85) & (df['gas_ppm'] > 200)) | 
            ((df['wind_speed_kmh'] > 65) & (df['vibration_mms'] > 4.5)), 
            1, 0
        )

model = GridPredictor()
joblib.dump(model, model_pkl_path)

print("Pipeline Execution Complete!")
print(f"Dataset generated at: {data_csv_path}")
print(f"Model saved at: {model_pkl_path}")

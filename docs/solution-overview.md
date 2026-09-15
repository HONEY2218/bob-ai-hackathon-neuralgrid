# Solution Overview

## What We Built

NeuralGrid is an AI and IoT-driven grid failure prediction platform. It monitors power substation health metrics in real time—such as oil temperature, vibration, and dissolved gas levels—combining telemetry with weather conditions to proactively forecast equipment risks before blackouts happen.

## How It Works

1. Synthetic or real-time IoT sensor telemetry streams from electrical substations into the data engine.
2. The predictive ML pipeline evaluates risk scores based on transformer temperature, dissolved gas levels, and ambient weather.
3. High-risk substations are flagged automatically with critical severity levels and estimated maintenance timeframes.
4. The GIS interactive dashboard visualizes affected grid locations on an open-source map for field engineering dispatch.

## Architecture Diagram

[IoT Telemetry Data] → [Data Preprocessing & EDA Engine] → [Scikit-Learn ML Model]
↓
[Interactive Folium Map] ← [Streamlit Web Interface] ← [Risk Analytics Engine]
```

## Key Design Decisions

| Decision | Rationale |
|---|---|
| [e.g., Used watsonx.ai for anomaly detection] | [e.g., Pre-trained models reduced time-to-value vs. building from scratch] |
| [Decision 2] | [Rationale 2] |
| [Decision 3] | [Rationale 3] |

## IBM Technologies Used

[Explain specifically HOW you used each IBM technology — not just that you used it.]

- **[IBM Tech 1, e.g., watsonx.ai]:** [How it was used — e.g., "Used the `ibm/granite-13b-instruct-v2` model via the Python SDK to classify anomaly types from log text."]
- **[IBM Tech 2]:** [How it was used]

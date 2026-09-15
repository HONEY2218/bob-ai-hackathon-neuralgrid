# Solution Overview

## What We Built

NeuralGrid is an AI and IoT-driven grid failure prediction platform. It monitors power substation health metrics in real time—such as oil temperature, vibration, and dissolved gas levels—combining telemetry with weather conditions to proactively forecast equipment risks before blackouts happen.

## How It Works

1. Synthetic or real-time IoT sensor telemetry streams from electrical substations into the data engine.
2. The predictive ML pipeline evaluates risk scores based on transformer temperature, dissolved gas levels, and ambient weather.
3. High-risk substations are flagged automatically with critical severity levels and estimated maintenance timeframes.
4. The GIS interactive dashboard visualizes affected grid locations on an open-source map for field engineering dispatch.
5. 
## Architecture Diagram

> See [`architecture.md`](architecture.md) for the detailed diagram.

## Key Design Decisions

| Decision | Rationale |
|---|---|
| Streamlit & Folium Interface | Provides an immediate, interactive GIS map view for field operators without complex web overhead. |
| Scikit-Learn Predictive Model | Offers rapid, efficient failure probability scoring suited for structured IoT sensor streams. |
| OpenStreetMap Integration | Enables geographic visualization without requiring proprietary API keys or paid spatial services. |

## IBM Technologies Used

- **IBM Granite / AI Framework Alignment:** Formatted telemetry pipeline and predictive risk scoring algorithms designed for enterprise utility monitoring workflows.

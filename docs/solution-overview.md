# Solution Overview

The **Enterprise Power Outage Prediction & Grid Equipment Failure Advisor** provides a predictive maintenance platform integrating sensor analytics with spatial GIS intelligence.

## System Capabilities

- **Telemetry Ingestion & Simulation:** Simulates critical mechanical and chemical indicators:
  - Dissolved Gas Analysis (DGA PPM)
  - Transformer Oil Temperature (°C)
  - Acoustic/Mechanical Vibration (mm/s)
- **Multi-Factor Risk Engine:** Combines internal equipment health with external stress factors (ambient temperature and wind speed) into a normalized failure probability score.
- **Impact-Weighted Prioritization:** Calculates severity scores by weighting failure probability against downstream customer counts, ensuring highest-impact assets are serviced first.
- **Interactive Spatial Monitoring:** Integrates real-time geocoding via the OpenStreetMap Nominatim API, enabling operators to inspect substations in any geographic area.

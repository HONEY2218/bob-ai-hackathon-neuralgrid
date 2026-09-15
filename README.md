# Enterprise Power Outage Prediction & Grid Equipment Failure Advisor

---

## Team

| Field | Value |
|---|---|
| Team Name | NeuralGrid |
| Track | AI |
| Team Lead | Honey Patel - 25cs063@charusat.edu.in |
| Members | Heni Patel (25cs061@charusat.edu.in), Krisha A. Patel (25cs068@charusat.edu.in), Hinal Patel (25dce083@charusat.edu.in) |

---

## Problem Statement

Power utilities face unexpected power outages and equipment failures because equipment sensor data, weather conditions, and historical incident records are not analyzed together. This makes it difficult for grid operators to identify risky equipment and plan timely maintenance and crew deployment.

---

## Solution

We built an end-to-end telemetry risk analytics engine and interactive GIS dashboard that predicts transformer failures using IoT telemetry (oil temp, gas PPM, vibration) and environmental factors. The solution integrates an exploratory data analysis pipeline with real-time location geocoding to prioritize critical assets and automate maintenance crew dispatch directives.

---

## Key Features

- Automated synthetic IoT telemetry generation and model training pipeline (train.py)
- Exploratory Data Analysis (EDA) engine for substation-wise risk breakdown and impact analytics (eda_analysis.py)
- Interactive Streamlit Web Dashboard featuring dynamic location geocoding via OpenStreetMap API (app.py)
- Real-time GIS risk visualization with color-coded asset severity indicators on Folium maps
- Automated Priority Crew Dispatch planner based on estimated customer outage severity

---

## Tech Stack

| Category | Technologies |
|---|---|
| Languages | Python |
| Frameworks | Streamlit |
| IBM Technologies | IBM Predictive Analytics Concepts |
| Databases | CSV File System, Pandas Flat-File Storage |
| Other | Pandas, NumPy, Joblib, Folium, OpenStreetMap API |

---

## Repository Structure

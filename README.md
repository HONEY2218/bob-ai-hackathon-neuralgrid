# 🚀 Enterprise Power Outage Prediction & Grid Equipment Failure Advisor

---

## 👥 Team

| Field | Value |
|---|---|
| **Team Name** | NeuralGrid |
| **Track** | AI |
| **Team Lead** | Honey Patel — 25cs063@charusat.edu.in |
| **Members** | Heni Patel, Krisha A.Patel, Hinal Patel |

---

## 🎯 Problem Statement

Power utilities face unexpected power outages and equipment failures because equipment sensor data, weather conditions, and historical incident records are not analyzed together. This makes it difficult for grid operators to identify risky equipment and plan timely maintenance and crew deployment.

---

## 💡 Solution

We built an end-to-end telemetry risk analytics engine and interactive GIS dashboard that predicts transformer failures using IoT telemetry (oil temp, gas PPM, vibration) and environmental factors. The solution integrates an exploratory data analysis pipeline with real-time location geocoding to prioritize critical assets and automate maintenance crew dispatch directives.
---

## ✨ Key Features

- **Feature 1:** Automated synthetic IoT telemetry generation and model training pipeline (`train.py`)
- **Feature 2:** Exploratory Data Analysis (EDA) engine for substation-wise risk breakdown and impact analytics (`eda_analysis.py`)
- **Feature 3:** Interactive Streamlit Web Dashboard featuring dynamic location geocoding via OpenStreetMap API (`app.py`)
- **Feature 4:** Real-time GIS risk visualization with color-coded asset severity indicators on Folium maps
- **Feature 5:** Automated Priority Crew Dispatch planner based on estimated customer outage severity
---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| **Languages** | Python |
| **Frameworks** | Streamlit |
| **IBM Technologies** | IBM Predictive Analytics Concepts |
| **Databases** | CSV File System, Pandas Flat-File Storage |
| **Other** | Pandas, NumPy, Joblib, Folium, OpenStreetMap API |
---

## 📁 Repository Structure

```
├── src/                  # All source code
├── docs/                 # Written documentation
│   ├── problem-statement.md
│   ├── solution-overview.md
│   ├── architecture.md
│   └── setup-guide.md
├── demo/                 # Demo artifacts
│   ├── screenshots/      # App screenshots
│   └── demo-video-link.txt  # Link to demo video
├── presentation/         # Slide deck
└── submission.yaml       # Structured submission metadata
```

---

## ⚡ How to Run

```bash
# 1. Clone the repo
git clone https://github.com/HONEY2218/bob-ai-hackathon-neuralgrid.git
cd bob-ai-hackathon-neuralgrid

# 2. Install dependencies
py -m pip install --only-binary=:all: numpy pandas joblib streamlit folium streamlit-folium

# 3. Generate dataset and train predictive engine
cd src
py train.py

# 4. View CLI Analytics Report
py eda_analysis.py

# 5. Launch Interactive Web Dashboard
py -m streamlit run app.py
```



---

## 🖥️ Demo

| Artifact | Link |
|---|---|
| 📹 Demo Video | https://drive.google.com/file/d/1vJ0IYYcdsTTI0bl_x2pBH8vCyzGbuBgW/view?usp=sharing |
| 🌐 Live Demo | http://localhost:8501/ |
| 🖼️ Screenshots | Available in `demo/screenshots` |
| 📊 Presentation |Available in `demo/slide.pdf`|

---

## ⚠️ Known Limitations

- Currently relies on synthetic telemetry dataset generation (`grid_data.csv`) and deterministic fallback rules due to offline environment execution constraints.
- External Nominatim OpenStreetMap API rate limits may occasionally cause map re-rendering fallbacks for complex location queries.
---

## 🏅 What We're Most Proud Of



We are most proud of building a fully responsive, end-to-end operational pipeline that seamlessly connects low-level IoT telemetry risk calculation with live OpenStreetMap geocoding. This enables grid operators to search any real-world location and instantly view priority crew dispatch advisories mapped directly onto actual spatial infrastructure.

---

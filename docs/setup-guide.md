# Setup Guide

## Prerequisites

Before you begin, ensure you have the following installed:

- [x] Python 3.9+
- [x] pip package manager
- [x] Git CLI
- [x] Web browser (Chrome, Firefox, or Edge)

## Environment Variables

Copy `.env.example` to `.env` and fill in the values:

```bash
cp .env.example .env

```

| Variable | Description | Required |
|---|---|---|
| `PORT` | Local port number for Streamlit execution (default: 8501) | No |
| `NOMINATIM_USER_AGENT` | User agent header for OpenStreetMap API requests | No |

## Installation

### 1. Clone the repository
git clone https://github.com/HONEY2218/bob-ai-hackathon-neuralgrid.git
cd bob-ai-hackathon-neuralgrid

### 2. Install dependencies
pip install -r requirements.txt

## Running the Application

```bash
# Start the Streamlit web dashboard
streamlit run src/app.py
## Running Tests

```bash
[your test command — e.g.: pytest tests/ -v]
```

## Quick Demo (Optional)

Run the automated pipeline script to synthesize telemetry, train the model, and evaluate substation metrics:

```bash
python src/train.py
python src/eda_analysis.py
streamlit run src/app.py
```

## Troubleshooting

| Issue | Solution |
|---|---|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` to install missing packages. |
| Map markers not displaying | Check internet connection required for OpenStreetMap API tile fetching. |
| Model missing error | Run `python src/train.py` first to generate `grid_data.csv` and `model.joblib`. |
e up db`] |
| [e.g., watsonx.ai 401 error] | [e.g., Check `WATSONX_API_KEY` in your `.env` file] |

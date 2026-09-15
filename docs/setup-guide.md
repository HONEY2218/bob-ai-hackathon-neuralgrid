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

# 1. Clone the repository
git clone https://github.com/HONEY2218/bob-ai-hackathon-neuralgrid.git
cd bob-ai-hackathon-neuralgrid

# 2. Install dependencies
pip install -r requirements.txt

## Running the Application

```bash
# Start the backend
[your command — e.g.: uvicorn app.main:app --reload]

# Start the frontend (in a separate terminal, if applicable)
[your command — e.g.: cd frontend && npm run dev]
```

The application will be available at: `http://localhost:[PORT]`

## Running Tests

```bash
[your test command — e.g.: pytest tests/ -v]
```

## Quick Demo (Optional)

If you have a demo script or sample data to showcase the project quickly:

```bash
[e.g.: python demo/seed_demo_data.py]
[e.g.: open http://localhost:8000/demo]
```

## Troubleshooting

| Issue | Solution |
|---|---|
| [e.g., `ModuleNotFoundError`] | [e.g., Run `pip install -r requirements.txt` again] |
| [e.g., Database connection refused] | [e.g., Ensure PostgreSQL is running: `docker compose up db`] |
| [e.g., watsonx.ai 401 error] | [e.g., Check `WATSONX_API_KEY` in your `.env` file] |

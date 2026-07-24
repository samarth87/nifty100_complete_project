# Nifty 100 Analytics Platform

Complete runnable scaffold for Sprints 1–6: ETL, SQLite, DQ, ratios, CAGR, screener, peers, valuation, clustering, Streamlit, FastAPI, NLP, reports and tests.

## Setup
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts/download_data.py
python scripts/inspect_sources.py
python -m src.etl.loader --init-db --load-all
python -m src.analytics.pipeline
pytest -q
streamlit run src/dashboard/app.py
uvicorn src.api.main:app --reload --port 8000
```

The loader is schema-tolerant. After downloading, inspect `output/source_inventory.csv` and update `config/file_map.yaml` if the detected source files use different names.
# nifty100_complete_project

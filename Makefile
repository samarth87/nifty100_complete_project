download:
	python scripts/download_data.py
load:
	python -m src.etl.loader --init-db --load-all
ratios:
	python -m src.analytics.pipeline
test:
	pytest -v
dashboard:
	streamlit run src/dashboard/app.py
api:
	uvicorn src.api.main:app --reload --port 8000

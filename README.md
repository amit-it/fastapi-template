# FastAPI Template

High-level template for a FastAPI project with MySQL, repository + service layers, and a sales reporting API.

## Features
- FastAPI app factory (`app/factory.py`)
- MySQL via SQLAlchemy
- Repository + service layers (currently concrete implementations)
- Health check endpoint
- Sales reporting API (monthly aggregates by brand/category/region)
- 3NF sales schema + seed scripts

## Project Structure
- app/
  - api/
    - routes/
    - deps.py
    - router.py
  - core/
    - config.py
    - database.py
  - models/
  - repositories/
  - services/
  - schemas/
  - factory.py
  - main.py

## Requirements
- Python 3.12+
- MySQL 8+

## Setup
1. Create a virtualenv and install deps:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\pip install -r requirements.txt
   .\.venv\Scripts\pip install -r requirements-dev.txt
   ```
2. Create `.env` (copy from `.env.example`) and update DB credentials.

## Run
```powershell
.\.venv\Scripts\python -m uvicorn app.main:app
```

## Database Schema
If you want to create tables manually (instead of SQLAlchemy `create_all`), use:
- `sql/sales_schema.sql`

## Seed Data
- Seed sales data (10,000 rows):
  ```powershell
  .\.venv\Scripts\python -m app.seed_sales_data
  ```

## Tests
Run tests with coverage (90% minimum):
```powershell
.\.venv\Scripts\python -m pytest
```

## API Endpoints (High Level)
- `GET /health`
- `GET /sales/monthly?brand=...&category=...&region=...&year=...`

## Notes
- The app currently creates tables on startup in `app/factory.py`.
- The sales API expects dimension values to exist (brands, categories, regions).

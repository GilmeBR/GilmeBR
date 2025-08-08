# NBA Historical Dashboard (Prototype)

This repository contains a minimal proof-of-concept for a historical NBA stats
dashboard. The backend uses [nba_api](https://github.com/swar/nba_api) to query
official NBA statistics and exposes them through a small FastAPI service. A
static frontend demonstrates how the data can be visualised with Chart.js.

## Local Development

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then visit [http://localhost:8000](http://localhost:8000) to view the dashboard.

## Docker Deployment

Build and run the full stack with Docker:

```bash
docker-compose up --build
```

The app will be available at [http://localhost:8000](http://localhost:8000).

## Tests

A basic test suite ensures that the API returns data:

```bash
cd backend
pytest
```

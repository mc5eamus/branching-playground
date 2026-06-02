# Branching Playground

A testing ground to explore how **GitHub Copilot** behaves with respect to default branch conventions and branching strategies.

## Project Overview

This repository hosts a minimal **FastAPI** weather API. Its primary purpose is not the API itself, but to serve as a sandbox for experimenting with GitHub Copilot's awareness of branching rules, pull request targets, and repository conventions.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| API framework | [FastAPI](https://fastapi.tiangolo.com/) |
| Server | [Uvicorn](https://www.uvicorn.org/) |
| Testing | [pytest](https://pytest.org/) + [httpx](https://www.python-httpx.org/) |
| Containerisation | Docker |

## Branching Strategy

| Branch | Purpose |
|--------|---------|
| `dev` | Default development branch — all PRs target here |
| `main` | Production/release branch — only receives merges from `dev` |

Feature branches should be created from `dev` and merged back into `dev` via pull request.

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/health` | Health check — returns `{"status": "ok"}` |
| `GET` | `/weather/{city}` | Returns weather data for the given city |

### Supported Cities

`London`, `New York`, `Tokyo`, `Paris`, `Sydney`

### Example

```bash
curl http://localhost:8000/weather/london
```

```json
{
  "city": "London",
  "temperature_c": 15.0,
  "humidity_pct": 72,
  "condition": "Cloudy"
}
```

## Local Development

### Prerequisites

- Python 3.12+
- Docker (optional)

### Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.  
Interactive docs: `http://localhost:8000/docs`

### Run with Docker

```bash
docker build -t branching-playground .
docker run -p 8000:8000 branching-playground
```

### Run Tests

```bash
pytest tests/
```

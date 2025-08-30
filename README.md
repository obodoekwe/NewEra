# New Era Class 24 — Flask + Docker Demo

A clean Flask app to practice Dockerfiles, images, and containers.

## Quick start (local)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export APP_NAME="New Era Class 24" APP_ENV=dev LOG_LEVEL=debug
python app.py  # visit http://localhost:8080
```

## Build & run with Docker
```bash
# Build
docker build -t newera:1.0 .

# Run (publish port)
docker run --rm --name app1 -p 8080:8080   -e APP_NAME="New Era Class 24" -e APP_ENV=prod -e LOG_LEVEL=info   newera:1.0
```

## Network demo (two services)
```bash
# Create a network
docker network create appnet
# Start the app on that network
docker run -d --name api --network appnet newera:1.0
# Start a tiny curl container to talk to api by name
docker run --rm --network appnet curlimages/curl:8.9.1 http://api:8080/status
```

## Compose
```bash
cp .env.example .env
docker compose up --build -d
```

## Test
```bash
pip install -r requirements.txt
pytest -q
```

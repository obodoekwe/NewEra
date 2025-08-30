# syntax=docker/dockerfile:1
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

WORKDIR /app

# Create non-root user
RUN useradd -r -u 10001 -m app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
USER app
EXPOSE 8080

ENTRYPOINT ["gunicorn", "-w", "2", "-b", "0.0.0.0:8080", "app:app"]

FROM python:3.11-slim

WORKDIR /app/backend

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY backend/pyproject.toml /app/backend/
COPY pyproject.toml /app/

RUN pip install --no-cache-dir \
    asyncpg>=0.30.0 \
    "fastapi==0.128.7" \
    "httpx==0.28.1" \
    "pydantic==2.12.5" \
    "pydantic-settings==2.12.0" \
    "sqlmodel>=0.0.22" \
    "uvicorn[standard]==0.40.0"

COPY backend /app/backend

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

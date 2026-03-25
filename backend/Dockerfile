FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies directly
COPY backend/pyproject.toml backend/requirements.txt* /app/backend/
COPY pyproject.toml /app/

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy asyncpg pydantic httpx python-multipart

# Copy backend source
COPY backend /app/backend

# Expose port
EXPOSE 8000

# Run backend
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

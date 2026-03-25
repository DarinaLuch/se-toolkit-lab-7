FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir python-telegram-bot httpx pydantic-settings pydantic

COPY bot/ .

CMD ["python", "bot.py"]

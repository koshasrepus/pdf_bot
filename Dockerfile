FROM python:3.10-slim-bookworm


RUN apt-get update && apt install build-essential libpoppler-cpp-dev pkg-config python3-dev -y

RUN pip install poetry==1.4.2 && poetry config virtualenvs.create false

WORKDIR /app

COPY . .

RUN poetry install --no-interaction --no-root

ENV PYTHONPATH=/app:$PYTHONPATH
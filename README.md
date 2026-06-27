# NGI-BOT

NGI-BOT is a lightweight, Bible-based spiritual chatbot built with Flask. The
current version uses deterministic keyword rules and local static assets, so it
has no paid AI API, database, login, or external service dependency.

## Current architecture

```text
Browser -> Flask route -> Rule-based chatbot -> Server-rendered response
```

- `app.py` contains the Flask application and routes.
- `chatbot.py` contains the current response rules.
- `templates/` contains Jinja HTML templates.
- `static/` contains CSS, JavaScript, and images.
- `documents/` is reserved for approved local source documents.
- `data/bible/` is reserved for local Bible datasets.
- `data/indexes/` is reserved for generated local search indexes.

The reserved folders do not implement RAG or local search yet.

## Run locally

Create and activate a virtual environment, then install the dependencies:

```bash
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

## Run tests

The regression suite uses Python's standard `unittest` module:

```bash
python -m unittest discover -s tests -v
```

## Render deployment

Use the existing Python dependencies and this start command:

```text
gunicorn app:app
```

No environment variable or external API key is required.

## Future low-cost evolution

A later version can add curated Bible content and local full-text search while
keeping the Flask route and current rule engine. SQLite may eventually be used
for statistics, but it is intentionally not part of this version. Durable
SQLite storage on Render will require an appropriate persistence strategy.

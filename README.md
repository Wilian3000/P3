# Usability Evaluator

![CI](https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg)

Minimal Flask application that evaluates basic accessibility and computes a global usability score.

## Installation

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running

```bash
flask --app app.factory:create_app run
```

## Environment Variables

Copy `.env.example` to `.env` and adjust values.

## Testing

```bash
pytest -q
```

## Deploy to Render

1. Push this repository to GitHub.
2. Create a new Web Service in Render connected to the repo.
3. Use the provided `Dockerfile` and start command `gunicorn 'app.factory:create_app()'`.

## Scoring Weights

Weights for the global score are defined in `app/services/scoring.py`.

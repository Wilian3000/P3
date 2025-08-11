from urllib.parse import urlparse

from flask import Blueprint, jsonify, request

from ...services import a11y, sanitize, scoring

api_bp = Blueprint("api", __name__)


def _validate_payload(payload: dict) -> tuple[str | None, str | None]:
    url = payload.get("url")
    html = payload.get("html")
    if url:
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"}:
            raise ValueError("invalid url")
    if not (url or html):
        raise ValueError("provide url or html")
    return url, html


@api_bp.post("/evaluate")
def evaluate():
    try:
        url, html = _validate_payload(request.get_json(force=True))
    except Exception as exc:  # pragma: no cover - simple validation
        return jsonify({"error": str(exc)}), 400

    html_content = (
        html
        or "<html><body><p>Placeholder fetched content for %s</p></body></html>" % url
    )
    cleaned = sanitize.clean_html(html_content)
    a11y_findings = a11y.check_alt_attributes(cleaned)

    scores = scoring.compute_global_score(
        {
            "nielsen": 0.8,
            "shneiderman": 0.7,
            "iso9241": 0.9,
            "iso25010": 0.6,
            "wcag": 0.5,
        }
    )

    result = {
        "global_score": scores,
        "a11y": a11y_findings,
    }
    return jsonify(result)

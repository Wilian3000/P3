import pytest

flask = pytest.importorskip("flask")
from app.factory import create_app


def test_evaluate_endpoint():
    app = create_app()
    client = app.test_client()
    resp = client.post("/api/evaluate", json={"html": '<img src="x.png">'})
    assert resp.status_code == 200
    data = resp.get_json()
    assert "global_score" in data
    assert "a11y" in data

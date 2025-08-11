from app.services import scoring


def test_compute_global_score():
    scores = {
        "nielsen": 1.0,
        "shneiderman": 1.0,
        "iso9241": 1.0,
        "iso25010": 1.0,
        "wcag": 1.0,
    }
    assert scoring.compute_global_score(scores) == 100

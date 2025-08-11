WEIGHTS = {
    "nielsen": 0.30,
    "shneiderman": 0.15,
    "iso9241": 0.25,
    "iso25010": 0.15,
    "wcag": 0.15,
}


def compute_global_score(scores: dict[str, float]) -> float:
    """Combine partial scores into a global score 0-100."""
    total = 0.0
    for key, weight in WEIGHTS.items():
        total += scores.get(key, 0) * weight
    return round(total * 100, 2)

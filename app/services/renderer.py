import requests


def fetch_url(url: str) -> str:
    """Fetch HTML content from a URL (simplified)."""
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.text

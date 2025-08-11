import re

SCRIPT_RE = re.compile(r"<script.*?>.*?</script>", re.IGNORECASE | re.DOTALL)


def clean_html(raw_html: str) -> str:
    """Very small sanitization removing script tags."""
    return SCRIPT_RE.sub("", raw_html)

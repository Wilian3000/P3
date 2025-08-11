from app.services import sanitize


def test_clean_html():
    dirty = "<script>alert(1)</script><p>ok</p>"
    cleaned = sanitize.clean_html(dirty)
    assert "<script>" not in cleaned
    assert "<p>ok</p>" in cleaned

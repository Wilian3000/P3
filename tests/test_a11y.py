from app.services import a11y


def test_missing_alt_detected():
    html = '<img src="test.png">'
    issues = a11y.check_alt_attributes(html)
    assert issues and issues[0]["issue"] == "missing alt"

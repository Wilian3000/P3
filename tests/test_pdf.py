from pathlib import Path

from app.services import pdf


def test_generate_pdf(tmp_path: Path):
    output = tmp_path / "test.pdf"
    pdf.generate_pdf("Hello", output)
    assert output.exists()

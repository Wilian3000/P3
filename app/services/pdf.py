from pathlib import Path

MINIMAL_PDF = """%PDF-1.1\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 200 200] /Contents 4 0 R >>\nendobj\n4 0 obj\n<< /Length {length} >>\nstream\n{content}\nendstream\nendobj\nxref\n0 5\n0000000000 65535 f \n0000000010 00000 n \n0000000063 00000 n \n0000000124 00000 n \n0000000215 00000 n \ntrailer\n<< /Root 1 0 R /Size 5 >>\nstartxref\n281\n%%EOF"""


def generate_pdf(content: str, output_path: Path) -> Path:
    payload = MINIMAL_PDF.format(length=len(content) + 20, content=content)
    output_path.write_text(payload)
    return output_path

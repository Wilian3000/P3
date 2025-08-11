from html.parser import HTMLParser


class ImgAltParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.issues = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            attr_dict = dict(attrs)
            if "alt" not in attr_dict or not attr_dict["alt"]:
                self.issues.append({"element": "img", "issue": "missing alt"})


def check_alt_attributes(html: str) -> list[dict]:
    parser = ImgAltParser()
    parser.feed(html)
    return parser.issues

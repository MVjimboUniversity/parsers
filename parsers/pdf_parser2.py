import fitz


def pdf_parser(path: str) -> list[str]:
    text = []
    with fitz.open(path) as doc:
        for page in doc.pages():
            text.append(page.get_text())
    return text


def main():
    text = pdf_parser(r"parsers\2006_Congestions_power law.pdf")
    for page in text:
        print(page)


if __name__ == "__main__":
    main()
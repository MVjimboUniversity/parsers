import fitz


def parser(path: str) -> list[str]:
    text = []
    with fitz.open(path) as doc:
        for page in doc.pages():
            text.append(page.get_text())
    return text


def main():
    text = parser(r"test_files\multieng test.pdf")
    for page in text:
        print(page)


if __name__ == "__main__":
    main()
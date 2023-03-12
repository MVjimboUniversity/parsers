from docx_parser import DocumentParser


def parser(path: str) -> list[str]:
    """Parsing paragraphs and tables from docx file.

    Args:
        path (str): path to docx file

    Returns:
        list[str]: content of docx file
    """
    doc = DocumentParser(path)
    text = []
    for type, content in doc.parse():
        if type in ("paragraph"):
            text.append(content.get("text"))
        elif type in ("table"):
            text.append(content.get("data") )
    return text


def main():
    text = parser(r"parsers\test2.docx")
    for paragraph in text:
        print(paragraph)


if __name__ == "__main__":
    main()

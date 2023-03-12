from pathlib import Path
import io

import requests
from PyPDF2 import PdfReader


def get_pdf_content(f) -> list[str]:
    reader = PdfReader(f)
    text = [page.extract_text() for page in reader.pages]
    return text


def parser(path: str) -> list[str]|None:
    file_path = Path(path)
    if file_path.exists():
        with open(path, "rb") as f:
           text =  get_pdf_content(f)
    else:
        response = requests.get(path)
        if response.status_code != 200:
            return None
        byteContent = io.BytesIO(response.content)
        text =  get_pdf_content(byteContent)
    return text


def main():
    # text = parser(r"parsers\path_to_pdf")
    text = parser(r"http://www-personal.umich.edu/~mejn/courses/2006/cmplxsys899/powerlaws.pdf")
    for page in text:
        print(page)


if __name__ == "__main__":
    main()
from pathlib import Path
import io
 
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
import requests


def extract_text_by_page(f) -> str:
    for page in PDFPage.get_pages(f, 
                                  caching=True,
                                  check_extractable=True):
        resource_manager = PDFResourceManager()
        fake_file_handle = io.StringIO()
        converter = TextConverter(resource_manager, fake_file_handle)
        page_interpreter = PDFPageInterpreter(resource_manager, converter)
        page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()
        yield text

        # close open handles
        converter.close()
        fake_file_handle.close()
    

def pdf_parser(path: str) -> list[str]|None:
    filePath = Path(path)
    text = []
    if filePath.exists():
        with open(path, "rb") as f:
            text = [page for page in extract_text_by_page(f)]
    else:
        response = requests.get(path)
        if response.status_code != 200:
            return None
        byteContent = io.BytesIO(response.content)
        text = extract_text_by_page(byteContent)
    return text


def main():
    # text = pdf_parser(r"parsers\2006_Congestions_power law.pdf")
    text = pdf_parser(r"http://www-personal.umich.edu/~mejn/courses/2006/cmplxsys899/powerlaws.pdf")
    for page in text:
        print(page)


if __name__ == "__main__":
    main()

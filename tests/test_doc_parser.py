from parsers.doc_parser import doc_to_docx # how to not import docx__parser here?
import parsers.docx__parser as docx__parser 
from pathlib import Path


URL1 = r"G:\Vlad\parsers_real\parsers\test_files\Hello world test.doc"
URL2 = r"G:\Vlad\parsers_real\parsers\test_files\multieng test.doc"
URL3 = r"G:\Vlad\parsers_real\parsers\test_files\text_14_paragraphs.doc"

EXPECTED_TEXT_1 = """HELLO WORLD!!!
Advanced-technolocies’s in 2015` year./"""

EXPECTED_TEXT_2 = """Файл WORD был преобразован в PDF
HELLO WORLD!!!"""
EXPECTED_TEXT_3 = Path(r"test_files\powerlaws.txt").read_text()

EXPECTED_TABLE = """[['Привет', 'Пока', 'До', 'Встречи'], ['Увидимся', 'С', 'Тобой', 'В'], ['Следующем', '2024', 'Году', '*']]"""

def test_parser_correctness_multieng():
    new_path = doc_to_docx(URL1)
    text = docx__parser.parser(new_path)
    assert  '\n'.join(text) == EXPECTED_TEXT_1, f'texts do not match, {text} expected'


def test_parser_correctness():
    new_path = doc_to_docx(URL2)
    text = docx__parser.parser(new_path)
    assert  '\n'.join(text) == EXPECTED_TEXT_2, f'texts do not match, {text} expected'

def test_parser_page_counts():
    new_path = doc_to_docx(URL3)
    text = docx__parser.parser(new_path)
    page_count = 0
    for _ in text:
        page_count += 1
    assert page_count == 14, f'texts paragraphs do not match, got {len(text)} but 27 expected'

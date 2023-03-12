from parsers.pdf_parser2 import parser
from pathlib import Path



URL1 = r"test_files\multieng test.pdf"
URL2 = r'test_files\powerlaws.pdf'
URL3 = r'test_files\Hello world test_advanced.pdf'

EXPECTED_TEXT_1 = """Файл WORD был преобразован в PDF 
HELLO WORLD!!! 
"""
EXPECTED_TEXT_2 = Path(r"test_files\powerlaws.txt").read_text()

EXPECTED_TEXT_3 = """HELLO WORLD!!! 
Advanced-technolocies’s in 2015` year./ 
"""

def test_parser_correctness_multieng():
    text = parser(URL1)
    assert  text[0] == EXPECTED_TEXT_1, f'texts do not match, {text[-1]} expected'


def test_parser_correctness():
    text = parser(URL2)
    assert  text[-1].replace('\n', ' ')[:100] == EXPECTED_TEXT_2.replace('\n', ' ')[:100], f'texts do not match, {text[-1]} expected'

def test_parser_correctness_full_file():
    text = parser(URL3)
    assert  text[0] == EXPECTED_TEXT_3, f'texts do not match, {text[-1]} expected'



def test_parser_page_counts():
    text = parser(URL2)
    page_count = 0
    for _ in text:
        page_count += 1
    assert page_count == 27, f'texts pages do not match, got {len(text)} but 27 expected'

from parsers.docx__parser import parser
from pathlib import Path


URL1 = r'test_files\Hello world test.docx'
URL2 = r"test_files\multieng test.docx"
URL3 = r"test_files\text_14_paragraphs.docx"

EXPECTED_TEXT_1 = """HELLO WORLD!!!
Advanced-technolocies’s in 2015` year./"""

EXPECTED_TEXT_2 = """Файл WORD был преобразован в PDF
HELLO WORLD!!!"""
EXPECTED_TEXT_3 = Path(r"test_files\powerlaws.txt").read_text()

EXPECTED_TABLE = """[['Привет', 'Пока', 'До', 'Встречи'], ['Увидимся', 'С', 'Тобой', 'В'], ['Следующем', '2024', 'Году', '*']]"""

def test_parser_correctness_multieng():
    text = parser(URL1)
    assert  '\n'.join(text) == EXPECTED_TEXT_1, f'texts do not match, {text} expected'


def test_parser_correctness():
    text = parser(URL2)
    assert  '\n'.join(text) == EXPECTED_TEXT_2, f'texts do not match, {text} expected'

def test_parser_page_counts():
    text = parser(URL3)
    page_count = 0
    for _ in text:
        page_count += 1
    assert page_count == 14, f'texts paragraphs do not match, got {len(text)} but 27 expected'

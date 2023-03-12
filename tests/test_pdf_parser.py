from parsers.pdf_parser import parser


URL_local = r"test_files\Hello world test_advanced.pdf"
URL_global = r'http://www-personal.umich.edu/~mejn/courses/2006/cmplxsys899/powerlaws.pdf'
URL_multieng = r"test_files\multieng test.pdf"

EXPECTED_TEXT = """HELLO WORLD!!! Advanced-technolocies’s in 2015` year./ \x0c"""


def test_parser_correctness_multieng():
    text = parser(URL_multieng)
    assert  text[0] == 'Файл WORD был преобразован в PDF HELLO WORLD!!! \x0c', f'texts do not match, {text[0]} expected'

def test_parser_correctness():
    text = parser(URL_local)
    assert  text[0] == EXPECTED_TEXT, f'texts do not match, {text[0]} expected'

def test_parser_page_counts():
    text = parser(URL_global)
    page_count = 0
    for _ in text:
        page_count += 1
    assert page_count == 27, f'texts pages do not match, got {len(text)} but 27 expected'

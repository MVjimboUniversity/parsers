from parsers.pdf_parser import parser

EXPECTED_TEXTS = ['http://info.cern.ch', 'http://info.cern.ch - home of the first website',
                   'From here you can:', 'Browse the first website', 'Browse the first website using the line-mode browser simulator',
                   'Learn about the birth of the web', 'Learn about CERN, the physics laboratory where the web was born']
EXPECTED_URLS = ['http://info.cern.ch/hypertext/WWW/TheProject.html', 'http://line-mode.cern.ch/www/hypertext/WWW/TheProject.html', 'http://home.web.cern.ch/topics/birth-web', 'http://home.web.cern.ch/about']

URL_local = r"test_files\multieng test.pdf"
URL_global = r'http://www-personal.umich.edu/~mejn/courses/2006/cmplxsys899/powerlaws.pdf'



def test_parser_correctness():
    text = parser(URL_local)
    assert  text[0] == 'Файл WORD был преобразован в PDF HELLO WORLD!!! \x0c', f'texts do not match, {text[0]} expected'


def test_parser_page_counts():
    text = parser(URL_global)
    page_count = 0
    for _ in text:
        page_count += 1
    assert page_count == 27, f'texts pages do not match, got {len(text)} but 27 expected'

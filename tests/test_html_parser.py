from parsers.html_parser import parser

EXPECTED_TEXTS = ['http://info.cern.ch', 'http://info.cern.ch - home of the first website',
                   'From here you can:', 'Browse the first website', 'Browse the first website using the line-mode browser simulator',
                   'Learn about the birth of the web', 'Learn about CERN, the physics laboratory where the web was born']
EXPECTED_URLS = ['http://info.cern.ch/hypertext/WWW/TheProject.html', 'http://line-mode.cern.ch/www/hypertext/WWW/TheProject.html', 'http://home.web.cern.ch/topics/birth-web', 'http://home.web.cern.ch/about']

URL1 = 'http://info.cern.ch/'
URL2 = 'http://info.cern.ch/hypertext/WWW/TheProject.html'



def test_parser_correctness():
    text, links = parser(URL1)
    assert  text == EXPECTED_TEXTS, 'texts do not match'
    assert  links == EXPECTED_URLS, 'links do not match'


def test_parser_urls_counts():
    _, links = parser(URL2)
    assert  len(links) == 25, f'urls number do not match {len(links)} expected'
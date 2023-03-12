import requests
from bs4 import BeautifulSoup
import lxml


def parser(link: str, parser: str = "lxml") -> tuple[list[str], list[str]]:
    response = requests.get(link)
    if response.status_code != 200:
        return None
    soup = BeautifulSoup(response.text, parser)
    return [s for s in soup.stripped_strings], [a.get('href') for a in soup.find_all('a')]


def main():
    text, links = parser("https://pypi.org/project/beautifulsoup4/")
    print(text)
    print(links)
    

if __name__ == "__main__":
    main()

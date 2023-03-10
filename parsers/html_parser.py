import requests
from bs4 import BeautifulSoup
import lxml


def html_parser(link: str) -> tuple[list[str], list[str]]:
    response = requests.get(link)
    if response.status_code != 200:
        return None
    soup = BeautifulSoup(response.text, "lxml")
    return [s for s in soup.stripped_strings], [a.get('href') for a in soup.find_all('a')]


def main():
    text, links = html_parser("https://pypi.org/project/beautifulsoup4/")
    print(text)
    print(links)
    

if __name__ == "__main__":
    main()

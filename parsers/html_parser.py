import requests
from bs4 import BeautifulSoup


def parser(link: str, parser: str = "lxml") -> tuple[list[str], list[str]]:
    response = requests.get(link)
    if response.status_code != 200:
        return None
    soup = BeautifulSoup(response.text, parser)
    
    #finds all <a> tags urls
    #return [s for s in soup.stripped_strings], [a.get('href') for a in soup.find_all('a')]
    
    #finds all tags where url != None
    return [s for s in soup.stripped_strings], [a.get('href') for a in soup.find_all() if a.get('href') != None]
    

def main():
    text, links = parser("https://pypi.org/project/beautifulsoup4/")
    for par in text:
        print(par)
    print()
    for link in links:
        print(link)
    

if __name__ == "__main__":
    main()

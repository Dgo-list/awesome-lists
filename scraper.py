import requests
from bs4 import BeautifulSoup as Soup

class Scraper:
    def __init__(self):
        self.root_url = 'https://github.com/sindresorhus/awesome/blob/master/readme.md'

    def get_topics(self):
        contents = requests.get(self.root_url)
        soup = Soup(contents.text)
        tags = soup.find_all('article', 'markdown-body')[0].find_all(['h2', 'a'])

        data = {}
        topic = None

        for tag in tags:
            if tag.name == 'h2':
                topic = tag.text
            if tag.name == 'a':
                link = tag['href']
                if 'github' in link:
                    print(link)




scraper = Scraper()
scraper.get_topics()

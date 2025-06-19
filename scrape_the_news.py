from bs4 import BeautifulSoup
import requests

PAGE_SETTINGS = {
    "bild": {
        'url': 'https://www.bild.de',
        'container_class': 'teaser__title__headline'
    },
    "spiegel": {
        'url': 'https://www.spiegel.de',
        'container_class': ''
    },
}


class NewsScraper:
    def __init__(self, page: str):
        self.page = page.lower()        
        self.url = PAGE_SETTINGS[self.page]['url']
        self.container_class = PAGE_SETTINGS[self.page]['container_class']

    @staticmethod
    def get_snapshot(url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup

    def get_headline_and_link(self):
        soup = self.get_snapshot(self.url)
        main = soup.find('main')
        headline = main.find("span", class_=self.container_class)
        headline_link = self.url + main.find("a", ).get("href")
        return headline.text, headline_link

    def get_spiegel_headline_and_link(self):
        soup = self.get_snapshot(self.url)
        main = soup.find('main')
        header = main.find("header")
        headline_text = header.find("a").get("title")
        headline_link = header.find("a", ).get("href")
        return headline_text, headline_link

    def start(self):
        if self.page == "bild":
            scraper = self.get_headline_and_link()
        elif self.page == "spiegel":
            scraper = self.get_spiegel_headline_and_link()
        else:
            scraper = None
        return scraper

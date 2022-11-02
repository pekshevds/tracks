from datetime import datetime
from bs4 import BeautifulSoup

from webapp.news.parsers.utils import get_html, save_news


def get_habr_snipets():
    html = get_html("https://habr.com/ru/search/?target_type=posts&q=python&order")
    if html:
        soup = BeautifulSoup(html, "html.parser")
        all_news = soup.findAll('article', class_="tm-articles-list__item")
        for news in all_news:
            
            title = news.find('span', class_="").text
            url = news.find('a', class_="tm-article-snippet__title-link")['href']
            published = news.find('time')['datetime']
            print(title, url, published)
        """try:
                published = datetime.strptime(published, '%Y-%m-%d')
            except ValueError:
                published = datetime.now()

            save_news(title, url, published)"""
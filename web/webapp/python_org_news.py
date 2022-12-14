from datetime import datetime

import requests
from bs4 import BeautifulSoup
from webapp.news.models import News
from webapp.db import db


def get_html(url):
    try:
        result = requests.get(url=url)
        result.raise_for_status()
        return result.text
    except (requests.RequestException, ValueError):
        return False


def get_python_news():
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, "html.parser")
        all_news = soup.find('ul', class_="list-recent-posts").findAll('li')
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time')['datetime']
            try:
                published = datetime.strptime(published, '%Y-%m-%d')
            except ValueError:
                published = datetime.now()

            save_news(title, url, published)


def save_news(title, url, published):
    news_exist = News.query.filter(News.url == url).count()
    if not news_exist:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()

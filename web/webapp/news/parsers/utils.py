import requests
from webapp.news.models import News
from webapp.db import db


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0',
    }
    try:
        result = requests.get(url=url, headers=headers)
        result.raise_for_status()
        return result.text
    except (requests.RequestException, ValueError):
        return False


def save_news(title, url, published):
    news_exist = News.query.filter(News.url == url).count()
    if not news_exist:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()

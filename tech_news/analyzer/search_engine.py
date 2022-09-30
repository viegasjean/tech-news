from datetime import datetime

from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news = search_news({'title': {'$regex': title, '$options': 'i'}})

    return [(item['title'], item['url']) for item in news]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        data = datetime.strptime(date, "%Y-%m-%d")
    except ValueError():
        raise ValueError('Data inválida')

    news = search_news({'date': data})
    return news


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""

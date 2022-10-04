from collections import Counter

from tech_news.database import search_news


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    news = search_news({})
    news.sort(key=lambda x: x["comments_count"], reverse=True)

    if len(news) < 5:
        return [(item["title"], item["url"]) for item in news]
    return [(item["title"], item["url"]) for item in news][:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    news = search_news({})
    categories = Counter([item['category'] for item in news])
    sorted_cat = sorted(categories.items(), key=lambda x: (-x[1], x[0]))

    return [i[0] for i in sorted_cat]

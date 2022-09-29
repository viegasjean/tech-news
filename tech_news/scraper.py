import time

import requests
from parsel import Selector

from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    headers = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, timeout=3, headers=headers)
        if response.status_code != 200:
            return None
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    posts_links = selector.css(".entry-title a::attr(href)").getall()
    return posts_links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    next_page = selector.css(".next::attr(href)").get()
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url = selector.css('head > link[rel="canonical"]::attr(href)').get()
    title = selector.css(".entry-title::text").get()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    comments_count = selector.css(".post-comments").get() or 0
    summary = selector.css(".entry-content > p:first-of-type *::text").getall()
    tags = selector.css("a[rel=tag]::text").getall()
    category = selector.css(".label::text").get()

    return {
        "url": url,
        "title": title.strip(),
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": "".join(summary).strip(),
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    html_content = fetch('https://blog.betrybe.com/')
    news_links = scrape_novidades(html_content)

    while len(news_links) < amount:
        next_page_link = scrape_next_page_link(html_content)
        html_content = fetch(next_page_link)
        news_links.append(scrape_novidades(html_content))
    all_links = news_links[:amount]

    data = []
    for url in all_links:
        noticia = scrape_noticia(fetch(url))
        data.append(noticia)

    create_news(data)

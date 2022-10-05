# Requisito 12
import sys

from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (search_by_category,
                                              search_by_date, search_by_tag,
                                              search_by_title)
from tech_news.scraper import get_tech_news


def news_amount():
    amount = input("Digite quantas notícias serão buscadas:")
    get_tech_news(amount)


def by_title():
    title = input("Digite o título:")
    search_by_title(title)


def by_date():
    date = input("Digite a data no formato aaaa-mm-dd:")
    search_by_date(date)


def by_tag():
    tag = input("Digite a tag:")
    search_by_tag(tag)


def by_category():
    category = input("Digite a categoria:")
    search_by_category(category)


def finish():
    print("Encerrando script")


def invalid_option():
    print("Opção inválida", file=sys.stderr)


def analyzer_menu():
    """Seu código deve vir aqui"""
    option = input(
        "Selecione uma das opções a seguir:\n 0 - Popular o banco com notícias"
        ";\n 1 - Buscar notícias por título;\n 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n 4 - Buscar notícias por categoria;\n "
        "5 - Listar top 5 notícias;\n 6 - Listar top 5 categorias;\n 7 - Sair."
    )

    options = {
        "0": news_amount,
        "1": by_title,
        "2": by_date,
        "3": by_tag,
        "4": by_category,
        "5": top_5_news,
        "6": top_5_categories,
        "7": finish,
    }

    options.get(option, invalid_option)()


if __name__ == "__main__":
    analyzer_menu()

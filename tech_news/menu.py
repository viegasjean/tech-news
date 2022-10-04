# Requisito 12
import sys

from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (search_by_category,
                                              search_by_date, search_by_tag,
                                              search_by_title)
from tech_news.scraper import get_tech_news


def analyzer_menu():
    """Seu código deve vir aqui"""
    option = input(
        "Selecione uma das opções a seguir:\n 0 - Popular o banco com notícias"
        ";\n 1 - Buscar notícias por título;\n 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n 4 - Buscar notícias por categoria;\n "
        "5 - Listar top 5 notícias;\n 6 - Listar top 5 categorias;\n 7 - Sair."
    )

    if option == "0":
        amount = input("Digite quantas notícias serão buscadas:")
        get_tech_news(amount)
    elif option == "1":
        title = input("Digite o título:")
        search_by_title(title)
    elif option == "2":
        date = input("Digite a data no formato aaaa-mm-dd:")
        search_by_date(date)
    elif option == "3":
        tag = input("Digite a tag:")
        search_by_tag(tag)
    elif option == "4":
        category = input("Digite a categoria:")
        search_by_category(category)
    elif option == "5":
        top_5_news()
    elif option == "6":
        top_5_categories()
    elif option == "7":
        print('Encerrando script')
    else:
        print("Opção inválida", file=sys.stderr)


if __name__ == "__main__":
    analyzer_menu()

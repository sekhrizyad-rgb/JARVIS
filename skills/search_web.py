import webbrowser
from urllib.parse import quote_plus


def search_web(query):
    query_encodee = quote_plus(query)
    url = f"https://www.google.com/search?q={query_encodee}"
    webbrowser.open(url)
    return f"Recherche lancée : {query}"

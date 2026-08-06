
from services.scraper import get_page


TECHCRUNCH_URL = "https://techcrunch.com/category/startups/"


def collect_funding_news(state):

    soup = get_page(TECHCRUNCH_URL)

    articles = []

    for article in soup.find_all("article"):

        title = article.get_text(" ", strip=True)

        link = article.find("a")

        if not link:
            continue

        href = link.get("href")

        articles.append(
            {
                "title": title,
                "url": href
            }
        )

    state["articles"] = articles

    return state
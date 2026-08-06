from sources.entrackr import get_articles as entrackr_articles
from sources.inc42 import get_articles as inc42_articles


def collect_funding_news(state):

    articles = []

    print("\nCollecting Entrackr...")
    articles.extend(entrackr_articles())

    print("\nCollecting Inc42...")
    articles.extend(inc42_articles())

    # Remove duplicate articles
    seen_titles = set()
    unique_articles = []

    for article in articles:

        title = article["title"].strip().lower()

        if title in seen_titles:
            continue

        seen_titles.add(title)
        unique_articles.append(article)

    print("\n" + "=" * 100)
    print("TOTAL ARTICLES:", len(unique_articles))
    print("=" * 100)

    state["articles"] = unique_articles

    return state
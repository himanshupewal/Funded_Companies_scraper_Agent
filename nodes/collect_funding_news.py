from sources.entrackr import get_articles as entrackr_articles
from sources.inc42 import get_articles as inc42_articles


def collect_funding_news(state):

    articles = []

    # -------------------------
    # Entrackr
    # -------------------------
    try:
        print("\nCollecting Entrackr...")
        entrackr = entrackr_articles()
        articles.extend(entrackr)
        print(f"✓ Entrackr: {len(entrackr)} articles")
    except Exception as e:
        print(f"❌ Entrackr failed: {e}")

    # -------------------------
    # Inc42
    # -------------------------
    try:
        print("\nCollecting Inc42...")
        inc42 = inc42_articles()
        articles.extend(inc42)
        print(f"✓ Inc42: {len(inc42)} articles")
    except Exception as e:
        print(f"❌ Inc42 failed: {e}")

    # -------------------------
    # Remove duplicate articles
    # -------------------------
    seen_titles = set()
    unique_articles = []

    for article in articles:

        title = article["title"].strip().lower()

        if title not in seen_titles:
            seen_titles.add(title)
            unique_articles.append(article)

    print("\n" + "=" * 100)
    print("TOTAL ARTICLES:", len(unique_articles))
    print("=" * 100)

    state["articles"] = unique_articles

    return state
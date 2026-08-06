from urllib.parse import urljoin
import re

from services.scraper import get_soup


BASE_URL = "https://inc42.com"
URL = "https://inc42.com/buzz/"

FUNDING_KEYWORDS = [
    "raises",
    "raised",
    "funding",
    "funded",
    "investment",
    "invests",
    "seed",
    "series",
]


def get_articles():

    soup = get_soup(URL)

    articles = []
    seen = set()

    # ----------------------------
    # Collect funding article links
    # ----------------------------

    links = []

    for a in soup.select(".entry-title a"):

        href = a.get("href")

        title = a.get_text(" ", strip=True).lower()

        if not href:
            continue

        if any(keyword in title for keyword in FUNDING_KEYWORDS):
            links.append(href)

    print(f"Found {len(links)} funding articles from Inc42")

    # Keep latest 5
    links = links[:5]

    # ----------------------------
    # Visit each article
    # ----------------------------

    for href in links:

        full_url = urljoin(BASE_URL, href)

        if full_url in seen:
            continue

        seen.add(full_url)

        print("=" * 80)
        print(full_url)

        try:

            article_soup = get_soup(full_url)

            html = str(article_soup)

            published = ""

            patterns = [
                r'"datePublished":"([^"]+)"',
                r'"dateModified":"([^"]+)"',
            ]

            for pattern in patterns:

                match = re.search(pattern, html)

                if match:
                    published = match.group(1)
                    break

            paragraphs = article_soup.find_all("p")

            print("Paragraphs:", len(paragraphs))

            if len(paragraphs) < 5:
                continue


            content = "\n".join(
                p.get_text(" ", strip=True)
                for p in paragraphs
            )

            articles.append(
                {
                    "title": article_soup.title.get_text(strip=True),
                    "url": full_url,
                    "published": published,
                    "content": content,
                    "source": "Inc42",
                }
            )

            print("Added ✅")

        except Exception as e:

            print("ERROR:", e)

    print("\n" + "=" * 80)
    print("INC42 ARTICLES:", len(articles))
    print("=" * 80)

    return articles
from urllib.parse import urljoin
import re

from services.scraper import get_soup


BASE_URL = "https://entrackr.com"
URL = "https://entrackr.com/report/weekly-funding-report"


def get_articles():

    soup = get_soup(URL)

    articles = []
    seen = set()

    links = []

    for link in soup.find_all("a", href=True):

        href = link["href"]

        if "/report/weekly-funding-report/" in href:
            links.append(link)

    links = links[:1]

    for link in links:

        full_url = urljoin(BASE_URL, link["href"])

        if full_url in seen:
            continue

        seen.add(full_url)

        article_soup = get_soup(full_url)

        html = str(article_soup)

        match = re.search(
            r'postFirstPublishedAt="([^"]+)"',
            html
        )

        published = match.group(1) if match else ""

        paragraphs = article_soup.find_all("p")

        content = "\n".join(
            p.get_text(" ", strip=True)
            for p in paragraphs
        )

        articles.append(
            {
                "title": link.get_text(strip=True),
                "url": full_url,
                "published": published,
                "content": content,
                "source": "Entrackr",
            }
        )

    return articles
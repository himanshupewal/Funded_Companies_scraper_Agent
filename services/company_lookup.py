from ddgs import DDGS
from urllib.parse import urlparse

from services.company_enrichment import enrich_company


BLOCKED_DOMAINS = [
    "linkedin.com",
    "facebook.com",
    "instagram.com",
    "twitter.com",
    "x.com",
    "youtube.com",
    "wikipedia.org",
    "booking.com",
    "tripadvisor",
    "google.com",
    "translate.google",
    "play.google",
    "apps.apple.com",
    "amazon.",
    "flipkart.",
    "crunchbase.com",
    "tracxn.com",
    ".gov",
    ".go.",
]


def get_company_info(company_name: str) -> dict:

    query = f'"{company_name}" official website India'

    try:

        with DDGS() as ddgs:

            results = list(
                ddgs.text(
                    query,
                    max_results=10,
                )
            )

        company = (
            company_name.lower()
            .replace(" ", "")
            .replace("-", "")
        )

        best_url = ""
        best_score = -1

        for result in results:

            url = result["href"]
            domain = urlparse(url).netloc.lower()

            # Skip unwanted domains
            if any(x in domain for x in BLOCKED_DOMAINS):
                continue

            score = 0

            clean_domain = (
                domain.replace("www.", "")
                .replace(".com", "")
                .replace(".in", "")
                .replace(".ai", "")
                .replace(".co", "")
                .replace(".io", "")
                .replace("-", "")
            )

            # Company name appears in domain
            if company in clean_domain:
                score += 10

            title = result.get("title", "").lower()

            if "official" in title:
                score += 3

            if url.startswith("https"):
                score += 1

            if score > best_score:
                best_score = score
                best_url = url

        print(f"{company_name} -> {best_url}")

        info = {
            "industry": "",
            "headquarters": "",
            "company_website": best_url,
            "careers_page": "",
        }

        if best_url:

            enrichment = enrich_company(best_url)

            return {
            "company_website": best_url,
            "industry": enrichment["industry"],
            "headquarters": enrichment["headquarters"],
            "careers_page": enrichment["careers_page"],
        }
    except Exception as e:

        print(e)

        return {
            "industry": "",
            "headquarters": "",
            "company_website": "",
            "careers_page": "",
        }
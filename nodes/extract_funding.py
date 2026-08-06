import time
from datetime import datetime

from models.funding import FundingCompany
from prompts.funding_prompt import PROMPT
from services.llm import structured_llm


def extract_funding(state):

    companies = []

    for article in state["articles"]:

        announcement_date = datetime.fromisoformat(
            article["published"]
        ).date()

        # Keep only funding-related paragraphs
        paragraphs = article["content"].split("\n")

        funding_text = "\n".join(
            p for p in paragraphs
            if any(
                keyword in p.lower()
                for keyword in [
                    "raised",
                    "secured",
                    "funding",
                    "series",
                    "seed",
                    "round",
                ]
            )
        )

        # Retry if Gemini is busy
        response = None

        for attempt in range(3):
            try:
                response = structured_llm.invoke(
                    PROMPT + "\n\n" + funding_text
                )
                break

            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(5)

        if response is None:
            print(f"❌ Skipping article: {article['title']}")
            continue

        print("=" * 80)
        print(article["title"])
        print(response)
        print("=" * 80)

        for item in response.companies:

            
                companies.append(
    FundingCompany(
        announcement_date=announcement_date,
        company=item.company,
        funding_amount=item.funding_amount,
        funding_round=item.funding_round,

        industry="",
        headquarters="",

        company_website="",
        careers_page="",

        source=article["source"],
        source_url=article["url"],
    )
)

    state["companies"] = companies

    print("\n" + "=" * 80)
    print(f"TOTAL COMPANIES: {len(companies)}")
    print("=" * 80)

    return state
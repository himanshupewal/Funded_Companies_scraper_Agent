from datetime import datetime

from models.funding import FundingCompany
from services.parser import extract_companies

def process_data(state):

    companies = []

    for article in state["articles"]:

        announcement_date = datetime.fromisoformat(
            article["published"]
        ).date()

        extracted = extract_companies(
            article["content"]
        )

        print("=" * 80)
        print(f"Found {len(extracted)} companies")
        print("=" * 80)

        for item in extracted:

            print(item)

            companies.append(
                FundingCompany(
                    announcement_date=announcement_date,
                    company=item.get("company", "Unknown"),
                    funding_amount=item.get("amount") or "Unknown",
                    funding_round=item.get("round", "Unknown"),
                    source="Entrackr",
                    source_url=article["url"],
                )
            )

    state["companies"] = companies

    return state
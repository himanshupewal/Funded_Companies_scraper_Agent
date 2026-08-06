from typing import TypedDict
from models.funding import FundingCompany


class FundingState(TypedDict):
    start_date: str
    end_date: str
    articles: list[dict]
    companies: list[FundingCompany]
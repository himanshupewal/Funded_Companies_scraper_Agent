from datetime import date
from pydantic import BaseModel
from datetime import date
from pydantic import BaseModel


class FundingCompany(BaseModel):
    announcement_date: date

    company: str
    funding_amount: str
    funding_round: str

    industry: str = ""
    headquarters: str = ""

    company_website: str = ""
    careers_page: str = ""

    source: str
    source_url: str

class ExtractedFunding(BaseModel):
    company: str
    funding_amount: str
    funding_round: str


class ExtractFundingResponse(BaseModel):
    companies: list[ExtractedFunding]
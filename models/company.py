from pydantic import BaseModel


class CompanyInfo(BaseModel):

    industry: str = ""

    headquarters: str = ""

    careers_page: str = ""
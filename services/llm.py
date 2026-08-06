import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from models.funding import ExtractFundingResponse
from models.company import CompanyInfo

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0,
)

# Funding extraction
structured_llm = llm.with_structured_output(
    ExtractFundingResponse
)

# Company enrichment
company_llm = llm.with_structured_output(
    CompanyInfo
)

# General Gemini
article_filter_llm = llm
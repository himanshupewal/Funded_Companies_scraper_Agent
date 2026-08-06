from langgraph.graph import StateGraph, START, END

from state import FundingState

from nodes.generate_dates import generate_dates
from nodes.collect_funding_news import collect_funding_news
from nodes.extract_funding import extract_funding
from nodes.find_company_website import find_company_website
from nodes.update_google_sheet import update_google_sheet


# Create Graph
builder = StateGraph(FundingState)

# Add Nodes
builder.add_node("generate_dates", generate_dates)
builder.add_node("collect_funding_news", collect_funding_news)
builder.add_node("extract_funding", extract_funding)
builder.add_node("find_company_website", find_company_website)
builder.add_node("update_google_sheet", update_google_sheet)

# Define Flow
builder.add_edge(START, "generate_dates")
builder.add_edge("generate_dates", "collect_funding_news")
builder.add_edge("collect_funding_news", "extract_funding")
builder.add_edge("extract_funding", "find_company_website")
builder.add_edge("find_company_website", "update_google_sheet")
builder.add_edge("update_google_sheet", END)

# Compile Graph
graph = builder.compile()
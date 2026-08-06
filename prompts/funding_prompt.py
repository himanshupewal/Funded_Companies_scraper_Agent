PROMPT = """
You are an expert at extracting startup funding information.

Extract every company that raised funding.

For each company return:
- company
- funding_amount
- funding_round

Rules:
- Ignore weekly summaries.
- Ignore acquisitions.
- Ignore layoffs.
- Ignore IPOs.
- Ignore investors unless they are the funded company.
- Return every funding event separately.
"""
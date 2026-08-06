from services.google_sheet import append_rows

def update_google_sheet(state):

    rows = []

    for company in state["companies"]:
      rows.append([
    str(company.announcement_date),
    company.company,
    company.funding_amount,
    company.funding_round,
    company.industry,
    company.headquarters,
    company.company_website,
    company.careers_page,
    company.source,
])
    append_rows(rows)

    print(f"✅ Uploaded {len(rows)} companies to Google Sheets")

    return state
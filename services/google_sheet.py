import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]

creds = Credentials.from_service_account_file(
    "credentials/service_account.json",
    scopes=SCOPES,
)

client = gspread.authorize(creds)

sheet = client.open_by_url(
    "https://docs.google.com/spreadsheets/d/1nOBpGcSUM8VUVftH6EYt7AOzwgLcvDRzBqwGhV0UODA/edit?usp=sharing"
).sheet1


def append_rows(rows):

    headers = [
    "Announcement Date",
    "Company",
    "Funding Amount",
    "Funding Round",
    "Industry",
    "Headquarters",
    "Company Website",
    "Careers Page",
    "Source",
]

    # Add header if sheet is empty
    if not sheet.get_all_values():
        sheet.append_row(headers)

    # Existing rows
    existing_rows = sheet.get_all_values()

    # Create a set of (date, company)
    existing = {
        (row[0], row[1])
        for row in existing_rows[1:]   # Skip header
        if len(row) >= 2
    }

    new_rows = []

    for row in rows:

        key = (row[0], row[1])

        if key not in existing:
            new_rows.append(row)

    if new_rows:
        sheet.append_rows(new_rows)
        print(f"Uploaded {len(new_rows)} new rows")
    else:
        print("No new companies found")
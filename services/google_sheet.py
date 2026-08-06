import os
import json

import gspread
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials

load_dotenv()

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]

# ===============================
# Google Credentials
# ===============================

service_account_json = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")

if service_account_json:
    # Railway
    creds = Credentials.from_service_account_info(
        json.loads(service_account_json),
        scopes=SCOPES,
    )
else:
    # Local
    creds = Credentials.from_service_account_file(
        "credentials/service_account.json",
        scopes=SCOPES,
    )

client = gspread.authorize(creds)

# ===============================
# Google Sheet
# ===============================

sheet_url = os.getenv(
    "GOOGLE_SHEET_URL",
    "https://docs.google.com/spreadsheets/d/1nOBpGcSUM8VUVftH6EYt7AOzwgLcvDRzBqwGhV0UODA/edit?usp=sharing"
)

sheet = client.open_by_url(sheet_url).sheet1


def append_rows(rows):
    if rows:
        sheet.append_rows(rows)
        print(f"✅ Uploaded {len(rows)} rows")
    else:
        print("✅ No rows to upload")
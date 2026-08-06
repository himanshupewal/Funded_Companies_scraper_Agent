
from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()

@dataclass(frozen=True)
class Settings:
    google_sheet_name: str = os.getenv("GOOGLE_SHEET_NAME", "")
    google_service_account: str = os.getenv(
        "GOOGLE_SERVICE_ACCOUNT",
        "credentials/service_account.json",
    )

settings = Settings()
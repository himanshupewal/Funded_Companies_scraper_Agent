
from datetime import timedelta,date
from state import FundingState

def generate_dates(state: FundingState):
    today = date.today()
    current_monday = today - timedelta(days=today.weekday())
    previous_monday = current_monday - timedelta(days=7)
    previous_sunday = current_monday - timedelta(days=1)
    state["start_date"] = previous_monday.isoformat()
    state["end_date"] = previous_sunday.isoformat()
    return state
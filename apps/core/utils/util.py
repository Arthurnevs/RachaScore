from datetime import datetime

import pytz

TIME_ZONE = "America/Sao_Paulo"

def normalize_email(email: str) -> str:
    return email.strip().lower()

def now_datetime():
    return datetime.now(pytz.timezone(TIME_ZONE))

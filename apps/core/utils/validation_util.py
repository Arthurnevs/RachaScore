from apps.core.errors.user_errors import Error
from email_validator import validate_email, EmailNotValidError


def validate_payload_required_fields(payload: dict, required_fields):
    return [message for field, message in required_fields.items() if not payload.get(field)]


def validate_password(password: str, confirmation_password: str):
    errors = []
    if len(password) < 8:
        errors.append(Error.PASSWORD_TOO_SHORT)

    if password != confirmation_password:
        errors.append(Error.PASSWORD_CONFIRMATION_MISMATCH)

    return errors

def is_valid_email(email: str):
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False

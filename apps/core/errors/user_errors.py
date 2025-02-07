# user_errors.py

class Error:
    REQUIRED_FIELD_NAME = 'required.field.name'
    REQUIRED_FIELD_EMAIL = 'required.field.email'
    REQUIRED_FIELD_PASSWORD = 'required.field.password'
    REQUIRED_FIELD_CONFIRMATION_PASSWORD = 'required.field.confirmation.password'

    PASSWORD_TOO_SHORT = "password.too.short"
    PASSWORD_CONFIRMATION_MISMATCH = "password.confirmation.mismatch"

    INVALID_FIELD_EMAIL = "invalid.field.email"

    EMAIL_IS_ALREADY_IN_USE = "email.already_in_use"
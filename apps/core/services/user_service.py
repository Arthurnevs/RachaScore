from django.core.exceptions import ValidationError, BadRequest
from apps.core.errors.user_errors import Error
from apps.core.repositories.user_repository import get_user_by_email
from apps.core.serializers.user_serializers import UserRegisterSerializer, UserBasicFieldsSerializer
from apps.core.utils.bcrypt_util import hash_password
from apps.core.utils.validation_util import validate_payload_required_fields, is_valid_email, validate_password


def register_user(user_data: dict) -> dict:
    errors = validate_user_register(user_data)
    if errors:
        raise ValidationError(errors)

    raw_password = user_data.get('password')
    password = hash_password(raw_password)
    user_data.update({'password': password})

    user_serializer = UserRegisterSerializer(data=user_data)
    if user_serializer.is_valid() and user_serializer.save():
        return UserBasicFieldsSerializer(instance=user_serializer.instance).data

    raise BadRequest(user_serializer.errors)


def validate_user_register(user_data: dict) -> list:
    errors = validate_user_required_fields(user_data)
    if errors:
        return errors

    return validate_user_registration_fields(user_data)


def validate_user_required_fields(user_data: dict) -> list:
    required_fields = {
        "name": Error.REQUIRED_FIELD_NAME,
        "email": Error.REQUIRED_FIELD_EMAIL,
        "password": Error.REQUIRED_FIELD_PASSWORD,
        "confirmation_password": Error.REQUIRED_FIELD_CONFIRMATION_PASSWORD,
    }

    return validate_payload_required_fields(required_fields, user_data)

def validate_user_registration_fields(user_data: dict) -> list:
    errors = []

    email = user_data.get("email", "")
    if not is_valid_email(email):
        errors.append(Error.INVALID_FIELD_EMAIL)

    password, confirmation_password = user_data.get("password", ""), user_data.get("confirmation_password", "")
    errors_password = validate_password(password, confirmation_password)

    return errors_password + errors

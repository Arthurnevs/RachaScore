from datetime import timedelta

import jwt
from rest_framework.exceptions import NotFound, AuthenticationFailed

from apps.core.repositories.user_repository import get_user_by_email
from apps.core.utils.bcrypt_util import verify_password
from apps.core.utils.util import now_datetime


def make_login(auth_data):
    email, password = auth_data.get('email'), auth_data.get('password')

    user = get_user_by_email(email.lower())
    if not user:
        raise NotFound()

    if not verify_password(password, user.password):
        raise AuthenticationFailed()

    token = generate_access_token(user)

SECRET_KEY = "SECRET_KEY"

def generate_access_token(user) -> str:
    payload = {
        "user_id": user.id,
        "exp": now_datetime() + timedelta(hours=2),
    }

    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")




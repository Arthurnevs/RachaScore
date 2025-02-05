import bcrypt


def hash_password(password: str) -> str:
    BCRYPT_DEFAULT_SALT = 8
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(BCRYPT_DEFAULT_SALT))
    return hashed_password.decode('utf-8')

def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

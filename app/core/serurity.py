from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated='auto'
)

def create_hash(password: str) -> str:
    hashed = pwd_context.hash(password)
    return hashed

def verify_hash(hashed_password: str, password: str) -> bool:
    return pwd_context.verify(password, hashed_password)

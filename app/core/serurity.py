from passlib.context import CryptContext
import hashlib

pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated='auto'
)

def create_hash(password: str) -> str:
    hashed = pwd_context.hash(password)
    return hashed

def verify_hash(hashed_password: str, password: str) -> bool:
    return pwd_context.verify(password, hashed_password)

def create_lookup(token: str) -> str:
    hashed = hashlib.sha256(token.encode()).hexdigest()
    return hashed

from passlib.context import CryptContext
import hashlib
import string
import secrets

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

def create_activate_code() -> str:
     alphabet = string.ascii_letters + string.digits

     part1 = "".join(secrets.choice(alphabet) for _ in range(4))
     part2 = "".join(secrets.choice(alphabet) for _ in range(4))

     return f"{part1}-{part2}"


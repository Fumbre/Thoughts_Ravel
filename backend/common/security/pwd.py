from passlib.context import CryptContext

# Tell passlib to use argon2 instead of bcrypt
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str) -> str:
    """Hashes a plain text password using Argon2."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a plain text password against the Argon2 hash."""
    return pwd_context.verify(plain_password, hashed_password)
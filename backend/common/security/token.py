from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError

from threading import Lock

ALGORITHM = "HS256"

class Token:
    _instance = None
    _lock = Lock()
    _secret_key = None

    @classmethod
    def init(cls, secret_key: str):
        if cls._instance is None:
            with cls._lock:
                cls._instance = super().__new__(cls)
                cls._secret_key = secret_key

        return cls._instance

    @classmethod
    def create_access_token(cls, data: dict) -> str:
        """Generates a JWT token containing the payload data."""
        to_encode = data.copy()
        
        
        # Encode and return the JWT
        encoded_jwt = jwt.encode(to_encode, cls._secret_key, algorithm=ALGORITHM)
        return encoded_jwt

    @classmethod
    def verify_access_token(cls, token: str) -> dict | None:
        """Decodes and validates a JWT token."""
        try:
            payload = jwt.decode(token, cls._secret_key, algorithms=[ALGORITHM])
            return payload  # This will contain your user data (e.g., {"sub": "username"})
        except JWTError:
            return None  # Token is invalid or expired
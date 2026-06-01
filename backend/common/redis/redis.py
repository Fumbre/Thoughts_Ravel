from threading import Lock
from redis import asyncio as aioredis

class Redis:
    _instance = None
    _lock = Lock()

    @classmethod
    def init(cls, ip: str, port: int, db: int, password: str):
        if cls._instance is None:
            with cls._lock:
                path = f"redis://:{password}@{ip}:{port}/{db}"
                cls._instance = aioredis.from_url(path)

        return cls._instance
    
    @classmethod
    def _get_client(cls) -> aioredis.Redis:
        """Internal safety check to make sure init was called first."""
        if cls._instance is None:
            raise RuntimeError("Redis has not been initialized. Call Redis.init(...) first.")
        return cls._instance

    @classmethod
    async def add(cls, key: str, value: str, expire_seconds: int | None = None) -> bool:
        """Sets a string value in cache. Optionally handles expiration timeouts."""
        client = cls._get_client()
        return await client.set(key, value, ex=expire_seconds)

    @classmethod
    async def get(cls, key: str) -> str | None:
        """Retrieves a string value from cache by its key."""
        client = cls._get_client()
        return await client.get(key)

    @classmethod
    async def remove(cls, *keys: str) -> int:
        """Deletes one or multiple keys from the database."""
        client = cls._get_client()
        return await client.delete(*keys)
        
    @classmethod
    async def close(cls):
        """Closes connection pools gracefully on system shutdown."""
        if cls._instance is not None:
            await cls._instance.close()
            cls._instance = None
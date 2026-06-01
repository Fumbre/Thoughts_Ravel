from threading import Lock
from redis import asyncio as aioredis

class Redis:
    _instance = None
    _lock = Lock()

    @classmethod
    def init(cls):
        if cls._instance is None:
            with cls._lock:
                cls._instance = aioredis.

        return cls._instance
    



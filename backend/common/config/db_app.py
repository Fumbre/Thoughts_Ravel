from contextlib import asynccontextmanager
from fastapi import FastAPI
from common.db.session import DB
from dotenv import load_dotenv
import os

from common.security.token import Token
from common.redis.redis import Redis

load_dotenv()
DB_DRIVER = os.getenv("DB_DRIVER", "")
DB_IP = os.getenv("DB_IP", "")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_NAME = os.getenv("DB_NAME", "")
DB_USER = os.getenv("DB_USER", "")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_LOG = bool(os.getenv("DB_LOG", "False"))

TOKEN = os.getenv("TOKEN", "")

REDIS_IP = os.getenv("REDIS_IP", "")
REDIS_PORT = os.getenv("REDIS_PORT", "")
REDIS_DB = os.getenv("REDIS_DB", "")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "")


@asynccontextmanager
async def lifespan(db: FastAPI):
    DB.init(DB_DRIVER, DB_IP, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD, '', DB_LOG)
    Token.init(TOKEN)
    Redis.init(REDIS_IP, REDIS_PORT, REDIS_DB, REDIS_PASSWORD)
    yield
    Redis.close()
    DB.close()

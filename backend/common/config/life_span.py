from contextlib import asynccontextmanager
from fastapi import FastAPI
from common.db.session import DB
from dotenv import load_dotenv
import os

from common.security.token import Token
from common.redis.redis import Redis
from ai_agent.ai_agent import AiAgent
from ai_agent.tools import get_nodes

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
    AiAgent.init('qwen3:8b', [get_nodes], 0.1)
    yield
    await Redis.close()
    await DB.close()

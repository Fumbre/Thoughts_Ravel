from functools import wraps
from common.db.session import DB

def Transactional(func:callable):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        # get async session
        async for db in DB.get_session():
            try:
                kwargs["db"] = db
                result = await func(*args,**kwargs)
                await db.commit()
                return result
            except Exception as e:
                await db.rollback()
                raise e
    return wrapper
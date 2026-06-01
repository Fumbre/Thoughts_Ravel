from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BigInteger, String, FLOAT, CHAR

class Base(DeclarativeBase):
    # abstract class for every table
    # example: if I add in future to all of my tables "created_at" I can do it here
    pass

from common.db.base_model import Base, Mapped, mapped_column, BigInteger, String, CHAR
from common.id.snowflake_id_util import getId

class User(Base):
    __tablename__ = "users"

    id:Mapped[int] = mapped_column("id", BigInteger, nullable=False, primary_key=True, default=getId)
    email:Mapped[str] = mapped_column("email", String, nullable=False)
    username:Mapped[str] = mapped_column("username", String, nullable=False)
    password:Mapped[str] = mapped_column("password", String, nullable=False)
    status:Mapped[str] = mapped_column("status", CHAR, nullable=False, default=0)

from common.db.base_model import Base, Mapped, mapped_column, BigInteger, String, FLOAT
from common.id.snowflake_id_util import getId

class Space(Base):
    __tablename__ = "spaces"

    id:Mapped[int] = mapped_column("id", BigInteger, nullable=False, primary_key=True, default=getId)
    userId:Mapped[int] = mapped_column("userId", BigInteger, nullable=False)
    title:Mapped[str] = mapped_column("title", String, nullable=False)
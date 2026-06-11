from datetime import datetime
from common.db.base_model import Base, Mapped, mapped_column, BigInteger, String, FLOAT

class NodeCorrelations(Base):
    __tablename__ = "node_correlations"

    parent_node_id: Mapped[int] = mapped_column(
        "parent_node_id", 
        BigInteger, 
        primary_key=True,
        nullable=False, 
    )
    

    destination_node_id: Mapped[int] = mapped_column(
        "destination_node_id", 
        BigInteger, 
        primary_key=True,
        nullable=False, 
    )

    name: Mapped[str] = mapped_column(
        "name", 
        String(255), 
        nullable=False, 
    )
from common.db.base_model import Base, Mapped, mapped_column, BigInteger, String, FLOAT
from common.id.snowflake_id_util import getId
from sqlalchemy import PrimaryKeyConstraint

class Node(Base):
    __tablename__ = "nodes"

    id:Mapped[int] = mapped_column("id", BigInteger, nullable=False, primary_key=True, default=getId)
    name:Mapped[str] = mapped_column("name", String, nullable=False)
    desc:Mapped[str] = mapped_column("desc", String, nullable=True)
    positionX:Mapped[float] = mapped_column("positionX", FLOAT, nullable=False)
    positionY:Mapped[float] = mapped_column("positionY", FLOAT, nullable=False)
    color:Mapped[str] = mapped_column("color", String, nullable=False)
    shape:Mapped[str] = mapped_column("shape", String, nullable=False)


# class InsideNodes(Base):
#     __tablename__ = "inside_nodes"
#     id:Mapped[int] = mapped_column("id", nullable=False, primary_key=True, default=getId)


class NodesRelations(Base):
    __tablename__ = "nodes_relations"

    parentId:Mapped[int] = mapped_column("parentId", BigInteger, nullable=False)
    nodeId:Mapped[int] = mapped_column("nodeId", BigInteger, nullable=False)
    spaceId:Mapped[int] = mapped_column("spaceId", BigInteger, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('parentId', 'nodeId', 'spaceId'),
    )
    

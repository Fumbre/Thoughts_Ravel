from datetime import datetime
from common.db.base_model import Base, Mapped, mapped_column, BigInteger, String
from common.id.snowflake_id_util import getId
from sqlalchemy import Text, Integer, CHAR, DateTime, text

class Nodes(Base):
    __tablename__ = "nodes"

    # Primary Key
    id: Mapped[int] = mapped_column(
        "id", 
        BigInteger, 
        primary_key=True, 
        nullable=False, 
        default=getId, 
        comment="id of the node"
    )
    
    # Core Attributes
    name: Mapped[str] = mapped_column(
        "name", 
        String(255), 
        nullable=False, 
        comment="name of node"
    )
    parent_id: Mapped[int] = mapped_column(
        "parent_id", 
        BigInteger, 
        nullable=False, 
        comment="0 for root, parent_id is where nodes are stored"
    )
    ancestor: Mapped[str] = mapped_column(
        "ancestor", 
        Text, 
        nullable=False, 
        comment="the full length of all ancestors like (0,1,2,3,4) for node id 5"
    )
    description: Mapped[str] = mapped_column(
        "description", 
        String(255), 
        nullable=True, 
        server_default=text("NULL"), 
        comment="node description like h1 tag"
    )
    type: Mapped[str] = mapped_column(
        "type", 
        CHAR(1), 
        nullable=False, 
        comment="0 - node, 1 - space (node of nodes), 2 - show the content, 3 - make the node executable (if music is inside after click - play music)"
    )
    
    # Spatial Positioning
    position_x: Mapped[int] = mapped_column(
        "position_x", 
        Integer, 
        nullable=False, 
        comment="position X of node"
    )
    position_y: Mapped[int] = mapped_column(
        "position_y", 
        Integer, 
        nullable=False, 
        comment="position Y of node"
    )
    
    # Audit & Customization
    creater_id: Mapped[int] = mapped_column(
        "creater_id", 
        BigInteger, 
        nullable=False, 
        comment="the user_id who created a node"
    )
    shape: Mapped[str] = mapped_column(
        "shape", 
        String(255), 
        nullable=False, 
        comment="shape of a node"
    )
    color: Mapped[str] = mapped_column(
        "color", 
        String(255), 
        nullable=False, 
        comment="color of a node"
    )
    
    # Timestamps
    created_time: Mapped[datetime] = mapped_column(
        "created_time", 
        DateTime, 
        nullable=False, 
        server_default=text("CURRENT_TIMESTAMP"), 
        comment="time when it was created"
    )
    updated_time: Mapped[datetime] = mapped_column(
        "updated_time", 
        DateTime, 
        nullable=False, 
        server_default=text("CURRENT_TIMESTAMP"), 
        onupdate=datetime.now, 
        comment="Update time"
    )


# class InsideNodes(Base):
#     __tablename__ = "inside_nodes"
#     id:Mapped[int] = mapped_column("id", nullable=False, primary_key=True, default=getId)


# class NodesRelations(Base):
#     __tablename__ = "nodes_relations"

#     parentId:Mapped[int] = mapped_column("parentId", BigInteger, nullable=False)
#     nodeId:Mapped[int] = mapped_column("nodeId", BigInteger, nullable=False)
#     spaceId:Mapped[int] = mapped_column("spaceId", BigInteger, nullable=False)
#     userId:Mapped[int] = mapped_column("userId", BigInteger, nullable=False)
#     public_status:Mapped[str] = mapped_column("public_status", String(1), nullable=False)

#     __table_args__ = (
#         PrimaryKeyConstraint('parentId', 'nodeId', 'spaceId', 'userId'),
#     )
    

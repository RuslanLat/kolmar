from dataclasses import dataclass
from typing import Optional
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
)
from sqlalchemy.orm import relationship

from app.store.database.sqlalchemy_base import db


@dataclass
class Group:
    group_id: Optional[int]
    group: str


class GroupModel(db):
    __tablename__ = "groups"
    group_id = Column(Integer, primary_key=True)
    group = Column(String, unique=True)
    # user_boot = relationship("UserBotModel", back_populates="group")

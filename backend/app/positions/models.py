from dataclasses import dataclass
from typing import Optional
from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from app.store.database.sqlalchemy_base import db


@dataclass
class Position:
    position_id: Optional[int]
    position: str


class PositionModel(db):
    __tablename__ = "positions"
    position_id = Column(Integer, primary_key=True)
    position = Column(String, unique=True)
    user = relationship("UserModel", back_populates="position")
    # user_job = relationship("UserJobModel", back_populates="position")

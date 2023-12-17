from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from sqlalchemy.sql import func
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from app.store.database.sqlalchemy_base import db


@dataclass
class Rating:
    row_id: Optional[int]
    date: datetime
    user_id: int
    rating: int


class RatingModel(db):
    __tablename__ = "ratings"
    row_id = Column(Integer, primary_key=True)
    date = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"))
    rating = Column(Integer)
    user = relationship("UserModel", back_populates="rating")

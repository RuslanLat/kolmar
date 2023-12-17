from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from sqlalchemy.sql import func
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    ForeignKey,
    Boolean,
    Float,
)
from sqlalchemy.orm import relationship

from app.store.database.sqlalchemy_base import db


@dataclass
class Predict:
    row_id: Optional[int]
    date: datetime
    user_id: int
    dismiss: bool
    probability: float


class PredictModel(db):
    __tablename__ = "predicts"
    row_id = Column(Integer, primary_key=True)
    date = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"))
    dismiss = Column(Boolean)
    probability = Column(Float)
    user = relationship("UserModel", back_populates="predict")

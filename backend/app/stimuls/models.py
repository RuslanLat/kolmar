from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, ForeignKey, Boolean, String, Float, DateTime
from sqlalchemy.orm import relationship

from app.store.database.sqlalchemy_base import db


@dataclass
class Stimul:
    row_id: Optional[int]
    user_id: int
    date: datetime
    q1: str
    q2: str
    q3: str
    q4: str
    q5: str
    q6: str
    q7: str
    q8: str
    q9: str
    q10: str
    q11: str


class StimulModel(db):
    __tablename__ = "stimuls"
    row_id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"))
    date = Column(DateTime(timezone=True), server_default=func.now())
    q1 = Column(String)
    q2 = Column(String)
    q3 = Column(String)
    q4 = Column(String)
    q5 = Column(String)
    q6 = Column(String)
    q7 = Column(String)
    q8 = Column(String)
    q9 = Column(String)
    q10 = Column(String)
    q11 = Column(String)
    user = relationship("UserModel", back_populates="stimul")

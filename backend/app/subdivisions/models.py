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
class Subdivision:
    subdivision_id: Optional[int]
    subdivision: str
    email: str
    telegram_id: int


@dataclass
class SubdivisionBot:
    subdivision_id: Optional[int]
    telegram_id: int
    link: str


class SubdivisionModel(db):
    __tablename__ = "subdivisions"
    subdivision_id = Column(Integer, primary_key=True)
    subdivision = Column(String, unique=True)
    email = Column(String)
    telegram_id = Column(Integer)
    user = relationship("UserModel", back_populates="subdivision")
    subdivision_boot = relationship("SubdivisionBotModel", back_populates="subdivision")


class SubdivisionBotModel(db):
    __tablename__ = "subdivision_bots"
    id = Column(Integer, primary_key=True)
    subdivision_id = Column(ForeignKey("subdivisions.subdivision_id", ondelete="CASCADE"))
    telegram_id = Column(Integer)
    link = Column(String, default="")
    subdivision = relationship(SubdivisionModel, back_populates="subdivision_boot")

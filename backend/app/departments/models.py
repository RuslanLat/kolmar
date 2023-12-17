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
class Department:
    department_id: Optional[int]
    department: str
    email: str
    telegram_id: int


@dataclass
class DepartmentBot:
    department_id: Optional[int]
    telegram_id: int
    link: str


class DepartmentModel(db):
    __tablename__ = "departments"
    department_id = Column(Integer, primary_key=True)
    department = Column(String, unique=True)
    email = Column(String)
    telegram_id = Column(Integer)
    user = relationship("UserModel", back_populates="department")
    department_boot = relationship("DepartmentBotModel", back_populates="department")


class DepartmentBotModel(db):
    __tablename__ = "department_bots"
    id = Column(Integer, primary_key=True)
    department_id = Column(ForeignKey("departments.department_id", ondelete="CASCADE"))
    telegram_id = Column(Integer)
    link = Column(String, default="")
    department = relationship(DepartmentModel, back_populates="department_boot")

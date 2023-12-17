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
class Role:
    role_id: Optional[int]
    role: str


class RoleModel(db):
    __tablename__ = "roles"
    role_id = Column(Integer, primary_key=True)
    role = Column(String, unique=True)
    user = relationship("UserModel", back_populates="role")

from dataclasses import dataclass
from hashlib import sha256
from typing import Optional
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Boolean,
)
from sqlalchemy.orm import relationship

from app.store.database.sqlalchemy_base import db


@dataclass
class UserLogin:
    id: Optional[int]
    login: str
    password: Optional[str] = None

    def is_password_valid(self, password: str) -> bool:
        return self.password == sha256(password.encode()).hexdigest()

    @classmethod
    def from_session(cls, session: Optional[dict]) -> Optional["UserLogin"]:
        return cls(id=session["user"]["id"], login=session["user"]["login"])


@dataclass
class User:
    id: Optional[int]
    name: str
    lastname: str
    male: bool
    age: int
    experience: int
    is_view: bool
    department_id: int
    subdivision_id: int
    position_id: int
    role_id: int
    fired: bool
    email: str = None
    telegram_id: int = None
    
    
@dataclass
class UserBot:
    id: Optional[int]
    user_id: int
    is_view: bool


@dataclass
class UserFull:
    id: Optional[int]
    name: str
    lastname: str
    male: bool
    age: int
    experience: int
    is_view: bool
    department: str
    subdivision: str
    position: str
    role: str
    fired: bool
    email: str = None
    telegram_id: int = None


class UserLoginModel(db):
    __tablename__ = "user_logins"
    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True)
    password = Column(String)
    user = relationship("UserModel", back_populates="user_login")


class UserModel(db):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    user_login_id = Column(ForeignKey("user_logins.id", ondelete="CASCADE"))
    name = Column(String)
    lastname = Column(String)
    male = Column(Boolean)
    age = Column(Integer)
    experience = Column(Integer)
    is_view = Column(Boolean, default=False)
    email = Column(String)
    telegram_id = Column(Integer)
    department_id = Column(ForeignKey("departments.department_id", ondelete="CASCADE"))
    subdivision_id = Column(
        ForeignKey("subdivisions.subdivision_id", ondelete="CASCADE")
    )
    position_id = Column(ForeignKey("positions.position_id", ondelete="CASCADE"))
    role_id = Column(ForeignKey("roles.role_id", ondelete="CASCADE"))
    fired = Column(Boolean, default=False)
    user_login = relationship(UserLoginModel, back_populates="user")
    department = relationship("DepartmentModel", back_populates="user")
    position = relationship("PositionModel", back_populates="user")
    role = relationship("RoleModel", back_populates="user")
    email_list = relationship("EmailModel", back_populates="user")
    predict = relationship("PredictModel", back_populates="user")
    rating = relationship("RatingModel", back_populates="user")
    subdivision = relationship("SubdivisionModel", back_populates="user")
    user_bot = relationship("UserBotModel", back_populates="user")


class UserBotModel(db):
    __tablename__ = "user_bots"
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.id"))
    is_view = Column(Boolean, default=False)
    user = relationship(UserModel, back_populates="user_bot")

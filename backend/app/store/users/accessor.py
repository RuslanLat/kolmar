import typing
from typing import List, Optional
from hashlib import sha256
from sqlalchemy import select, update, and_, delete
from sqlalchemy.orm import joinedload

from app.users.models import (
    User,
    UserLogin,
    UserModel,
    UserLoginModel,
    UserBot,
    UserBotModel,
    UserFull,
)
from app.base.base_accessor import BaseAccessor

if typing.TYPE_CHECKING:
    from app.web.app import Application


class UserLoginAccessor(BaseAccessor):
    async def get_by_login(self, login: str) -> Optional[UserLogin]:
        async with self.app.database.session() as session:
            query = select(UserLoginModel).where(UserLoginModel.login == login)
            user: Optional[UserLoginModel] = await session.scalar(query)

        if not user:
            return None

        return UserLogin(id=user.id, login=user.login, password=user.password)

    async def create_user_login(self, login: str, password: str) -> Optional[UserLogin]:
        new_user: User = UserLoginModel(
            login=login, password=self.encode_password(password)
        )

        async with self.app.database.session.begin() as session:
            session.add(new_user)

        return UserLogin(
            id=new_user.id, login=new_user.login, password=new_user.password
        )

    async def update_user_login(self, login: str, password: str) -> Optional[UserLogin]:
        query = (
            update(UserLoginModel)
            .where(UserLoginModel.login == login)
            .values(password=self.encode_password(password))
            .returning(UserLoginModel)
        )

        async with self.app.database.session.begin() as session:
            user = await session.scalar(query)

        if not user:
            return None

        return UserLogin(id=user.id, login=user.login, password=user.password)

    async def delete_user_login(self, login: str) -> Optional[UserLogin]:
        query = (
            delete(UserLoginModel)
            .where(UserLoginModel.login == login)
            .returning(UserLoginModel)
        )

        async with self.app.database.session.begin() as session:
            user = await session.scalar(query)

        if not user:
            return None

        return UserLogin(id=user.id, login=user.login, password=user.password)

    async def list_user_logins(self) -> List[Optional[UserLogin]]:
        query = select(UserLoginModel)

        async with self.app.database.session() as session:
            users = await session.scalars(query)

        if not users:
            return []

        return [
            UserLogin(id=user.id, login=user.login, password=user.password)
            for user in users.all()
        ]

    def encode_password(self, password: str) -> str:
        return sha256(password.encode()).hexdigest()

    def copmare_passwords(self, existing_user: UserLogin, password: str) -> bool:
        return existing_user.password == self.encode_password(password)


class UserAccessor(BaseAccessor):
    async def get_by_id(self, id: int) -> Optional[User]:
        async with self.app.database.session() as session:
            query = select(UserModel).where(UserModel.id == id)
            user: Optional[UserModel] = await session.scalar(query)

        if not user:
            return None

        return User(
            id=user.id,
            name=user.name,
            lastname=user.lastname,
            male=user.male,
            age=user.age,
            experience=user.experience,
            is_view=user.is_view,
            department_id=user.department_id,
            subdivision_id=user.subdivision_id,
            position_id=user.position_id,
            role_id=user.role_id,
            email=user.email,
            telegram_id=user.telegram_id,
            fired=user.fired,
        )

    async def get_by_full_name(self, name: str, lastname: str) -> Optional[User]:
        async with self.app.database.session() as session:
            query = select(UserModel).where(
                and_(UserModel.name == name, UserModel.lastname == lastname)
            )
            user: Optional[UserModel] = await session.scalar(query)

        if not user:
            return None

        return User(
            id=user.id,
            name=user.name,
            lastname=user.lastname,
            male=user.male,
            age=user.age,
            experience=user.experience,
            is_view=user.is_view,
            department_id=user.department_id,
            subdivision_id=user.subdivision_id,
            position_id=user.position_id,
            role_id=user.role_id,
            email=user.email,
            telegram_id=user.telegram_id,
            fired=user.fired,
        )

    async def create_user(
        self,
        name: str,
        lastname: str,
        male: bool,
        age: int,
        experience: int,
        department_id: int,
        subdivision_id: int,
        position_id: int,
        role_id: int,
        email: str,
        telegram_id: int,
    ) -> Optional[User]:
        new_user: UserModel = UserModel(
            name=name,
            lastname=lastname,
            male=male,
            age=age,
            experience=experience,
            department_id=department_id,
            subdivision_id=subdivision_id,
            position_id=position_id,
            role_id=role_id,
            email=email,
            telegram_id=telegram_id,
        )

        async with self.app.database.session.begin() as session:
            session.add(new_user)

        return User(
            id=new_user.id,
            name=new_user.name,
            lastname=new_user.lastname,
            male=new_user.male,
            age=new_user.age,
            is_view=new_user.is_view,
            experience=new_user.experience,
            department_id=new_user.department_id,
            subdivision_id=new_user.subdivision_id,
            position_id=new_user.position_id,
            role_id=new_user.role_id,
            email=new_user.email,
            telegram_id=new_user.telegram_id,
            fired=new_user.fired,
        )

    async def create_insert_user(
        self,
        id: int,
        name: str,
        lastname: str,
        male: bool,
        age: int,
        experience: int,
    ) -> Optional[User]:
        new_user: UserModel = UserModel(
            id=id,
            name=name,
            lastname=lastname,
            male=male,
            age=age,
            experience=experience,
        )
        async with self.app.database.session.begin() as session:
            session.add(new_user)

        return User(
            id=new_user.id,
            name=new_user.name,
            lastname=new_user.lastname,
            male=new_user.male,
            age=new_user.age,
            is_view=new_user.is_view,
            experience=new_user.experience,
            department_id=new_user.department_id,
            subdivision_id=new_user.subdivision_id,
            position_id=new_user.position_id,
            role_id=new_user.role_id,
            email=new_user.email,
            telegram_id=new_user.telegram_id,
            fired=new_user.fired,
        )

    async def create_boot_user(
        self,
        user_id: int,
    ) -> Optional[User]:
        new_user: UserBotModel = UserBotModel(
            id=user_id,
            user_id=user_id,
        )

        async with self.app.database.session.begin() as session:
            session.add(new_user)

        return UserBot(
            id=new_user.id,
            user_id=new_user.user_id,
            is_view=new_user.is_view,
        )

    async def update_user(self, id: int, is_view: bool) -> Optional[User]:
        query = (
            update(UserModel)
            .where(UserModel.id == id)
            .values(is_view=is_view)
            .returning(UserModel)
        )

        async with self.app.database.session.begin() as session:
            user: UserModel = await session.scalar(query)

        if not user:
            return None

        return User(
            id=user.id,
            name=user.name,
            lastname=user.lastname,
            male=user.male,
            age=user.age,
            is_view=user.is_view,
            experience=user.experience,
            department_id=user.department_id,
            subdivision_id=user.subdivision_id,
            position_id=user.position_id,
            role_id=user.role_id,
            email=user.email,
            telegram_id=user.telegram_id,
            fired=user.fired,
        )

    async def delete_user(self, name: str, lastname: str) -> Optional[User]:
        query = (
            delete(UserModel)
            .where(
                and_(
                    UserModel.name == name,
                    UserModel.lastname == lastname,
                )
            )
            .returning(UserModel)
        )

        async with self.app.database.session.begin() as session:
            user: UserModel = await session.scalar(query)

        if not user:
            return None

        return User(
            id=user.id,
            name=user.name,
            lastname=user.lastname,
            male=user.male,
            age=user.age,
            experience=user.experience,
            is_view=user.is_view,
            department_id=user.department_id,
            subdivision_id=user.subdivision_id,
            position_id=user.position_id,
            role_id=user.role_id,
            email=user.email,
            telegram_id=user.telegram_id,
            fired=user.fired,
        )

    async def list_user(self) -> List[Optional[User]]:
        query = select(UserModel)

        async with self.app.database.session() as session:
            users = await session.scalars(query)

        if not users:
            return []

        return [
            User(
                id=user.id,
                name=user.name,
                lastname=user.lastname,
                male=user.male,
                age=user.age,
                experience=user.experience,
                is_view=user.is_view,
                department_id=user.department_id,
                subdivision_id=user.subdivision_id,
                position_id=user.position_id,
                role_id=user.role_id,
                email=user.email,
                telegram_id=user.telegram_id,
                fired=user.fired,
            )
            for user in users.all()
        ]

    async def list_full_user(self) -> List[Optional[UserFull]]:
        query = (
            select(UserModel)
            .options(joinedload(UserModel.department))
            .options(joinedload(UserModel.subdivision))
            .options(joinedload(UserModel.position))
            .options(joinedload(UserModel.role))
        )

        async with self.app.database.session() as session:
            users = await session.scalars(query)

        if not users:
            return []

        return [
            UserFull(
                id=user.id,
                name=user.name,
                lastname=user.lastname,
                male=user.male,
                age=user.age,
                experience=user.experience,
                is_view=user.is_view,
                department=user.department.department,
                subdivision=user.subdivision.subdivision,
                position=user.position.position,
                role=user.role.role,
                email=user.email,
                telegram_id=user.telegram_id,
                fired=user.fired,
            )
            for user in users.all()
        ]

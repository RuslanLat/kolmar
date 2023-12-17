import typing
from typing import List, Optional
from sqlalchemy import select, update, delete

from app.roles.models import Role, RoleModel
from app.base.base_accessor import BaseAccessor


class RoleAccessor(BaseAccessor):
    async def get_by_role(self, role: str) -> Optional[Role]:
        async with self.app.database.session() as session:
            query = select(RoleModel).where(RoleModel.role == role)
            role: Optional[RoleModel] = await session.scalar(query)

        if not role:
            return None

        return Role(role_id=role.role_id, role=role.role)

    async def get_by_role_id(self, role_id: int) -> Optional[Role]:
        async with self.app.database.session() as session:
            query = select(RoleModel).where(RoleModel.role_id == role_id)
            role: Optional[RoleModel] = await session.scalar(query)

        if not role:
            return None

        return Role(role_id=role.role_id, role=role.role)

    async def create_role(self, role: str) -> Optional[Role]:
        new_role: RoleModel = RoleModel(role=role)

        async with self.app.database.session.begin() as session:
            session.add(new_role)

        return Role(role_id=new_role.role_id, role=new_role.role)

    async def update_role(self, role_id: int, role: str) -> Optional[Role]:
        query = (
            update(RoleModel)
            .where(RoleModel.role_id == role_id)
            .values(role=role)
            .returning(RoleModel)
        )

        async with self.app.database.session.begin() as session:
            role = await session.scalar(query)

        if not role:
            return None

        return Role(role_id=role.role_id, role=role.role)

    async def delete_role(self, role: str) -> Optional[Role]:
        query = delete(RoleModel).where(RoleModel.role == role).returning(RoleModel)

        async with self.app.database.session.begin() as session:
            role: RoleModel = await session.scalar(query)

        if not role:
            return None

        return Role(role_id=role.role_id, role=role.role)

    async def list_roles(self) -> List[Optional[Role]]:
        query = select(RoleModel)

        async with self.app.database.session() as session:
            roles: List[Optional[RoleModel]] = await session.scalars(query)

        if not roles:
            return []

        return [Role(role_id=role.role_id, role=role.role) for role in roles.all()]

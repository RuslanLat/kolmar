import typing
from typing import List, Optional
from sqlalchemy import select, update, delete

from app.groups.models import Group, GroupModel
from app.base.base_accessor import BaseAccessor


class GroupAccessor(BaseAccessor):
    async def get_by_group(self, group: str) -> Optional[Group]:
        async with self.app.database.session() as session:
            query = select(GroupModel).where(GroupModel.group == group)
            group: Optional[GroupModel] = await session.scalar(query)

        if not group:
            return None

        return Group(group_id=group.group_id, group=group.group)

    async def get_by_group_id(self, group_id: int) -> Optional[Group]:
        async with self.app.database.session() as session:
            query = select(GroupModel).where(
                GroupModel.group_id == group_id
            )
            group: Optional[GroupModel] = await session.scalar(query)

        if not group:
            return None

        return Group(group_id=group.group_id, group=group.group)

    async def create_group(self, group: str) -> Optional[Group]:
        new_group: Group = GroupModel(group=group)

        async with self.app.database.session.begin() as session:
            session.add(new_group)

        return Group(group_id=new_group.group_id, group=new_group.group)

    async def update_group(
        self, group_id: int, group: str
    ) -> Optional[Group]:
        query = (
            update(GroupModel)
            .where(GroupModel.group_id == group_id)
            .values(group=group)
            .returning(GroupModel)
        )

        async with self.app.database.session.begin() as session:
            group: GroupModel = await session.scalar(query)

        if not group:
            return None

        return Group(group_id=group.group_id, group=group.group)

    async def delete_group(self, group: str) -> Optional[Group]:
        query = (
            delete(GroupModel)
            .where(GroupModel.group == group)
            .returning(GroupModel)
        )

        async with self.app.database.session.begin() as session:
            group: GroupModel = await session.scalar(query)

        if not group:
            return None

        return Group(group_id=group.group_id, group=group.group)

    async def list_groups(self) -> List[Optional[Group]]:
        query = select(GroupModel)

        async with self.app.database.session() as session:
            groups = await session.scalars(query)

        if not groups:
            return []

        return [
            Group(group_id=group.group_id, group=group.group)
            for group in groups.all()
        ]

from typing import List, Optional
from sqlalchemy import select, update, delete, and_
from sqlalchemy.orm import joinedload
from app.subdivisions.models import (
    Subdivision,
    SubdivisionModel,
    SubdivisionBot,
    SubdivisionBotModel,
)
from app.base.base_accessor import BaseAccessor


class SubdivisionAccessor(BaseAccessor):
    async def create_subdivision(
        self, subdivision: str, email: str, telegram_id: int
    ) -> Optional[Subdivision]:
        new_subdivision: SubdivisionModel = SubdivisionModel(
            subdivision=subdivision, email=email, telegram_id=telegram_id
        )

        async with self.app.database.session.begin() as session:
            session.add(new_subdivision)

        return Subdivision(
            subdivision_id=new_subdivision.subdivision_id,
            subdivision=new_subdivision.subdivision,
            email=new_subdivision.email,
            telegram_id=new_subdivision.telegram_id,
        )

    async def create_boot_subdivision(
        self, subdivision_id: int, telegram_id: int
    ) -> Optional[SubdivisionBot]:
        new_subdivision: SubdivisionBotModel = SubdivisionBotModel(
            subdivision_id=subdivision_id, telegram_id=telegram_id
        )

        async with self.app.database.session.begin() as session:
            session.add(new_subdivision)

        return SubdivisionBot(
            subdivision_id=new_subdivision.subdivision_id,
            telegram_id=new_subdivision.telegram_id,
            link=new_subdivision.link,
        )

    async def update_subdivision_telegram_id(
        self, subdivision_id: int, telegram_id: int
    ) -> Optional[Subdivision]:
        query = (
            update(SubdivisionModel)
            .where(SubdivisionModel.subdivision_id == subdivision_id)
            .values(telegram_id=telegram_id)
            .returning(SubdivisionModel)
        )

        async with self.app.database.session.begin() as session:
            subdivision: SubdivisionModel = await session.scalar(query)

        if not subdivision:
            return None

        return Subdivision(
            subdivision_id=subdivision.subdivision_id,
            subdivision=subdivision.subdivision,
            email=subdivision.email,
            telegram_id=subdivision.telegram_id,
        )

    async def update_boot_subdivision(
        self, subdivision_id: int, telegram_id: int
    ) -> Optional[SubdivisionBot]:
        query = (
            update(SubdivisionBotModel)
            .where(SubdivisionBotModel.subdivision_id == subdivision_id)
            .values(telegram_id=telegram_id)
            .returning(SubdivisionBotModel)
        )

        async with self.app.database.session.begin() as session:
            subdivision: SubdivisionBotModel = await session.scalar(query)

        if not subdivision:
            return None

        return SubdivisionBot(
            subdivision_id=subdivision.subdivision_id,
            telegram_id=subdivision.telegram_id,
            link=subdivision.link,
        )

    async def get_id_subdivision(self, subdivision: str) -> Optional[Subdivision]:
        query = select(SubdivisionModel).where(
            SubdivisionModel.subdivision == subdivision
        )

        async with self.app.database.session.begin() as session:
            subdivision: SubdivisionModel = await session.scalar(query)

        if not subdivision:
            return None

        return Subdivision(
            subdivision_id=subdivision.subdivision_id,
            subdivision=subdivision.subdivision,
            email=subdivision.email,
            telegram_id=subdivision.telegram_id,
        )

    async def delete_subdivision(self, subdivision: str) -> Optional[Subdivision]:
        query = (
            delete(SubdivisionModel)
            .where(SubdivisionModel.subdivision == subdivision)
            .returning(SubdivisionModel)
        )

        async with self.app.database.session.begin() as session:
            subdivision: SubdivisionModel = await session.scalar(query)

        if not subdivision:
            return None

        return Subdivision(
            subdivision_id=subdivision.subdivision_id,
            subdivision=subdivision.subdivision,
            email=subdivision.email,
            telegram_id=subdivision.telegram_id,
        )

    async def list_subdivisions(self) -> List[Optional[Subdivision]]:
        query = select(SubdivisionModel)

        async with self.app.database.session() as session:
            subdivisions: List[SubdivisionModel] = await session.scalars(query)

        if not subdivisions:
            return []

        return [
            Subdivision(
                subdivision_id=subdivision.subdivision_id,
                subdivision=subdivision.subdivision,
                email=subdivision.email,
                telegram_id=subdivision.telegram_id,
            )
            for subdivision in subdivisions.all()
        ]

import typing
from typing import List, Optional
from sqlalchemy import select, update, delete

from app.stimuls.models import Stimul, StimulModel
from app.base.base_accessor import BaseAccessor


class StimulAccessor(BaseAccessor):
    async def get_by_stimul_id(self, row_id: int) -> Optional[Stimul]:
        async with self.app.database.session() as session:
            query = select(StimulModel).where(StimulModel.row_id == row_id)
            stimul: Optional[StimulModel] = await session.scalar(query)

        if not stimul:
            return None

        return Stimul(
            row_id=stimul.row_id,
            user_id=stimul.user_id,
            date=stimul.date,
            q1=stimul.q1,
            q2=stimul.q2,
            q3=stimul.q3,
            q4=stimul.q4,
            q5=stimul.q5,
            q6=stimul.q6,
            q7=stimul.q7,
            q8=stimul.q8,
            q9=stimul.q9,
            q10=stimul.q10,
            q11=stimul.q11,
        )

    async def create_stimul(
        self,
        user_id: int,
        q1: str,
        q2: str,
        q3: str,
        q4: str,
        q5: str,
        q6: str,
        q7: str,
        q8: str,
        q9: str,
        q10: str,
        q11: str,
    ) -> Optional[Stimul]:
        new_stimul = StimulModel(
            user_id=user_id,
            q1=q1,
            q2=q2,
            q3=q3,
            q4=q4,
            q5=q5,
            q6=q6,
            q7=q7,
            q8=q8,
            q9=q9,
            q10=q10,
            q11=q11,
        )

        async with self.app.database.session.begin() as session:
            session.add(new_stimul)

        return Stimul(
            row_id=new_stimul.row_id,
            user_id=new_stimul.user_id,
            date=new_stimul.date,
            q1=new_stimul.q1,
            q2=new_stimul.q2,
            q3=new_stimul.q3,
            q4=new_stimul.q4,
            q5=new_stimul.q5,
            q6=new_stimul.q6,
            q7=new_stimul.q7,
            q8=new_stimul.q8,
            q9=new_stimul.q9,
            q10=new_stimul.q10,
            q11=new_stimul.q11,
        )

    # async def update_position(
    #     self, position_id: int, position: str
    # ) -> Optional[Position]:
    #     query = (
    #         update(PositionModel)
    #         .where(PositionModel.position_id == position_id)
    #         .values(position=position)
    #         .returning(PositionModel)
    #     )

    #     async with self.app.database.session.begin() as session:
    #         position = await session.scalar(query)

    #     if not position:
    #         return None

    #     return Position(position_id=position.position_id, position=position.position)

    # async def delete_position(self, position: str) -> Optional[Position]:
    #     query = (
    #         delete(PositionModel)
    #         .where(PositionModel.position == position)
    #         .returning(PositionModel)
    #     )

    #     async with self.app.database.session.begin() as session:
    #         position = await session.scalar(query)

    #     if not position:
    #         return None

    #     return Position(position_id=position.position_id, position=position.position)

    async def list_stimuls(self) -> List[Optional[Stimul]]:
        query = select(StimulModel)

        async with self.app.database.session() as session:
            stimuls = await session.scalars(query)

        if not stimuls:
            return []

        return [
            Stimul(
                row_id=stimul.row_id,
                user_id=stimul.user_id,
                date=stimul.date,
                q1=stimul.q1,
                q2=stimul.q2,
                q3=stimul.q3,
                q4=stimul.q4,
                q5=stimul.q5,
                q6=stimul.q6,
                q7=stimul.q7,
                q8=stimul.q8,
                q9=stimul.q9,
                q10=stimul.q10,
                q11=stimul.q11,
            )
            for stimul in stimuls.all()
        ]

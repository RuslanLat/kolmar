import typing
from typing import List, Optional
from sqlalchemy import select, update, delete

from app.ratings.models import Rating, RatingModel
from app.base.base_accessor import BaseAccessor


class RatingAccessor(BaseAccessor):
    async def get_by_rating(self, user_id: int) -> Optional[Rating]:
        async with self.app.database.session() as session:
            query = select(RatingModel).where(RatingModel.user_id == user_id)
            rating: Optional[RatingModel] = await session.scalar(query)

        if not rating:
            return None

        return Rating(
                row_id=rating.row_id,
                date=rating.date,
                user_id=rating.user_id,
                rating=rating.rating
            )

    async def get_by_rating_id(self, row_id: int) -> Optional[Rating]:
        async with self.app.database.session() as session:
            query = select(RatingModel).where(RatingModel.row_id == row_id)
            rating: Optional[RatingModel] = await session.scalar(query)

        if not rating:
            return None

        return Rating(
                row_id=rating.row_id,
                date=rating.date,
                user_id=rating.user_id,
                rating=rating.rating
            )

    async def create_rating(
        self,
        user_id: int,
        rating: int,
    ) -> Optional[Rating]:
        new_rating: RatingModel = RatingModel(
            user_id=user_id, rating=rating
        )

        async with self.app.database.session.begin() as session:
            session.add(new_rating)

        return Rating(
                row_id=new_rating.row_id,
                date=new_rating.date,
                user_id=new_rating.user_id,
                rating=new_rating.rating
            )

    async def delete_rating(self, row_id: int) -> Optional[Rating]:
        query = (
            delete(RatingModel)
            .where(RatingModel.row_id == row_id)
            .returning(RatingModel)
        )

        async with self.app.database.session.begin() as session:
            rating: Optional[RatingModel] = await session.scalar(query)

        if not rating:
            return None

        return Rating(
                row_id=rating.row_id,
                date=rating.date,
                user_id=rating.user_id,
                rating=rating.rating
            )

    async def list_ratings(self) -> List[Optional[Rating]]:
        query = select(RatingModel)

        async with self.app.database.session() as session:
            ratings = await session.scalars(query)

        if not ratings:
            return []

        return [
            Rating(
                row_id=rating.row_id,
                date=rating.date,
                user_id=rating.user_id,
                rating=rating.rating
            )
            for rating in ratings.all()
        ]

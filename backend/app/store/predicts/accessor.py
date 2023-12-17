from typing import List, Optional
from sqlalchemy import select, update, delete

from app.predicts.models import Predict, PredictModel
from app.base.base_accessor import BaseAccessor


class PredictAccessor(BaseAccessor):
    async def get_by_predict(self, user_id: int) -> Optional[Predict]:
        async with self.app.database.session() as session:
            query = select(PredictModel).where(PredictModel.user_id == user_id)
            predict: Optional[PredictModel] = await session.scalar(query)

        if not predict:
            return None

        return Predict(
            row_id=predict.row_id,
            date=predict.date,
            user_id=predict.user_id,
            dismiss=predict.dismiss,
            probability=predict.probability,
        )

    async def get_by_predict_id(self, row_id: int) -> Optional[Predict]:
        async with self.app.database.session() as session:
            query = select(PredictModel).where(PredictModel.row_id == row_id)
            predict: Optional[PredictModel] = await session.scalar(query)

        if not predict:
            return None

        return Predict(
            row_id=predict.row_id,
            date=predict.date,
            user_id=predict.user_id,
            dismiss=predict.dismiss,
            probability=predict.probability,
        )

    async def create_predict(
        self, user_id: int, dismiss: bool, probability: float
    ) -> Optional[Predict]:
        new_predict: PredictModel = PredictModel(
            user_id=user_id, dismiss=dismiss, probability=probability
        )

        async with self.app.database.session.begin() as session:
            session.add(new_predict)

        return Predict(
            row_id=new_predict.row_id,
            date=new_predict.date,
            user_id=new_predict.user_id,
            dismiss=new_predict.dismiss,
            probability=new_predict.probability,
        )

    async def create_predict_all(
        self,
        predicts,
    ) -> Optional[List[Predict]]:
        new_predicts = [
            PredictModel(
                user_id=predict["user_id"],
                date=predict["date"],
                dismiss=predict["dismiss"],
                probability=predict["probability"],                
            )
            for predict in predicts
        ]

        async with self.app.database.session.begin() as session:
            session.add_all(new_predicts)

        return [
            Predict(
                row_id=new_predict.row_id,
                user_id=new_predict.user_id,
                date=new_predict.date,
                dismiss=new_predict.dismiss,
                probability=new_predict.probability,                
            )
            for new_predict in new_predicts
        ]

    async def delete_predict(self, row_id: int) -> Optional[Predict]:
        query = (
            delete(PredictModel)
            .where(PredictModel.row_id == row_id)
            .returning(PredictModel)
        )

        async with self.app.database.session.begin() as session:
            predict = await session.scalar(query)

        if not predict:
            return None

        return Predict(
            row_id=predict.row_id,
            date=predict.date,
            user_id=predict.user_id,
            dismiss=predict.dismiss,
            probability=predict.probability,
        )

    async def list_predicts(self) -> List[Optional[Predict]]:
        query = select(PredictModel)

        async with self.app.database.session() as session:
            predicts: List[PredictModel] = await session.scalars(query)

        if not predicts:
            return []

        return [
            Predict(
            row_id=predict.row_id,
            date=predict.date,
            user_id=predict.user_id,
            dismiss=predict.dismiss,
            probability=predict.probability,
        )
            for predict in predicts.all()
        ]

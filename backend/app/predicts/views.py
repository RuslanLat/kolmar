from typing import List
from aiohttp.web import HTTPConflict
from aiohttp_apispec import (
    docs,
    request_schema,
    response_schema,
)
from aiohttp.web_response import Response
from sqlalchemy import exc

from app.predicts.schemes import (
    PredictRequestSchema,
    PredictResponseSchema,
    PredictListResponseSchema,
    PredictDeleteRequestSchema,
    PredictListRequestSchema,
)
from app.web.app import View
from app.web.mixins import (
    AuthRequiredMixin,
    AuthUserRequiredMixin,
)
from app.web.utils import json_response
from app.predicts.models import Predict


class PredictAddView(AuthUserRequiredMixin, View):
    @request_schema(PredictRequestSchema)
    @response_schema(PredictResponseSchema, 200)
    @docs(
        tags=["predicts"],
        summary="Add predict add view",
        description="Add predict to database",
    )
    async def post(self) -> Response:
        user_id: int = self.data["user_id"]
        dismiss: bool = self.data["dismiss"]
        probability: float = self.data["probability"]

        try:
            predict: Predict = await self.store.predicts.create_predict(
                user_id=user_id, dismiss=dismiss, probability=probability
            )
        except exc.IntegrityError as e:
            if "23505" in e.orig.pgcode:
                raise HTTPConflict

        return json_response(data=PredictResponseSchema().dump(predict))


class PredictListAddView(AuthUserRequiredMixin, View):
    @request_schema(PredictListRequestSchema)
    @response_schema(PredictListResponseSchema, 200)
    @docs(
        tags=["predicts"],
        summary="Add predict list add view",
        description="Add predict list to database",
    )
    async def post(self) -> Response:
        predicts: List = self.data["predicts"]
        try:
            predicts = await self.store.predicts.create_predict_all(
                predicts=predicts,
            )

        except exc.IntegrityError as e:
            if "23505" in e.orig.pgcode:
                raise HTTPConflict

        return json_response(PredictListRequestSchema().dump({"predicts": predicts}))


class PredictDeleteView(AuthUserRequiredMixin, View):
    @request_schema(PredictDeleteRequestSchema)
    @response_schema(PredictResponseSchema, 200)
    @docs(
        tags=["predicts"],
        summary="Add predict delete view",
        description="Delete predict from database",
    )
    async def delete(self) -> Response:
        row_id: int = self.data["row_id"]

        predict: Predict = await self.store.predicts.delete_predict(row_id=row_id)

        return json_response(data=PredictResponseSchema().dump(predict))


class PredictListView(AuthUserRequiredMixin, View):  # AuthRequiredMixin,
    @response_schema(PredictListResponseSchema, 200)
    @docs(
        tags=["predicts"],
        summary="Add predict list view",
        description="Get list predicts from database",
    )
    async def get(self) -> Response:
        predicts: List[Predict] = await self.store.predicts.list_predicts()
        return json_response(PredictListResponseSchema().dump({"predicts": predicts}))

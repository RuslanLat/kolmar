from typing import List
from aiohttp.web import HTTPConflict
from aiohttp_apispec import (
    docs,
    request_schema,
    response_schema,
)
from aiohttp.web_response import Response
from sqlalchemy import exc

from app.ratings.schemes import (
    RatingRequestSchema,
    RatingResponseSchema,
    RatingListResponseSchema,
    RatingDeleteRequestSchema,
)
from app.web.app import View
from app.web.mixins import (
    AuthRequiredMixin,
    AuthUserRequiredMixin,
)
from app.web.utils import json_response
from app.ratings.models import Rating


class RatingAddView(AuthUserRequiredMixin, View):
    @request_schema(RatingRequestSchema)
    @response_schema(RatingResponseSchema, 200)
    @docs(
        tags=["ratings"],
        summary="Add rating add view",
        description="Add rating to database",
    )
    async def post(self) -> Response:
        user_id: int = self.data["user_id"]
        rating: str = self.data["rating"]

        try:
           rating: Rating = await self.store.ratings.create_rating(
                user_id=user_id, rating=rating
            )
        except exc.IntegrityError as e:
            if "23505" in e.orig.pgcode:
                raise HTTPConflict

        return json_response(data=RatingResponseSchema().dump(rating))


class RatingDeleteView(AuthUserRequiredMixin, View):
    @request_schema(RatingDeleteRequestSchema)
    @response_schema(RatingResponseSchema, 200)
    @docs(
        tags=["ratings"],
        summary="Add rating delete view",
        description="Delete rating from database",
    )
    async def delete(self) -> Response:
        row_id: int = self.data["row_id"]

        rating: Rating = await self.store.ratings.delete_rating(row_id=row_id)

        return json_response(data=RatingResponseSchema().dump(rating))


class RatingListView(AuthUserRequiredMixin, View):  # AuthRequiredMixin,
    @response_schema(RatingListResponseSchema, 200)
    @docs(
        tags=["ratings"],
        summary="Add rating list view",
        description="Get list ratings from database",
    )
    async def get(self) -> Response:
        ratings: List[Rating] = await self.store.ratings.list_ratings()
        return json_response(RatingListResponseSchema().dump({"ratings": ratings}))

from typing import List, Optional
from aiohttp.web import HTTPConflict
from aiohttp_apispec import (
    docs,
    request_schema,
    response_schema,
)
from aiohttp.web_response import Response
from sqlalchemy import exc

from app.subdivisions.schemes import (
    SubdivisionRequestSchema,
    SubdivisionSchema,
    SubdivisionResponseSchema,
    SubdivisionListResponseSchema,
    SubdivisionBotUpdateSchema,
    SubdivisionBotResponseSchema,
)
from app.web.app import View
from app.web.mixins import (
    AuthRequiredMixin,
    AuthUserRequiredMixin,
)
from app.web.utils import json_response
from app.subdivisions.models import Subdivision, SubdivisionBot


class SubdivisionAddView(AuthUserRequiredMixin, View):
    @request_schema(SubdivisionRequestSchema)
    @response_schema(SubdivisionResponseSchema, 200)
    @docs(
        tags=["subdivisions"],
        summary="Add subdivision add view",
        description="Add subdivision to database",
    )
    async def post(self) -> Response:
        subdivision: str = self.data["subdivision"]
        email: str = self.data["email"]
        telegram_id: int = self.data["telegram_id"]

        try:
            subdivision: Subdivision = await self.store.subdivisions.create_subdivision(
                subdivision=subdivision, email=email, telegram_id=telegram_id
            )
            subdivision_boot = await self.store.subdivisions.create_boot_subdivision(
                subdivision_id=subdivision.subdivision_id, telegram_id=telegram_id
            )
        except exc.IntegrityError as e:
            if "23505" in e.orig.pgcode:
                raise HTTPConflict

        return json_response(data=SubdivisionResponseSchema().dump(subdivision))


class SubdivisionDeleteView(AuthUserRequiredMixin, View):
    @request_schema(SubdivisionRequestSchema)
    @response_schema(SubdivisionResponseSchema, 200)
    @docs(
        tags=["subdivisions"],
        summary="Add subdivision delete view",
        description="Delete subdivision from database",
    )
    async def delete(self) -> Response:
        subdivision: str = self.data["subdivision"]

        subdivision: Subdivision = await self.store.subdivisions.delete_subdivision(
            subdivision=subdivision
        )

        return json_response(data=SubdivisionResponseSchema().dump(subdivision))


class SubdivisionListView(AuthUserRequiredMixin, View):  # AuthRequiredMixin,
    @response_schema(SubdivisionListResponseSchema, 200)
    @docs(
        tags=["subdivisions"],
        summary="Add subdivision list view",
        description="Get list subdivisions from database",
    )
    async def get(self) -> Response:
        subdivisions: List[
            Optional[Subdivision]
        ] = await self.store.subdivisions.list_subdivisions()
        return json_response(
            SubdivisionListResponseSchema().dump({"subdivisions": subdivisions})
        )


class SubdivisionBotUpdateView(AuthUserRequiredMixin, View):
    @request_schema(SubdivisionBotUpdateSchema)
    @response_schema(SubdivisionBotResponseSchema, 200)
    @docs(
        tags=["subdivisions"],
        summary="Add subdivision update view",
        description="Update subdivision from database",
    )
    async def put(self) -> Response:
        subdivision_id: int = self.data["subdivision_id"]
        telegram_id: int = self.data["telegram_id"]

        subdivision = await self.store.subdivisions.update_subdivision_telegram_id(subdivision_id=subdivision_id, telegram_id=telegram_id)

        subdivision_boot: SubdivisionBot = await self.store.subdivisions.update_boot_subdivision(
            subdivision_id=subdivision_id, telegram_id=telegram_id
        )

        return json_response(data=SubdivisionBotResponseSchema().dump(subdivision_boot))

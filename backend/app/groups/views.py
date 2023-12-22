from typing import List, Optional
from aiohttp.web import HTTPConflict
from aiohttp_apispec import (
    docs,
    request_schema,
    response_schema,
)
from aiohttp.web_response import Response
from sqlalchemy import exc

from app.groups.schemes import (
    GroupRequestSchema,
    GroupSchema,
    GroupResponseSchema,
    GroupListResponseSchema,
)
from app.web.app import View
from app.web.mixins import (
    AuthRequiredMixin,
    AuthUserRequiredMixin,
)
from app.web.utils import json_response
from app.groups.models import Group


class GroupAddView(AuthUserRequiredMixin, View):
    @request_schema(GroupRequestSchema)
    @response_schema(GroupResponseSchema, 200)
    @docs(
        tags=["groups"],
        summary="Add group add view",
        description="Add group to database",
    )
    async def post(self) -> Response:
        group: str = self.data["group"]

        try:
            group: Group = await self.store.groups.create_group(group=group)

        except exc.IntegrityError as e:
            if "23505" in e.orig.pgcode:
                raise HTTPConflict

        return json_response(data=GroupResponseSchema().dump(group))


class GroupDeleteView(AuthUserRequiredMixin, View):
    @request_schema(GroupRequestSchema)
    @response_schema(GroupResponseSchema, 200)
    @docs(
        tags=["groups"],
        summary="Add group delete view",
        description="Delete group from database",
    )
    async def delete(self) -> Response:
        group: str = self.data["group"]

        group: Group = await self.store.groups.delete_group(group=group)

        return json_response(data=GroupResponseSchema().dump(group))


class GroupListView(AuthUserRequiredMixin, View):  # AuthRequiredMixin,
    @response_schema(GroupListResponseSchema, 200)
    @docs(
        tags=["groups"],
        summary="Add group list view",
        description="Get list groups from database",
    )
    async def get(self) -> Response:
        groups: List[Optional[Group]] = await self.store.groups.list_groups()
        return json_response(GroupListResponseSchema().dump({"groups": groups}))

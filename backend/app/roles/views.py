from typing import List
from aiohttp.web import HTTPConflict
from aiohttp_apispec import (
    docs,
    request_schema,
    response_schema,
)
from aiohttp.web_response import Response
from sqlalchemy import exc

from app.roles.schemes import (
    RoleRequestSchema,
    RoleResponseSchema,
    RoleListResponseSchema,
    RoleUpdateRequestSchema,
)
from app.web.app import View
from app.web.mixins import (
    AuthRequiredMixin,
    AuthUserRequiredMixin,
)
from app.web.utils import json_response
from app.roles.models import Role


class RoleAddView(AuthUserRequiredMixin, View):
    @request_schema(RoleRequestSchema)
    @response_schema(RoleResponseSchema, 200)
    @docs(
        tags=["roles"],
        summary="Add role add view",
        description="Add role to database",
    )
    async def post(self) -> Response:
        role: str = self.data["role"]

        try:
            role: Role = await self.store.roles.create_role(role=role)
        except exc.IntegrityError as e:
            if "23505" in e.orig.pgcode:
                raise HTTPConflict

        return json_response(data=RoleResponseSchema().dump(role))


class RoleUpdateView(AuthUserRequiredMixin, View):
    @request_schema(RoleUpdateRequestSchema)
    @response_schema(RoleResponseSchema, 200)
    @docs(
        tags=["roles"],
        summary="Add role update view",
        description="Update role in database",
    )
    async def put(self) -> Response:
        role: str = self.data["role"]
        role_id: int = self.data["role_id"]

        try:
            role: Role = await self.store.roles.update_role(role_id=role_id, role=role)
        except exc.IntegrityError as e:
            if "23505" in e.orig.pgcode:
                raise HTTPConflict

        return json_response(data=RoleResponseSchema().dump(role))


class RoleDeleteView(AuthUserRequiredMixin, View):
    @request_schema(RoleRequestSchema)
    @response_schema(RoleResponseSchema, 200)
    @docs(
        tags=["roles"],
        summary="Add role delete view",
        description="Delete role from database",
    )
    async def delete(self) -> Response:
        role: str = self.data["role"]

        role: Role = await self.store.roles.delete_role(role=role)

        return json_response(data=RoleResponseSchema().dump(role))


class RoleListView(AuthUserRequiredMixin, View):  # AuthRequiredMixin,
    @response_schema(RoleListResponseSchema, 200)
    @docs(
        tags=["roles"],
        summary="Add role list view",
        description="Get list roles from database",
    )
    async def get(self) -> Response:
        roles: List[Role] = await self.store.roles.list_roles()

        return json_response(RoleListResponseSchema().dump({"roles": roles}))

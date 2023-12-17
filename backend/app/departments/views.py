from typing import List, Optional
from aiohttp.web import HTTPConflict
from aiohttp_apispec import (
    docs,
    request_schema,
    response_schema,
)
from aiohttp.web_response import Response
from sqlalchemy import exc

from app.departments.schemes import (
    DepartmentRequestSchema,
    DepartmentSchema,
    DepartmentResponseSchema,
    DepartmentListResponseSchema,
    DepartmentBotUpdateSchema,
    DepartmentBotResponseSchema,
)
from app.web.app import View
from app.web.mixins import (
    AuthRequiredMixin,
    AuthUserRequiredMixin,
)
from app.web.utils import json_response
from app.departments.models import Department, DepartmentBot


class DepartmentAddView(AuthUserRequiredMixin, View):
    @request_schema(DepartmentRequestSchema)
    @response_schema(DepartmentResponseSchema, 200)
    @docs(
        tags=["departments"],
        summary="Add department add view",
        description="Add department to database",
    )
    async def post(self) -> Response:
        department: str = self.data["department"]
        email: str = self.data["email"]
        telegram_id: int = self.data["telegram_id"]

        try:
            department: Department = await self.store.departments.create_department(
                department=department, email=email, telegram_id=telegram_id
            )
            department_boot = await self.store.departments.create_boot_department(
                department_id=department.department_id, telegram_id=telegram_id
            )
        except exc.IntegrityError as e:
            if "23505" in e.orig.pgcode:
                raise HTTPConflict

        return json_response(data=DepartmentResponseSchema().dump(department))


class DepartmentDeleteView(AuthUserRequiredMixin, View):
    @request_schema(DepartmentRequestSchema)
    @response_schema(DepartmentResponseSchema, 200)
    @docs(
        tags=["departments"],
        summary="Add department delete view",
        description="Delete department from database",
    )
    async def delete(self) -> Response:
        department: str = self.data["department"]

        department: Department = await self.store.departments.delete_department(
            department=department
        )

        return json_response(data=DepartmentResponseSchema().dump(department))


class DepartmentListView(AuthUserRequiredMixin, View):  # AuthRequiredMixin,
    @response_schema(DepartmentListResponseSchema, 200)
    @docs(
        tags=["departments"],
        summary="Add department list view",
        description="Get list departments from database",
    )
    async def get(self) -> Response:
        departments: List[
            Optional[Department]
        ] = await self.store.departments.list_departments()
        return json_response(
            DepartmentListResponseSchema().dump({"departments": departments})
        )


class DepartmentBotUpdateView(AuthUserRequiredMixin, View):
    @request_schema(DepartmentBotUpdateSchema)
    @response_schema(DepartmentBotResponseSchema, 200)
    @docs(
        tags=["departments"],
        summary="Add department update view",
        description="Update department from database",
    )
    async def put(self) -> Response:
        department_id: int = self.data["department_id"]
        telegram_id: int = self.data["telegram_id"]

        department = await self.store.departments.update_department_telegram_id(department_id=department_id, telegram_id=telegram_id)

        department_boot: DepartmentBot = await self.store.departments.update_boot_department(
            department_id=department_id, telegram_id=telegram_id
        )

        return json_response(data=DepartmentBotResponseSchema().dump(department_boot))

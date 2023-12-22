from hashlib import sha256
from typing import List, Optional
from aiohttp.web import (
    HTTPForbidden,
    HTTPUnauthorized,
    HTTPConflict,
)
from aiohttp_session import new_session
from aiohttp_apispec import (
    docs,
    request_schema,
    response_schema,
)
from aiohttp.web_response import Response
from sqlalchemy import exc

from app.users.schemes import (
    UserLoginBaseSchema,
    UserLoginRequestSchema,
    UserLoginResponseSchema,
    UserLoginUpdateRequestSchema,
    UserLoginListResponseSchema,
    UserBaseSchema,
    UserRequestSchema,
    UserResponseSchema,
    UserListResponseSchema,
    UserUpdateRequestSchema,
    UserInsertRequestSchema,
    UserFullListResponseSchema,
    UserBotFullListResponseSchema,
)
from app.web.app import View
from app.web.mixins import (
    AuthRequiredMixin,
    AuthUserRequiredMixin,
)
from app.web.utils import json_response
from app.users.models import User, UserLogin, UserBotFull


class UserLoginView(View):
    @request_schema(UserLoginRequestSchema)
    @response_schema(UserLoginResponseSchema, 200)
    @docs(
        tags=["user_logins"],
        summary="Add user login view",
        description="Get user login from database",
    )
    async def post(self) -> Response:
        login: str = self.data["login"]
        password: str = self.data["password"]

        user: Optional[UserLogin] = await self.store.user_logins.get_by_login(login)

        if not user:
            raise HTTPForbidden(text="No user with provided login was found")
        if not user.is_password_valid(password):
            raise HTTPForbidden(reason="Invalid credentials")

        user_data = UserLoginResponseSchema().dump(user)

        session = await new_session(request=self.request)
        session["user"] = user_data

        return json_response(data=user_data)


class UserLoginCurrentView(View):
    @response_schema(UserLoginResponseSchema, 200)
    @docs(
        tags=["user_logins"],
        summary="Add user login current view",
        description="Current user login from session",
    )
    async def get(self) -> Response:
        if not hasattr(self.request, "user"):
            raise HTTPUnauthorized

        user_data: UserLoginResponseSchema = UserLoginResponseSchema().dump(
            self.request.user
        )

        return json_response(data=user_data)


class UserLoginAddView(AuthUserRequiredMixin, View):
    @request_schema(UserLoginRequestSchema)
    @response_schema(UserLoginResponseSchema, 200)
    @docs(
        tags=["user_logins"],
        summary="Add user login add view",
        description="Add user login to database",
    )
    async def post(self) -> Response:
        login: str = self.data["login"]
        password: str = self.data["password"]

        try:
            user: UserLogin = await self.store.user_logins.create_user_login(
                login=login, password=password
            )
        except exc.IntegrityError as e:
            if "23505" in e.orig.pgcode:
                raise HTTPConflict

        return json_response(data=UserLoginResponseSchema().dump(user))


class UserLoginUpdateView(AuthUserRequiredMixin, View):
    @request_schema(UserLoginUpdateRequestSchema)
    @response_schema(UserLoginResponseSchema, 200)
    @docs(
        tags=["user_logins"],
        summary="Add user login update view",
        description="Update user login in database",
    )
    async def put(self) -> Response:
        login: str = self.data["login"]
        password: str = self.data["password"]

        try:
            user: UserLogin = await self.store.user_logins.update_user_login(
                login=login, password=password
            )
        except exc.IntegrityError as e:
            if "23505" in e.orig.pgcode:
                raise HTTPConflict

        return json_response(data=UserLoginResponseSchema().dump(user))


class UserLoginDeleteView(AuthUserRequiredMixin, View):
    @request_schema(UserLoginBaseSchema)
    @response_schema(UserLoginResponseSchema, 200)
    @docs(
        tags=["user_logins"],
        summary="Add user login delete view",
        description="Delete user login from database",
    )
    async def delete(self) -> Response:
        login: str = self.data["login"]

        user: UserLogin = await self.store.user_logins.delete_user_login(login=login)

        return json_response(data=UserLoginResponseSchema().dump(user))


class UserLoginListView(AuthUserRequiredMixin, View):
    @response_schema(UserLoginListResponseSchema, 200)
    @docs(
        tags=["user_logins"],
        summary="Add user login list view",
        description="Get list users login from database",
    )
    async def get(self) -> Response:
        users: List[UserLogin] = await self.store.user_logins.list_user_logins()

        return json_response(UserLoginListResponseSchema().dump({"users": users}))


class UserAddView(AuthUserRequiredMixin, View):
    @request_schema(UserRequestSchema)
    @response_schema(UserResponseSchema, 200)
    @docs(
        tags=["users"],
        summary="Add user add view",
        description="Add user to database",
    )
    async def post(self) -> Response:
        name: str = self.data["name"]
        lastname: str = self.data["lastname"]
        male: bool = self.data["male"]
        age: int = self.data["age"]
        experience: int = self.data["experience"]
        department_id: int = self.data["department_id"]
        subdivision_id: int = self.data["subdivision_id"]
        position_id: int = self.data["position_id"]
        role_id: int = self.data["role_id"]
        email: str = self.data["email"]
        telegram_id: int = self.data["telegram_id"]

        try:
            user: User = await self.store.users.create_user(
                name=name,
                lastname=lastname,
                male=male,
                age=age,
                experience=experience,
                department_id=department_id,
                subdivision_id=subdivision_id,
                position_id=position_id,
                role_id=role_id,
                email=email,
                telegram_id=telegram_id,
            )
            user_boot = await self.store.users.create_boot_user(user_id=user.id)
        except exc.IntegrityError as e:
            if "23505" in e.orig.pgcode:
                raise HTTPConflict

        return json_response(data=UserResponseSchema().dump(user))


class UserInsertAddView(AuthUserRequiredMixin, View):
    @request_schema(UserInsertRequestSchema)
    @response_schema(UserResponseSchema, 200)
    @docs(
        tags=["users"],
        summary="Add insert user add view",
        description="Add user to database",
    )
    async def post(self) -> Response:
        id: int = self.data["id"]
        name: str = self.data["name"]
        lastname: str = self.data["lastname"]
        male: bool = self.data["male"]
        age: int = self.data["age"]
        experience: int = self.data["experience"]
        # email: str = self.data["email"]
        # telegram_id: int = self.data["telegram_id"]

        try:
            user: User = await self.store.users.create_insert_user(
                id=id,
                name=name,
                lastname=lastname,
                male=male,
                age=age,
                experience=experience,
            )
            user_boot = await self.store.users.create_boot_user(user_id=user.id)
        except exc.IntegrityError as e:
            if "23505" in e.orig.pgcode:
                raise HTTPConflict

        return json_response(data=UserResponseSchema().dump(user))


class UserUpdateView(AuthUserRequiredMixin, View):
    @request_schema(UserUpdateRequestSchema)
    @response_schema(UserResponseSchema, 200)
    @docs(
        tags=["users"],
        summary="Add user delete view",
        description="Delete user from database",
    )
    async def put(self) -> Response:
        id: int = self.data["id"]
        is_view: str = self.data["is_view"]

        user: User = await self.store.users.update_user(id=id, is_view=is_view)

        return json_response(data=UserResponseSchema().dump(user))


class UserDeleteView(AuthUserRequiredMixin, View):
    @request_schema(UserBaseSchema)
    @response_schema(UserResponseSchema, 200)
    @docs(
        tags=["users"],
        summary="Add user delete view",
        description="Delete user from database",
    )
    async def delete(self) -> Response:
        name: str = self.data["name"]
        lastname: str = self.data["lastname"]

        user: User = await self.store.users.delete_user(name=name, lastname=lastname)

        return json_response(data=UserResponseSchema().dump(user))


class UserListView(AuthUserRequiredMixin, View):
    @response_schema(UserListResponseSchema, 200)
    @docs(
        tags=["users"],
        summary="Add user list view",
        description="Get list users from database",
    )
    async def get(self) -> Response:
        users: List[User] = await self.store.users.list_user()

        return json_response(UserListResponseSchema().dump({"users": users}))


class UserFullListView(AuthUserRequiredMixin, View):
    @response_schema(UserFullListResponseSchema, 200)
    @docs(
        tags=["users"],
        summary="Add full user list view",
        description="Get full list users from database",
    )
    async def get(self) -> Response:
        users: List[User] = await self.store.users.list_full_user()

        return json_response(UserFullListResponseSchema().dump({"users": users}))


class UserBotFullListView(AuthUserRequiredMixin, View):
    @response_schema(UserBotFullListResponseSchema, 200)
    @docs(
        tags=["users"],
        summary="Add full user bot list view",
        description="Get full list users bot from database",
    )
    async def get(self) -> Response:
        users: List[UserBotFull] = await self.store.users.list_full_user_bot()

        return json_response(UserBotFullListResponseSchema().dump({"users": users}))
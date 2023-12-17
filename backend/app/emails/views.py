from typing import List, Optional
from datetime import datetime
from aiohttp.web import HTTPConflict
from aiohttp_apispec import (
    docs,
    request_schema,
    response_schema,
)
from aiohttp.web_response import Response
from sqlalchemy import exc

from app.emails.schemes import (
    EmailRequestSchema,
    EmailResponseSchema,
    EmailDeleteRequestSchema,
    EmailUserRequestSchema,
    EmailListResponseSchema,
    EmailListRequestSchema,
)
from app.web.app import View
from app.web.mixins import (
    AuthRequiredMixin,
    AuthUserRequiredMixin,
)
from app.web.utils import json_response
from app.emails.models import Email


class EmailAddView(AuthUserRequiredMixin, View):
    @request_schema(EmailRequestSchema)
    @response_schema(EmailResponseSchema, 200)
    @docs(
        tags=["emails"],
        summary="Add email add view",
        description="Add email to database",
    )
    async def post(self) -> Response:
        user_id: int = self.data["user_id"]
        date: datetime = self.data["date"]
        use_email_total: int = self.data["use_email_total"]
        active_use_email: int = self.data["active_use_email"]
        use_email_last: int = self.data["use_email_last"]
        out_work_internal_email_total: int = self.data["out_work_internal_email_total"]
        out_work_internal_email_last: int = self.data["out_work_internal_email_last"]
        out_work_external_email_total: int = self.data["out_work_external_email_total"]
        out_work_external_email_last: int = self.data["out_work_external_email_last"]
        cnt_days_pause_total: int = self.data["cnt_days_pause_total"]
        cnt_days_pause_last: int = self.data["cnt_days_pause_last"]
        cnt_4hours_later_total: int = self.data["cnt_4hours_later_total"]
        cnt_4hours_later_last: int = self.data["cnt_4hours_later_last"]
        total_letters_total: int = self.data["total_letters_total"]
        total_letters_last: int = self.data["total_letters_last"]
        received_total: int = self.data["received_total"]
        received_last: int = self.data["received_last"]
        answer_total: int = self.data["answer_total"]
        answer_last: int = self.data["answer_last"]
        out_work_email_total: int = self.data["out_work_email_total"]
        out_work_email_last: int = self.data["out_work_email_last"]
        external_email_total: int = self.data["external_email_total"]
        external_email_last: int = self.data["external_email_last"]
        internal_email_total: int = self.data["internal_email_total"]
        internal_email_last: int = self.data["internal_email_last"]
        cnt_addressees: int = self.data["cnt_addressees"]
        cnt_address_copy_total: int = self.data["cnt_address_copy_total"]
        cnt_address_copy_last: int = self.data["cnt_address_copy_last"]
        cnt_address_hidden_copy_total: int = self.data["cnt_address_hidden_copy_total"]
        cnt_address_hidden_copy_last: int = self.data["cnt_address_hidden_copy_last"]
        div_bytes_emails: int = self.data["div_bytes_emails"]
        cnt_question_incoming: int = self.data["cnt_question_incoming"]
        cnt_text_mean_total: float = self.data["cnt_text_mean_total"]
        cnt_text_mean_last: float = self.data["cnt_text_mean_last"]

        try:
            email: Email = await self.store.emails.create_email(
                user_id=user_id,
                date=date,
                use_email_total=use_email_total,
                active_use_email=active_use_email,
                use_email_last=use_email_last,
                out_work_internal_email_total=out_work_internal_email_total,
                out_work_internal_email_last=out_work_internal_email_last,
                out_work_external_email_total=out_work_external_email_total,
                out_work_external_email_last=out_work_external_email_last,
                cnt_days_pause_total=cnt_days_pause_total,
                cnt_days_pause_last=cnt_days_pause_last,
                cnt_4hours_later_total=cnt_4hours_later_total,
                cnt_4hours_later_last=cnt_4hours_later_last,
                total_letters_total=total_letters_total,
                total_letters_last=total_letters_last,
                received_total=received_total,
                received_last=received_last,
                answer_total=answer_total,
                answer_last=answer_last,
                out_work_email_total=out_work_email_total,
                out_work_email_last=out_work_email_last,
                external_email_total=external_email_total,
                external_email_last=external_email_last,
                internal_email_total=internal_email_total,
                internal_email_last=internal_email_last,
                cnt_addressees=cnt_addressees,
                cnt_address_copy_total=cnt_address_copy_total,
                cnt_address_copy_last=cnt_address_copy_last,
                cnt_address_hidden_copy_total=cnt_address_hidden_copy_total,
                cnt_address_hidden_copy_last=cnt_address_hidden_copy_last,
                div_bytes_emails=div_bytes_emails,
                cnt_question_incoming=cnt_question_incoming,
                cnt_text_mean_total=cnt_text_mean_total,
                cnt_text_mean_last=cnt_text_mean_last,
            )

        except exc.IntegrityError as e:
            if "23505" in e.orig.pgcode:
                raise HTTPConflict

        return json_response(data=EmailResponseSchema().dump(email))


class EmailListAddView(AuthUserRequiredMixin, View):
    @request_schema(EmailListRequestSchema)
    @response_schema(EmailListResponseSchema, 200)
    @docs(
        tags=["emails"],
        summary="Add email list add view",
        description="Add email list to database",
    )
    async def post(self) -> Response:
        emails: List = self.data["emails"]
        try:
            emails = await self.store.emails.create_email_all(
                emails=emails,
            )

        except exc.IntegrityError as e:
            if "23505" in e.orig.pgcode:
                raise HTTPConflict

        return json_response(EmailListResponseSchema().dump({"emails": emails}))


class EmailDeleteView(AuthUserRequiredMixin, View):  # AuthRequiredMixin,
    @request_schema(EmailDeleteRequestSchema)
    @response_schema(EmailResponseSchema, 200)
    @docs(
        tags=["emails"],
        summary="Add email delete view",
        description="Delete email from database",
    )
    async def get(self) -> Response:
        row_id: int = self.data["row_id"]
        email: Email = await self.store.emails.delete_email(row_id=row_id)

        return json_response(EmailResponseSchema().dump(email))


class EmailListView(AuthUserRequiredMixin, View):  # AuthRequiredMixin,
    @response_schema(EmailListResponseSchema, 200)
    @docs(
        tags=["emails"],
        summary="Add email list view",
        description="Get list emails from database",
    )
    async def get(self) -> Response:
        emails: List[Optional[Email]] = await self.store.emails.list_emails()
        return json_response(EmailListResponseSchema().dump({"emails": emails}))


class EmailUserListView(AuthUserRequiredMixin, View):  # AuthRequiredMixin,
    @request_schema(EmailUserRequestSchema)
    @response_schema(EmailListResponseSchema, 200)
    @docs(
        tags=["emails"],
        summary="Add email user list view",
        description="Get list user emails from database",
    )
    async def get(self) -> Response:
        user_id: int = self.data["user_id"]
        week: int = self.data["week"]
        emails: List[Optional[Email]] = await self.store.emails.list_user_emails(
            user_id=user_id, week=week
        )

        return json_response(EmailListResponseSchema().dump({"emails": emails}))

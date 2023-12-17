from typing import List, Optional
from datetime import datetime
from sqlalchemy import select, update, delete
from sqlalchemy.orm import joinedload

from app.emails.models import Email, EmailModel
from app.base.base_accessor import BaseAccessor


class EmailAccessor(BaseAccessor):
    async def get_by_email(self, row_id: int) -> Optional[Email]:
        async with self.app.database.session() as session:
            query = select(EmailModel).where(EmailModel.row_id == row_id)
            email: Optional[EmailModel] = await session.scalar(query)

        if not email:
            return None

        return Email(
            row_id=email.row_id,
            user_id=email.user_id,
            date=email.date,
            use_email_total=email.use_email_total,
            active_use_email=email.active_use_email,
            use_email_last=email.use_email_last,
            out_work_internal_email_total=email.out_work_internal_email_total,
            out_work_internal_email_last=email.out_work_internal_email_last,
            out_work_external_email_total=email.out_work_external_email_total,
            out_work_external_email_last=email.out_work_external_email_last,
            cnt_days_pause_total=email.cnt_days_pause_total,
            cnt_days_pause_last=email.cnt_days_pause_last,
            cnt_4hours_later_total=email.cnt_4hours_later_total,
            cnt_4hours_later_last=email.cnt_4hours_later_last,
            total_letters_total=email.total_letters_total,
            total_letters_last=email.total_letters_last,
            received_total=email.received_total,
            received_last=email.received_last,
            answer_total=email.answer_total,
            answer_last=email.answer_last,
            out_work_email_total=email.out_work_email_total,
            out_work_email_last=email.out_work_email_last,
            external_email_total=email.external_email_total,
            external_email_last=email.external_email_last,
            internal_email_total=email.internal_email_total,
            internal_email_last=email.internal_email_last,
            cnt_addressees=email.cnt_addressees,
            cnt_address_copy_total=email.cnt_address_copy_total,
            cnt_address_copy_last=email.cnt_address_copy_last,
            cnt_address_hidden_copy_total=email.cnt_address_hidden_copy_total,
            cnt_address_hidden_copy_last=email.cnt_address_hidden_copy_last,
            div_bytes_emails=email.div_bytes_emails,
            cnt_question_incoming=email.cnt_question_incoming,
            cnt_text_mean_total=email.cnt_text_mean_total,
            cnt_text_mean_last=email.cnt_text_mean_last,
        )

    async def create_email(
        self,
        user_id: int,
        date: datetime,
        use_email_total: int,
        active_use_email: int,
        use_email_last: int,
        out_work_internal_email_total: int,
        out_work_internal_email_last: int,
        out_work_external_email_total: int,
        out_work_external_email_last: int,
        cnt_days_pause_total: int,
        cnt_days_pause_last: int,
        cnt_4hours_later_total: int,
        cnt_4hours_later_last: int,
        total_letters_total: int,
        total_letters_last: int,
        received_total: int,
        received_last: int,
        answer_total: int,
        answer_last: int,
        out_work_email_total: int,
        out_work_email_last: int,
        external_email_total: int,
        external_email_last: int,
        internal_email_total: int,
        internal_email_last: int,
        cnt_addressees: int,
        cnt_address_copy_total: int,
        cnt_address_copy_last: int,
        cnt_address_hidden_copy_total: int,
        cnt_address_hidden_copy_last: int,
        div_bytes_emails: int,
        cnt_question_incoming: int,
        cnt_text_mean_total: float,
        cnt_text_mean_last: float,
    ) -> Optional[Email]:
        new_email: Email = EmailModel(
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
        async with self.app.database.session.begin() as session:
            session.add(new_email)

        return Email(
            row_id=new_email.row_id,
            user_id=new_email.user_id,
            date=new_email.date,
            use_email_total=new_email.use_email_total,
            active_use_email=new_email.active_use_email,
            use_email_last=new_email.use_email_last,
            out_work_internal_email_total=new_email.out_work_internal_email_total,
            out_work_internal_email_last=new_email.out_work_internal_email_last,
            out_work_external_email_total=new_email.out_work_external_email_total,
            out_work_external_email_last=new_email.out_work_external_email_last,
            cnt_days_pause_total=new_email.cnt_days_pause_total,
            cnt_days_pause_last=new_email.cnt_days_pause_last,
            cnt_4hours_later_total=new_email.cnt_4hours_later_total,
            cnt_4hours_later_last=new_email.cnt_4hours_later_last,
            total_letters_total=new_email.total_letters_total,
            total_letters_last=new_email.total_letters_last,
            received_total=new_email.received_total,
            received_last=new_email.received_last,
            answer_total=new_email.answer_total,
            answer_last=new_email.answer_last,
            out_work_email_total=new_email.out_work_email_total,
            out_work_email_last=new_email.out_work_email_last,
            external_email_total=new_email.external_email_total,
            external_email_last=new_email.external_email_last,
            internal_email_total=new_email.internal_email_total,
            internal_email_last=new_email.internal_email_last,
            cnt_addressees=new_email.cnt_addressees,
            cnt_address_copy_total=new_email.cnt_address_copy_total,
            cnt_address_copy_last=new_email.cnt_address_copy_last,
            cnt_address_hidden_copy_total=new_email.cnt_address_hidden_copy_total,
            cnt_address_hidden_copy_last=new_email.cnt_address_hidden_copy_last,
            div_bytes_emails=new_email.div_bytes_emails,
            cnt_question_incoming=new_email.cnt_question_incoming,
            cnt_text_mean_total=new_email.cnt_text_mean_total,
            cnt_text_mean_last=new_email.cnt_text_mean_last,
        )

    async def create_email_all(
        self,
        emails,
    ) -> Optional[Email]:
        new_emails = [
            EmailModel(
                user_id=email["user_id"],
                date=email["date"],
                use_email_total=email["use_email_total"],
                active_use_email=email["active_use_email"],
                use_email_last=email["use_email_last"],
                out_work_internal_email_total=email["out_work_internal_email_total"],
                out_work_internal_email_last=email["out_work_internal_email_last"],
                out_work_external_email_total=email["out_work_external_email_total"],
                out_work_external_email_last=email["out_work_external_email_last"],
                cnt_days_pause_total=email["cnt_days_pause_total"],
                cnt_days_pause_last=email["cnt_days_pause_last"],
                cnt_4hours_later_total=email["cnt_4hours_later_total"],
                cnt_4hours_later_last=email["cnt_4hours_later_last"],
                total_letters_total=email["total_letters_total"],
                total_letters_last=email["total_letters_last"],
                received_total=email["received_total"],
                received_last=email["received_last"],
                answer_total=email["answer_total"],
                answer_last=email["answer_last"],
                out_work_email_total=email["out_work_email_total"],
                out_work_email_last=email["out_work_email_last"],
                external_email_total=email["external_email_total"],
                external_email_last=email["external_email_last"],
                internal_email_total=email["internal_email_total"],
                internal_email_last=email["internal_email_last"],
                cnt_addressees=email["cnt_addressees"],
                cnt_address_copy_total=email["cnt_address_copy_total"],
                cnt_address_copy_last=email["cnt_address_copy_last"],
                cnt_address_hidden_copy_total=email["cnt_address_hidden_copy_total"],
                cnt_address_hidden_copy_last=email["cnt_address_hidden_copy_last"],
                div_bytes_emails=email["div_bytes_emails"],
                cnt_question_incoming=email["cnt_question_incoming"],
                cnt_text_mean_total=email["cnt_text_mean_total"],
                cnt_text_mean_last=email["cnt_text_mean_last"],
            )
            for email in emails
        ]

        async with self.app.database.session.begin() as session:
            session.add_all(new_emails)

        return [
            Email(
                row_id=new_email.row_id,
                user_id=new_email.user_id,
                date=new_email.date,
                use_email_total=new_email.use_email_total,
                active_use_email=new_email.active_use_email,
                use_email_last=new_email.use_email_last,
                out_work_internal_email_total=new_email.out_work_internal_email_total,
                out_work_internal_email_last=new_email.out_work_internal_email_last,
                out_work_external_email_total=new_email.out_work_external_email_total,
                out_work_external_email_last=new_email.out_work_external_email_last,
                cnt_days_pause_total=new_email.cnt_days_pause_total,
                cnt_days_pause_last=new_email.cnt_days_pause_last,
                cnt_4hours_later_total=new_email.cnt_4hours_later_total,
                cnt_4hours_later_last=new_email.cnt_4hours_later_last,
                total_letters_total=new_email.total_letters_total,
                total_letters_last=new_email.total_letters_last,
                received_total=new_email.received_total,
                received_last=new_email.received_last,
                answer_total=new_email.answer_total,
                answer_last=new_email.answer_last,
                out_work_email_total=new_email.out_work_email_total,
                out_work_email_last=new_email.out_work_email_last,
                external_email_total=new_email.external_email_total,
                external_email_last=new_email.external_email_last,
                internal_email_total=new_email.internal_email_total,
                internal_email_last=new_email.internal_email_last,
                cnt_addressees=new_email.cnt_addressees,
                cnt_address_copy_total=new_email.cnt_address_copy_total,
                cnt_address_copy_last=new_email.cnt_address_copy_last,
                cnt_address_hidden_copy_total=new_email.cnt_address_hidden_copy_total,
                cnt_address_hidden_copy_last=new_email.cnt_address_hidden_copy_last,
                div_bytes_emails=new_email.div_bytes_emails,
                cnt_question_incoming=new_email.cnt_question_incoming,
                cnt_text_mean_total=new_email.cnt_text_mean_total,
                cnt_text_mean_last=new_email.cnt_text_mean_last,
            )
            for new_email in new_emails
        ]

    async def delete_email(self, row_id: int) -> Optional[Email]:
        query = (
            delete(EmailModel).where(EmailModel.row_id == row_id).returning(EmailModel)
        )

        async with self.app.database.session.begin() as session:
            email = await session.scalar(query)

        if not email:
            return None

        return Email(
            row_id=email.row_id,
            user_id=email.user_id,
            date=email.date,
            use_email_total=email.use_email_total,
            active_use_email=email.active_use_email,
            use_email_last=email.use_email_last,
            out_work_internal_email_total=email.out_work_internal_email_total,
            out_work_internal_email_last=email.out_work_internal_email_last,
            out_work_external_email_total=email.out_work_external_email_total,
            out_work_external_email_last=email.out_work_external_email_last,
            cnt_days_pause_total=email.cnt_days_pause_total,
            cnt_days_pause_last=email.cnt_days_pause_last,
            cnt_4hours_later_total=email.cnt_4hours_later_total,
            cnt_4hours_later_last=email.cnt_4hours_later_last,
            total_letters_total=email.total_letters_total,
            total_letters_last=email.total_letters_last,
            received_total=email.received_total,
            received_last=email.received_last,
            answer_total=email.answer_total,
            answer_last=email.answer_last,
            out_work_email_total=email.out_work_email_total,
            out_work_email_last=email.out_work_email_last,
            external_email_total=email.external_email_total,
            external_email_last=email.external_email_last,
            internal_email_total=email.internal_email_total,
            internal_email_last=email.internal_email_last,
            cnt_addressees=email.cnt_addressees,
            cnt_address_copy_total=email.cnt_address_copy_total,
            cnt_address_copy_last=email.cnt_address_copy_last,
            cnt_address_hidden_copy_total=email.cnt_address_hidden_copy_total,
            cnt_address_hidden_copy_last=email.cnt_address_hidden_copy_last,
            div_bytes_emails=email.div_bytes_emails,
            cnt_question_incoming=email.cnt_question_incoming,
            cnt_text_mean_total=email.cnt_text_mean_total,
            cnt_text_mean_last=email.cnt_text_mean_last,
        )

    async def list_user_emails(self, user_id: int, week: int) -> List[Optional[Email]]:
        query = select(EmailModel).where(EmailModel.user_id == user_id)

        if week:
            query = query.where(EmailModel.week == week)

        async with self.app.database.session() as session:
            emails = await session.scalars(query)

        if not emails:
            return []

        return [
            Email(
                row_id=email.row_id,
                user_id=email.user_id,
                date=email.date,
                use_email_total=email.use_email_total,
                active_use_email=email.active_use_email,
                use_email_last=email.use_email_last,
                out_work_internal_email_total=email.out_work_internal_email_total,
                out_work_internal_email_last=email.out_work_internal_email_last,
                out_work_external_email_total=email.out_work_external_email_total,
                out_work_external_email_last=email.out_work_external_email_last,
                cnt_days_pause_total=email.cnt_days_pause_total,
                cnt_days_pause_last=email.cnt_days_pause_last,
                cnt_4hours_later_total=email.cnt_4hours_later_total,
                cnt_4hours_later_last=email.cnt_4hours_later_last,
                total_letters_total=email.total_letters_total,
                total_letters_last=email.total_letters_last,
                received_total=email.received_total,
                received_last=email.received_last,
                answer_total=email.answer_total,
                answer_last=email.answer_last,
                out_work_email_total=email.out_work_email_total,
                out_work_email_last=email.out_work_email_last,
                external_email_total=email.external_email_total,
                external_email_last=email.external_email_last,
                internal_email_total=email.internal_email_total,
                internal_email_last=email.internal_email_last,
                cnt_addressees=email.cnt_addressees,
                cnt_address_copy_total=email.cnt_address_copy_total,
                cnt_address_copy_last=email.cnt_address_copy_last,
                cnt_address_hidden_copy_total=email.cnt_address_hidden_copy_total,
                cnt_address_hidden_copy_last=email.cnt_address_hidden_copy_last,
                div_bytes_emails=email.div_bytes_emails,
                cnt_question_incoming=email.cnt_question_incoming,
                cnt_text_mean_total=email.cnt_text_mean_total,
                cnt_text_mean_last=email.cnt_text_mean_last,
            )
            for email in emails.all()
        ]

    async def list_emails(self) -> List[Optional[Email]]:
        query = select(EmailModel)

        async with self.app.database.session() as session:
            emails: List[Optional[EmailModel]] = await session.scalars(query)

        if not emails:
            return []
        return [
            Email(
                row_id=email.row_id,
                user_id=email.user_id,
                date=email.date,
                use_email_total=email.use_email_total,
                active_use_email=email.active_use_email,
                use_email_last=email.use_email_last,
                out_work_internal_email_total=email.out_work_internal_email_total,
                out_work_internal_email_last=email.out_work_internal_email_last,
                out_work_external_email_total=email.out_work_external_email_total,
                out_work_external_email_last=email.out_work_external_email_last,
                cnt_days_pause_total=email.cnt_days_pause_total,
                cnt_days_pause_last=email.cnt_days_pause_last,
                cnt_4hours_later_total=email.cnt_4hours_later_total,
                cnt_4hours_later_last=email.cnt_4hours_later_last,
                total_letters_total=email.total_letters_total,
                total_letters_last=email.total_letters_last,
                received_total=email.received_total,
                received_last=email.received_last,
                answer_total=email.answer_total,
                answer_last=email.answer_last,
                out_work_email_total=email.out_work_email_total,
                out_work_email_last=email.out_work_email_last,
                external_email_total=email.external_email_total,
                external_email_last=email.external_email_last,
                internal_email_total=email.internal_email_total,
                internal_email_last=email.internal_email_last,
                cnt_addressees=email.cnt_addressees,
                cnt_address_copy_total=email.cnt_address_copy_total,
                cnt_address_copy_last=email.cnt_address_copy_last,
                cnt_address_hidden_copy_total=email.cnt_address_hidden_copy_total,
                cnt_address_hidden_copy_last=email.cnt_address_hidden_copy_last,
                div_bytes_emails=email.div_bytes_emails,
                cnt_question_incoming=email.cnt_question_incoming,
                cnt_text_mean_total=email.cnt_text_mean_total,
                cnt_text_mean_last=email.cnt_text_mean_last,
            )
            for email in emails.all()
        ]

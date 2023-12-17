from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, ForeignKey, Boolean, String, Float, DateTime
from sqlalchemy.orm import relationship

from app.store.database.sqlalchemy_base import db


@dataclass
class Email:
    row_id: Optional[int]
    user_id: int
    date: datetime
    use_email_total: int
    active_use_email: int
    use_email_last: int
    out_work_internal_email_total: int
    out_work_internal_email_last: int
    out_work_external_email_total: int
    out_work_external_email_last: int
    cnt_days_pause_total: int
    cnt_days_pause_last: int
    cnt_4hours_later_total: int
    cnt_4hours_later_last: int
    total_letters_total: int
    total_letters_last: int
    received_total: int
    received_last: int
    answer_total: int
    answer_last: int
    out_work_email_total: int
    out_work_email_last: int
    external_email_total: int
    external_email_last: int
    internal_email_total: int
    internal_email_last: int
    cnt_addressees: int
    cnt_address_copy_total: int
    cnt_address_copy_last: int
    cnt_address_hidden_copy_total: int
    cnt_address_hidden_copy_last: int
    div_bytes_emails: int
    cnt_question_incoming: int
    cnt_text_mean_total: float
    cnt_text_mean_last: float


class EmailModel(db):
    __tablename__ = "emails"
    row_id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"))
    date = Column(DateTime(timezone=True), server_default=func.now())
    use_email_total = Column(Integer)
    active_use_email = Column(Integer)
    use_email_last = Column(Integer)
    out_work_internal_email_total = Column(Integer)
    out_work_internal_email_last = Column(Integer)
    out_work_external_email_total = Column(Integer)
    out_work_external_email_last = Column(Integer)
    cnt_days_pause_total = Column(Integer)
    cnt_days_pause_last = Column(Integer)
    cnt_4hours_later_total = Column(Integer)
    cnt_4hours_later_last = Column(Integer)
    total_letters_total = Column(Integer)
    total_letters_last = Column(Integer)
    received_total = Column(Integer)
    received_last = Column(Integer)
    answer_total = Column(Integer)
    answer_last = Column(Integer)
    out_work_email_total = Column(Integer)
    out_work_email_last = Column(Integer)
    external_email_total = Column(Integer)
    external_email_last = Column(Integer)
    internal_email_total = Column(Integer)
    internal_email_last = Column(Integer)
    cnt_addressees = Column(Integer)
    cnt_address_copy_total = Column(Integer)
    cnt_address_copy_last = Column(Integer)
    cnt_address_hidden_copy_total = Column(Integer)
    cnt_address_hidden_copy_last = Column(Integer)
    div_bytes_emails = Column(Integer)
    cnt_question_incoming = Column(Integer)
    cnt_text_mean_total = Column(Float)
    cnt_text_mean_last = Column(Float)
    user = relationship("UserModel", back_populates="email_list")

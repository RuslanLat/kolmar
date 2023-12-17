"""update user  models

Revision ID: a8088d793e3e
Revises: f79599f2564b
Create Date: 2023-12-15 19:18:04.280153

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a8088d793e3e'
down_revision: Union[str, None] = 'f79599f2564b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    
    op.add_column('emails', sa.Column('date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    op.add_column('emails', sa.Column('use_email_total', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('active_use_email', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('use_email_last', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('out_work_internal_email_total', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('out_work_internal_email_last', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('out_work_external_email_total', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('out_work_external_email_last', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('cnt_days_pause_total', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('cnt_days_pause_last', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('cnt_4hours_later_total', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('cnt_4hours_later_last', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('total_letters_total', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('total_letters_last', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('received_total', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('received_last', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('answer_total', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('answer_last', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('out_work_email_total', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('out_work_email_last', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('external_email_total', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('external_email_last', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('internal_email_total', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('internal_email_last', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('cnt_addressees', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('cnt_address_copy_total', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('cnt_address_copy_last', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('cnt_address_hidden_copy_total', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('cnt_address_hidden_copy_last', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('div_bytes_emails', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('cnt_question_incoming', sa.Integer(), nullable=True))
    op.add_column('emails', sa.Column('cnt_text_mean_total', sa.Float(), nullable=True))
    op.add_column('emails', sa.Column('cnt_text_mean_last', sa.Float(), nullable=True))
    op.drop_column('emails', 'is_inner')
    op.drop_column('emails', 'get_message')
    op.drop_column('emails', 'hidden_copy')
    op.drop_column('emails', 'later_read')
    op.drop_column('emails', 'byte_ratio')
    op.drop_column('emails', 'addresses')
    op.drop_column('emails', 'pause_read')
    op.drop_column('emails', 'answer')
    op.drop_column('emails', 'copy')
    op.drop_column('emails', 'not_send_question_count')
    op.drop_column('emails', 'message_len')
    op.drop_column('emails', 'week')
    op.drop_column('emails', 'not_work_day_send')
    op.drop_column('emails', 'send_message')
    op.drop_column('emails', 'message_ratio')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_bots', type_='foreignkey')
    op.alter_column('user_bots', 'user_id',
               existing_type=sa.Integer(),
               type_=sa.BIGINT(),
               existing_nullable=True)
    op.alter_column('user_bots', 'id',
               existing_type=sa.Integer(),
               type_=sa.BIGINT(),
               nullable=True,
               autoincrement=True)
    op.drop_constraint(None, 'subdivision_bots', type_='foreignkey')
    op.alter_column('subdivision_bots', 'link',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=True)
    op.alter_column('subdivision_bots', 'telegram_id',
               existing_type=sa.Integer(),
               type_=sa.BIGINT(),
               existing_nullable=True)
    op.alter_column('subdivision_bots', 'subdivision_id',
               existing_type=sa.Integer(),
               type_=sa.BIGINT(),
               existing_nullable=True)
    op.alter_column('subdivision_bots', 'id',
               existing_type=sa.Integer(),
               type_=sa.BIGINT(),
               nullable=True,
               autoincrement=True)
    op.add_column('emails', sa.Column('message_ratio', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('emails', sa.Column('send_message', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('emails', sa.Column('not_work_day_send', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('emails', sa.Column('week', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('emails', sa.Column('message_len', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('emails', sa.Column('not_send_question_count', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('emails', sa.Column('copy', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('emails', sa.Column('answer', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('emails', sa.Column('pause_read', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('emails', sa.Column('addresses', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('emails', sa.Column('byte_ratio', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('emails', sa.Column('later_read', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('emails', sa.Column('hidden_copy', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('emails', sa.Column('get_message', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('emails', sa.Column('is_inner', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('emails', 'cnt_text_mean_last')
    op.drop_column('emails', 'cnt_text_mean_total')
    op.drop_column('emails', 'cnt_question_incoming')
    op.drop_column('emails', 'div_bytes_emails')
    op.drop_column('emails', 'cnt_address_hidden_copy_last')
    op.drop_column('emails', 'cnt_address_hidden_copy_total')
    op.drop_column('emails', 'cnt_address_copy_last')
    op.drop_column('emails', 'cnt_address_copy_total')
    op.drop_column('emails', 'cnt_addressees')
    op.drop_column('emails', 'internal_email_last')
    op.drop_column('emails', 'internal_email_total')
    op.drop_column('emails', 'external_email_last')
    op.drop_column('emails', 'external_email_total')
    op.drop_column('emails', 'out_work_email_last')
    op.drop_column('emails', 'out_work_email_total')
    op.drop_column('emails', 'answer_last')
    op.drop_column('emails', 'answer_total')
    op.drop_column('emails', 'received_last')
    op.drop_column('emails', 'received_total')
    op.drop_column('emails', 'total_letters_last')
    op.drop_column('emails', 'total_letters_total')
    op.drop_column('emails', 'cnt_4hours_later_last')
    op.drop_column('emails', 'cnt_4hours_later_total')
    op.drop_column('emails', 'cnt_days_pause_last')
    op.drop_column('emails', 'cnt_days_pause_total')
    op.drop_column('emails', 'out_work_external_email_last')
    op.drop_column('emails', 'out_work_external_email_total')
    op.drop_column('emails', 'out_work_internal_email_last')
    op.drop_column('emails', 'out_work_internal_email_total')
    op.drop_column('emails', 'use_email_last')
    op.drop_column('emails', 'active_use_email')
    op.drop_column('emails', 'use_email_total')
    op.drop_column('emails', 'date')
    op.drop_constraint(None, 'department_bots', type_='foreignkey')
    op.alter_column('department_bots', 'link',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=True)
    op.alter_column('department_bots', 'telegram_id',
               existing_type=sa.Integer(),
               type_=sa.BIGINT(),
               existing_nullable=True)
    op.alter_column('department_bots', 'department_id',
               existing_type=sa.Integer(),
               type_=sa.BIGINT(),
               existing_nullable=True)
    op.alter_column('department_bots', 'id',
               existing_type=sa.Integer(),
               type_=sa.BIGINT(),
               nullable=True,
               autoincrement=True)
    # ### end Alembic commands ###

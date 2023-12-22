"""add default user bot  model

Revision ID: eb5d7c8dd2b4
Revises: a8088d793e3e
Create Date: 2023-12-21 16:04:39.785063

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eb5d7c8dd2b4'
down_revision: Union[str, None] = 'a8088d793e3e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    
    op.add_column('user_bots', sa.Column('group', sa.Integer(), nullable=True))
    
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
   
    op.drop_column('user_bots', 'group')
   
    # ### end Alembic commands ###
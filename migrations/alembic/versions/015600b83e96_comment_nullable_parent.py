"""comment-nullable-parent

Revision ID: 015600b83e96
Revises: ee9f2baad680
Create Date: 2024-08-29 18:02:39.770703

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '015600b83e96'
down_revision: Union[str, None] = 'ee9f2baad680'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comments', 'parent_id',
               existing_type=sa.UUID(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comments', 'parent_id',
               existing_type=sa.UUID(),
               nullable=False)
    # ### end Alembic commands ###

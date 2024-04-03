"""Make description nullable=False

Revision ID: d1d9836bfde3
Revises: 6520e59d7293
Create Date: 2024-04-02 19:52:21.427801

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd1d9836bfde3'
down_revision: Union[str, None] = '6520e59d7293'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('todos', 'description', nullable=False)


def downgrade() -> None:
    pass

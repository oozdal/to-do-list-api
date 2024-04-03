"""Make description Optinal

Revision ID: 8c4b752aa9ef
Revises: d1d9836bfde3
Create Date: 2024-04-02 20:03:04.054167

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c4b752aa9ef'
down_revision: Union[str, None] = 'd1d9836bfde3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('todos', 'description', nullable=True)


def downgrade() -> None:
    pass

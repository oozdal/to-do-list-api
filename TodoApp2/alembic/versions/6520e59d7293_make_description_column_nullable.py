"""Make description column nullable

Revision ID: 6520e59d7293
Revises: 
Create Date: 2024-04-02 19:31:50.524407

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6520e59d7293'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('todos', 'description', nullable=True)


def downgrade() -> None:
    pass

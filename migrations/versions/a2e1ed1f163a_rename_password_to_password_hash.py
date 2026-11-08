"""rename password to password hash

Revision ID: a2e1ed1f163a
Revises: 254261765a71
Create Date: 2026-11-05 15:19:19.667675

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2e1ed1f163a'
down_revision: Union[str, Sequence[str], None] = '254261765a71'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "users",
        "password",
        new_column_name="password_hash",
        existing_type=sa.String(length=255),
        existing_nullable=False
    )

def downgrade() -> None:
    op.alter_column(
        "users",
        "password_hash",
        new_column_name="password",
        existing_type=sa.String(length=255),
        existing_nullable=False
    )
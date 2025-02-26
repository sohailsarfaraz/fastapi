"""add user table

Revision ID: f60770fa1baf
Revises: 51b4ae45c1ea
Create Date: 2025-02-24 16:57:14.781899

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f60770fa1baf'
down_revision: Union[str, None] = '51b4ae45c1ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

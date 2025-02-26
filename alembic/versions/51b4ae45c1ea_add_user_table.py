"""add user table

Revision ID: 51b4ae45c1ea
Revises: dd8464853ae3
Create Date: 2025-02-24 15:44:50.845455

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '51b4ae45c1ea'
down_revision: Union[str, None] = 'dd8464853ae3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

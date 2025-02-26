"""add content column to posts table

Revision ID: dd8464853ae3
Revises: 352d3dfaccc0
Create Date: 2025-02-24 15:31:44.541291

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd8464853ae3'
down_revision: Union[str, None] = '352d3dfaccc0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass

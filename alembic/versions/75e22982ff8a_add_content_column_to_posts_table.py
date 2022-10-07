"""add content column to posts table

Revision ID: 75e22982ff8a
Revises: a8f5cb94b424
Create Date: 2022-10-03 13:40:21.269110

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75e22982ff8a'
down_revision = 'a8f5cb94b424'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')

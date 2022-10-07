"""add last few columns to posts table

Revision ID: bfef64804fa8
Revises: 3f24b3b222c8
Create Date: 2022-10-03 13:57:12.779501

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfef64804fa8'
down_revision = '3f24b3b222c8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
                  sa.Column('published',
                  sa.Boolean(),
                  nullable=False,
                  server_default='TRUE'))
    op.add_column('posts',
                  sa.Column('created_at',
                  sa.TIMESTAMP(timezone=True),
                  nullable=False,
                  server_default=sa.text('now()')))


def downgrade() -> None:
    op.drop_column('posts', 'created_at')
    op.drop_column('posts', 'published')

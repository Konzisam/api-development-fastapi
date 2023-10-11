"""add last few coluimns to posts table

Revision ID: d07e5d387dd5
Revises: 50c6a725cb85
Create Date: 2023-09-28 23:06:47.755268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd07e5d387dd5'
down_revision = '50c6a725cb85'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column(
        'published', sa.Boolean(), nullable=False, server_default= 'TRUE'),)
    op.add_column('posts',sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass

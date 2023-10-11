"""add content column to post

Revision ID: 7bac70052917
Revises: 97374afcc411
Create Date: 2023-09-28 22:26:41.601330

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bac70052917'
down_revision = '97374afcc411'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    # op.drop_column('posts','content')
    pass

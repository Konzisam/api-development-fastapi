"""create posts table

Revision ID: 97374afcc411
Revises: 
Create Date: 2023-09-28 20:46:01.320835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97374afcc411'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id', sa.Integer(),nullable=False, primary_key=True)
                    , sa.Column('title',sa.String(), nullable=False))
    
    pass


def downgrade():
    # op.drop_table('posts')
    pass

"""add foreign key to postes table

Revision ID: 50c6a725cb85
Revises: aa8440f72957
Create Date: 2023-09-28 22:51:40.962035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50c6a725cb85'
down_revision = 'aa8440f72957'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('posts_users_fk', source_table ="posts",referent_table="users",
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    # op.drop_constraint('post_users_fk', table_name="posts")
    # op.drop_column('posts','owner_id')
    pass

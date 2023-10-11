"""add phone number

Revision ID: a0673ba6313b
Revises: ffc991a4f141
Create Date: 2023-09-28 23:34:09.971766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0673ba6313b'
down_revision = 'ffc991a4f141'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users',sa.Column('phone_number',sa.String(),nullable=True))
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
  op.drop_column('users','phone_number')
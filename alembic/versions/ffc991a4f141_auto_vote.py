"""auto-vote

Revision ID: ffc991a4f141
Revises: d07e5d387dd5
Create Date: 2023-09-28 23:23:00.682745

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ffc991a4f141'
down_revision = 'd07e5d387dd5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('user_id',sa.Integer(),nullable=True),
    sa.Column('post_id',sa.Integer(),nullable=True),
    sa.ForeignKeyConstraint(['post_id'],['posts.id'],ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'],['users.id'],ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id','post_id')
    )



def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')

    pass
    
    # ### end Alembic commands ###

"""Initial Migration

Revision ID: 514ab3b6ae68
Revises: 
Create Date: 2018-09-07 15:33:38.553553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '514ab3b6ae68'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('roles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='roles_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='roles_pkey')
    )
    op.drop_table('pitches')
    # ### end Alembic commands ###

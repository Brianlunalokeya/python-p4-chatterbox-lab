"""generating database tables

Revision ID: 8458a99314af
Revises: 0e12555d4c52
Create Date: 2023-06-30 05:59:20.052595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8458a99314af'
down_revision = '0e12555d4c52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('created_at', sa.String(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###

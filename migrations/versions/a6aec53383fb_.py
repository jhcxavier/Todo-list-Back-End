"""empty message

Revision ID: a6aec53383fb
Revises: f8f3046d60fe
Create Date: 2019-06-12 16:23:06.597500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6aec53383fb'
down_revision = 'f8f3046d60fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo1',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('todoItem', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('todoItem')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo1')
    # ### end Alembic commands ###

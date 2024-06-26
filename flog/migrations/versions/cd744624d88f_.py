"""empty message

Revision ID: cd744624d88f
Revises: f697cc7b56a2
Create Date: 2024-04-24 12:50:08.789458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd744624d88f'
down_revision = 'f697cc7b56a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=110), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('slug', sa.String(length=255), nullable=True),
    sa.Column('publish_date', sa.DateTime(), nullable=True),
    sa.Column('live', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    op.drop_table('category')
    # ### end Alembic commands ###

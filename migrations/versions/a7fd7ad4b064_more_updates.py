"""more updates

Revision ID: a7fd7ad4b064
Revises: bda98856ddd2
Create Date: 2019-04-01 05:08:47.570667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7fd7ad4b064'
down_revision = 'bda98856ddd2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('price', sa.Float(), nullable=True))
    op.add_column('item', sa.Column('stock', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('item', 'stock')
    op.drop_column('item', 'price')
    # ### end Alembic commands ###

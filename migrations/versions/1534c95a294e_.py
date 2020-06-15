"""empty message

Revision ID: 1534c95a294e
Revises: 3b9d7f732d07
Create Date: 2020-06-15 17:21:32.538966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1534c95a294e'
down_revision = '3b9d7f732d07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('genres', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'genres')
    # ### end Alembic commands ###

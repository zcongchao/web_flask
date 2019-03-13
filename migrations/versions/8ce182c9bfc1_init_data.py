"""init data

Revision ID: 8ce182c9bfc1
Revises: 051691f120e6
Create Date: 2019-03-07 10:23:07.500966

"""

# revision identifiers, used by Alembic.
revision = '8ce182c9bfc1'
down_revision = '051691f120e6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('files',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=5000), nullable=False),
    sa.Column('uploadtime', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('files')
    # ### end Alembic commands ###

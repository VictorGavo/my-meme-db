"""empty message

Revision ID: 8647dfb637aa
Revises: fff59413d597
Create Date: 2023-01-21 14:39:51.623507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8647dfb637aa'
down_revision = 'fff59413d597'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=150), nullable=True))
        batch_op.drop_column('top')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('top', sa.VARCHAR(length=150), autoincrement=False, nullable=True))
        batch_op.drop_column('email')

    # ### end Alembic commands ###

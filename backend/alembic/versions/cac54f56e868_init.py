"""init

Revision ID: cac54f56e868
Revises: 9cb3078019ff
Create Date: 2021-04-10 20:13:24.978860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cac54f56e868'
down_revision = '9cb3078019ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.drop_column('function_parameters')
        batch_op.drop_column('function_type')
        batch_op.drop_column('policy_expression_name')

    with op.batch_alter_table('connections', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('connections', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)

    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.add_column(sa.Column('policy_expression_name', sa.VARCHAR(length=4000), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('function_type', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('function_parameters', sa.VARCHAR(length=4000), autoincrement=False, nullable=True))

    # ### end Alembic commands ###

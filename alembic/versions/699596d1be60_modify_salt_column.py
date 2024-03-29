"""Modify salt column

Revision ID: 699596d1be60
Revises: b22fbd82561f
Create Date: 2024-02-07 14:56:50.659614

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '699596d1be60'
down_revision: Union[str, None] = 'b22fbd82561f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('phone_number', sa.String(length=15), nullable=False),
    sa.Column('country_code', sa.String(length=5), nullable=False),
    sa.Column('password_hash', sa.String(length=256), nullable=False),
    sa.Column('salt', sa.String(length=100), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('status', sa.Enum('active', 'inactive', name='accountstatus', schema='test', inherit_schema=True), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='test'
    )
    op.create_index(op.f('ix_test_accounts_id'), 'accounts', ['id'], unique=False, schema='test')
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['test.accounts.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='test'
    )
    op.create_index(op.f('ix_test_students_id'), 'students', ['id'], unique=False, schema='test')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_test_students_id'), table_name='students', schema='test')
    op.drop_table('students', schema='test')
    op.drop_index(op.f('ix_test_accounts_id'), table_name='accounts', schema='test')
    op.drop_table('accounts', schema='test')
    # ### end Alembic commands ###

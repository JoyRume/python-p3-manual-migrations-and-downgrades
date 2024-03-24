"""Renaming students to scholars

Revision ID: 42d30813369f
Revises: 791279dd0760
Create Date: 2024-03-24 10:10:37.343595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42d30813369f'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    


def downgrade() -> None:
    op.rename_table('scholars', 'students')

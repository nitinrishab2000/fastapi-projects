"""Create phone number for user column

Revision ID: 1a24a953e2a7
Revises: 
Create Date: 2025-06-10 09:47:00.681236

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a24a953e2a7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users',sa.Column('phone_number',sa.String(),nullable=True))


def downgrade() -> None:
    pass
    # op.drop_column('users','phone_number')

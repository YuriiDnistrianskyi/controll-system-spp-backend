"""update gateway_device

Revision ID: af2532253045
Revises: 242e1fa256c9
Create Date: 2026-07-18 00:54:38.728620

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af2532253045'
down_revision: Union[str, Sequence[str], None] = '242e1fa256c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

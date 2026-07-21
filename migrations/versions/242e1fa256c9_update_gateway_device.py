"""update gateway_device

Revision ID: 242e1fa256c9
Revises: 11a3e972f168
Create Date: 2026-07-17 23:47:54.566282

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '242e1fa256c9'
down_revision: Union[str, Sequence[str], None] = '11a3e972f168'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

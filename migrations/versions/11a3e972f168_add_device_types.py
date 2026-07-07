"""add device types

Revision ID: 11a3e972f168
Revises: 85b5888d908d
Create Date: 2026-07-07 15:59:49.303281

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '11a3e972f168'
down_revision: Union[str, Sequence[str], None] = '85b5888d908d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        INSERT INTO device_type (code, type)
        VALUES
            ('FRONT_SENSOR', 'front sensor'),
            ('BACK_SENSOR', 'back sensor')
    """)


def downgrade() -> None:
    op.execute("""
        DELETE FROM device_type
        WHERE code in ('FRONT_SENSOR', 'BACK_SENSOR
    """)

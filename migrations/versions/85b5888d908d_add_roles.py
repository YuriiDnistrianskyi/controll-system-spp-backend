"""add roles

Revision ID: 85b5888d908d
Revises: 286956034186
Create Date: 2026-07-07 15:58:10.348898

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '85b5888d908d'
down_revision: Union[str, Sequence[str], None] = '286956034186'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        INSERT INTO role_type (code, type)
        VALUES
            ('ADMIN', 'administrator'),
            ('OBSERVER', 'observer')
        """
    )


def downgrade() -> None:
    op.execute("""
        DELETE FROM role_type
        WHERE code IN ('ADMIN', 'OBSERVER')
    """)
    pass


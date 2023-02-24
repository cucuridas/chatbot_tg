"""tgday user_id정보 user 테이블로 이관

Revision ID: cd28b9c7eb70
Revises: d392eca656ec
Create Date: 2023-02-24 11:06:04.831096

"""
from alembic import op
import sqlalchemy as sa
from app.core.db.base import *
from app.core.db.models.tgday import Tgday
from app.core.db.models.users import Users

# revision identifiers, used by Alembic.
revision = "cd28b9c7eb70"
down_revision = "d392eca656ec"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("user_id", sa.String(1000)))
    op.drop_column("tgday", "user_id_webex")
    pass


def downgrade() -> None:
    pass

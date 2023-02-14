"""users field 업데이트

Revision ID: 05173f5ab0bc
Revises: d392eca656ec
Create Date: 2023-02-14 19:50:18.074899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "05173f5ab0bc"
down_revision = "d392eca656ec"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(
        "users", column_name="user_id_webex", new_column_name="user_room_info"
    )


def downgrade() -> None:
    pass

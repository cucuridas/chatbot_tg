"""tgday 테이블 추가

Revision ID: 98aef1eeadc5
Revises: 30b7ed852d08
Create Date: 2023-02-13 12:38:33.210153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "98aef1eeadc5"
down_revision = "30b7ed852d08"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "tgday",
        sa.Column("user_name", sa.String(length=80), nullable=False),
        sa.Column("tgday_regist_day", sa.Date(), nullable=False),
        sa.Column("user_id_webex", sa.String(length=300), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("tgday")

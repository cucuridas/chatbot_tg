"""users database

Revision ID: 30b7ed852d08
Revises: 
Create Date: 2023-02-12 11:32:53.510956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "30b7ed852d08"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.String(length=120), autoincrement=True, nullable=False),
        sa.Column("user_name", sa.String(length=80), nullable=False),
        sa.Column("user_email", sa.String(length=300), nullable=False),
        sa.Column("user_id_webex", sa.String(length=1000)),
        sa.Column("user_team", sa.String(length=20), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("users")

"""team 테이블 추가

Revision ID: 9cd15da05631
Revises: d392eca656ec
Create Date: 2023-02-15 11:01:35.275312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9cd15da05631"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    table = op.create_table(
        "team",
        sa.Column("team_id", sa.BigInteger(), primary_key=True),
        sa.Column("team_name", sa.String(length=200), nullable=False, unique=True),
        sa.Column("team_manager_email", sa.String(length=200), nullable=False),
    )
    op.bulk_insert(
        table,
        [
            {
                "team_name": "플랫폼개발1팀",
                "team_manager_email": "",
            },
            {
                "team_name": "플랫폼개발2팀",
                "team_manager_email": "",
            },
            {
                "team_name": "플랫폼개발3팀",
                "team_manager_email": "ce.choi@time-gate.com",
            },
        ],
    )
    pass


def downgrade() -> None:
    pass

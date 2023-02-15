"""users database

Revision ID: 30b7ed852d08
Revises: 
Create Date: 2023-02-12 11:32:53.510956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "30b7ed852d08"
down_revision = "9cd15da05631"
branch_labels = None
depends_on = None


def upgrade():
    talbe = op.create_table(
        "users",
        sa.Column("id", sa.BigInteger(), primary_key=True),
        sa.Column("user_name", sa.String(length=80), nullable=False, unique=True),
        sa.Column("user_email", sa.String(length=300), nullable=False),
        sa.Column("user_room_info", sa.String(length=1000)),
        sa.Column("user_team", sa.String(length=20), nullable=False),
    )
    op.create_foreign_key(
        "update_foreign_key_user",
        "users",
        "team",
        ["user_team"],
        ["team_name"],
        ondelete="CASCADE",
    )

    op.bulk_insert(
        talbe,
        [
            {
                "user_name": "최충은",
                "user_email": "3310223@naver.com",
                "user_room_info": "",
                "user_team": "플랫폼개발3팀",
            },
            {
                "user_name": "석수민",
                "user_email": "sm.seok@time-gate.com",
                "user_room_info": "",
                "user_team": "플랫폼개발3팀",
            },
            {
                "user_name": "김훈석",
                "user_email": "kha5064@gmail.com",
                "user_room_info": "",
                "user_team": "플랫폼개발3팀",
            },
        ],
    )
    pass


def downgrade() -> None:
    op.drop_table("users")

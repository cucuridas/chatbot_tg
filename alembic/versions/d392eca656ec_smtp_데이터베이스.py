"""snmp 데이터베이스

Revision ID: d392eca656ec
Revises: 98aef1eeadc5
Create Date: 2023-02-14 12:46:39.740919

"""
from alembic import op
import sqlalchemy as sa
from app.core.config import DefaultSnmpSettings

# revision identifiers, used by Alembic.
revision = "d392eca656ec"
down_revision = "98aef1eeadc5"
branch_labels = None
depends_on = None


def upgrade() -> None:
    table = op.create_table(
        "smtpinfo",
        sa.Column("id", sa.BigInteger(), primary_key=True),
        sa.Column("send_mail", sa.String(length=200), nullable=False),
        sa.Column("send_password", sa.String(length=200), nullable=False),
        sa.Column("smtp_url", sa.String(length=200), nullable=False),
        sa.Column("smtp_port", sa.Integer(), nullable=False),
        sa.Column("receive_mail", sa.String(length=200), nullable=False),
    )

    op.bulk_insert(
        table,
        [
            {
                "send_mail": DefaultSnmpSettings.SEND_MAIL,
                "send_password": DefaultSnmpSettings.SEND_PASSWORD,
                "smtp_url": DefaultSnmpSettings.SMTP_URL,
                "smtp_port": DefaultSnmpSettings.SMTP_PORT,
                "receive_mail": DefaultSnmpSettings.RECEIVE_MAIL,
            }
        ],
    )


def downgrade() -> None:
    op.drop_table("snmpinfo")

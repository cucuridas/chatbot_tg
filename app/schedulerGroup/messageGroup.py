from rocketry import Grouper
from rocketry.conds import cron, after_success
from app.connection.smtp import Smtp

group: Grouper = Grouper()


@group.task("every 1 minute")
def send_mail():
    Smtp.getConnection()


@group.task(after_success(send_mail))
async def do_after():
    pass


@group.task(cron("1 * * * *"))
def print_():
    print("잉 기모링~")

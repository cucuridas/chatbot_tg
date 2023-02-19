from datetime import datetime


class CreateDatetime:
    def today():
        today = datetime.now()
        date = {
            "year": today.year,
            "month": today.month,
            "day": today.day,
            "hour": today.hour,
            "minute": today.minute,
            "second": today.second,
        }

        return date

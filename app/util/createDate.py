from datetime import datetime, timedelta


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

    def todayToWeek(y, m, d):
        def _ymd_to_datetime(y, m, d):  # 3
            s = f"{y:04d}-{m:02d}-{d:02d}"
            return datetime.strptime(s, "%Y-%m-%d")

        target_day = _ymd_to_datetime(y, m, d)  # 4
        firstday = target_day.replace(day=1)  # 5
        while firstday.weekday() != 0:  # 6
            firstday += timedelta(days=1)

        if target_day < firstday:  # 7
            return 0

        return (target_day - firstday).days // 7 + 2  # 8

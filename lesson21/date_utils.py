from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

class DateUtils:
    """Helper class for working with dates"""

    @staticmethod
    def compare_two_dates(date1: str, date2: str, date_format: str = "%Y-%m-%d"):
        d1 = datetime.strptime(date1, date_format)
        d2 = datetime.strptime(date2, date_format)
        return d1 == d2

    @staticmethod
    def compare_n_dates(dates: list[str], date_format: str = "%Y-%m-%d"):
        parsed_dates = [datetime.strptime(date, date_format) for date in dates]
        return all(d == parsed_dates[0] for d in parsed_dates)

    @staticmethod
    def add_days_to_date(date: str, days: int, date_format: str = "%Y-%m-%d"):
        d1 = datetime.strptime(date, date_format)
        new_date = d1 + timedelta(days=days)
        return new_date

    @staticmethod
    def convert_to_timezone(date: str, from_tz: str, to_tz: str, date_format: str = "%Y-%m-%d %H:%M:%S"):
        from_zone = ZoneInfo(from_tz)
        to_zone = ZoneInfo(to_tz)
        dt = datetime.strptime(date, date_format).replace(tzinfo=from_zone)
        converted = dt.astimezone(to_zone)
        return converted.strftime(date_format)

    @staticmethod
    def get_current_time_in_timezone(tz_name: str, date_format: str = "%Y-%m-%d %H:%M:%S"):
        tz = ZoneInfo(tz_name)
        d = datetime.now(tz)
        return d.strftime(date_format)


if __name__ == "__main__":
    result = DateUtils.compare_n_dates(["2024-09-01", "2024-09-08", "2024-09-01"])
    assert result is False
    result = DateUtils.convert_to_timezone("2024-09-01 22:00:00", "Europe/Kyiv", "Hongkong")
    print(result)
    result = DateUtils.get_current_time_in_timezone("Hongkong")
    print(result)
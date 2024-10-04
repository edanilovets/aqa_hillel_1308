from datetime import datetime
import pytz

class DateUtils:

    _base_timezone = "UTC"  # class attribute

    @staticmethod
    def format_date(date_str: str, current_format: str, target_format: str):
        try:
            date_obj = datetime.strptime(date_str, current_format)
            return date_obj.strftime(target_format)
        except ValueError:
            pass


    @classmethod
    def set_base_timezone(cls, timezone: str):
        if timezone in pytz.all_timezones:
            cls._base_timezone = timezone
        else:
            raise ValueError(f"Invalid timezone {timezone}")

    @classmethod
    def get_base_timezone(cls):
        return cls._base_timezone


class DateAssertions:

    @staticmethod
    def validate_date(date_str: str, date_format: str = "%Y-%m-%d"):
        try:
            datetime.strptime(date_str, date_format)
            return True
        except ValueError:
            return False

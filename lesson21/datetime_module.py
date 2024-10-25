# epoch

from datetime import datetime, timedelta, timezone

timestamp = 1632323313
dt = datetime.fromtimestamp(timestamp)
print("Converted date:", dt)

# Use case 1 - fromtimestamp, timestamp
# Validate token expiration date
def is_token_expired(expiration_timestamp):
    """Checks if token expired"""
    expiration_date = datetime.fromtimestamp(expiration_timestamp)
    current_date = datetime.now()

    return current_date > expiration_date

is_expired = is_token_expired(datetime.now().timestamp() + 5)
print("Is expired:", is_expired)

# Use case 2 - timedelta
# Schedule test
def schedule_test(days_in_future):
    future_date = datetime.now() + timedelta(days=days_in_future)
    print(f"Test scheduled for future date: {future_date.strftime('%Y-%m-%dT%H:%M:%S.%f%z')}")
    # ...

schedule_test(3)

# Use case 3 - strptime
from datetime import datetime

time_string = '2023-12-31 23:59:59'
format_string = '%Y-%m-%d %H:%M:%S'

datetime_obj = datetime.strptime(time_string, format_string)

print(datetime_obj + timedelta(weeks=1))

# Use case 4 - working with timezones, transform UTC -> custom timezone
utc_time = datetime.now(timezone.utc)
print(utc_time)
custom_timezone = timezone(timedelta(hours=-5))
print(custom_timezone)
# local time +05:00
local_time = utc_time.astimezone(custom_timezone)
print(local_time)

# Use case 5 - compare UTC and local

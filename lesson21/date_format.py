# Use case 1, ISO 8601 datetime format
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f%z")
print(timestamp)

# Use case 2

timestamp = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
file_name = f"report_{timestamp}.html"
print(file_name)

# Use case 3

timestamp = datetime.now().strftime("%B %Y")
print(timestamp)
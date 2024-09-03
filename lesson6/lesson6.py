# import time

######################################################################
# Loops, if/else
######################################################################
# if/else/elif

age = 25
if 0 < age < 18:  # age > 0 and age < 18
    print("You are a minor")
elif 18 <= age < 65:
    print("You are an adult")
elif age >= 65:
    print("You are old")
else:
    print(f"You entered wrong age: {age}")

print("-" * 100)

element = ("button", "green", "enabled")

# some logic to interact with element
if element[0] == "button" and element[2] == "enabled":
    # clicking logic
    if element[1] == "green":
        print("Clicking the button")
        # click()
    else:
        print("Hovering the button")
        # hover()
elif element[0] == "button" and element[2] == "disabled":
    print("Clicking checkbox to enable the button")
else:
    print("Invalid element")

print("-" * 100)
######################################################################
# for loop

name = "Eugene"
names = ["Alice", "Eugene", "Bob", "Steve"]
ages = [10, 20, 30, 40]
for name in names:
    print(f"Name is {name}")
    for age in ages:
        print(f"age: {age}")
    print()
print("-" * 100)
######################################################################
# range()
# range(start, stop, step)

for i in range(5):
    print(i)
print("-" * 100)
for i in range(1, 6):
    print(i)
print("-" * 100)

for i in range(0, 10, 2):
    print(i)
print("-" * 100)

######################################################################
# _ - not used variable

for _ in range(5):
    print("Hello")

user_data = [
    ("Bob", 25, "B", "enabled"),
    ("John", 35, "C", "disabled"),
    ("Alice", 25, "B", "enabled"),
    ("Bob", 45, "D", "enabled"),
]
for name, _, category, _ in user_data:
    print(f"Username is {name}, category {category}")
    # some logic

for name, *_, status in user_data:
    print(f"Username is {name}, status {status}")
    # some logic

######################################################################
# a, b
# a = 10
# b = 20
#
# c = None
# c = b
# b = a
# a = c
#
# a, b = b, a
######################################################################
# continue, break, pass
buttons = [
    ("Upload", "green", "enabled"),
    ("Submit", "green", "enabled"),
    ("Close", "grey", "disabled"),
    ("Delete", "red", "enabled"),
    ("Delete", "red", "enabled"),
    ("Delete", "red", "enabled"),
    ("Delete", "red", "enabled"),
    ("Delete", "red", "enabled"),
    ("Delete", "red", "enabled"),
]

# Find first disabled button
found_button = None
for button in buttons:
    if button[2] == "disabled":
        found_button = button
        break
print("Found button", found_button)
# click(found_button)

# continue
input_fields = [
    {"placeholder": "Enter name", "data": "Bob"},
    {"placeholder": "Enter email", "data": "email@gmail.com"},
    {"placeholder": "Do not change", "data": "*****"},
    {"placeholder": "Enter password", "data": "*****"},
    {"placeholder": "Enter password", "data": "*****"},
]
print("-" * 100)
# Skip "Do not change placeholder"
for i in input_fields:
    if i["placeholder"] == "Do not change":
        continue
    print(f"Data {i['data']}")

for i in input_fields:
    # todo: implement later
    pass


# some method
def some_function(my_name, my_age):
    print(my_name, my_age)


some_function("Eugene", 35)

print("-" * 100)
######################################################################
# for/else loop

phones = ["iPhone X", "iPhone 11", "iPhone 12", "iPhone 12 pro", "iPhone 13 pro"]
for phone in phones:
    if phone == "iPhone 12":
        print(f"Found {phone}")
        break  # if comment this break, else will be executed
else:
    print("iPhone 12 was not found")
print("-" * 100)
######################################################################
# for (i = 0, i++, i < 10)

# NOT pythonic way
phones = ["iPhone X", "iPhone 11", "iPhone 12", "iPhone 12 pro", "iPhone 13 pro"]
for i in range(len(phones)):  # 5
    print(i, phones[i])

print("-" * 100)
# pythonic way
for i, phone in enumerate(phones):
    print(i, phone)

print("-" * 100)
######################################################################
# while

# max_retries = 5
# retry_count = 0
# server_available = False  # status of the server
#
#
# def check_server_availability():
#     # API call to the server
#     return False
#
#
# while retry_count < max_retries and not server_available:  # False and True = False
#     server_available = check_server_availability()   # API call
#     if server_available:
#         print("Server is available")
#     else:
#         retry_count += 1
#         print("Server is not available, retrying")
#         time.sleep(2)  # backoff
#
# if server_available:
#     print("Server is up")
# else:
#     print("Server is down")

######################################################################

# a = 0
# while True:
#     a += 1
#     print("Endless print...")
#     time.sleep(1)
#     if a > 5:
#         break

# while False:
#     pass
######################################################################
# List comprehension
# Dict comprehension
# Set comprehension

numbers = [1, 2, 3, 4, 5]
# create a new list with numbers squares
squared_numbers = []
for n in numbers:
    squared_numbers.append(n**2)
print(squared_numbers)

# list comprehension
print([n**2 for n in numbers])

#################
response_times_ms = [10000, 600, 500, 2500, 100, 100, 2000]
# convert to seconds if value > 1000 ms, convert value / 1000

converted_in_seconds = [resp_time / 1000 for resp_time in response_times_ms if resp_time > 1000]
print(converted_in_seconds)
print("-" * 100)
######################################################################
# nested list comprehension
user_ids = [100, 200, 300]
product_ids = [111, 222, 333]

test_cases = []
# create all combinations of user ids and products ids
for user in user_ids:
    for product in product_ids:
        test_cases.append((user, product))

print(test_cases)

# comprehension
test_cases = [(user, product) for user in user_ids for product in product_ids]
print(test_cases)

######################################################################
# Set comprehension
test_cases = {(user, product) for user in user_ids for product in product_ids}
print(test_cases)

######################################################################
# Dict comprehension
# map(), filler(), reduce() - old ways

api_response = [
    {
        "name": "Eugene",
        "age": 35,
        "email": "myemail@gmail.com",
        "address": {
            "street": "Jones st.",
            "postal_code": 13132
        }
    },
    {
        "name": "John0",
        "age": 25,
        "email": "john@gmail.com",
        "address": None
    },
    {
        "name": "John1",
        "age": 55,
        "email": "john@gmail.com",
        "address": None
    },
    {
        "name": "John2",
        "age": 20,
        "email": "john@gmail.com",
        "address": None
    }
]

# Filter users with age >= 20
senior_users = {resp["name"]: resp["email"] for resp in api_response if resp["age"] > 20}
print(senior_users)
######################################################################
# sorted
fruits = [
    ("apple", "green", 2),
    ("apple", "red", 34),
    ("apple", "yellow", 0),
    ("pear", "green", 23),
    ("pear", "yellow", 11),
    ("plum", "yellow", 13),
    ("plum", "red", 2)
]
sorted_fruits = sorted(fruits)
print(sorted_fruits)

sorted_fruits = sorted(fruits, key=lambda k: k[2])
print(sorted_fruits)

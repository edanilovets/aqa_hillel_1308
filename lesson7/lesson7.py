#############################################################
# functions

#############################################################

age = 20
is_user_has_access = True if age > 20 else False


#############################################################

def greet():
    # function body
    print("Hello Python")



message = greet()
print(message)
greet()
greet()


def greet(name, surname):
    # function body
    return f"Hello {name} {surname}"


message = greet("Eugene", "Danilovets")
print(message)
print("-" * 100)
#############################################################
# any(), all()

print(all([True, True, True]))  # True
print(all([True, True, False]))  # False


print(any([True, True, False]))  # False
print(any([False, False, False]))  # True

api_response = [
    {"username": "Eugene", "email": "email@test.com", "is_active": True},
    {"username": "Bob", "email": "email@test.com", "is_active": False},
    {"username": "Alice", "email": "email@test.com", "is_active": True},
    {"username": "Alice", "email": "email@test.com", "is_active": False}
]

are_emails_valid = all("@" in user["email"] for user in api_response)
print("Are emails valid:", are_emails_valid)

is_at_least_one_active = any(user["is_active"] for user in api_response)
print("At least one active:", is_at_least_one_active)
#############################################################
# bin(), hex()
print(bin(255))
print(bin(256))
print(hex(256))
#############################################################
# bytearray()
# url = "example.com/image1.jpeg"
# # image_data = bytearray(requests.get(url).content)
#
# png_signature = bytearray([130, 10, 10, 10])
# jpeg_signature = bytearray([130, 10, 10, 10])
# if image_data[:8] == png_signature:
#     print("This is png")
#     # some logic
#     # upload it in form
# else:
#     print("Reduce the size")
print("-" * 100)
#############################################################
# callable()


def greet():
    # function body
    print("Hello Python")


print(type(greet))
print(callable(greet))
print(callable(age))

greeting_method = greet
greeting_method()
#############################################################
# chr()
print(chr(65))
print(chr(66))
print(chr(67))
print(chr(91))
print("-" * 100)
#############################################################
# dir()
age = 20
print(dir(age))
print(dir(greet))
#############################################################
# enumerate()

fruits = ["apple", "pear", "banana", "banana"]
enumerate_fruits = list(enumerate(fruits))
enumerate_fruits1 = set(enumerate(fruits))
print(enumerate_fruits)
print(enumerate_fruits1)

for index, fruit in enumerate(fruits):
    print(f"Index {index} of {fruit}")

print("-" * 100)
#############################################################
# filter()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


prime_numbers = list(filter(is_prime, numbers))
print(prime_numbers)

numbers = [num for num in range(20)]
prime_numbers1 = list(filter(is_prime, numbers))
prime_numbers2 = [num for num in numbers if is_prime(num)]
print(prime_numbers1)
print(prime_numbers1)
#############################################################
# frozenset() vs set()

s_set = {1, 2, 3, 1, 3, 1, 4}
f_set = frozenset([1, 2, 3, 1, 3, 1, 4])
print(dir(s_set))
print(dir(f_set))
print("-" * 100)
#############################################################
# map()

words = ["hello", "world", "python", "map"]


def to_uppercase(word):
    return word.upper()


mapped_words = list(map(to_uppercase, words))
print(mapped_words)

mapped_words1 = [word.upper() for word in words]
print(mapped_words1)
#############################################################
users = [
    {"username": "Eugene", "email": "eugene@test.com"},
    {"username": "Bob", "email": "bob@test.com"}
]

def send_welcome_message(user):
    return f"Welcome {user['username']}. We have a welcome email to {user['email']}"


welcome_messages = list(map(send_welcome_message, users))
print(welcome_messages)

for message in welcome_messages:
    # verify
    # actual welcome messages
    pass
#############################################################
# zip()
emails = [
    "eugene@test.com",
    "bob@test.com",
    "bob1@test.com"
]
user_ids = [100, 101, 102]

zipped = list(zip(emails, user_ids))
print(zipped)

for email, user_id in zip(emails, user_ids):
    print(f"User ID: {user_id} with email {email}")

#############################################################
# Creation of function with default parameter


def create_user(username, user_email, role="admin", is_active=True):
    """Creates user for the portal.
    :param username: Username
    :param user_email: User email
    :param role: User role
    :param is_active: Shows user activity
    """
    user = {
        "username": username,
        "email": user_email,
        "role": role,
        "is_active": is_active
    }
    # api call to the site POST create_user...
    print(f"User created {user_email}")
    return user


create_user("John", "john@email.com")
create_user("John1", "john1@email.com", role="super admin")
create_user("John2", "john2@email.com", is_active=False)
print("-" * 100)
#############################################################
# Function scope
name = "Eugene"


def create_user_no_args():
    print("Creating user", name)


def create_user_with_args(name):
    # first looks up in inner scope
    print("Creating user with args", name)


def create_user_with_updates_arg():
    name = "Updated"
    print("Creating user with args", name)


def create_user_with_updates_arg1():
    global name
    name = "Updated"
    print("Creating user with args", name)


create_user_no_args()
create_user_with_args("Bob")
create_user_with_updates_arg()
create_user_with_updates_arg1()
print(name)

print("-" * 100)
#############################################################
# Function inside function


def calc_with_2_numbers(num1, num2, operation="+"):

    def make_calc():
        result = None
        # Operation defines ...
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "/":
            result = num1 / num2
        elif operation == "*":
            result = num1 * num2
        else:
            print("Invalid operation")
        return result

    return make_calc()


print(calc_with_2_numbers(10, 20))
print(calc_with_2_numbers(10, 20, operation="-"))

#############################################################
# add = lambda x, y: x + y
# print(add(3, 4))  # Виведе: 7

words = ["hello", "world", "python", "map"]
mapped_words = list(map(lambda w: w.upper(), words))
print(mapped_words)
#############################################################
# *args and **kwargs


def create_report(title, *args, author="Director", **kwargs):
    """Creates a report for test run"""
    print("Report title:", title)
    print("Sections included in the report:")

    for section in args:
        print(f" - {section}")

    print("Additional settings:")
    print(print(f"author: {author}"))
    for key, value in kwargs.items():
        print(f"{key}: {value}")

    return f"Report {title} with {len(args)} sections"


report1 = create_report("Monthly sales report", "Intro", "Sales in april", "Sales in may")
print("-" * 100)
report2 = create_report("Project update report", "Summary", "Milestones", author="Eugene D.", format="PDF", version=1.0)
print("-" * 100)
report3 = create_report("Project update report", "Summary", "Milestones", version=1.0, confidential=True)
#############################################################

print("a", "b", "c", sep="/", end="!")





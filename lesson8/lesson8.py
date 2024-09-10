##################################################################################
# Lesson8: try/except/finally, raise, unpacking

##################################################################################
# *args, **kwargs, unpacking
def sep():
    print("-" * 100)
# * - unpacking position arguments
list_of_numbers = [1, 2, 3, 4, 5]
first, second, *other, last = list_of_numbers
print(first, second, other)
print(first, second, last)

# * - combining list
list1 = [1, 2, 3]
list2 = [3, 4, 5]
list3 = [3, 4, 5]
list4 = [3, 4, 5]
list1.extend(list2)

result_list = [*list1, *list2, *list3, *list4]
print(result_list)

# ** - unpacking keyword arguments
dict1 = {"name": "Bob", "age": 30}
# print(**dict1)
# print(name="Bob", age=30)
def greeting(name, age):
    print(f"Hello {name}, your age {age}")

greeting(**dict1)  # -> greeting(name="Bob", age=30)

dict2 = {"address": "Jones st", "app": 30}
result = {**dict1, **dict2}
print(result)
##################################################################################
# try/except
# What is error?
# ---> Syntax error
# ---> Exceptions
def divide(a, b):
    return a / b

# Variant 1
def divide_1(a, b):
    if b == 0:
        print("Division by zero is not allowed")
    return a / b

sep()
def divide_2(a, b):
    try:
        res =  a / b
        return res
    except ZeroDivisionError:
        print("Division by zero is not allowed")

result = divide_2(2, 3)
print(result)
result = divide_2(1, 0)

##################################################################################
def get_element_by_index(lst, index):
    el = None
    try:
        el = lst[index]
        # return el
    except IndexError:
        print("Index out of range")
    except TypeError as e:
        print(f"Button type is wrong. It should int. Error: {e}")
    except Exception as error:
        print(f"Error: {error}")

    return el

result1 = get_element_by_index([100, 200, 300], 5)
result2 = get_element_by_index([100, 200, 300], '4')

sep()
##################################################################################
# finally
def divide_3(a, b):  # returns None by default
    try:
        res =  a / b
        return res
    except ZeroDivisionError:
        print("Division by zero is not allowed")
    except TypeError as e:
        print(f"Type is wrong. Error: {e}")
    finally:
        print("This is always executed")


result3_1 = divide_3(2, 3)
print(result3_1)
sep()
result3_2 = divide_3(1, 0)
print(result3_2)
sep()
result3_3 = divide_3(1, '2')
print(result3_3)
sep()
##################################################################################
# raise
def divide_4(a, b):  # returns None by default
    try:
        if b == 0:
            raise Exception("Please do not use 0!!!")
        res =  a / b
        return res
    except TypeError as e:
        raise Exception(f"Type is nor OK! {e}")
    finally:
        print("This is always executed")

# result4 = divide_4(2, 0)
# result4_1 = divide_4(2, "3")
sep()
##################################################################################
# example from qa automation
def read_test_data(file_path):
    try:
        file = open(file_path, "r")
        print(f"File was opened: {file_path}")
        data = file.read()
        if not data:
            raise ValueError("Test data is empty")
        print(f"Data from file: {data}")
    except FileNotFoundError:
        print(f"Error in file {file_path}. It should have name...")
    except ValueError:
        print(f"Error in file {file_path}. It should have data...")
    else:
        print("No exceptions occurred. All is ok")
    finally:
        print("Closing file")
        try:
            # File was never opened
            file.close()
        except NameError:
            print("File wasn't opened")
example_file_path = "/Users/danilovets/Personal/Hillel/aqa_hillel_1308/lesson8/test_cases.txt"
read_test_data(example_file_path)
sep()
##################################################################################
# another example with raising exception
def get_user_input():
    while True:
        try:
            user_input = int(input("Enter number: "))
            if user_input < 0:
                raise Exception("Please enter the number > 0")
            if user_input > 100:
                raise Exception("Please enter the number < 100")
            return user_input
        except Exception as e:
            print(f"Error: {e}")

# number = get_user_input()
##################################################################################
def divide_5(a, b):  # returns None by default
    try:
        return  a / b
    except (TypeError, ZeroDivisionError) as e:
        # block of code
        print(f"Error is occurred {e}")

divide_5(1, '1')
sep()
##################################################################################
# UpdateFileNotFound, ErrorInPathError

class NegativeNumberError(Exception):
    pass


class LargeNumberError(Exception):
    pass

def get_user_input1():
    while True:
        try:
            user_input = int(input("Enter number: "))
            if user_input < 0:
                raise NegativeNumberError("Please enter the number > 0")
            if user_input > 100:
                raise LargeNumberError("Please enter the number < 100")
            return user_input
        except Exception as e:
            print(f"Error: {e}")
# number = get_user_input1()

##################################################################################
# another example of custom exception

class TooLargeValueError(Exception):
    def __init__(self, value, limit1):
        self.value = value
        self.limit = limit1
        message = f"Value {value} is above limit {limit1}"
        super().__init__(message)

# try:
#     limit = 100
#     user_input = int(input("Enter the number: "))
#
#     if user_input > limit:
#         raise TooLargeValueError(user_input, limit)
#     else:
#         print("Thank you")
# except TooLargeValueError as e:
#     print(f"Error: {e}")
# except ValueError:
#     print("Enter positive number.")
sep()
##################################################################################
# with
with open(example_file_path, 'r') as file:
    data = file.read()
    print(data)
sep()
##################################################################################
import sqlite3
from contextlib import contextmanager

@contextmanager
def db_connection(db_name):
    with sqlite3.connect(db_name) as conn:
        # cursor -> object used to interact with db
        cursor = conn.cursor()
        yield cursor
        # connection will be auto closed

db_path = "/Users/danilovets/Personal/Hillel/aqa_hillel_1308/lesson8/test_db.sqlite"
def add_data(db_path=db_path):
    with db_connection(db_path) as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users 
            (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)
            """
        )
        cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
        cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 40)")

        # cursor will be closed

def output_data(db_path=db_path):
    with db_connection(db_path) as cursor:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

add_data()
output_data()
##################################################################################



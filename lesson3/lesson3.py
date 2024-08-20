# name = "John"
# name1 = 'John'
# query = """
# SELECT * FROM users
# WHERE name = "John"
# ORDER BY id DESC
# """
#
# command = """
# find / -name "*.log"; grep -r 'error' /var/log
# """
#
# js_code = """
# document.querySelector('#username').value == 'admin';
# document.querySelector('#username').value == 'admin';
# document.querySelector('#username').value == 'admin';
# """
#
# # driver.execute_script(js_code)
# # import = "John"
#
# print("Division: ", 10 / 3)
# number = 10 / 3
# print("Division with round: ", number)
# print(f"Division with round 1: {number:.4f}")
#
# rounded_number = round(10 / 3, 2)
# print("Division with round 2: ", rounded_number)
#
# int_number = int(10 / 3)    # int / int = float
# int_number1 = int(34.223)   # int / int = float
# print(type(int_number))     # int

##################################################################################
# ==

# 1. Compare values
# 2. Compare data type
# 3. Compare memory address

# a = 10
# b = 10
# print("a == b: ", a == b)
# print("ids", id(a), id(b))
#
# c = 100000
# d = 100000
# print("ids c and d", id(c), id(d))

# print(10 == '10')

# == vs is
# 1. Compare memory address
# c = 100000
# d = 100000
# print(c is d)

# list1 = [1, 2, 3]
# list2 = list1
# list3 = [1, 2, 3]
# print("Lists comparison1: ", list1 == list2)
# print("Lists comparison2: ", list1 == list3)
# print("Lists comparison3: ", list1 is list2)
# print("Lists comparison4: ", list1 is list3)
#
# some = None
# print(some is None)
#
# some = 10
# print("Some is not 10:", some != 10)


# a = 2
# a = a + 2
# a += 2
# b = 10
# b = b - 2
# b -= 2
# b /= 2
# b *= 2

# and, or, not

# 0: False
# 1: True
# and: 0 * 0 = 0, 0 * 1 = 0,  1 * 0 = 0, 1 * 1 = 1
# print("False and False: ", False and False)
# print("False and True: ", False and True)
# print("True and False: ", True and False)
# print("True and True: ", True and True)
# # or: 0 + 0 = 0, 1 + 0 = 1, 0 + 1 = 1, 1 + 1 = 1
# print("False or False: ", False or False)
# print("False or True: ", False or True)
# print("True or False: ", True or False)
# print("True or True: ", True or True)
# # not
# print(not True)
# print(not False)

# a = True
# b = True
# if a and b:
#     print("Something")

# name = "John1"
# surname = "Smith"
# if name == "John" and surname == "Smith":
#     print("AND: Name is ok")
# if name == "John" or surname == "Smith":
#     print("OR: Name is ok")

# name = "John1"
# is_john = name == "John"
# if is_john:
#     print("It is John")
# is_not_john = name != "John"
# surname = "Smith"
# if (name == "John" and surname == "Smith") or True:
#     print("AND: Name is ok")
#
# a = (1 + 2) - (1 + 2)

# int and float
# price = 20.0
# if price == 20:
#     print("ok")
# print(10 == 10.0)
# print(10 == [10])

##  Системи числення
# d = 0xA
# d1 = 0x1A
# print(type(d1))

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# binary
# 0, 1, 10, 11, 100
# print(0b101010)

# 16
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f, 10, 11...
# 0x113da
# 0x12241241faa3333

# print(hex(10000))
# print(bin(10000))
# print(oct(10000))
##################################################################################
# Sequences: list, str, tuple
# sentence = "log 2024-10-10: London is the capital of GB"
# sentence1 = "log 2024-10-11: London is the capital of GB price<24.9>"
# print(sentence[0])
# print(sentence[1])
# print(sentence[-1])
# print(sentence[-10])
# # slices
# print(sentence[0:5])  # [0:5)
# print(sentence[3:10])
# print(sentence[16:])
# # print(sentence[start:end:step])
# print(sentence[16::2])
# print(sentence[16::3])
#
# print("Length of sentence:", len(sentence))
# print("Length of sentence:", sentence.index("L"))
# print("Length of sentence:", sentence.count("24"))
#
# prices = [23.2, 2111, 233, 100]
# print(prices[0])
# print(prices[:3])
#
# not_updatable_prices = (121, 121, 3234, 424)
# print(not_updatable_prices[0])
# print(not_updatable_prices[:3])
# ##################################################################################
# # Sequences: set
# numbers = {1, 2, 3, 4}
# print(type(numbers))
# print(len(numbers))
# print(numbers[0])
# print(numbers[0:2])


##################################################################################
# Data type: None
# a = None
# print(a)
# print(a is None)
# print(a is not None)
# print(bool(a))  # a -> bool
#
# # falsy values:
# print(bool(""))
# print(bool([]))
#
# list1 = []
# if not list1:
#     print("List is empty")
#
# max_value = max(prices)
# min_value = min(prices)
# prices = [23.2, 2111, 233, 100, 11, 323, 0, -1]
# print("Max price: ", max_value)
# print("Min price: ", min_value)


##################################################################################
# Output/input
# name = input("Enter your name: ")
# print(f"Hello {name}")

# age = int(input("Enter your age: "))
# age += 1
# print(f"My age {age}")

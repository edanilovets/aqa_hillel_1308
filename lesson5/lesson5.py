import sys
import copy

######################################################################
# List

fruits = ["apple", "banana", "cherry"]
# fruits[0]
print(fruits)

list_of_everything = ["apple", 1, 1.2, [1, 2, 3], (55, 66), {"key": "value"}, None]
print(list_of_everything)

print("-" * 100)

fruits = []
fruits1 = list()
fruits2 = list((1, 2, 3))
fruits3 = list({1, 2, 3, 4, 5, 6})
print(fruits3)

print(fruits3[2:5])

######################################################################

my_list = []
initial_capacity = sys.getsizeof(my_list)
print("Initial capacity of empty list: ", initial_capacity, "bytes")
for i in range(100):
    my_list.append(i)
    if sys.getsizeof(my_list) != initial_capacity:
        print(f"Capacity changed: {sys.getsizeof(my_list)} bytes at {len(my_list)} elements")
        initial_capacity = sys.getsizeof(my_list)

print("-" * 100)
######################################################################
# append(), extend() methods

cars = ["Honda", "Mazda"]
cars.append("BMW")
print(cars)

cars.extend(("Mercedes", "Nissan"))
print(cars)

cars = cars + ["Ford", "Volvo"]
print(cars)
print("-" * 100)
######################################################################
# insert()

cars = ["Honda", "Mazda"]
cars.insert(0, "Volvo")
cars.insert(2, "BMW")
print(cars)
print("-" * 100)
######################################################################
# remove(), pop() methods

cars = ["Honda", "Mazda", "Volvo", "BMW"]
cars.remove("Honda")
print(cars)
cars.pop()
print(cars)
cars = ["Honda", "Mazda", "Volvo", "BMW"]
cars.pop(1)
print(cars)


print("-" * 100)
######################################################################
# index(), count()
cars = ["Honda", "Mazda", "Volvo", "BMW", "Honda", "Mazda"]
number_of_cars = cars.count("Honda")
print(number_of_cars)
index_of_mazda = cars.index("Mazda", 2)
print(index_of_mazda)
print("-" * 100)
######################################################################
# copy()

fruits = ["apple", "banana", "pineapple", ["orange", "kiwi"]]

x = fruits.copy()
print("List copy:", x)

fruits.insert(0, "CHERRY")
fruits[4].append("banana")
print("Original list:", fruits)
print("List copy:", x)

print("-" * 100)

######################################################################
# shallow vs deepcopy

fruits = ["apple", "banana", "pineapple", ["orange", "kiwi"]]
x = copy.deepcopy(fruits)
fruits[3].append("banana")
print("Original list:", fruits)
print("List copy:", x)

print("-" * 100)
######################################################################
# Dictionary

######################################################################
# Create dictionary

this_dict = {
    "brand": "Audi",  # key: value
    "model": "Q5",
    "year": 2024
}
this_dict0 = {}
print(type(this_dict0))
this_dict1 = dict()
this_dict2 = dict([("key1", "value1"), ("key2", "value2")])
print("New dict:", this_dict)
print("New dict 2:", this_dict2)

# Accessing dict items
this_dict = {
    "brand": "Audi",  # key: value
    "model": "Q5",
    "year": 2024
}
x = this_dict["brand"]
# color = this_dict["color"]
print("Brand:", x)

y = this_dict.get("brand")
c = this_dict.get("color")
c1 = this_dict.get("color", "black")
print("Brand:", c1)
######################################################################
users = [
    {
        "name": "Eugene",
        "age": 35,
        "email": "myemail@gmail.com",
        "address": {
            "street": "Kreschatik",
            "postal_code": 13132
        }
    },
    {
        "name": "John",
        "age": 25,
        "email": "john@gmail.com",
        "address": None
    }
]
print("My street is: ", users[0]["address"]["street"])

# Set items

this_dict1 = {
    "brand": "Audi",  # key: value
    "model": "Q5",
    "year": 2024
}
this_dict1["year"] = 2023

this_dict1.update({"year": 2020, "color": "white"})
print("Updated dict:", this_dict1)
print("-" * 100)
######################################################################
sentence = "I am a QA engineer and I am writing Python code. I am a QA engineer and I am writing Python code"
counter = {}
words = sentence.split()
for word in words:
    if word not in counter:
        counter[word] = 1
    else:
        counter[word] += 1
print("Word counter:", counter)

print("-" * 100)
######################################################################
# items()
this_dict1 = {
    "brand": "Audi",  # key: value
    "model": "Q5",
    "year": 2024
}
print("Items:", this_dict1.items())
print("-" * 100)

for key in this_dict1:
    print("Key:", key)

for a, b in this_dict1.items():
    print("Key:", a, "Value:", b)

for value in this_dict1.values():
    print("Value:", value)

print("-" * 100)
######################################################################
# copy()
this_dict1 = {
    "brand": "Audi",  # key: value
    "model": "Q5",
    "year": 2024,
    "colors": ["black", "white"]
}
x = this_dict1.copy()
print("Dict copy:", x)
x = copy.deepcopy(this_dict1)
print("Dict copy:", x)
######################################################################
# fromkeys() method

x = ('keys1', 'keys2', 'key3')  # tuple
y = ""  # value
new_dict = dict.fromkeys(x, y)

print("Dict from keys:", new_dict)
new_dict = dict.fromkeys(x)
print("Dict from keys:", new_dict)
######################################################################
# pop(), popitem()
this_dict1 = {
    "brand": "Audi",  # key: value
    "model": "Q5",
    "year": 2024,
    "colors": ["black", "white"]
}
this_dict1.pop("model")

print("Pop example:", this_dict1)
this_dict1.popitem()

print("Popitem example:", this_dict1)

######################################################################
# setdefault()

this_dict1 = {
    "brand": "Audi",  # key: value
    "model": "Q5",   # keys: str, int, float, tuple, None, bool
    "colors": ["black", "white"]
}
x = this_dict1.setdefault("year", 2024)
print("Setdefault example:", this_dict1)
print(hash("brand"))
######################################################################

# Operator in
if "brand" in this_dict1:
    print("Brand is here.")

list1 = this_dict1.items()
if ("brand", "Audi") in list1:
    print("Brand is here.")

z = "brand" in this_dict1
print(z)
######################################################################
# Tuple

def some_func():
    some_tuple = (1, 2, 3)
    one, two, three = some_tuple
    return one, two, three

a, b, c = some_func()

some_tuple = (1, 2, 3, 2)
x = some_tuple[1]
######################################################################
my_tuple = ()
initial_capacity = sys.getsizeof(my_tuple)
print("Initial capacity of empty tuple: ", initial_capacity, "bytes")
for i in range(100):
    my_tuple = my_tuple + (i,)
    if sys.getsizeof(my_tuple) != initial_capacity:
        print(f"Capacity changed: {sys.getsizeof(my_tuple)} bytes at {len(my_tuple)} elements")
        initial_capacity = sys.getsizeof(my_tuple)

print("-" * 100)
######################################################################
# Set

# Create set
this_set = {"apple", 1, 2.0, True, 0, False, 0, 1.0, "apple", "string"}
print("Set creation:", this_set)

this_set = {"apple", 1, 2.0, True, (1, 2, 5)}
print("Set creation:", this_set)

this_set = set([1, 2, 1, 1, 1, 1])
print("Set creation:", this_set)

# Accessing set items
for x in this_set:
    print(x)
######################################################################
def is_hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False

print("-" * 100)
print(is_hashable(42))
print(is_hashable(42.22))
print(is_hashable("apple"))
print(is_hashable([1, 2, 3]))
print(is_hashable((0, 3)))
print(is_hashable(None))
print(is_hashable(True))
print(is_hashable({"key": "value"}))
print(is_hashable({1, 2, 4}))
print("-" * 100)
######################################################################
# discard(), remove(), pop()

this_set = {0, 1, 2.0, 'string', 'apple', None, ("I'm", "tuple")}
this_set.discard('apple')
this_set.discard('cherry')
# this_set.remove("apple")
this_set.pop()
print("Set discard:", this_set)
######################################################################
# difference(), difference_update()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
# z = x.difference(y)  # z = x - y
# z1 = y.difference(x)
x.difference_update(y)  # x -= y
print(x)
print()
######################################################################
# union(), intersection()
x = {"Honda", "Toyota", "Nissan"}
y = {"Toyota", "Nissan", "Mazda"}

z = x.union(y)
z1 = y.union(x)
print("Union:", z)
print("Union:", z1)

i = x.intersection(y)  #
print("Intersection:", i)

list_of_emails = ["email@dada.com", "ewew@dasda.com"]
unique_emails = set(list_of_emails)
######################################################################

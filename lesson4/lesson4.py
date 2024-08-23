###############
# class str

string = ""
dir(string)
###############
# split()

s = "    My name is  Eugene.    I'm QA engineer.    "
print("String: ", s)
words = s.split()
print("Example 1.1: ", words)
print("Example 1.2: ", s.split(" "))
print("Example 1.3: ", s.split("  "))
print(words[0:4])

#####
print("String: ", s)
print("Example 1.4: ", s.split(maxsplit=2))
s = "My name is  Eugene. I work as a QA engineer. I work and work..."
print("Example 1.5: ", s.split("work"))
###############################################
# splitlines()
s = "My name is  Eugene. \nI work as a QA engineer. \nI work and work...\nWORK....."
print("Example 1.5: ", s.splitlines())

print("Example 1.5: ", s.splitlines()[0].split())
####################
# for char in s:
#     print(char)
###############################################
s = "Name,Age,Occupation\nEugene,35,..."
lines = s.splitlines()
params = lines[1].split(",")
print(params)
###############################################
# startswith(), endswith() -> return True or False

s = "My name is  Eugene. I work as a QA engineer. I work and work..."
print("Example 1.6: ", s.startswith("My"))
if not s.startswith("My"):
    # test step, some verification
    print("s is starting with 'My'")

if s.endswith("...."):
    # test step, some verification
    print("Sentence ends with ...")

for word in s.split():
    if word.startswith("w"):
        print("Word starts with 'w'")
###############################################
# lower(), upper(), islower(), isupper(), swapcase(), istitle(), capitalize()

expected_email = "eugene.danilovets@gmail.com"
email_from_api = "EugenE.DanilovetS@gmail.com"

lower_email_from_api = email_from_api.lower()

if expected_email.lower() == email_from_api.lower():
    print(f"Emails are identical: {lower_email_from_api}")

expected_email = expected_email.upper()
print("Example UPPER: ", expected_email.upper())
print("Is email upper? -> ", expected_email.isupper())

print("Example swap case: ", email_from_api.swapcase())

print("Is title? -> ", "Style Guide for Python Code".istitle())
print("Is title? -> ", "Style Guide For Python Code".istitle())

print("Capitalize: ", "style guide for Python Code".capitalize())
print("Title: ", "style guide for Python Code".title())
###############################################
# find() vs in, count()
s = "My name is  Eugene. I work as a QA engineer. I work and work..."
print("Example of find: ", s.find("name"))
print("Example of find: ", s.find("QA QA"))
print("Example of find: ", s.find("work"))
print("Example of find with params: ", s.find("work", 10, 20))
print("Example of find with params: ", s.find("work", 25, 100))

if "Eugene" in s:
    print("Found name 'Eugene'")

if "work" not in s:
    print("Found 'work'")

s = "My name is  Eugene. I work as a QA engineer. I work and work..."
print("Example of count: ", s.count("work"))

# counter = 0
# for word in s.split():
#     if "work" == word:
#         counter += 1
# print(counter)
###############################################
# strip(), rstrip(), lstrip()
s = "    My name is  Eugene.    I'm QA engineer.    "
stripped = s.strip()
print("Example of strip: ", stripped)
print("Example of strip: ", stripped == "My name is  Eugene.    I'm QA engineer.")


print("Example of rstrip: ", s.rstrip())
print("Example of lstrip: ", s.lstrip())

header = '((Built-in Types.))'
print("Header: ", header)
print("Example of strip with params: ", header.strip('()'))

###############################################
# replace()

expected_header_with_price = "Apples cost 24.5 uah. So really? Yes 24.5 uah"
new_h = expected_header_with_price.replace("24.5", "100.1")
new_h_count = expected_header_with_price.replace("24.5", "100.1", 1)
print("Replace: ", new_h)
print("Replace: ", new_h_count)
###############################################
# join()
# expected_header_with_price = "Apples cost 24.5 uah. So really? Yes 24.5 uah"
# Name,Age,Email
# Eugene,35,eugene@gmail.com
# John,20, john@gmail.com
# apple,banana,pear,apple,pineapple,banana
fruits = "apple,banana,pear,apple,pineapple,banana"

fruits_without_apple = fruits.replace("apple", "")
print(fruits_without_apple)

list_of_fruits = fruits.split(",")
print(list_of_fruits)
fruits_without_apple = []
for word in list_of_fruits:
    if word != 'apple':
        fruits_without_apple.append(word)

print(fruits)
print(fruits_without_apple)
print(",".join(fruits_without_apple))  # list, tuple, dict (items)
print(" | ".join(fruits_without_apple))  # list, tuple, dict (items)
###############################################
#

form_data = {
    "first_name": "Eugene",
    "last_name": "",
    "age": "35",
    "is_working": "False"
}

print(int(form_data["age"]) + 2)
print(int("131232121"))
print(float("131232121.3"))
# print(float("12!"))  # ValueError: could not convert string to float: '12!'

print("Empty string -> bool: ", bool(""))   # falsy ""
print("String -> bool: ", bool("Eugene"))
print("String -> bool: ", bool("True"))
print("String 'False' -> bool: ", bool("False"))


form_data = {
    "first_name": "Eugene",
    "last_name": "",
    "age": "35",
    "is_working": ""
}
# not correct
if bool(form_data["is_working"]):
    print("Is working")

if form_data["is_working"]:  # if "":
    print("Is working")

###############################################
list_of_fruits = fruits.split(",")
print(type(list_of_fruits))
tuple_of_fruits = tuple(list_of_fruits)
print(type(tuple_of_fruits))
tuple_of_fruits = tuple("apple, banana")
print(tuple_of_fruits)
tuple_of_fruits = list("1,2,3,4")
print(tuple_of_fruits)
###############################################
numbers = "131232121a@gmail.com"
email_1 = numbers.split("@")
print("Is all numbers: ", email_1[0].isalnum())
print("Is all numbers: ", email_1[1].isalnum())
print("Is all numbers: ", "asdasdsa.com".isalnum())

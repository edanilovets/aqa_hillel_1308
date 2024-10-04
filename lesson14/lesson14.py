#############################################################
# OOP

#############################################################
# class
class Person:
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age    # instance attribute

    def introduce(self, day):  # method
        print(f"Hi, I'm {self.name}. Today is {day}")

    def walk(self, day):
        self.introduce(day)
        print("I'm walking")


# object (instance)
person1 = Person('Alice', 25)
print(person1.age)
print(dir(person1))
person2 = Person('Bob', 30)
print(person2.name)
print("Ids:", id(person1) == id(person2))

# call method
day = "Monday"
person1.introduce(day)
person2.introduce(day)
print("-" * 40)
person1.walk(day)
#############################################################
class Car:
    def __init__(self, brand, model, *args, **kwagrs):
        self.brand = brand
        self.model = model
        self.args = args
        self.kwargs = kwagrs

my_car = Car("Toyota", "Camry", 50, "SUV", year=2020)
print(my_car.args)
print(my_car.kwargs)
#############################################################
# __new__
class MyClass:

    def __new__(cls, *args, **kwargs):
        print("Creating an instance...")
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        print("Initializing MyClass..")
        self.value = value

new_object = MyClass(100)
#############################################################
# class attributes
class User:
    age = 20  # class attr
    def __init__(self, name):
        self.name = name

user1 = User("John")
user2 = User("Katy")

print("-" * 40)
print(user1.name)
print(user1.age)
print(user2.name)
print(user2.age)

print(User.age)
print("-" * 40)
user2.age = 30
print(user1.age)
print(user2.age)
print(User.age)
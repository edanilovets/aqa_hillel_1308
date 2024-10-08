
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setattr__(self, key, value):
        if key == "age" and (value < 0 or value > 120):
            raise ValueError("Age must be from 0 to 120")
        super().__setattr__(key, value)

    def __getattr__(self, item):
        return "Unknown"


person1 = Person("Eugene", 35)
person1.age = 100
print(person1.age)

print(person1.occupation)

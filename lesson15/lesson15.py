# Lesson 15
# --> @staticmethod and @classmethod
# --> class attribute
# --> magic methods (dunder methods)
# --> Class/instance life cycle

class MyClass:

    def __new__(cls, *args, **kwargs):
        print("Creating an instance...")
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        print("Initializing MyClass..")
        self.value = value

    def __del__(self):
        print(f"object with {self.value} was deleted")

    def __repr__(self):
        return f"MyClass(value={self.value})"

obj = MyClass(100)
print(obj)
# del obj
obj1 = MyClass(200)

# --> DRY - Don't repeat yourself
def function():
    pass

# --> SOLID
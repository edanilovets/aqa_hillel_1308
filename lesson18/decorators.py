def simple_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper


@simple_decorator
def say_hello():
    print("Hello world")

@simple_decorator
def say_python():
    print("Hello python")

# wrapped_say_hello = simple_decorator(say_hello)
# wrapped_say_hello()

# say_hello()
# say_python()

def simple_decorator_with_param(func):
    def wrapper(name):
        print(f"Before print {name}")
        func(name)
        print("After")
    return wrapper

@simple_decorator_with_param
def say_python(name):
    print(f"Hello python {name}")

say_python("Eugene")
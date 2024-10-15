# general function: return
# generator function: yield

# general function
def get_values_return():
    return [1, 2, 3]  # 1000000

print(get_values_return())

# generator function
def get_values_yield():
    for i in range(1, 4): # 1000000
        yield i

gen = get_values_yield()
print(next(gen))
print(next(gen))
print(next(gen))

print("-" * 10)
def countdown(num):
    while num > 0:
        yield num ** 2
        num -= 1

c = countdown(1000)
print(next(c))
print(next(c))
print(next(c))
print(next(c))

# []
# {}
# () generator expression
print("-" * 10)
gen = (x ** 2 for x in range(1, 5))
for item in gen:
    print(item)
    if item == 4:
        break
print("-" * 10)
for item in gen:
    print(item)





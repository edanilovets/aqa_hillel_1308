# iterator
# iterable
# __iter__, __next__

my_list = [1, 2, 3]  # class list
my_iterator = iter(my_list)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
# print(next(my_iterator))

# set, tuple ...
# for item in my_list:
#     print(item)

rng = range(1, 5)
rng_iter = iter(rng)
print(next(rng_iter))
print(next(rng_iter))
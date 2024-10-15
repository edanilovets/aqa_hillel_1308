class InfiniteCounter:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        return self.current - 1

counter = InfiniteCounter(1)
# my_iterator = iter(counter)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

for item in counter:
    print(item)
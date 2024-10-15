import itertools
import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        test_data = itertools.combinations([1, 2, 3], 10)
        for a, b in test_data:
            print(a, b)

if __name__ == "__main__":
    unittest.main()
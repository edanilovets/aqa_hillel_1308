import unittest

from lesson9.src.functions import division


# test suite
class TestDivisionFunction(unittest.TestCase):

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division(1, 0)

    def test_divide_by_zero_no_with(self):
        try:
            result = division(1, 0)
        except ZeroDivisionError:
            pass
        else:
            self.fail("ZeroDivisionError is not raised")

    def test_division_positive(self):
        result = division(1, 3)
        self.assertEqual(result, 1, msg=f"Result {result} is not as expected 1")


if __name__ == '__main__':
    unittest.main(verbosity=2)  # test runner
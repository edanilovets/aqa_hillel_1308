import unittest

from lesson9.src.functions import add


# test suite
# class - CamelCase
class TestAddFunction(unittest.TestCase):

    # test case, snake_case
    def test_add_positive(self):
        result = add(1, 2)
        self.assertEqual(result, 4)  # result == 3, # AssertionError
        result = add(0.1, 1)
        self.assertAlmostEqual(result, 1.0, delta=0.2)  # 0.9 - 1.2

    # test case
    def test_add_negative(self):
        result = add(-100, -200)
        self.assertEqual(result, -300)

    # def test_dicts(self):
    #     expected_result = {
    #         "username": "dadasd",
    #         "email": "dadas@fasf.com",
    #         "role": "QA",
    #         "is_active": True
    #     }
    #     result = {
    #         "username": "dadasdd",
    #         "email": "dadas@fasf.com",
    #         "role": "AQA",
    #         "is_active": True
    #     }
    #     self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main(verbosity=2)  # test runner

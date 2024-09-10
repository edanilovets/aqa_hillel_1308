import unittest

from lesson9.src.functions import factorial


# test suite
class TestFactorial(unittest.TestCase):

    def test_factorial_positive_0(self):
        # Arrange (setup data for the test)
        expected_result = 1
        input_param = 0
        # Act
        result = factorial(input_param)
        # Assert
        self.assertEqual(result, expected_result, msg="Factorial result is not as expected")

    def test_factorial_positive_5(self):
        # Arrange (setup data for the test)
        expected_result = 120
        input_param = 5
        # Act
        result = factorial(input_param)
        # Assert
        self.assertEqual(result, expected_result, msg="Factorial result is not as expected")

    def test_factorial_negative_string(self):
        # Arrange (setup data for the test)
        input_param = "2"   # [], (), dict, None
        expected_error = TypeError
        expected_message = "unsupported operand type(s) for -: 'str' and 'int'"

        # Act & Assert
        with self.assertRaises(expected_error) as cm:
            factorial(input_param)
        the_exception = cm.exception
        actual_message = the_exception.args[0]
        self.assertEqual(actual_message, expected_message)


if __name__ == '__main__':
    unittest.main(verbosity=2)  # test runner
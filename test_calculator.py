import unittest

import calculator


class TestCalculator(unittest.TestCase):


    def test_add_digits(self):
        result = calculator.add_digits(4,7)
        self.assertEqual(result, 11)

    def test_subtraction(self):
        result = calculator.subtract_digits(10,3)
        self.assertEqual(result, 7)

    def test_multiplication(self):
        result = calculator.multiply(3, 4)
        self.assertEqual(result, 12)

    def test_division(self):
        result = calculator.divide(10, 2)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()

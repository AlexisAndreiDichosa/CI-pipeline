import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(3, 2), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(3, 2), 1)
        self.assertEqual(self.calculator.subtract(-1, 1), -2)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 2), 6)
        self.assertEqual(self.calculator.multiply(-1, 5), -5)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 2), 3)
        self.assertEqual(self.calculator.divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(1, 0)


if __name__ == '__main__':
    unittest.main()

import unittest
from simple_calculator import SimpleCalculator
class TestClass(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(1, 2), 3)
    def test_division(self):
        self.assertEqual(self.calc.divide(4, 2), 2)
import unittest
from simple_calculator import SimpleCalculator
class TestClass(unittest.TestCase):
    
    calc = SimpleCalculator()
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)
    def test_subtract(self):
        self.assertEqual(calc.subtract(1, 2), -1)
    def test_multiply(self):
        self.assertEqual(calc.multiply(1, 2), 3)
    def test_divide(self):
        self.assertEqual(calc.divide(4, 2), 2)
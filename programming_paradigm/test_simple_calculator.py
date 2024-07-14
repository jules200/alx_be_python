import unittest
from simple_calculator import SimpleCalculator
class TestClass(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(1, 2), 3)
    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2)
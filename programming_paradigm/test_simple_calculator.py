import unittest
from simple_calculator import SimpleCalculator
class TestClass(unittest.TestCase):
    
    test = SimpleCalculator
    def testadd(self):
        self.assertEqual(test.add(1, 2), 3)
    def testsubtract(self):
        self.assertEqual(test.subtract(1, 2), -1)
    def testmultiply(self):
        self.assertEqual(test.multiply(1, 2), 3)
    def testdivide(self):
        self.assertEqual(test.divide(4, 2), 2)
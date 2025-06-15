
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0) 
        
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(3,4),-1)
        self.assertEqual(self.calc.subtract(6,4),2)
        
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3,4),12)
        self.assertEqual(self.calc.multiply(6,4),24)
        
    def test_divide(self):
        self.assertEqual(self.calc.divide(6,2),3)
        self.assertRaises( ZeroDivisionError, self.calc.divide,6,0)
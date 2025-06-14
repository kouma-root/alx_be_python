import unittest


def square(x,y):
    
    return x*y

class TestSauare(unittest.TestCase):
    
    def test_saquare(self):
        self.assertEqual(square(2,2), 4)
        
    
    def test_square_negative(self):
        self.assertEqual(square(2,2), 0)
          
if __name__ == '__main__':
    unittest.main()
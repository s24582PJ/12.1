import unittest
from calculator import multiply

class TestCalculator(unittest.TestCase):
    def test_multiply_integers(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
    
    def test_multiply_floats(self):
        self.assertAlmostEqual(multiply(2.5, 4.2), 10.5)
        self.assertAlmostEqual(multiply(-1.5, 2.0), -3.0)
    
    def test_multiply_zero(self):
        self.assertEqual(multiply(0, 10), 0)
        self.assertEqual(multiply(10, 0), 0)
        self.assertEqual(multiply(0, 0), 0)

if __name__ == "__main__":
    unittest.main()

#https://github.com/antoniamunozp-cloud/lab11-AM-SM.git
#Partner 1: Antonia Munoz Paez
#Partner 2: Saisha Mahindroo
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(1, 2), -1)


    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(5, 10), 50)
        self.assertEqual(mul(1, 0), 0)
        self.assertEqual(mul(-5, 3), -15)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(5, 0), 0)
        with self.assertRaises(ZeroDivisionError):
            div(0,10)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)


    def test_logarithm(self):
        def test_logarithm(self):
            self.assertAlmostEqual(log(8, 2), 3)


    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(10, 1)

    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, -5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual((hypotenuse(3, 4)), 5)
        self.assertEqual((hypotenuse(5, 12)), 13)
        self.assertEqual((hypotenuse(14, 48)), 50)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
             square_root(-1)
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(81), 9)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
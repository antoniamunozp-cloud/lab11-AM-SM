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
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
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
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
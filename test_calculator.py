# https://github.com/Rherr055/lab10-RH-VW
# Partner 1: Rolando Herrera
# Partner 2: Val Wehnau


from unittest import *
from calculator import *

class TestCalculator(TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(3,2),5)
        self.assertEqual(add(-5, 0), -5)
        self.assertEqual(add(0, 0), 0)
    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(0, 0), 0)
        self.assertEqual(sub(1, 0), 1)
        self.assertEqual(sub(0, 1), -1)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2,3),6)
        self.assertEqual(mul(3,3),9)
        self.assertEqual(mul(10,10),100)
    def test_divide(self): # 3 assertions
        self.assertEqual(div(3, 3), 1)
        self.assertEqual(div(1, 10), 10)
        self.assertEqual(div(5, 35), 7)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(4,0)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(log(2, 2), 1)
        self.assertAlmostEqual(log(2, 2), 1)
        self.assertAlmostEqual(log(2, 2), 1)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0,12)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, -5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(0,2),2)
        self.assertAlmostEqual(hypotenuse(2, 0), 2)
        self.assertAlmostEqual(hypotenuse(0, 0), 0)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
            square_root(-2)
            square_root(-3)

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
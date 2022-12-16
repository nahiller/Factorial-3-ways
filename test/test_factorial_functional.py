import unittest
from src.factorial_functional import *
from test_base import *

class TestFactorialFunctional(TestBase, unittest.TestCase): 
    def test_returns_1_when_input_is_0(self):
        self.assertEqual(1, return_1_if_number_is_0_num_else(0))
        
    def get_factorial(self):
        return factorial
     
if __name__ == '__main__':
    unittest.main()
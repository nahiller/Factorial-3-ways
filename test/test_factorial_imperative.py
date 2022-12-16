import unittest
from src.factorial_imperative import *
from test_base import *

class TestFactorialImperative(TestBase, unittest.TestCase): 
    def get_factorial(self):
        return factorial

if __name__ == '__main__':
    unittest.main()
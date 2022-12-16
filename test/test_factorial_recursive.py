import unittest
from test_base import *
from src.factorial_recursive import *

class TestFactorialRecursive(TestBase, unittest.TestCase): 
    def get_factorial(self):
        return factorial

if __name__ == '__main__':
    unittest.main()

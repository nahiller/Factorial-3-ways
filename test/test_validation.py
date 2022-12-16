import unittest
from src.factorial_validation import *

class TestValidation(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)
        
    def test_neg_num_returns_an_exception(self):
        self.assertRaisesRegex(Exception, 'Value must be greater than or equal to 0', exception_neg, -1)

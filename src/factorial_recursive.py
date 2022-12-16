from src.factorial_validation import *

def factorial(number):
    exception_neg(number)
        
    return number * factorial(number - 1) if number > 0 else 1

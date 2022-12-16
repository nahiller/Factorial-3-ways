from src.factorial_validation import *

def return_1_if_number_is_0_num_else(number):
    return number if number != 0 else 1

def factorial(number):
    exception_neg(number)
    return return_1_if_number_is_0_num_else(number) * (factorial(number - 1) if number - 1 > 1 else 1)
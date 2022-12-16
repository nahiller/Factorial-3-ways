from src.factorial_validation import *

def factorial(number): 
    exception_neg(number)   
    
    product = 1

    for i in range(1, number + 1): 
        product *= i 
        
    return product
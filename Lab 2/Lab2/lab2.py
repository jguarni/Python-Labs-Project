# Lab02 CISC106 Joe Guarni
from cisc106 import *

# Problem 1

def divide_by_5(number):
    return(number/5)
divide_by_5(3)

"""
a. (4 pts) What is the function name?
The Function name is devide_by_5


b. (4 pts) What is the input type?
The input type is a integer.

c. (4 pts) What is the output type?
The output type is a float.

d. (4 pts) What is the instruction (code) for calculating the function?
The instruction is retrun(number/5)

e. (4 pts) What does line 3 do?
Line 3 calls the divide_by_3 function to run.
"""

# Problem 2

def plus1(number):
    return number + 1
print(plus1(plus1(plus1(0))))


#Problem 3

def math(x):
    """
    This will compute the equation f(x) = (x + 3)^2
        
    x -- number

    return -- number
    """
    return (x + 3) ** 2

assertEqual(math(2), 25)
assertEqual(math(10), 169)
assertEqual(math(12), 225)

#Problem 4

from cisc106 import *

def f(x):
    return x ** 2

def g(x):
    return x + x + x

def h(x):
    return x / 2

def composition1(x):
    return f(g(h(x)))

assertEqual(composition1(0), 0)

def composition2(x):
    return h(h(g(f(x))))

assertEqual(composition2(4), 12)
assertEqual(composition2(10), 75)

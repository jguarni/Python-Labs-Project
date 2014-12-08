# Lab02 CISC106 Joe Guarni
from cisc106 import *
import math

# Problem 1

def divide_by_5(number):
    return(number/5)
divide_by_5(3)

"""
a. (4 pts) What is the function name?
The Function name is devide_by_5


b. (4 pts) What is the input type?
The input type is either an integer or float.

c. (4 pts) What is the output type?
The output type is either an integer or float.

d. (4 pts) What is the instruction (code) for calculating the function?
The instruction code is retrun(number/5)

e. (4 pts) What does line 3 do?
Line 3 calls the divide_by_3 function to execute.
"""

# Problem 2

def plus1(number):
    return number + 1
print(plus1(plus1(plus1(0))))


#Problem 3

def matheq(x):
    """
    This will compute the equation f(x) = (x + 3)^2 with a value for x.
        
    x -- number

    return -- number
    """
    return (x + 3) ** 2

assertEqual(matheq(2), 25)
assertEqual(matheq(10), 169)
assertEqual(matheq(12), 225)

#Problem 4

def f(x):
    return x ** 2

def g(x):
    return x + x + x

def h(x):
    return x / 2

def composition1(x):
    return f(g(h(x)))

assertEqual(composition1(10), 225)

def composition2(x):
    return h(h(g(f(x))))

assertEqual(composition2(4), 12)
assertEqual(composition2(10), 75)


#Problem 5

def total_weight(density, volume):
    """ This function will calculate the mass of a liquid when given
    the volume and density of that specific liquid.

    volume -- number
    density -- number

    return -- number
    """
    return density * volume

assertEqual(total_weight(1.0, 5), 5)
assertEqual(total_weight(1.03, 5), 5.15)
assertEqual(total_weight(0.7, 5), 3.5)

def max_contents(density):
    """ This function will calculate the maximum weight of contents
    that could be placed in a 100cm by 100cm by 100cm box so that it still
    floats in the liquid.

    density -- number

    return -- number
    """

    return total_weight(density, 100 ** 3) - 500

assertEqual(max_contents(1.0), 999500)
assertEqual(max_contents(1.03), 1029500)
assertEqual(max_contents(0.7), 699500)

def box_orders(density, mass):
    """ This function will give you the amount of boxes needed to
    keep the a specific amount of liquid contained in the boxes afloat.
    
    density -- number
    mass -- number

    return -- number
    """
    
    return math.ceil(total_weight(density, mass)/max_contents(density))

assertEqual(box_orders(1.0, 999500), 1)
assertEqual(box_orders(1.03, 1029500), 2)
assertEqual(box_orders(0.7, 699500), 1)

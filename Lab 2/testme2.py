from cisc106 import *
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

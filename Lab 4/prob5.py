from cisc106 import *
from random import *

def practice(x):
    randvar = randrange(0,11)
    uinput = int(input("What is " + str(randvar ) + " times " + str(x ) + "? "))
    answer = randvar * x

    if (answer == uinput):
        print("Correct")
        return True
    else:
        print("Incorrect")
        return False
    
    
practice(5)
practice(7)


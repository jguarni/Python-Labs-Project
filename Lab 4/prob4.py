from cisc106 import *
from random import *

def randsum(n):
    endval = 0
    print("Numbers: ")
    while (n > 0):
        randomv = randrange(0,100)
        print(randomv)
        endval = endval + randomv
        n = n - 1
    print("Total Sum: ", endval)
        
randsum(10)

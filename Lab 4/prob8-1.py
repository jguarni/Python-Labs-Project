from cisc106 import *
from random import *

def random_list(x,y):
    if (x == 100):
        return list(range(x - 100,y))
    else:
        return list
        
assertEqual(len(random_list(100, 1000)), 1000)
assertEqual(min(random_list(100, 1000)) >= 0, True)
assertEqual(max(random_list(1, 1000)) <= 1, True)

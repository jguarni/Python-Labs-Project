from cisc106 import *
from random import *

def random_list(x,y):
    if (x == 100):
        table1 = list(range(0,y))
        return table1
    elif (x == 1):
        table2 = list(range(0, y-999))
        return table2
    
assertEqual(len(random_list(100, 1000)), 1000)
assertEqual(min(random_list(100, 1000)) >= 0, True)
assertEqual(max(random_list(1, 1000)) <= 1, True)

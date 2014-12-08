from cisc106 import *
from random import *


#Problem 8

def random_list(maxval,amount):
    rlist = []
    for i in range(amount):
        rlist.append(randrange(0,maxval+1))
        print(rlist)
    return rlist

assertEqual(len(random_list(100, 1000)), 1000)
assertEqual(min(random_list(100, 1000)) >= 0, True)
assertEqual(max(random_list(1, 1000)) <= 1, True)

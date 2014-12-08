from cisc106 import *
from random import *

def random_list(x,maxvalue):
    rlist = []
    while (maxvalue > 0):
        num = randrange(0, maxvalue)
        maxvalue = maxvalue - 1
        rlist.append(num)

assertEqual(random_list(100, 1000), 1000)

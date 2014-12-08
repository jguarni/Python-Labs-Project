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


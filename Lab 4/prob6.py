from cisc106 import *
from random import *

numbers1 = [2, 4, 6, 8, 1, 5, 7, 9, 10, 12, 14]
numbers2 = [1, 5, 7, 9]
numbers3 = [9, 10, 12, 14]


def square(valuel):
    for num in valuel:
        sq = num ** 2
        print(sq)
square(numbers1)

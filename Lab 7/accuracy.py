#Lab 7
#File 3 of 3
#Joe Guarni
#CISC106 - 7/22/13

from cisc106 import *

def accuracy(points,finalword):
        
    """

    This function takes two parameters, points and finalword. It then uses the length of the
    finalword in order to find out the max amount of points that the user could have scored by
    multiplying the length by 50 not including the first letter. After the function does this it
    then divides the actual amount of points the user scored by the max amount of points and multiplies
    that number by 100 to find the percent accuracy.

    points -- number
    finalword -- string

    return -- number
    
    """
    if (points == 0):
        return 0
    
    scoredword = finalword[1:]
    optimal = (len(scoredword)) * 50
    actual = int(points/optimal * 100)

    return actual

accuracy(150,'Google')

assertEqual(accuracy(150,'Google'),60)
assertEqual(accuracy(100,'Google'),40)
assertEqual(accuracy(190,'Google'),76)

# This function will determine the mass from a given density and a fixed volume.

from cisc106 import *
import math

def total_weight(density, volume):
    """ This function will calculate the mass off a liquid when given
    the volume and density of that specific liquid.

    volume -- number
    density -- number

    return -- number
    """
    return density * volume

assertEqual(total_weight(1.0, 5), 5)
assertEqual(total_weight(1.03, 5), 5.15)
assertEqual(total_weight(0.7, 5), 3.5)

def max_contents(density):
    """ This function will calculate the maximum weight of contents
    that could be placed in a 100cm by 100cm by 100cm box so that it still
    floats in the liquid

    density -- number

    return -- number
    """

    return total_weight(density, 100 ** 3) - 500

assertEqual(max_contents(1.0), 999500)
assertEqual(max_contents(1.03), 1029500)
assertEqual(max_contents(0.7), 699500)

def box_orders(density, mass):
    """ This function will give you the amount of boxes needed to
    need the said amount of liquid afloat

    density -- number
    mass -- number

    return -- number
    """
    
    return math.ceil(total_weight(density, mass)/max_contents(density))

assertEqual(box_orders(1.0, 999500), 1)
assertEqual(box_orders(1.03, 1029500), 2)
assertEqual(box_orders(0.7, 699500), 1)


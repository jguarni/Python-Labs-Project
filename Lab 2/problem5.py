from cisc106 import *

def total_weight(volume_water, volume_milk, volume_gas):
    """ This function will calculate the mass off a liquid when given
    the volume and density of that specific liquid.

    volume -- number
    density -- number

    return -- number
    """

    WATER_DENSITY = 1.0
    MILK_DENSITY = 1.03
    GASOLINE_DENSITY = 0.7

    return WATER_DENSITY * volume_water
    return MILK_DENSITY * volume_milk
    return GASOLINE_DENSITY * volume_gas


assertEqual(total_weight(1, 3, 5), 1.0, 3, 3.5)
assertEqual(total_weight(2, 4, 6), 2.0, 4.12, 4.2)

from cisc106 import *

def total_weight2(liquidtype, volume):
    """ This function will calculate the mass off a liquid when given
    the volume and density of that specific liquid.

    volume -- number
    density -- number

    return -- number
    """

    WATER_DENSITY = 1.0
    MILK_DENSITY = 1.03
    GASOLINE_DENSITY = 0.7
    if (liquidtype=="water"):
        return WATER_DENSITY * volume
    elif (liquidtype=="milk"):
        return MILK_DENSITY * volume
    elif (liquidtype=="gas"):
        return GASOLINE_DENSITY * volume

assertEqual(total_weight2('gas', 5), 3.5)
assertEqual(total_weight2('milk', 6), 6.18)
assertEqual(total_weight2('water', 10), 10.0)


testwater = eval(input("What is the volume of your water?: "))
print('The mass of your water is:', total_weight2("water", testwater))
testmilk = float(input("What is the volume of your milk?: "))
print('The mass of your milk is:', total_weight2("milk", testmilk))
testgas = eval(input("What is the volume of your gas?: "))
print('The mass of your gas is:', total_weight2("gas", testgas))

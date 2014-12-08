from cisc106 import *

def total_weight():
    """ This function will calculate the mass off a liquid when given
    the volume and density of that specific liquid.

    volume -- number
    density -- number

    return -- number

    """
    vol_water = float(input('Please Enter the volume(cm^3) of Water: '))
    vol_milk = float(input('Please Enter the volume(cm^3) of Milk: '))
    vol_gas = float(input('Please Enter the volume(cm^3) of Gas: '))
    
    mass_water = vol_water * 1.0
    mass_milk = vol_milk * 1.03
    mass_gas = vol_gas * 0.7

    print(mass_water)
    print(mass_milk)
    print(mass_gas)

total_weight()

from cisc106 import *
from random import *

def blackjack():
    ans = 'yes'
    uhand = 0
    while (ans == 'yes'):
        unumber = randrange(1,11)
        print('Your card is',unumber)
        uhand = uhand + unumber
        print('Your total is',uhand)
        if (uhand > 21):
            print('You went over 21!')
            ans = input('Would you like to try again? ')
            uhand = 0
        else:
            ans = input('Would you like to continue? ')
        
        
    if (ans == 'no'):
        dhand = randrange(11,31)
        print('The dealers score is',dhand)
    if (dhand > 21):
        print('The user has won the game!')
    elif (dhand <= 21) and (uhand > 21):
        print('The computer has won the game!')
    elif (dhand <= 21) and (dhand > uhand):
        print('The computer has won the game!')
    elif (uhand <= 21) and (uhand > dhand):
        print('The user has won the game!')
        
blackjack()

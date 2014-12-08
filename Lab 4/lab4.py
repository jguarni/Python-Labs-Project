# Lab 4
# CISC 106 6/24/13
# Joe Guarni

from cisc106 import *
from random import *

#Problem 1

def rand(num):
    """

    This function will first set a range from 0 to an input parameter,
    then prompt the user to guess a number in that range. It will then
    notify the user weather their input was correct, too high, or too low
    compared to the random number.

    num -- number
    return - nothing as this function prints its output

    """
    
    randvar = randrange(0,num+1)
    number = int(input("Please enter a number between 0 and " + str(num ) +": "))
    if (number == randvar):
        print("Congratulations! You guessed the number!")
    elif (number > randvar):
        print("Your guess was too high")
    elif (number < randvar):
        print("Your guess was too low")
              
rand(10)
rand(100)
rand(1000)

# Problem 2

def hort():
    """
    This function will ask the user for heads or tails and compare
    thier answer to a randomly generated true or false, and return
    weather their guess was correct.

    return -- boolean
    
    """
    
    randvar = randrange(0,2)
    guess = int(input("Heads[Press 0] or Tails[Press 1] ?: "))
                
    if (guess == 1) and (randvar == 1) or (guess == 0) and (randvar == 0):
        return True
    else:
        return False

def hort2():
    """
    This function will determine the winner of the best of 5 game. If the user
    or computer wins 3 times the loop will stop as one of the players has won.


    """

    time = 0
    user = 0
    computer = 0
    
    while(time < 5):
        
        if hort():
            user = user + 1
        else:
            computer = computer + 1
        if (user >= 3):
            print('The user has beaten the computer!')
            return
        if (computer >= 3):
            print('The computer has beaten the user!')
            return
            
        time = time + 1
    
hort2()

#Problem 3

def addition(x):
    """
    This function will take a numerical input and return the sum
    of all the numbers from 0 until the input number.

    x -- number
    
    return -- number
    
    """
    
    total = 0
    while(x > 0):
        total = total + x
        x = x - 1
    return total

assertEqual(addition(3),(6))
assertEqual(addition(4),(10))
assertEqual(addition(6),(21))

#Problem 4

def randsum(n):
    """
    This function will generate n amount of numbers between 0 and 100
    and print the random numbers and their sum total.

    n -- number
    
    return -- number

    """
    
    endval = 0
    print("Numbers: ")
    while (n > 0):
        randomv = randrange(0,101)
        print(randomv)
        endval = endval + randomv
        n = n - 1
    print("Total Sum: ", endval)
        
randsum(10)
randsum(15)
randsum(20)

#Problem 5

def practice(x):
    """
    This function will generate a number between 0-10, and then ask the user
    for the answer of that random number multiplied against the input x value.
    If the user is correct, the function will return true, and if incorrect,
    return false.

    

    x -- Number

    return -- Boolean

    """
    randvar = randrange(0,11)
    uinput = int(input("What is " + str(randvar ) + " times " + str(x ) + "? "))
    answer = randvar * x

    if (answer == uinput):
        print("Correct")
        return True
    else:
        print("Incorrect")
        return False
    
practice(5)
practice(7)

#Problem 6

numbers1 = [2, 4, 6, 8, 1, 5, 7, 9, 10, 12, 14]

def square(valuelist):
    """
    This function will take input as a list and print the square of each
    number in that list.

    valuelist -- number
    print -- number

    """
    for num in valuelist:
        sq = num ** 2
        print(sq)

square(numbers1)

#Problem 7

def blackjack():
    """
    This function will emulate a game of blackjack. It will hand random card
    numbers to the user and ask them each time if they want another card. It
    will then test the users hand against the randomly generated computers
    hand to see who won the game according to the rules of blackjack.

    """
    print('Welcome to Wacky BlackJack!')
    ans = 'yes'
    uhand = 0
    while (ans == 'yes'):
        unumber = randrange(1,12)
        print('Your card is',unumber)
        uhand = uhand + unumber
        print('Your hand total is',uhand)
        if (uhand > 21):
            print('You went over 21!')
            ans = input('Would you like to try again? ')
            uhand = 0
        else:
            ans = input('Do you wish to continue? ')
        
        
    if (ans == 'no'):
        dhand = randrange(11,31)
        print('The dealers score is',dhand)
    if (dhand > 21):
        print('The user has won the game!')
    elif (dhand <= 21) and (uhand > 21):
        print('The computer has won the game!')
    elif (dhand <= 21) and (dhand > uhand):
        print('The computer has won the game!')
    elif (uhand <= 21) and (uhand >= dhand):
        print('The user has won the game!')
        
blackjack()

#Problem 8

def random_list(maxval,amount):
    """
    This function will produce a input value(amount) list of random numbers between 0 and
    specified maxvaule input with legnth N

    maxval -- number
    amount -- number

    return -- list with numbers

    """
    rlist = []
    for i in range(amount):
        rlist.append(randrange(0,maxval+1))
    return rlist
    
assertEqual(len(random_list(100, 1000)), 1000)
assertEqual(min(random_list(100, 1000)) >= 0, True)
assertEqual(max(random_list(1, 1000)) <= 1, True)

    
    


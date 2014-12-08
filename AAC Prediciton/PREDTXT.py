# AAC Prediction
# Workspace -- Project
# Joe Guarni, Peter Manniel

from readFile import *
from collections import Counter
import collections
import sys
import os


def main():

    """

    This is the main function of the program. It determines weather the user is entering a letter for the
    first time or for any subsequent times.It also knows when the usr enters 0 to stop the prediction
    and give the user their final results. It calls all the necessary functions and links them together to
    give the user the overall experiemce.
    

    """

    displayscreen()

    stop = 0
    stop2 = 0
    counter = 0
    finalword = str('')
    
    #first loop entering the first letter of their word
    while (stop == 0): 
        while (counter == 0):
            utext = input('Please Enter the first letter of your word: ').lower()
            print('')
            print('')
            letter = userinput(utext)
            finalword = finalword + str(letter)
            
            if (finalword != '0'):
                print("Your word is:", finalword)

            #quit if 0 is entered and no letter is entered.
            if (letter == '0'):
                print('No word entered')
                print('Program will quit')
                counter = 1
                stop = 1
                stop2 = 1
                
            elif (letter !=0):
                wordlist = read_file(letter)
                cinput = chopper(wordlist, letter)
                lcount = counts(cinput)
                userscore = points(lcount, letter)
                counter += 1
                stop2 = 0
        #Any subsequent letter entered after                
        while (counter >= 1) and (stop2 == 0):
            utext = input('Please enter another letter: ')
            checktext = userinput(utext)
            
            #this will display all output when user is finished with their word by entering 0
            if (checktext == 0) or ('0' in checktext):
                stop = 1
                stop2 = 1
                print('Your final word is', finalword)
                print('Your final score is', userscore,'points')
                print('The prediction accuracy is', accuracy(userscore,finalword),'%')
                wordcheck(wordlist,finalword)
                break
            
            cinput = chopper(cinput, checktext)
            userscore += points(lcount, checktext)
            lcount = counts(cinput)
            finalword = finalword + str(checktext)
            print("Your word is:", finalword)

def displayscreen():

    """

    This function displays the start screen to the user.

    """
    
    print(

    
    '''             *** Welcome to PRED-TXT for AAC devices! ***

    ---------------------------------------------------------------
    ***************************************************************
    ---------------------------------------------------------------

    This software will predict the next five most probable letters

    based on user input to aid in helping the handicap communicate

    more effectively and faster with others.

    At any time, enter the value 0 to signal the end of your word.

    ---------------------------------------------------------------
    ***************************************************************
    ---------------------------------------------------------------

    '''
    )


def userinput(atext):
        
    """

    This function checks the user input for validity. If they use a character that is not a letter
    then this function will not return but ask them to please try again and subsequently check the input.
    This function also allows the user to end the program whenever they have finished their word by passing it '0'.

    atext -- string

    return -- string
    
    """

    # This while loop is for when the user wants to end the program. If the user has finished
    # their word, all they have to do is enter the number '0' and the program will be terminated.

    while (atext == '0'):
        print('Word Completed! \n')
        return '0'

    
    # If the user enters a character that is not a letter then the program will ask the user to
    # please try again and enter another letter.
    
    while not atext.isalpha() and (atext != '0') or (len(atext) > 1):
            
        print('That is not a letter')
        atext = input('Please enter another letter: ').lower() #Converts to lower
    return atext

def chopper(slist, utext):
    
    """

    This function takes two parameters, slist and utext. It will examine each element in slist
    and check to see if the user input (utext) is equal to the first letter. If it is, the word will
    then stay in the list. That letter will then be stripped from the beginning of the word and
    the remaining parts of the word will be appended to the list 'chopped'.

    slist -- list of strings
    utext -- string

    return -- list of strings

    """
    
    chopped = []

    # This while loop strips whitespace from the list. If the user inputs 'abs' and the word
    # 'ab' was in the list, the whitespace from 'ab' is removed out of the list.
       
    while '' in slist:
        slist.remove('')

    # By using this for loop, the list becomes smaller with each input and will ultimately
    # decrease down to the users possible final word.
    
    for word in slist:
        if utext != word[0]: # user input != first letter of word
            del word
        else:
            word = word[1:]
            chopped.append(word)
            
    return chopped

def counts(clist):

    
    """

    This function will take the returned list from the function chopper and count word[0]
    of each element. It will then append the first element to a list named llist, that then sorts
    the most frequent letters in decending order.  It uses if-elif statements to see the amount of
    predicted letters and, if it is not equal to 5 to add more letters to predict.

    clist -- list of strings

    return -- list of strings
    
    """
    
    llist = []
    
    for word in clist: #Append the first element to the new list
        x = word[0:1]
        llist.append(x)
        
    while '' in llist: #Strip whitespace
        llist.remove('')
    
    top_count = sorted(Counter((llist)).items(), key=lambda x: x[1], reverse = True) #Sort in decending order
    top_countp = [x[:1] for x in top_count]
    top_countp2 = [j for i in top_countp for j in i] #display only the chars and not the letter count

    if (len(top_countp2) >= 5): #Normal Prediction
        print("The next most probable letters are:", top_countp2[0] + str('  |  ') 
              + top_countp2[1] + str('  |  ') + top_countp2[2] + str('  |  ') + top_countp2[3] +
              str('  |  ') + top_countp2[4])
        return (top_countp2[:5])
    
    elif (len(top_countp2) == 4): #If there are only 4 predicted letters
        listL4 = ['a']
        temp4 = (top_countp2[0] + str('  |  ') + top_countp2[1] + str('  |  ') + top_countp2[2] +
        str('  |  ') + top_countp2[3] + str('  |  ') + listL4[0])
        print("The next most probable letters are:", temp4)
        return top_countp2[:5] + listL4
    
    elif (len(top_countp2) == 3): #If there are only 3 predicted letters
        listL3 = ['a','e']
        temp3 = (top_countp2[0] + str('  |  ') + top_countp2[1] + str('  |  ') + top_countp2[2] +
        str('  |  ') + listL3[0] + str('  |  ') + listL3[1])
        print("The next most probable letters are:", temp3)
        return top_countp2[:5] + listL3
    
    elif (len(top_countp2) == 2): #If there are only 2 predicted letters
        listL2 = ['i','o','s']
        temp2 = (top_countp2[0] + str('  |  ') + top_countp2[1] + str('  |  ') + listL2[0] +
        str('  |  ') + listL2[1] + str('  |  ') + listL2[2])
        print("The next most probable letters are:", temp2)
        return top_countp2[:5] + listL2
    
    elif (len(top_countp2) == 1): #If there are only 1 predicted letters
        listL1 = ['u','z','e','r']
        temp1 = (top_countp2[0] + str('  |  ') + listL1[0] +
        str('  |  ') + listL1[1] + str('  |  ') + listL1[2] + str('  |  ') + listL1[3])
        print("The next most probable letters are:", temp1)
        return top_countp2[:5] + listL1
    
    elif (len(top_countp2) == 0): #If there are 0 predicted letters
        listL0 = ['a','e','i','o','u']
        temp0 = (listL0[0] + str('  |  ') + listL0[1] +
        str('  |  ') + listL0[2] + str('  |  ') + listL0[3] + str('  |  ') + listL0[4])
        print("The next most probable letters are:", temp0)
        return top_countp2[:5] + listL0
    
def points(lcount, utext):

    
    """

    This function tells you the amount of points that the user recieves for each
    individual letter that they input. Depending on what letter is chosen of the
    list of 5 letters predicted they will receieve points ranging from 0 to  50
    in increments of 10's.

    lcount -- list of strings
    utext -- string

    return -- number
    
    """
    
    user_print = [x[:1] for x in lcount]
    striplist = [j for i in user_print for j in i]

    total = 0
    if utext in striplist:
        # If the user chooses the first position from the left, they recieve 50 points.
        if (utext == striplist[0]):
            print('Awarded 50 points! \n')
            total += 50
        # If the user chooses the second position from the left, they recieve 40 points.
        elif (utext == striplist[1]) and (len(striplist) > 1):
            print('Awarded 40 points! \n')
            total += 40
        # If the user chooses the letter in the middle position, they recieve 30 points.
        elif (utext == striplist[2]) and (len(striplist) > 2):
            print('Awarded 30 points! \n')
            total += 30
        # If the user chooses the second position from the right, they recieve 20 points.
        elif (utext == striplist[3]) and (len(striplist) > 3):
            print('Awarded 20 points! \n')
            total += 20
        # If the user chooses the first position from the right, they recieve 10 points.
        elif (len(striplist) > 4):
            if (utext == striplist[4]):
                print('Awarded 10 points! \n')
                total += 10
        return total
    # If the user chooses a number that the program doesn't predict then they recieve 0 points.
    else:
        print("You recieved no points for this letter. \n")
    
        return total

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

def wordcheck(wordlist,finalword):

    #opens the file
    wordfile = open(finalword[0] +'.txt','r')
    #checks if their word is in the list
    if finalword in wordlist:
        print("Your word is in the dictionary")
    #appends if the word is not in the dictionary
    else:
        wordfile = open(finalword[0] +'.txt','a')
        finalprint = finalword
        finalword = str(', ') + finalword
        print(finalprint,"is not in the dictionary.")
        print(finalprint,"has been added to the dictionary")
        wordfile.write(finalword)
        
main()

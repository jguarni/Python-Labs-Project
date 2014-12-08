# Lab 5
# CISC 106
# Joe Guarni

from cisc106 import *
# Problem 1

def fib(number):
    
    """

    This function will return the value in the fibbonacci sequence of
    the input parameter the function takes.

    number - number

    return - number
    
    """
    if (number < 40000000):
    
        if (number == 0):
            return 0
        elif (number == 1):
            return 1
        else:
            return fib(number-1) + fib(number-2)
        

assertEqual(fib(7),13)
assertEqual(fib(10),55)
assertEqual(fib(11),89)

def fib2(number):
    
    """

    This function will return the sum of the even valued terms in the
    fibbonacci sequence up to the input parameter number.

    number - number

    return - number

    """
    
    counter = 0
  
    while (number > 0):
        if (fib(number) % 2) == 0:
            counter += fib(number)
        number -= 1
    return counter
        
assertEqual(fib2(10),44)
assertEqual(fib2(5),2)
assertEqual(fib2(12),188)

#Problem 2


# Part A
def tuple_avg(aList):
    """

    This function will take a list of non-empty tuples that are integers
    and return a list of averages of the elements in each tuple.

    aList - list of tuples in which the elements are integers

    return  - list of floats
    
    """
    
    newList = []
    for ele in aList:
        newList.append(sum(ele)/len(ele))
    return newList

assertEqual(tuple_avg(([(4,5,6),(1,2,3),(7,8,9)])),[5.0, 2.0, 8.0])
assertEqual(tuple_avg(([(100,200,300),(0,500,1000),(200,400,600)])),[200.0,500.0,400.0])
assertEqual(tuple_avg(([(5,10,15),(20,25,30),(30,35,40)])),[10.0, 25.0, 35.0])

# Part B

def tuple_avg_rec(aList):
    
    """
    
    This function will take a list of non-empty tuples that are integers
    and return a list of averages of the elements in each tuple using recursion.

    aList - list of tuples in which the elements are integers

    return  - list of floats
       
    """
    newList = []
    if (len(aList) == 1):
        newList.append((sum(aList[0]))/(len(aList[0])))
    
    else:
        newList.append((sum(aList[0]))/(len(aList[0])))
        newList.extend(tuple_avg_rec(aList[1:]))
    return newList

assertEqual(tuple_avg_rec(([(4,5,6),(1,2,3),(7,8,9)])),[5.0, 2.0, 8.0])
assertEqual(tuple_avg(([(100,200,300),(0,500,1000),(200,400,600)])),[200.0,500.0,400.0])
assertEqual(tuple_avg(([(5,10,15),(20,25,30),(30,35,40)])),[10.0, 25.0, 35.0])

#Problem 3

#Part A

def del_dup_neighbhor(aList):
    
    """

    This function recieves a list of numbers and returns a list where all adjacent
    elements that are equal to each other are reduced to a single element.

    aList - List of integers

    return - List of integers
    
    """
    
    newList = aList[:1]
    for ele in aList[1:]:
        if ele != newList[-1]:
            newList.append(ele)
    return newList

assertEqual(del_dup_neighbhor(([6, 7, 8, 8, 9, 2, 1, 2, 2, 3])),[6, 7, 8, 9, 2, 1, 2, 3])           
assertEqual(del_dup_neighbhor(([1,1,2,2,3,3,3,4,5,6,7,7,8,9,9])),[1,2,3,4,5,6,7,8,9])
assertEqual(del_dup_neighbhor(([1,2,2,1,1,5,6,7,7,8,7,7,9])),[1,2,1,5,6,7,8,7,9])

        
#Part B

def del_dup_neighbor_rec(aList):
    
    """
    
    This function recieves a list of numbers and returns a list where all adjacent
    elements that are equal to each other are reduced to a single element using recursion.

    aList - List of integers

    return - List of integers
    
    """
    
    newList = []
    if len(aList) == 1:
        newList.append(aList[0])
        return newList
    if aList[0] != aList[1]:
        newList.append(aList[0])
        newList.extend(del_dup_neighbor_rec(aList[1:]))
    elif aList[0] == aList[1]:
        newList.extend(del_dup_neighbor_rec(aList[1:]))
    return newList
    


assertEqual(del_dup_neighbor_rec(([1,2,2,1,1,5,6,7,7,8,7,7,9])),[1,2,1,5,6,7,8,7,9])
assertEqual(del_dup_neighbor_rec(([1,1,1,2,3,4,5,5,6])),[1,2,3,4,5,6])
assertEqual(del_dup_neighbor_rec(([1,1,1,2,2,3,3,4,5,5,5,6,4,5,5,9,8,8])),[1,2,3,4,5,6,4,5,9,8])

#Problem 4

def merging_lists(aList1, aList2):

    """

    This function recieves two lits sorted in increasing order and returns a merged list
    of all the elements sorted in increasing order completed in linear time. This function
    only makes a single pass of both lists.

    aList1 - Sorted list of integers
    aList2 - Sorted list of integers

    return - Sorted list of integers
    
    """
    
    newList = []
    index1 = 0
    index2 = 0
    final = len(aList1) + len(aList2)
    while len(newList) != final:
        if len(aList1) == index1:
            newList += aList2[index2:]
            break
        elif len(aList2) == index2:
            newList += aList1[index1:]
            break
        elif aList1[index1] < aList2[index2]:
            newList.append(aList1[index1])
            index1 += 1
        else:
            newList.append(aList2[index2])
            index2 += 1
    return newList


assertEqual(merging_lists([1,2],[3,4]), [1,2,3,4])
assertEqual(merging_lists([5,6,7,8,9],[1,2,3,4]), [1,2,3,4,5,6,7,8,9])
assertEqual(merging_lists([1,3,5,7,9],[2,4,6,8,10]), [1,2,3,4,5,6,7,8,9,10])

#Problem 5

def counting_strings(aList):
    
    """

    This function reieves a list of strings and returns a count as an integer for the
    elements where the string length is at least two and the first and last character
    of the string is the same.

    aList - List of Strings

    return - Integer
    
    """
    
    counter = 0
    for word in aList:
        if (word[0] == word[-1] and len(word) > 2):
            counter += 1
    return counter

assertEqual(counting_strings(["hello", "elude", "emancipate", "about", "good"]),2)
assertEqual(counting_strings(["sassafras", "seamless", "bots","hack", "seamstress", "sedulous"]),4)
assertEqual(counting_strings(["poor","cookie","tent","loaf", "terrorist", "therapist"]),3)

#Problem 6

def snap_two(x,y):
    
    """

    This function will recieve two strings and return a single string
    with the strings seperated and swap the first two characters of each string.

    x - string
    y- string

    return - string
    
    """
    string = y[:2] + x[2:] + str(' ') + x[:2] + y[2:]
    return string

assertEqual(snap_two('fix','pod'), 'pox fid')
assertEqual(snap_two('dog','dinner'), 'dig donner')
assertEqual(snap_two('computer','brain'), 'brmputer coain')

#Problem 7

def verb_ending(string):
    
    """

    This function will recieve a string and if the string length is atleast
    three, add 'ing' to the end. If it already ends in 'ing' it will append
    'ly' to the end. If the length is less than three it will return unchanged.

    string - string

    return - string

    """
    
    if string.endswith('ing') and (len(string) >= 3):
        string += 'ly'
        return string
    
    elif (string.endswith('ing') == False) and (len(string) >= 3):
        string += 'ing'
        return string
    
    elif (len(string) < 3):
        return string

assertEqual(verb_ending('he'), 'he')
assertEqual(verb_ending('blast'), 'blasting')
assertEqual(verb_ending('blasting'), 'blastingly')

#Problem 8

#Part A

def reverse(string):

    """

    This function will return the reverse of the arguement inputed into
    the parameter.

    string - string

    return - string

    """
    
    newString = string[::-1]
    return newString
    
assertEqual(reverse('Foobar'),'rabooF')
assertEqual(reverse('Hello World'),'dlroW olleH')
assertEqual(reverse('Genius'),'suineG')

#Part B

def isPalindrome(string):

    """

    Ths function will take a string as an argument and return boolean weather or
    not the string is a pallindrome.

    string - string
    
    return - boolean

    """

    string = string.lower()
    reverse = string[::-1].lower()
    
    if (string == reverse):
        return True
    else:
        return False
    
assertEqual(isPalindrome('peep'), True)
assertEqual(isPalindrome('Foobar'), False)
assertEqual(isPalindrome('Dad'), True)

#Problem 9

def be_happy(string):

    """

    This function will recieve a string and find the first appearence of
    the substring 'not' or 'sad' If the 'sad' follows the 'not' the 'not..sad'
    will be replaced with the substring 'happy'

    string - string

    return - string

    """

    val1 = string.find('sad')
    val2 = string.find('not')
    if (val1 > val2):
        string = string.replace(string[val2:val1+3], 'happy')
        return string
    else:
        return string

assertEqual(be_happy('Actually, he was not that sad.'), 'Actually, he was happy.')
assertEqual(be_happy('The boy was not that sad today.'), 'The boy was happy today.')
assertEqual(be_happy('Actually, he was sad that not.'), 'Actually, he was sad that not.')

#Problem 10

def mixing_up(str1,str2):

    """

    This function will take two strings as parameters and divide both strings
    in half. It the sting length is even, it will split evenly. If it is odd, the
    remaining letter will be appended to the first half of the split. The function
    will then return a string in the order of str1-front + str2-front
    + str1-back + str2-back.

    str1 - string
    str2 - string

    return - string
    
    """
    
    if len(str1) % 2 == 0 and len(str2) % 2 == 0:
        split1 = str1[:int((len(str1)/2))]
        split2 = str1[int((len(str1)/2)):]
        split3 = str2[:int((len(str2)/2))]
        split4 = str2[int((len(str2)/2)):]
    elif len(str1) % 2 != 0 and len(str2) % 2 != 0:
        split1 = str1[:int((len(str1)/2+1))]
        split2 = str1[int((len(str1)/2+1)):]
        split3 = str2[:int((len(str2)/2+1))]
        split4 = str2[int((len(str2)/2+1)):]
    elif len(str1) % 2 == 0 and len(str2) % 2 != 0:
        split1 = str1[:int((len(str1)/2))]
        split2 = str1[int((len(str1)/2)):]
        split3 = str2[:int((len(str2)/2+1))]
        split4 = str2[int((len(str2)/2+1)):]
    elif len(str1) % 2 != 0 and len(str2) % 2 == 0:
        split1 = str1[:int((len(str1)/2+1))]
        split2 = str1[int((len(str1)/2+1)):]
        split3 = str2[:int((len(str2)/2))]
        split4 = str2[int((len(str2)/2)):]

    final = str(split1) + str(split3) + str(split2) + str(split4)
    return final

assertEqual(mixing_up('house', 'truck'), 'houtruseck')
assertEqual(mixing_up('computer', 'sciences'), 'compscieuternces')
assertEqual(mixing_up('mix', 'together'), 'mitogexther') 
assertEqual(mixing_up('together', 'mix'), 'togemitherx') 

#Problem 11



from collections import Counter
import collections
import sys



#These functions will return the five most probable letters
#based on a user input. For this example we will assume the
#user input is 'c' and the dictionary list is slist.

slist = ['cambodges','cop','cone','cognitive','cameo','cent','czech','curve']
utext = 'c'

def chopper(slist, utext):

    """

    This function takes two parameters, slist and utext. It will examine
    each element in slist and check if the user input (utext) is equal to
    the first letter. If it is, the word will stay in the list. That letter
    will then be stripped from the beginning of the word and the remaining
    parts of the word will be appended to the list 'chopped'.

    slist = list of strings
    utext - string

    return - list of strings

    """
    
    chopped = []

    #The following while loop strips whitespace from the list. If the user
    #inputs 'abs' and their word is 'absolute', the whitespace from 'abs'
    #is removed from the list.
    
    while '' in slist: 
        slist.remove('')
        
    #By using this for loop the list becomes smaller and smaller with
    #each input ultimately down to the users final word.
        
    for word in slist:
        if utext != word[0]:
            del word
        else:
            word = word[1:]
            chopped.append(word)
            
    return chopped


def counts(clist):

    """

    This function will take the returned list from the fuction chopper
    and count word[0] of each element. It will then append the counted
    elements and display + return the top 5 letters in decending order
    to the user.

    clist - list of strings

    return -- list of strings

    """
    
    llist = []
    
    for word in clist:
        x = word[0:1]
        llist.append(x)
        
    while '' in llist:
        llist.remove('')
        
    #Sort the letters in the list in decending order
    top_count = sorted(Counter((llist)).items(), key=lambda x: x[1], reverse = True)
    
    print("The next most probable letters are:", top_count[:5])
    return (top_count[:5])

chopper(slist,utext)
counts(chopper(slist,utext))

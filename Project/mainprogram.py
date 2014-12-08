from readFile import *
from collections import Counter
import collections


def main():
    utext = input('Please Enter the first letter of your word: ').lower()
    letter = userinput(utext)
    wordlist = read_file(letter)
    fsearch = firstsearch(wordlist)
    
    
def userinput(atext):

    while not atext.isalpha():
        print('That is not a letter')
        atext = input('Please enter another letter: ').lower()

    return atext

def firstsearch(slist):
    #takes in word list, filters first 2 letters of each word, sorts top 5 based on frequency
    secondc = [x[:2] for x in slist]
    sortlist = sorted(Counter((secondc)).items(), key=lambda x: x[1], reverse = True)
    print(sortlist[:5])
    print_char(sortlist)
    return sortlist[:5]

def print_char(word_list):
    user_print = [x[:1] for x in word_list]
    print(user_print[:5])
    
    
    
main()

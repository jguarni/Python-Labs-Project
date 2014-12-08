"""
This is a program developed to make typing in some accessibility devices easier.
The program tries to predict the next letter the user wants to type according
the frequency (probability) of the next letter being used.

"""

import sys
import re
import os

def read_file(file_name):
    """
    It receives a letter and returns a list with all the words starting with
    that letter

    file_name -- character
    aList -- list of strings
    """

    file_name += ".txt"
    
    try:
        os.chdir("input")
        f = open(file_name, 'r')
    except IOError as err:
        print("I/O error: {0}".format(err))
    else:
        my_list = f.read().split(', ')
        f.close()
        return my_list


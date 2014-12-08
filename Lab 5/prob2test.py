from cisc106 import *

def tuple_avg_rec(aList,index):
    """
    This function will take a list of non-empty tuples with integers
    as elements and return a list with the averages of the elements
    in each tuple using recursion.

    aList - List of Numbers
    
    return - List with Floating Numbers

    """
    newList = []
    
    if len(aList) == 0:
        return 0
    
    if (len(aList) != index):
        newList.append((sum(aList[index])/len(aList[index])))
        newList.extend((sum(aList[index])/len(aList[index])))
        print(aList[index])
    tuple_avg_rec(aList, index+1)
        
    
        
    return newList



assertEqual(tuple_avg_rec(([(4,5,6),(1,2,3),(7,8,9)]),0),[5.0, 2.0, 8.0])

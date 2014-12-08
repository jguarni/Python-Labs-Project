from cisc106 import *

def tuple_avg_rec(aList):
    newList = []
    if (len(aList) == 1):
        newList.append((sum(aList[0]))/(len(aList[0])))
    
    else:
        newList.append((sum(aList[0]))/(len(aList[0])))
        newList.extend(tuple_avg_rec(aList[1:]))
    print(newList)
    return newList

assertEqual(tuple_avg_rec(([(4,5,6),(1,2,3),(7,8,9)])),[5.0, 2.0, 8.0])

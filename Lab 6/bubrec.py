def bubblesort_rec1(ilist):
    
    """

    """
    newList = []
    index = 0
    counter = 0
    print(ilist)
    
    
        
    if ilist[index] > ilist[index+1]:
        variable = ilist[index]
        ilist[index] = ilist[index+1]
        ilist[index+1] = variable
        index =+1
        bubblesort_rec1(ilist[1:])
        
    if ilist[index] < ilist[index+1] :
        variable = ilist[index+1]
        ilist[index+1] = ilist[index]
        ilist[index] = variable
        index =+1
        bubblesort_rec1(ilist[1:])
    else:
        index += 1
        bubblesort_rec1(ilist)
        
    return ilist
print(bubblesort_rec1([9,5,7,8,3,5,6,1,2]))

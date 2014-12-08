def quickSort(unsortedList):
	
	# if the length of the unsorted list is less than one
	# return it
	if len(unsortedList) <= 1:
		return unsortedList

	# Otherwise, do this...
	
	# Choosing roughly the middle element as the pivot
	pivotIndex = int(len(unsortedList)/2)
	print "Pivot Index " + str(pivotIndex)
	
	pivotElement = unsortedList.pop(pivotIndex)
	print "Pivot Element " + str(pivotElement)
	
	# Lists to hold greater than and less than elements
	lessThanList = []
	greaterThanList = []
	
	# For each item, place into a 
	for item in unsortedList:
		if item <= pivotElement:
			lessThanList.append(item)
		else:
			greaterThanList.append(item)

	print "Less Than Array is: "
	print lessThanList
	
	print "Greater Then Array is: "
	print greaterThanList
	print

	# Create a new list to concat sublists
	sortedList = []
	
	if len(lessThanList) > 0:
		sortedList.extend(quickSort(lessThanList))
	
	sortedList.append(pivotElement)
	
	if len(greaterThanList) > 0:
		sortedList.extend(quickSort(greaterThanList))
	
	return sortedList
	

def main():
	myList = [99,87,234,4,5,222,5,7]
	mySortedList = quickSort(myList)

	print "The final, sorted list is... "
	print mySortedList

if __name__ == '__main__':
	main()

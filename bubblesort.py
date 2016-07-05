import random

#This function uses the bubble sort algorithm to sort the items in a list
def bubbleSort(list):
	while True: 
		swapped = False
		for i in range(1, len(list)): #array length 0, 1 still fine here
			if list[i] < list[i - 1]:
				(list[i], list[i - 1]) = (list[i - 1], list[i])
				swapped = True
		if not swapped: #no swaps made means already ordered, stop iterating!
			break
	return list



# a = [7, 1, 6, 2, 3, 4, 8, 8, 4, 5, 10]
# a = ["bob", 53, False, "joe"]
# result = bubbleSort(a)
# print result

#populate list of random values, sort it
testlist = []
for i in range(0, 100):
	testlist.append(random.randint(0, 10000))

print testlist
bubbleSort(testlist)
print testlist

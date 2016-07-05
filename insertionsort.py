import random
import datetime

def insertionSort(list):
	for i in range(0, len(list)):
		for j in range(i, 0, -1):
			if list[j] < list[j-1]:
				(list[j], list[j-1]) = (list[j-1], list[j])
				j -= 1
	return list


#populate randomly
testlist = []
for i in range(0, 10000):
	testlist.append(random.randint(0, 10000))

start = datetime.datetime.now()
insertionSort(testlist)
finish = datetime.datetime.now()
print "Insertion Sort took ", finish - start

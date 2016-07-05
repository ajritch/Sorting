import random
import datetime

#Testing selection sort algorithms
def selectionSort(list):
	for i in range(0, len(list)):
		min_index = i #index of minimum value
		for j in range(i, len(list)):
			#if current value lower, redefine min_index
			if list[j] < list[min_index]:
				min_index = j 
		#swap current with value at min_index:
		(list[i], list[min_index]) = (list[min_index], list[i])
	return list


#second algorithm: swap min and max with each iteration
def selectionSort2(list):
	#only iterate through half because we'll be moving mins and maxes
	for i in range(0, len(list) / 2 + 1):
		min_index = i
		max_index = i
		for j in range(i, len(list) - i):
			if list[j] < list[min_index]:
				min_index = j
			elif list[j] > list[max_index]:
				max_index = j
		#swap current with min, "end" with max
		(list[i], list[min_index]) = (list[min_index], list[i])
		(list[max_index], list[len(list) - 1 - i]) = (list[len(list) - 1 - i], list[max_index])
	return list


#populate randomly and time test
testlist = []
for i in range(0, 10000):
	testlist.append(random.randint(0, 10000))
testlist2 = testlist

start = datetime.datetime.now()
selectionSort(testlist)
finish = datetime.datetime.now()
print "regular selection sort takes: ", finish - start

start = datetime.datetime.now()
selectionSort2(testlist2)
finish = datetime.datetime.now()
print "modified selection sort takes: ", finish - start


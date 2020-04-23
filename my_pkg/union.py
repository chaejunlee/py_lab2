#!/usr/bin/python

def uniAndInt(list1, list2):
	final_list = list(set(list1) | set(list2))
	final_list.sort();
	print("=> union [", end='')
	print(','.join([str(l) for l in final_list]), end='')
	print("]")
	list3 = [value for value in list1 if value in list2]
	list3.sort()
	print("=> intersection [", end='')
	print(','.join([str(l) for l in list3]), end='')
	print("]")

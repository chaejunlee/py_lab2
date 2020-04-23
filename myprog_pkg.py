#!/user/bin/python
from my_pkg.binary import *
from my_pkg.union import *

if __name__ == '__main__':
	while True:
		option = input("Select menu: 1) conversion 2) union/intersection 3) exit ? ")
		if option == '1':
			binNum = input("input binary number : ")
			binToOther(binNum)
		elif option == '2':
			list1 = input("1st list: ").strip().replace('[','').replace(']','').split(',')
			list2 = input("2nd list: ").strip().replace('[','').replace(']','').split(',')
			uniAndInt(list1, list2)
		elif option == '3':
			print("exit the program")
			break
		else:
			print("wrong input")

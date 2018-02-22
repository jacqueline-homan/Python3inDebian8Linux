#!/usr/bin/python3

# Functions returning values and printing from main
# You can return any object from a function
def main():
	#print(testfunc())
	for n in testfunc():
		print(n, end=' ')

def testfunc():
	#return 42 
	return range(25)


if __name__ == "__main__": main()
#!/usr/bin/python3 

def main():
	print("This is the functions.py file.")
	for i in inclusive_range(0, 25, 1):
		print(i, end= ' ')

def inclusive_range(start, stop, step):
	i = start
	while i <- stop:
		yield i 
		i += step

if __name__ == "__main": main()
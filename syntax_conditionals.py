#!/usr/bin/python3

def main():
	a, b = 0, 1
	if a < b: 
		print("a is less than b")
	elif a > b: 
		print("a is greater than b")
	else:
		print("a is not less than b")
	s = "Less than" if a < b else "Not less than"
	print(s)
	print("This is the syntax.py file")

if __name__ == "__main__": main()
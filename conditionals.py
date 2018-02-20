#!/usr/bin/python3

a, b = 0, 1
if a < b: 
	print('a({}) is less than b({})' .format(a,b))
else: 
	print('a({}) is NOT less than b({})' .format(a,b)) 

print("foo" if a < b else "bar")



def main():
	x, y = 2, 2
	s = "less than" if x < y else "not less than"
	print(s)

	g = 7
	if g == 0:
		print('g = 0')
	elif g == 1:
		print('g = 1')
	elif g == 2:
		print('g = 2')
	else: 
		print ('g is something else')

	results = ' this is true' if x == y else 'this is not true'
	print(results)
if __name__ == "__main__": main()
#!/usr/bin/python3.6

def main():
	x = [5]
	kitten(x)
	print(f'in main: x is {x}')
	
def kitten(a, b = 1, c = 0):
	print('Meow')
	print(a, b, c)

def cats(*args):
	x = 2
	kitten(x)
	print(f'in main: x is {x}')
	if len(args):
		for s in args:
			print(s)
	else: print('Meow.')

def main():
	cats('meow', 'hiss', 'growl', 'wimper')

if __name__ == "__main__": main()
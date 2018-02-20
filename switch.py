#!/usr/bin/python3

def main():
	choices = dict(
		one = 'first',
		two = 'second',
		three = 'third',
		four = 'fourth',
		five = 'fifth'
		)
	v = 'seven'
	print(choices.get(v, 'other'))
if __name__ == "__main__": main()
#!/usr/bin/python3

def main():
	d = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5 } # a dictionary
	for k in sorted(d.keys()):
		print(k, d[k])

	e = dict(
		one = 1, two = 2, three = 3, four = 4, five = 'five'
		) # another way of defining a dictionary
	e['seven'] = 7	
	for k in sorted(e.keys()):
		print(k, e[k])

	animals = dict(cat = 'meow!', dog = 'woof!', pig = 'freeze muthafuckas! Put yo mofuckin hands above yo heads!')
	for k, v in animals.items():
		print(f'{k}: {v}')

def print_dict(o):
	for k, v in o.items: print(f'{k}: [v]')

if __name__ == "__main__": main()
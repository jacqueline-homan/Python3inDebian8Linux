#!/usr/bin/python3

a = True
b = False
x = ( 'bear', 'lynx', 'tree', 'sky', 'rain')
y = 'lynx'

if y in x: 
	print('expression is true')
else:
	print('expression is false')

if y is x[0]:
	print('expression is true')
else:
	print('expression is false')

print(id(y))
print(id(x[0]))
print(id(x))

if a and b: 
	print('expression is true')
else:
	print('expression is false')

if a or b: 
	print('expression is true')
else:
	print('expression is false')

if not b: 
	print('expression is true')
else:
	print('expression is false')

if not a: 
	print('expression is true')
else:
	print('expression is false')	
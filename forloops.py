#!/usr/bin/python3

# for-loops use an iterator
# Note: You can also use list(fh) to read all the lines of a file
fh = open('myFirst.txt', 'r+')
#fh.write('This is a test\n')
for line in fh:
	#print(line)
	print(line, end='') #this handles the newline
#list(fh)
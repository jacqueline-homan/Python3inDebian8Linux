#!/usr/bin/python3

#for-loop for iterating over a file's contents
# until there's no more lines of text left to loop over
fh = open('myFirst.txt', 'r+')
for line in fh:
	print(line, end='') 

#!/usr/bin/python3

def main():
#	fh = open('myFirst.txt')	
#	for index, line in enumerate(fh.readline()):
		#print(line)
#		print(index, line, end='') #this handles the newline

	s = 'this is a string'
	for i, c in enumerate(s):
		#print(i,c)
		if c == 's': print('index {} is an s'.format(i))
#list(fh)
if __name__ == "__main__": main()
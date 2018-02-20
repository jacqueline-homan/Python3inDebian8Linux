#!/usr/bin/python3

import re

def main():
	fh = open('EdgarAllanPoe.txt')
	for line in fh:
		if re.search('(Len/Neverm)ore', line):
			print(line, end=' ')

if __name__ == "__main__": main()
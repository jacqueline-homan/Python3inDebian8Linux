#!/usr/bin/python3 

def isprime(n):
	if n == 1:
		return False
	for x in range(2, n):
		if n % x == 0:
			return False
	else:
		return True

def primes(n = 1):
	while(True):
		if isprime(n): yield n
		n += 1

for n in primes(): 
	if n > 100: break
	print(n)


class inclusive_range:
	def __init__(self, *args):
		numargs = len(args)
		if numargs < 1: raise TypeError('Requires at least one argument')
		elif numargs == 1:
			self.stop = args[0]
			self.start = 0
			self.step = 1
		elif numargs == 2:
			(self.start, self.stop) = args
			self.step = 1
		elif numargs == 3:
			(self.start, self.stop, self.step) = args
		else: raise TypeError('Expected at most 3 arguments, but given {}'.format(numargs))

	def __iter__(self):
		i = self.start
		while i <= self.stop:
			yield i 
			i += self.step
def main():
	# range takes a start, a stop and a step
	# By default, range begins with 0 and step = 1
	o = inclusive_range(25) 
	for i in o: print(i, end = ' ')


if __name__ == "__main__": main()
#!/usr/bin/python3
import time

def f1(f):
	def f2():
		print('This is before the function call')
		f()
		print('This is after the function call')
	return f2

#def f3():
#	print('This is f3')

#x = f1(f3)
#x()
@f1
def f3():
	print('This is f3')

f3()

def elapsed_time(f):
	def wrapper():
		t1 = time.time()
		f()
		t2 = time.time()
		print(f'Elapsed time: {(t2 -t1) * 1000} ms')
	return wrapper

@elapsed_time
def big_sum():
	num_list = []
	for num in (range(0, 10000)):
		num_list.append(num)
	print(f'Big sum: {sum(num_list)}')

def main():
	big_sum()

if __name__ == '__main__': main()
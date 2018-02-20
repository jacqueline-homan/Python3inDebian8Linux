#!/usr/bin/python3

# Fibonacci sequence
def main():
	a, b = 0, 1
	while b < 50:
		print(b, end=' ')
		a, b = b, a + b
	print("Done")

if __name__ == "__main__": main()

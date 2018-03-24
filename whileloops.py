#!/usr/bin/python3


# Fibonacci sequence
def main():
	a, b = 0, 1
	while b < 50:
		print(b, end=' ')
		a, b = b, a + b
	print("Done")

	secret = 'swordfish'
	pw = ''
	while pw != secret:
		pw = input("what's the secret word? ")

if __name__ == "__main__": main()

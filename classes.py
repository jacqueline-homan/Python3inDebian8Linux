#!/usr/bin/python3

class Duck:
	def __init__(self, value): 
		#print('constructor')
		self._v = value

	def quack(self):
		print("Quaaaaack!", self._v)

	def walk(self):
		print("walks like a duck", self._v)

def main():
	donald = Duck(47)
	daffy = Duck(50)
	donald.quack()
	donald.walk()
	daffy.quack()
	daffy.walk()

if __name__ == "__main__": main()
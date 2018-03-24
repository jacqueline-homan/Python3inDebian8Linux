#!/usr/bin/python3

class Animal:
	def talk(self):
		print('I got something to say!')

	def walk(self):
		print('Hey! I''m walkin'' here!')

	def clothes(self):
		print('I have nice clothes.')

class Duck(Animal):
	
	def quack(self):
		print("Quaaaaack!")

	def walk(self):
		super().walk()
		print("walks like a duck")

	def bark(self):
		print('The duck cannot bark')

	def fur(self):
		print('The duck has feathers')


class Dog(Animal):

	def bark(self):
		print('Woof!')

	def walk(self):
		super().walk()
		print('Plays fetch')

	def fur(self):
		super().clothes()
		print('I have brown and white fur.')

	def quack(self):
		print('The dog does not quack')


def main():
	donald = Duck()	
	#donald.quack()
	#donald.walk()
	#donald.clothes()

	fido = Dog()
	#fido.bark()
	#fido.clothes()
	in_the_forest(donald)
	in_the_pond(fido)
	#for o in (donald,fido):
		#o.quack()
		#o.bark()
	#	o.walk()
def in_the_forest(dog):
	dog.bark()
	dog.fur()

def in_the_pond(duck):
	duck.quack()
	duck.walk()


if __name__ == "__main__": main()
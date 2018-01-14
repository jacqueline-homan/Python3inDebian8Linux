#!/usr/bin/python3 

#--View --
class AnimalActions:
	def quack(self): return self._doAction('quack')
	def feathers(self): return self._doAction('feathers')
	def bark(self): return self._doAction('bark')
	def fur(self): return self._doAction('fur')

	def _doAction(self, action):
		if action in self.strings:
			return self.strings[action]
		else:
			return 'The {} has no {}'.format(self.animalName(), action)

	def animalName(self):
		return self.__class__.__name__.lower()

#-- Model --
class Duck(AnimalActions):
	strings = dict(
		quack = "Quaaaaaaaaaaak!",
		feathers = "The duck as shiny green feathers on its head.",
		bark = "The duck cannot bark.",
		fur = "The duck has no fur."
		)

class Dog(AnimalActions):
	strings = dict(
		bark = "Woof!",
		fur = "The dog has white fur with black spots"
		)

class Person(AnimalActions):
	strings = dict(
		quack = "The person says 'quaak' to imitate a duck.",
		feathers = "The person wears a feather in a hat",
		bark = "The person says 'Woof!' to imitate a dog.",
		fur = "The person has some hair but not fur"
		)
#--Controller
def in_the_doghouse(dog):
	print(dog.bark())
	print(dog.fur())

def in_the_forest(duck):
	print(duck.quack())
	print(duck.feathers())

def main():
	donald = Duck()
	fido = Dog()
	dood = Person()

	print("- In the forest:")
	for o in (donald, fido, dood):
		in_the_forest(o)

	print("- In the doghouse:")
	for o in (donald, fido, dood):
		in_the_doghouse(o)

if __name__ == "__main__": main()
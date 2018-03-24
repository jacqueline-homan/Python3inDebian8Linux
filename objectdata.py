#!/usr/bin/python3

class Duck:
	#def __init__(self, color = 'white'):
	def __init__(self, **kwargs): 
		#self._color = color
		#self._color = kwargs.get('color', 'white')
		#self.variables = kwargs.get('color', 'white')
		self.variables = kwargs
		

	def quack(self):
		print("Quaaaaack!", self._v)

	def walk(self):
		print("walks like a duck", self._v)

#	def set_color(self, color):
		#self._color = color
#		self.variables['color'] = color

#	def get_color(self):
		#return self._color
#		return self.variables.get('color', None)
	def set_variable(self, k, v):
		self.variables[k] = v

	def get_variable(self, k):
		return self.variables.get(k, None)

	


def main():
	donald = Duck(feet = 2)
	#print(donald.get_color())
	donald.set_variable('color', 'blue')
	print(donald.get_variable('color'))
	print(donald.get_variable('feet'))
	#donald.set_color('blue')
	#print(donald.get_color())
	#donald.quack()
	#donald.walk()
	

if __name__ == "__main__": main()
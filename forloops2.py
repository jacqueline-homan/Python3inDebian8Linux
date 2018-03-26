#!/usr/bin/python3

animals = ('bear', 'lynx', 'serval', 'raccoon')

for pet in animals:
	if pet == 'lynx': continue
	if pet == 'raccoon': break
	print(pet)
else: 
	print('That is all of the animals')
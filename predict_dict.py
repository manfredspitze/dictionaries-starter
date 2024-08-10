# A simple Python dictionary that contains data about my cat

cat = {
	'name' : 'Sepp',
	'age' : 3,
	'color' : 'grey',
	'eye_color' : 'yellow',
	'friendly' : True
}



# How would I print my cat's age?
print('Just printing my cat\'s age...')
print(cat['age'])

print()

print('Adding my cat\'s age to an f-string...')
print(f"Sepp's age: { cat['age'] }")
print()



# print('Printing my cat\'s eye color...')
# print(cat['eye_color'])
# print()


# LIST containing data about an alien
alien1 = ['zork', 700, 'green', 'Zellian 7']

# DICTIONARY containing data about an alien
alien2 = {
	'first_name' : 'zork',
	'age' : 700,
	'color' : 'green',
	'home_planet' : 'Zellian 7'
}

# Using pop ( ) to remove a LIST item
print(alien1)
alien1.pop(0)
print(alien1)

# Using pop ( ) to remove a DICTIONARY item
print(alien2)
alien2.pop('first_name')
print(alien2)



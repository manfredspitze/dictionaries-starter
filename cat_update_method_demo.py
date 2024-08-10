cat = {
	'name' : 'Sepp',
	'age' : 2,
	'color' : 'grey',
	'friendly' : True
}

# Update a DICT item
cat['age'] = 5
print(f"Sepp is now { cat['age'] } years old.")

# Using update ( ) method to update a key-value pair (DICT item)
cat.update( {'age' : 4} )
print('Updated dictionary')
print(cat)
print(f"Sepp's age: {cat.get('age', 'Requested key not found in dictionary!') }")

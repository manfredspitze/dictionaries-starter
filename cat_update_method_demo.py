cat = {
	'name' : 'Sepp',
	'age' : 2,
	'color' : 'grey',
	'friendly' : True
}

# Update a DICT item using SQUARE BRACKET NOTATION
cat['age'] = 5
print(f"Sepp is now { cat['age'] } years old.")


# Using the update ( ) method to update a dictionary item
cat.update( {'age' : 4} )
print('Updated dictionary')
print(cat)
print(f"Sepp's age: {cat.get('age', 'Requested key not found in dictionary!') }")



# Another example that uses the built-in update ( ) method

# NOTE:
# If a key in the new dictionary already exists in the original dictionary, the value for that key will be overwritten
# If a key in the new dictionary does not exist in the original dictionary, a new key-value pair will be added to the dictionary

# Original dictionary
original_dict = {'apple': 3, 'banana': 2, 'cherry': 5}

# Dictionary with new/updated key-value pairs
new_dict = {'banana': 4, 'orange': 6}

# Update the original dictionary
original_dict.update(new_dict)

print(original_dict)
# Output: {'apple': 3, 'banana': 4, 'cherry': 5, 'orange': 6}



# get ( ) method
# What it does: Returns value of a specified key if the key is in the dictionary

# Takes two (2) parameters
# Parameter 1: Name of the key to search for in the dict
# Parameter 2 (optional): A value to be returned if the specified key is not found (Default value returned is None)

person = {'first_name': 'Phil', 'age': 22, 'salary' : 56780}




# person = {'first_name': 'Phil', 'age': 22, 'salary' : 57500}

# print(f" Name: {person.get('first_name') } ")
# print(f" Age: {person.get('age') } ")

# No default value is specified here for the get ( ) method (so the default value of None will be returned and printed)
# None means the key you requested was not found in the dictionary
# print(f" {person.get('salary') } ")
print(f"Your salary: ${person.get('salary', 25000) } ")


# Default value of 0.00 is used with the get ( ) method
# print(f"${person.get('salary', 'That key was not found in the dict.')}")
# print(f"Salary key not found in dictionary, so default salary of ${person.get('salary', 0.00) } will be used instead.")

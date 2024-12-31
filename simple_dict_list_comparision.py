# List of planets
planets = ['Mars', 'Jupiter', 'Saturn']

# Dictionary containing info about a specific alien
my_alien = {'first_name' : 'zork', 'home_planet' : 'delta 7'}


# Access alien's first name in the dictionary
print(my_alien['first_name'])
print()

# Build an f-string using key-value pairs from the dictionary
print(f"{my_alien['first_name'].title()} comes from the planet {my_alien['home_planet'].title()}.")
print()


# Display output from the list
print(planets[0])
print()

print(f'The first planet in the list is: {planets[0]}')
print(f'The second planet in the list is: {planets[1]}')
print()

last_item_index = len(planets) - 1
print(f'The last planet in the list is: {planets[last_item_index]}')
print(f'The last planet in the list is: {planets[-1]}')

# Source: https://youtu.be/ekkEq-OjAmg

suitcase = {
	'sweatshirts' : 2,
	'socks' : 7,
	'shoes' : 2,
	't-shirts' : 5,
	'toothbrush' : 1
}

# Print contents of the suitcase
print(suitcase)
print()

# Print all items using a loop
for item in suitcase:
	print(item)

# Print how many t-shirts and socks I have
print()
print(f"Number of pairs of socks: { suitcase['socks'] }")
print(f"Number of sweatshirts: { suitcase['sweatshirts'] }")
print()

# Display each key-value pair in the dict
print('Your suitcase contains the following items:\n')
for item in suitcase:
	print(f'{item} : {suitcase[item]} ')
print()
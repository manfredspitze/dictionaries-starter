## Python Dictionaries: Counting the Number of Key-Value Pairs 


### Three Techniques for Counting the Number of Key-Value Pairs

- Use the `len()` function (just like you would with a Python list)

# Using len()
```python
my_dict = {'apple': 3, 'banana': 2, 'cherry': 5}
num_pairs = len(my_dict)
print(num_pairs)  # Output: 3
```

- Use a `for` loop to count the number of keys in the dictionary

# Using a for loop over keys
```python
my_dict = {'apple': 3, 'banana': 2, 'cherry': 5}
count = 0
for key in my_dict:
    count += 1
print(count)  # Output: 3
```

- Use the `items()` method and a `for` loop to count the number of items in the dictionary
- Remember: A dictionary **item** is another word for a **key-value** pair

# Using a for loop over items()
```python
my_dict = {'apple': 3, 'banana': 2, 'cherry': 5}
count = 0
for key, value in my_dict.items():
    count += 1
print(count)  # Output: 3
```

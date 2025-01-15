### Python: Using the `get()` Method to Check for a Specific Dictionary Key

### Example 1: Basic Use
```python
# Define a dictionary of fruits and their colors
fruits = {
    'apple': 'red',
    'banana': 'yellow',
    'grape': 'purple'
}

# Use get() to retrieve the color of an apple
apple_color = fruits.get('apple', 'Color not found!')
print(f"The color of an apple is {apple_color}.")  # Output: The color of an apple is red.
```

### Example 2: Key Not Found
```python
# Define a dictionary of countries and their capitals
capitals = {
    'USA': 'Washington, D.C.',
    'France': 'Paris',
    'Germany': 'Berlin'
}

# Use get() to retrieve the capital of Italy (not in the dictionary)
italy_capital = capitals.get('Italy', 'Capital not found!')
print(f"The capital of Italy is: {italy_capital}")  # Output: The capital of Italy is: Capital not found!
```

### Example 3: Using a Default Value
```python
# Define a dictionary of students and their grades
grades = {
    'Alice': 90,
    'Bob': 85,
    'Charlie': 92
}

# Use get() to retrieve the grade of a student who is not in the dictionary
dave_grade = grades.get('Dave', '(Grade not available)')
print(f"Dave's grade: {dave_grade}")  # Output: Dave's grade: (Grade not available)
```

In these examples:
- The `get()` method is used to retrieve values associated with specific keys.
- If the key is found, Python returns the corresponding value; if not, Python returns a specified default value.

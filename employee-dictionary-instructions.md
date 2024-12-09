**Python Coding Assignment: Employee Dictionary**

**Objective:**

- Create a Python dictionary to store information about an employee. 

- Use the `get()` method to retrieve specific values from the dictionary.

- Also use the `get( )` method to handle cases where the key the user requests is not contained in the dictionary.

**Instructions:**

1. **Define the Dictionary:**
   - Create a Python dictionary named `employee`.
   - Add the following key-value pairs to the dictionary:
     - `'first_name'` (string)
     - `'last_name'` (string)
     - `'age'` (integer)
     - `'hire_date'` (string, in YYYY-MM-DD format)
     - `'base_salary'` (float)

   **Example:**

   ```python
   employee = {
       'first_name': 'John',
       'last_name': 'Doe',
       'age': 30,
       'hire_date': '2023-01-15',
       'base_salary': 50000.00
   }
   ```

2. **Using the `get()` Method:**
   - Use the `get()` method to retrieve specific values from the dictionary.
   - Provide the key as the first argument in the `get()` method.
   - If the key exists, return the corresponding value.
   - **If the key doesn't exist** the `get()` method should return `None` by default.

   **Example:**

   ```python
   first_name = employee.get('first_name')
   print(first_name)  # Output: John
   ```

3. **Using `get()` with a Default Value:**
   - You can provide a default value as the second argument in the `get()` method.
   - If the key doesn't exist, the default value of `None` will be returned instead.

   **Example:**

   - To retrieve the employee's middle name, which is not one of the keys in the `employee` dictionary shown above:

   ```python
   middle_name = employee.get('middle_name', 'N/A')
   print(middle_name)  # Output: N/A
   ```


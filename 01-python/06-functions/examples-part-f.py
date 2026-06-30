"""
============================================================
Topic 6 - Functions (Part F)
First-Class Functions

This file demonstrates:

1. Functions are Objects
2. Assigning Functions to Variables
3. Passing Functions as Arguments
4. Returning Functions
5. Storing Functions in Collections
6. Building a Simple ETL Pipeline
7. Interview Traps
8. Production Best Practices

Author: Sandeep Dass
============================================================
"""

# ============================================================
# Example 1 - Functions are Objects
# ============================================================

print("\n========== Example 1 ==========")


def greet(name):
    return f"Hello {name}"


print(type(greet))

"""
Output

<class 'function'>

Functions are objects in Python.
"""

# ============================================================
# Example 2 - Assign Function to a Variable
# ============================================================

print("\n========== Example 2 ==========")

say_hello = greet

print(say_hello("John"))

"""
Notice

No parentheses while assigning.

We are storing the function,
not calling it.
"""

# ============================================================
# Example 3 - Passing a Function as an Argument
# ============================================================

print("\n========== Example 3 ==========")


def square(number):
    return number * number


def execute(number, operation):
    return operation(number)


print(execute(5, square))

"""
execute()

doesn't know

what operation to perform.

It simply calls the function
that it receives.
"""

# ============================================================
# Example 4 - Passing Different Functions
# ============================================================

print("\n========== Example 4 ==========")


def cube(number):
    return number ** 3


print(execute(5, cube))

"""
The same execute() function
works with different behaviors.
"""

# ============================================================
# Example 5 - Returning a Function
# ============================================================

print("\n========== Example 5 ==========")


def choose_formatter(make_upper):

    if make_upper:
        return str.upper

    return str.lower


formatter = choose_formatter(True)

print(formatter("john"))

formatter = choose_formatter(False)

print(formatter("JOHN"))

"""
Functions can return
other functions.
"""

# ============================================================
# Example 6 - Store Functions Inside a List
# ============================================================

print("\n========== Example 6 ==========")

operations = [
    square,
    cube
]

for operation in operations:
    print(operation(3))

"""
Every list element
is a function object.
"""

# ============================================================
# Example 7 - ETL Pipeline Example
# ============================================================

print("\n========== Example 7 ==========")


def clean_name(record):
    record = record.copy()
    record["name"] = record["name"].strip().title()
    return record


def convert_salary(record):
    record = record.copy()
    record["salary"] = int(record["salary"])
    return record


def add_status(record):
    record = record.copy()
    record["status"] = "Processed"
    return record


employee = {
    "name": " john ",
    "salary": "100000"
}

pipeline = [
    clean_name,
    convert_salary,
    add_status
]

for step in pipeline:
    employee = step(employee)

print(employee)

"""
Very similar to
real ETL pipelines.

Each function performs
one responsibility.
"""

# ============================================================
# Example 8 - Interview Trap
# ============================================================

print("\n========== Example 8 ==========")

processor = clean_name

print(processor)

print(processor(employee))

"""
processor = clean_name

stores the function.

processor = clean_name()

would execute it immediately.
"""

# ============================================================
# Example 9 - First-Class Functions with map()
# ============================================================

print("\n========== Example 9 ==========")

numbers = [1, 2, 3, 4]

result = map(square, numbers)

print(list(result))

"""
map()

expects a function.

square is passed as
a function object.
"""

# ============================================================
# Example 10 - First-Class Functions with sorted()
# ============================================================

print("\n========== Example 10 ==========")

employees = [
    {"name": "John", "salary": 90000},
    {"name": "Alice", "salary": 120000},
    {"name": "Mike", "salary": 85000}
]

sorted_employees = sorted(
    employees,
    key=lambda employee: employee["salary"]
)

print(sorted_employees)

"""
sorted()

also accepts a function.

The lambda is passed
as a function object.
"""

# ============================================================
# Example 11 - Production Insight
# ============================================================

print("\n========== Example 11 ==========")

"""
Frameworks like:

- Airflow
- Flask
- FastAPI
- Pandas
- PySpark

all rely heavily on
first-class functions.

Understanding this concept
makes decorators and callbacks
much easier to learn.
"""

print("Production Insight Complete!")

# ============================================================
# Example 12 - Performance & Design Notes
# ============================================================

print("\n========== Example 12 ==========")

"""
Prefer passing functions
instead of using large
if-else chains.

Example:

pipeline = [
    clean_name,
    convert_salary,
    validate_country
]

Adding a new processing step
only requires appending
another function.

This follows the
Open/Closed Principle (OCP).
"""

print("Design Notes Complete!")

# ============================================================
# END
# ============================================================

print("\nCongratulations!")
print("You completed First-Class Functions examples.")
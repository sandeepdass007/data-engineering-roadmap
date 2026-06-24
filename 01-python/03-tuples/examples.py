"""
Topic 3 - Tuples
Examples for GitHub Repository

A tuple is an ordered and immutable collection.
Think:
List  -> Mutable
Tuple -> Immutable
"""

# ==========================================================
# 1. Creating Tuples
# ==========================================================

employee = ("John", 100000)

print(employee)

# Mixed datatypes are allowed

employee_record = ("John", 100000, True)

print(employee_record)

# Empty tuple

empty_tuple = ()

print(empty_tuple)


# ==========================================================
# 2. Single Element Tuple
# ==========================================================

# NOT a tuple

name = ("John")

print(type(name))

# Correct single element tuple

name_tuple = ("John",)

print(type(name_tuple))


# ==========================================================
# 3. Accessing Values
# ==========================================================

employee = ("John", 100000)

print(employee[0])  # John
print(employee[1])  # 100000

# Negative indexing

print(employee[-1])  # 100000


# ==========================================================
# 4. Slicing
# ==========================================================

employee = ("John", "Toronto", 100000)

print(employee[0:2])

# Output:
# ('John', 'Toronto')


# ==========================================================
# 5. Immutability
# ==========================================================

employee = ("John", 100000)

# This would fail

# employee[0] = "Mike"

# TypeError:
# 'tuple' object does not support item assignment


# ==========================================================
# 6. Tuple Packing
# ==========================================================

employee = "John", 100000

print(employee)

# Python automatically creates:

# ("John", 100000)


# ==========================================================
# 7. Tuple Unpacking
# ==========================================================

employee = ("John", 100000)

name, salary = employee

print(name)
print(salary)


# ==========================================================
# 8. Returning Multiple Values
# ==========================================================

def get_employee():
    return "David", 150000


name, salary = get_employee()

print(name)
print(salary)

# Behind the scenes Python returns:

# ("David", 150000)


# ==========================================================
# 9. Tuple Methods
# ==========================================================

numbers = (1, 2, 2, 3, 4)

print(numbers.count(2))

print(numbers.index(3))


# ==========================================================
# 10. Iterating Through Tuples
# ==========================================================

employee = ("John", 100000)

for value in employee:
    print(value)


# ==========================================================
# 11. List of Tuples
# ==========================================================

employees = [
    ("John", 100000),
    ("Mike", 120000),
    ("Alice", 90000)
]

for employee in employees:
    print(employee)


# ==========================================================
# 12. Tuple Unpacking in Loops
# ==========================================================

employees = [
    ("John", 100000),
    ("Mike", 120000),
    ("Alice", 90000)
]

for name, salary in employees:
    print(f"{name} earns {salary}")


# ==========================================================
# 13. Data Engineering Example
# ==========================================================

# Simulating records returned from a database

employees = [
    (1, "John", 100000),
    (2, "Mike", 120000),
    (3, "Alice", 90000)
]

for employee_id, name, salary in employees:
    print(
        f"ID={employee_id}, "
        f"Name={name}, "
        f"Salary={salary}"
    )


# ==========================================================
# 14. ETL Metrics Example
# ==========================================================

def process_batch():
    rows_processed = 1000
    rows_failed = 12

    return rows_processed, rows_failed


processed, failed = process_batch()

print(f"Processed={processed}")
print(f"Failed={failed}")


# ==========================================================
# 15. Advanced Unpacking
# ==========================================================

record = ("John", "Toronto", "Canada", 100000)

name, city, country, salary = record

print(name)
print(city)
print(country)
print(salary)


# ==========================================================
# 16. Star Unpacking
# ==========================================================

record = ("John", "Toronto", "Canada", 100000)

name, *location, salary = record

print(name)

# ['Toronto', 'Canada']
print(location)

print(salary)


# ==========================================================
# 17. Production Insight
# ==========================================================

# Good use case for tuples:
#
# Configuration values
# Database connection details
# Fixed coordinates
# Function return values
# Column definitions
#
# Because they should not change.


# ==========================================================
# 18. When NOT To Use Tuples
# ==========================================================

# Bad example:

employees = ("John", "Mike")

# If you expect to add/remove employees,
# use a List instead.

# employees.append("Alice")
# AttributeError


# ==========================================================
# 19. Interview Favorite
# ==========================================================

a = 10
b = 20

a, b = b, a

print(a)
print(b)

# Output:
# 20
# 10

# Uses tuple packing and unpacking internally.

# ==========================================================
# 20. Tuples as Dictionary Keys
# ==========================================================

employee_salary = {
    ("John", "IT"): 100000,
    ("Mike", "Finance"): 120000
}

print(employee_salary[("John", "IT")])


# ==========================================================
# 21. Composite Keys
# ==========================================================

sales = {
    ("Canada", 2024): 500000,
    ("Canada", 2025): 600000,
    ("USA", 2024): 900000
}

print(sales[("Canada", 2025)])


# ==========================================================
# 22. Unhashable Example
# ==========================================================

# This will fail

# bad_key = {
#     [1, 2]: "ABC"
# }

# TypeError:
# unhashable type: 'list'


# ==========================================================
# 23. Nested Tuple Caveat
# ==========================================================

good_key = (
    "Canada",
    2024
)

# Hashable


# bad_key = (
#     "Canada",
#     [2024]
# )

# Not hashable because list is mutable


# ==========================================================
# 24. Named Tuples
# ==========================================================

from collections import namedtuple

Employee = namedtuple(
    "Employee",
    ["id", "name", "city", "salary"]
)

employee = Employee(
    1001,
    "John",
    "Toronto",
    100000
)

print(employee.name)

print(employee.salary)

# Still supports indexing

print(employee[1])

# John


# ==========================================================
# 25. Production Example
# ==========================================================

sales = {
    ("Canada", "Laptop"): 100,
    ("Canada", "Phone"): 200,
    ("USA", "Laptop"): 300
}

print(
    sales[("Canada", "Laptop")]
)
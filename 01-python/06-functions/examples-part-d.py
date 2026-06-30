"""
============================================================
Topic 6 - Functions (Part D)
Lambda Functions

This file demonstrates:

1. Creating Lambda Functions
2. Lambda with Multiple Parameters
3. Conditional Lambda
4. Lambda with sorted()
5. Lambda with Lists of Dictionaries
6. Lambda in ETL Scenarios
7. Common Interview Traps
8. Production Best Practices

Author: Sandeep Dass
============================================================
"""

# ============================================================
# Example 1 - Your First Lambda
# ============================================================

print("\n========== Example 1 ==========")
print("Basic Lambda")

square = lambda x: x * x

print(square(5))
print(square(10))

"""
Equivalent Function

def square(x):
    return x * x
"""

# ============================================================
# Example 2 - Multiple Parameters
# ============================================================

print("\n========== Example 2 ==========")

add = lambda a, b: a + b

print(add(10, 20))
print(add(50, 25))

# ============================================================
# Example 3 - Conditional Expression
# ============================================================

print("\n========== Example 3 ==========")

status = lambda age: "Adult" if age >= 18 else "Minor"

print(status(25))
print(status(12))

# ============================================================
# Example 4 - Lambda Returning Boolean
# ============================================================

print("\n========== Example 4 ==========")

is_even = lambda number: number % 2 == 0

print(is_even(10))
print(is_even(7))

"""
Very common pattern.

Returns

True

or

False
"""

# ============================================================
# Example 5 - Sorting Numbers
# ============================================================

print("\n========== Example 5 ==========")

numbers = [5, 9, 1, 4, 8]

print(sorted(numbers))

"""
Lambda is NOT required here.

Python already knows
how to sort numbers.
"""

# ============================================================
# Example 6 - Sorting Strings by Length
# ============================================================

print("\n========== Example 6 ==========")

names = [
    "Alexander",
    "John",
    "Mike",
    "Sam"
]

sorted_names = sorted(
    names,
    key=lambda name: len(name)
)

print(sorted_names)

"""
Lambda tells sorted()

what to compare.

NOT

how to sort.
"""

# ============================================================
# Example 7 - Sorting Dictionaries
# ============================================================

print("\n========== Example 7 ==========")

employees = [

    {
        "name": "John",
        "salary": 90000
    },

    {
        "name": "Mike",
        "salary": 120000
    },

    {
        "name": "Alice",
        "salary": 80000
    }

]

sorted_employees = sorted(
    employees,
    key=lambda employee: employee["salary"]
)

for employee in sorted_employees:
    print(employee)

"""
Without lambda,

Python wouldn't know
which field to sort by.
"""

# ============================================================
# Example 8 - Descending Sort
# ============================================================

print("\n========== Example 8 ==========")

sorted_employees = sorted(
    employees,
    key=lambda employee: employee["salary"],
    reverse=True
)

for employee in sorted_employees:
    print(employee)

# ============================================================
# Example 9 - ETL Example
# ============================================================

print("\n========== Example 9 ==========")

customers = [

    {
        "id": 101,
        "name": "John",
        "records": 12
    },

    {
        "id": 102,
        "name": "Mike",
        "records": 5
    },

    {
        "id": 103,
        "name": "Alice",
        "records": 20
    }

]

customers = sorted(
    customers,
    key=lambda customer: customer["records"],
    reverse=True
)

for customer in customers:
    print(customer)

"""
Imagine these are

customers with

largest number

of transactions.
"""

# ============================================================
# Example 10 - Using max()
# ============================================================

print("\n========== Example 10 ==========")

highest_paid = max(
    employees,
    key=lambda employee: employee["salary"]
)

print(highest_paid)

"""
Lambda tells max()

which value

to compare.
"""

# ============================================================
# Example 11 - Using min()
# ============================================================

print("\n========== Example 11 ==========")

lowest_paid = min(
    employees,
    key=lambda employee: employee["salary"]
)

print(lowest_paid)

# ============================================================
# Example 12 - Interview Trap
# ============================================================

print("\n========== Example 12 ==========")

square = lambda x: x * x

print(type(square))

"""
Output

<class 'function'>

Many beginners think

lambda creates

a special object.

It doesn't.

Lambda creates

a normal function object.
"""

# ============================================================
# Example 13 - Function vs Lambda
# ============================================================

print("\n========== Example 13 ==========")

# Good
double = lambda x: x * 2

# Better when logic grows


def calculate_bonus(employee):

    if employee["salary"] > 100000:
        return employee["salary"] * 0.20

    return employee["salary"] * 0.10


employee = {
    "salary": 120000
}

print(calculate_bonus(employee))

"""
As logic becomes larger,

prefer normal functions.
"""

# ============================================================
# Example 14 - Production Insight
# ============================================================

print("\n========== Example 14 ==========")

"""
You'll see code like this

in Pandas

df["salary"].apply(
    lambda salary: salary * 1.10
)

and

in PySpark

rdd.map(
    lambda row: row.upper()
)

We'll learn both soon.

Lambda is one of the reasons
Python data processing code
is so concise.
"""

print("Preview Complete!")

# ============================================================
# END
# ============================================================

print("\nCongratulations!")
print("You completed Lambda examples.")
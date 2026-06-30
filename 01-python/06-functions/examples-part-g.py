"""
============================================================
Topic 6 - Functions (Part G)
filter() Function

This file demonstrates:

1. Basic filter()
2. filter() with Lambda
3. filter() with User-defined Functions
4. Filtering Dictionaries
5. Filtering Invalid Records
6. SQL & ETL Examples
7. Interview Traps
8. Production Best Practices

Author: Sandeep Dass
============================================================
"""

# ============================================================
# Example 1 - Basic filter()
# ============================================================

print("\n========== Example 1 ==========")


def is_even(number):
    return number % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]

result = filter(is_even, numbers)

print(result)          # Filter Object
print(list(result))    # Actual Values

"""
filter() returns
a lazy iterator.

It is evaluated only
when consumed.
"""

# ============================================================
# Example 2 - filter() using Lambda
# ============================================================

print("\n========== Example 2 ==========")

numbers = [10, 15, 20, 25, 30]

even_numbers = list(
    filter(
        lambda number: number % 2 == 0,
        numbers
    )
)

print(even_numbers)

# ============================================================
# Example 3 - Remove Empty Values
# ============================================================

print("\n========== Example 3 ==========")

countries = [
    "Canada",
    "",
    None,
    "USA",
    "India",
    ""
]

valid_countries = list(
    filter(
        lambda country: country,
        countries
    )
)

print(valid_countries)

"""
Falsy values:

None
""
0
False

are automatically removed.
"""

# ============================================================
# Example 4 - Salary Filter
# ============================================================

print("\n========== Example 4 ==========")

employees = [
    {"name": "John", "salary": 120000},
    {"name": "Mike", "salary": 60000},
    {"name": "Alice", "salary": 90000}
]

high_salary = list(
    filter(
        lambda employee:
            employee["salary"] >= 80000,
        employees
    )
)

print(high_salary)

# ============================================================
# Example 5 - Using a Named Function
# ============================================================

print("\n========== Example 5 ==========")


def is_high_salary(employee):
    return employee["salary"] >= 80000


filtered = list(
    filter(
        is_high_salary,
        employees
    )
)

print(filtered)

"""
Named functions become
more readable when
business logic grows.
"""

# ============================================================
# Example 6 - Multiple Conditions
# ============================================================

print("\n========== Example 6 ==========")

employees = [
    {
        "name": "John",
        "salary": 120000,
        "country": "Canada"
    },
    {
        "name": "Mike",
        "salary": 60000,
        "country": "USA"
    },
    {
        "name": "Alice",
        "salary": 150000,
        "country": "Canada"
    }
]

filtered = list(
    filter(
        lambda employee:
            employee["salary"] >= 100000
            and employee["country"] == "Canada",
        employees
    )
)

print(filtered)

# ============================================================
# Example 7 - ETL Data Validation
# ============================================================

print("\n========== Example 7 ==========")

incoming_records = [
    {"id": 101, "country": "Canada"},
    {"id": 102, "country": ""},
    {"id": 103, "country": "USA"},
    {"id": 104, "country": None}
]


def is_valid_record(record):
    return bool(record["country"])


valid_records = list(
    filter(
        is_valid_record,
        incoming_records
    )
)

print(valid_records)

"""
Imagine invalid records
being sent to a
rejection file.
"""

# ============================================================
# Example 8 - SQL Comparison
# ============================================================

print("\n========== Example 8 ==========")

print("""
SQL Equivalent

SELECT *
FROM employees
WHERE salary >= 80000;
""")

print("""
Python Equivalent

filter(
    lambda employee:
        employee["salary"] >= 80000,
    employees
)
""")

# ============================================================
# Example 9 - Interview Trap
# ============================================================

print("\n========== Example 9 ==========")

numbers = [5, 10, 15]

filtered = filter(
    lambda x: x > 7,
    numbers
)

print(list(filtered))
print(list(filtered))

"""
First Output

[10, 15]

Second Output

[]

Reason:

filter() returns
an iterator.

Iterators are exhausted
after consumption.
"""

# ============================================================
# Example 10 - map() vs filter()
# ============================================================

print("\n========== Example 10 ==========")

numbers = [1, 2, 3, 4]

mapped = list(
    map(
        lambda x: x * 10,
        numbers
    )
)

filtered = list(
    filter(
        lambda x: x % 2 == 0,
        numbers
    )
)

print("map():", mapped)
print("filter():", filtered)

"""
map()

Transforms values.

filter()

Keeps or removes values.
"""

# ============================================================
# Example 11 - Production Insight
# ============================================================

print("\n========== Example 11 ==========")

"""
Real-world ETL pipelines
usually perform filtering
before expensive processing.

Why?

Invalid records are removed
early, saving CPU, memory,
and network resources.

This principle becomes
very important when working
with millions of records.
"""

print("Production Insight Complete!")

# ============================================================
# Example 12 - Design Note
# ============================================================

print("\n========== Example 12 ==========")

"""
Good

filter(is_valid_customer, customers)

Better than

filter(
    lambda customer:
        customer["country"] == "Canada"
        and customer["salary"] > 80000
        and customer["department"] == "IT"
        and customer["experience"] > 5
        ...
)

If the condition becomes
complex,

extract it into
a named function.
"""

print("Design Note Complete!")

# ============================================================
# END
# ============================================================

print("\nCongratulations!")
print("You completed filter() examples.")
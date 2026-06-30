"""
============================================================
Topic 6 - Functions (Part H)
reduce() Function

This file demonstrates:

1. Basic reduce()
2. reduce() with Lambda
3. Finding Sum
4. Finding Product
5. Finding Maximum
6. Using Initial Value
7. ETL Aggregation Examples
8. map() vs filter() vs reduce()
9. Production Best Practices

Author: Sandeep Dass
============================================================
"""

from functools import reduce

# ============================================================
# Example 1 - Basic reduce()
# ============================================================

print("\n========== Example 1 ==========")

numbers = [1, 2, 3, 4]

result = reduce(
    lambda acc, value: acc + value,
    numbers
)

print(result)

"""
reduce()

Combines many values
into a single value.
"""

# ============================================================
# Example 2 - Product
# ============================================================

print("\n========== Example 2 ==========")

numbers = [2, 3, 4]

product = reduce(
    lambda acc, value: acc * value,
    numbers
)

print(product)

# ============================================================
# Example 3 - Maximum Value
# ============================================================

print("\n========== Example 3 ==========")

salaries = [50000, 85000, 120000, 90000]

highest = reduce(
    lambda acc, value:
    acc if acc > value else value,
    salaries
)

print(highest)

# ============================================================
# Example 4 - Initial Value
# ============================================================

print("\n========== Example 4 ==========")

numbers = [1, 2, 3]

result = reduce(
    lambda acc, value: acc + value,
    numbers,
    100
)

print(result)

"""
The accumulator starts at 100.
"""

# ============================================================
# Example 5 - Total Revenue
# ============================================================

print("\n========== Example 5 ==========")

transactions = [120, 350, 500, 80]

total_revenue = reduce(
    lambda total, amount:
    total + amount,
    transactions
)

print(total_revenue)

# ============================================================
# Example 6 - Merge Dictionaries
# ============================================================

print("\n========== Example 6 ==========")

records = [
    {"Canada": 10},
    {"USA": 8},
    {"India": 15}
]


def merge(accumulator, current):
    accumulator.update(current)
    return accumulator


merged = reduce(
    merge,
    records,
    {}
)

print(merged)

"""
Useful when combining
small dictionaries.
"""

# ============================================================
# Example 7 - Count Records
# ============================================================

print("\n========== Example 7 ==========")

employees = [
    {},
    {},
    {},
    {},
    {}
]

count = reduce(
    lambda total, _:
    total + 1,
    employees,
    0
)

print(count)

# ============================================================
# Example 8 - ETL Example
# ============================================================

print("\n========== Example 8 ==========")

transactions = [
    {"amount": 120},
    {"amount": 350},
    {"amount": 80},
    {"amount": 450}
]

total = reduce(
    lambda running_total, transaction:
    running_total + transaction["amount"],
    transactions,
    0
)

print(total)

"""
Common ETL task:

Calculate total revenue.
"""

# ============================================================
# Example 9 - map() vs filter() vs reduce()
# ============================================================

print("\n========== Example 9 ==========")

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

reduced = reduce(
    lambda a, b:
    a + b,
    numbers
)

print("map()    :", mapped)
print("filter() :", filtered)
print("reduce() :", reduced)

# ============================================================
# Example 10 - Prefer Built-ins
# ============================================================

print("\n========== Example 10 ==========")

numbers = [5, 10, 15, 20]

print(sum(numbers))
print(max(numbers))
print(min(numbers))

"""
Prefer built-in functions
over reduce() whenever
they solve the problem.
"""

# ============================================================
# Example 11 - Production Insight
# ============================================================

print("\n========== Example 11 ==========")

"""
Use reduce()

only when implementing
custom aggregation logic.

For common operations,
prefer:

sum()

max()

min()

any()

all()

These are more readable
and optimized.
"""

print("Production Insight Complete!")

# ============================================================
# END
# ============================================================

print("\nCongratulations!")
print("You completed reduce() examples.")
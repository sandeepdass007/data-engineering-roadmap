"""
============================================================
Topic 6 - Functions (Part J)
Recursion

This file demonstrates:

1. Basic Recursion
2. Base Case
3. Countdown Example
4. Factorial
5. Recursive Sum
6. Directory Traversal Concept
7. Nested JSON Traversal
8. Production Notes

Author: Sandeep Dass
============================================================
"""

# ============================================================
# Example 1 - Basic Recursion
# ============================================================

print("\n========== Example 1 ==========")


def countdown(number):

    if number == 0:
        return

    print(number)

    countdown(number - 1)


countdown(5)

"""
Every recursive function needs:

1. Base Case
2. Recursive Case
"""

# ============================================================
# Example 2 - Factorial
# ============================================================

print("\n========== Example 2 ==========")


def factorial(number):

    if number == 1:
        return 1

    return number * factorial(number - 1)


print(factorial(5))

# ============================================================
# Example 3 - Sum of Numbers
# ============================================================

print("\n========== Example 3 ==========")


def recursive_sum(numbers):

    if len(numbers) == 0:
        return 0

    return numbers[0] + recursive_sum(numbers[1:])


numbers = [10, 20, 30, 40]

print(recursive_sum(numbers))

# ============================================================
# Example 4 - Reverse Printing
# ============================================================

print("\n========== Example 4 ==========")


def print_reverse(number):

    if number == 0:
        return

    print_reverse(number - 1)

    print(number)


print_reverse(5)

"""
Notice:

The print happens

AFTER

the recursive call.

Understanding this is important.
"""

# ============================================================
# Example 5 - Traverse Nested Dictionary
# ============================================================

print("\n========== Example 5 ==========")

employee = {
    "name": "John",
    "manager": {
        "name": "Mike",
        "manager": {
            "name": "Alice"
        }
    }
}


def print_managers(node):

    print(node["name"])

    if "manager" in node:
        print_managers(node["manager"])


print_managers(employee)

"""
Typical nested JSON traversal.
"""

# ============================================================
# Example 6 - Simulating Folder Traversal
# ============================================================

print("\n========== Example 6 ==========")

folders = {
    "Project": {
        "Data": {
            "Jan": {},
            "Feb": {}
        },
        "Logs": {
            "2025": {}
        }
    }
}


def traverse(folder, level=0):

    for name, children in folder.items():

        print("    " * level + name)

        traverse(children, level + 1)


traverse(folders)

"""
Real operating systems use
similar recursive logic
to walk directory trees.
"""

# ============================================================
# Example 7 - Recursion Limit
# ============================================================

print("\n========== Example 7 ==========")

import sys

print("Current Recursion Limit:")

print(sys.getrecursionlimit())

"""
Usually around 1000.

Avoid deep recursion
for production ETL jobs.
"""

# ============================================================
# Example 8 - Loop vs Recursion
# ============================================================

print("\n========== Example 8 ==========")

numbers = [10, 20, 30, 40]

total = 0

for number in numbers:
    total += number

print("Loop Total :", total)

print("Recursive Total :", recursive_sum(numbers))

"""
Loops are usually preferred
for flat datasets.
"""

# ============================================================
# Example 9 - Production Insight
# ============================================================

print("\n========== Example 9 ==========")

"""
Use recursion for:

- Nested JSON
- XML
- Tree structures
- Directory traversal

Avoid recursion for:

- Large CSV files
- Flat datasets
- Millions of records

Use loops for those.
"""

print("Production Insight Complete!")

# ============================================================
# Example 10 - Interview Tip
# ============================================================

print("\n========== Example 10 ==========")

print("""
Every recursive function must have:

1. Base Case

2. Recursive Case
""")

print("Interview Tip Complete!")

# ============================================================
# END
# ============================================================

print("\nCongratulations!")
print("You completed Topic 6 - Recursion.")
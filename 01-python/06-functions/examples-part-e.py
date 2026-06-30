"""
============================================================
Topic 6 - Functions (Part E)
map() Function

This file demonstrates:

1. Basic map()
2. map() with User-defined Functions
3. map() with Lambda
4. map() with Built-in Functions
5. map() with Multiple Iterables
6. ETL Examples
7. Common Interview Traps
8. Production Best Practices

Author: Sandeep Dass
============================================================
"""

# ============================================================
# Example 1 - Basic map() using a User-defined Function
# ============================================================

print("\n========== Example 1 ==========")


def square(number):
    return number * number


numbers = [1, 2, 3, 4, 5]

result = map(square, numbers)

print(result)          # Map Object
print(list(result))    # Actual Values

"""
Notice:

map() returns a lazy iterator.

It does NOT immediately execute.
"""

# ============================================================
# Example 2 - map() using Lambda
# ============================================================

print("\n========== Example 2 ==========")

numbers = [10, 20, 30]

result = map(
    lambda number: number * 2,
    numbers
)

print(list(result))

"""
Equivalent to

for number in numbers:
    number * 2
"""

# ============================================================
# Example 3 - map() with int()
# ============================================================

print("\n========== Example 3 ==========")

salary_strings = [
    "100000",
    "85000",
    "92000"
]

salary_numbers = list(
    map(
        int,
        salary_strings
    )
)

print(salary_numbers)

"""
Very common in ETL.

CSV data

↓

String

↓

Integer
"""

# ============================================================
# Example 4 - map() with str.upper()
# ============================================================

print("\n========== Example 4 ==========")

names = [
    "john",
    "mike",
    "alice"
]

uppercase = list(
    map(
        str.upper,
        names
    )
)

print(uppercase)

# ============================================================
# Example 5 - Cleaning Customer Names
# ============================================================

print("\n========== Example 5 ==========")

customers = [
    " john ",
    " alice ",
    " mike "
]

cleaned = list(
    map(
        lambda customer:
        customer.strip().title(),

        customers
    )
)

print(cleaned)

"""
Very common

Cleaning incoming data.
"""

# ============================================================
# Example 6 - map() with Multiple Iterables
# ============================================================

print("\n========== Example 6 ==========")

salary = [50000, 70000, 90000]

bonus = [5000, 7000, 9000]

total = list(

    map(

        lambda s, b: s + b,

        salary,

        bonus

    )

)

print(total)

"""
Each iteration receives

salary[i]

bonus[i]
"""

# ============================================================
# Example 7 - ETL Record Transformation
# ============================================================

print("\n========== Example 7 ==========")

employees = [

    {
        "name": "john",
        "salary": "100000"
    },

    {
        "name": "alice",
        "salary": "85000"
    }

]


def clean_employee(employee):

    cleaned = employee.copy()

    cleaned["name"] = cleaned["name"].title()

    cleaned["salary"] = int(cleaned["salary"])

    return cleaned


processed = list(
    map(
        clean_employee,
        employees
    )
)

print(processed)

"""
Notice

Original list

is unchanged.
"""

# ============================================================
# Example 8 - map() vs Loop
# ============================================================

print("\n========== Example 8 ==========")

numbers = [1, 2, 3]

# Loop

result = []

for number in numbers:
    result.append(number * 10)

print(result)

# map()

result = list(
    map(
        lambda x: x * 10,
        numbers
    )
)

print(result)

"""
Both produce

the same output.

Choose whichever

is more readable.
"""

# ============================================================
# Example 9 - Interview Trap
# ============================================================

print("\n========== Example 9 ==========")

numbers = [1, 2, 3]

mapped = map(
    lambda x: x * 2,
    numbers
)

print(list(mapped))

print(list(mapped))

"""
First Output

[2,4,6]

Second Output

[]

Why?

Because map()

returns an iterator.

Once consumed,

it is exhausted.
"""

# ============================================================
# Example 10 - Production Insight
# ============================================================

print("\n========== Example 10 ==========")

"""
Pandas

df["salary"] = df["salary"].apply(
    lambda x: x * 1.10
)

PySpark

rdd.map(
    lambda row: row.upper()
)

The concept is identical.

Apply one transformation

to every record.
"""

print("Production Insight Complete!")

# ============================================================
# Example 11 - Performance Note
# ============================================================

print("\n========== Example 11 ==========")

"""
Use map()

when

the same operation

is applied

to every element.

If the transformation

becomes complex,

prefer a normal loop

or a named function.
"""

print("Performance Note Complete!")

# ============================================================
# END
# ============================================================

print("\nCongratulations!")
print("You completed map() examples.")
"""
============================================================
Topic 6 - Functions (PART A)
examples.py

This file contains executable examples for learning Python Functions.

Run the file from top to bottom.

Each section introduces one concept before moving to the next.

Author: Sandeep Dass
============================================================
"""

# ============================================================
# Example 1 - Your First Function
# ============================================================

print("\n========== Example 1 ==========")


def greet():
    print("Hello, Data Engineer!")


greet()

"""
Expected Output

Hello, Data Engineer!
"""

# ------------------------------------------------------------

# Functions allow us to reuse code.

# Instead of writing the same code many times,
# write it once and call it whenever needed.


# ============================================================
# Example 2 - Parameters vs Arguments
# ============================================================

print("\n========== Example 2 ==========")


def greet(name):
    print(f"Hello {name}")


greet("Mike")
greet("Alice")
greet("John")

"""
Parameter

name

Argument

"Mike"

"Alice"

"John"
"""

# ============================================================
# Example 3 - Multiple Parameters
# ============================================================

print("\n========== Example 3 ==========")


def employee_details(name, department, salary):
    print(f"Name       : {name}")
    print(f"Department : {department}")
    print(f"Salary     : ${salary}")


employee_details("John", "Engineering", 100000)

# ============================================================
# Example 4 - Return vs Print
# ============================================================

print("\n========== Example 4 ==========")


def add_print(a, b):
    print(a + b)


result = add_print(10, 20)

print("Returned Value:", result)

"""
Notice:

print()

shows output

return

sends data back to caller
"""

# ============================================================
# Example 5 - Returning Values
# ============================================================

print("\n========== Example 5 ==========")


def add(a, b):
    return a + b


result = add(10, 20)

print(result)

# Functions become reusable because they return values.


# ============================================================
# Example 6 - Returning Multiple Values
# ============================================================

print("\n========== Example 6 ==========")


def employee_summary():

    name = "John"

    salary = 100000

    department = "Engineering"

    return name, salary, department


employee = employee_summary()

print(employee)

print(type(employee))

"""
Python automatically packs
multiple returned values
into a Tuple.
"""

# ============================================================
# Example 7 - Tuple Unpacking
# ============================================================

print("\n========== Example 7 ==========")

name, salary, department = employee_summary()

print(name)
print(salary)
print(department)

# ============================================================
# Example 8 - Default Parameters
# ============================================================

print("\n========== Example 8 ==========")


def greet(name, country="Canada"):

    print(f"{name} is from {country}")


greet("John")

greet("Mike", "USA")

"""
Default value used

↓

Canada

Only overridden when supplied.
"""

# ============================================================
# Example 9 - Keyword Arguments
# ============================================================

print("\n========== Example 9 ==========")


def create_employee(id, name, salary):

    print(id)

    print(name)

    print(salary)


create_employee(

    salary=100000,

    id=101,

    name="John"

)

"""
Keyword arguments improve readability.

Especially useful when a function
has many parameters.
"""

# ============================================================
# Example 10 - Local Variables
# ============================================================

print("\n========== Example 10 ==========")


def calculate_bonus():

    salary = 100000

    bonus = salary * 0.10

    return bonus


print(calculate_bonus())

"""
salary

bonus

exist only inside the function.
"""

# ============================================================
# Example 11 - Simple Data Cleaning Function
# ============================================================

print("\n========== Example 11 ==========")


def clean_customer_name(name):

    return name.strip().title()


print(clean_customer_name("    john smith    "))

"""
One of the most common ETL patterns.

Clean once.

Reuse everywhere.
"""

# ============================================================
# Example 12 - Record Validation
# ============================================================

print("\n========== Example 12 ==========")


def validate_customer(customer):

    required_fields = [

        "customer_id",

        "name",

        "country"

    ]

    for field in required_fields:

        if field not in customer:

            return False

    return True


customer = {

    "customer_id": 101,

    "name": "John",

    "country": "Canada"

}

print(validate_customer(customer))

# ============================================================
# Example 13 - Function Composition
# ============================================================

print("\n========== Example 13 ==========")


def remove_extra_spaces(text):

    return text.strip()


def capitalize_name(text):

    return text.title()


customer_name = "   john smith   "

customer_name = remove_extra_spaces(customer_name)

customer_name = capitalize_name(customer_name)

print(customer_name)

"""
Large ETL jobs are often built
using many small functions
instead of one huge function.
"""

# ============================================================
# Example 14 - Mini ETL Pipeline
# ============================================================

print("\n========== Example 14 ==========")


def extract():

    return [

        {"name": " john ", "country": "canada"},

        {"name": " alice ", "country": "usa"}

    ]


def transform(records):

    for record in records:

        record["name"] = record["name"].strip().title()

        record["country"] = record["country"].title()

    return records


def load(records):

    print("Loading records...")

    for record in records:

        print(record)


records = extract()

records = transform(records)

load(records)

"""
Notice how readable this becomes.

Extract

↓

Transform

↓

Load
"""

# ============================================================
# Example 15 - Pure Function
# ============================================================

print("\n========== Example 15 ==========")


def square(number):

    return number * number


print(square(5))

print(square(10))

"""
Pure Function

Same input

↓

Same output

No side effects.
"""

# ============================================================
# Example 16 - Production Style Helper Function
# ============================================================

print("\n========== Example 16 ==========")


def calculate_success_rate(success, total):

    if total == 0:

        return 0

    return (success / total) * 100


print(calculate_success_rate(950, 1000))

"""
Useful for

ETL Monitoring

Data Quality

Pipeline Metrics

Dashboard Calculations
"""

# ============================================================
# END OF FILE
# ============================================================

print("\nCongratulations!")
print("You have completed the Functions examples.")
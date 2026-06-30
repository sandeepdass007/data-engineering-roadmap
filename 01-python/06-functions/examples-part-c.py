"""
============================================================
Topic 6 - Functions (Part C)
Variable Scope

This file demonstrates:

1. Local Variables
2. Global Variables
3. Variable Shadowing
4. global Keyword
5. LEGB Rule
6. Production Best Practices

Author: Sandeep Dass
============================================================
"""

# ============================================================
# Example 1 - Local Variables
# ============================================================

print("\n========== Example 1 ==========")
print("Local Variables")


def calculate_bonus():
    salary = 100000
    bonus = salary * 0.10

    print(f"Salary : {salary}")
    print(f"Bonus  : {bonus}")


calculate_bonus()

"""
Notice:

salary

bonus

exist ONLY inside the function.
"""

# ============================================================
# Example 2 - NameError
# ============================================================

print("\n========== Example 2 ==========")

"""
DO NOT RUN

print(salary)

Reason:

salary only exists inside calculate_bonus().
"""

# ============================================================
# Example 3 - Global Variables
# ============================================================

print("\n========== Example 3 ==========")
print("Global Variables")

company = "ABC Corporation"


def display_company():
    print(company)


display_company()

"""
Functions can READ
global variables.
"""

# ============================================================
# Example 4 - Variable Shadowing
# ============================================================

print("\n========== Example 4 ==========")

country = "Canada"


def display_country():
    country = "USA"

    print("Inside Function :", country)


display_country()

print("Outside Function:", country)

"""
Output

Inside Function : USA

Outside Function: Canada

The local variable
shadows the global one.
"""

# ============================================================
# Example 5 - Why This Fails
# ============================================================

print("\n========== Example 5 ==========")

counter = 0

"""
DO NOT RUN

def increment():
    counter += 1

Reason:

Python treats counter
as LOCAL because
it is assigned inside
the function.

But it has no value yet.

Result:

UnboundLocalError
"""

# ============================================================
# Example 6 - global Keyword
# ============================================================

print("\n========== Example 6 ==========")


counter = 0


def increment():
    global counter

    counter += 1

    print(counter)


increment()
increment()
increment()

"""
Output

1

2

3
"""

# ============================================================
# Example 7 - Better Design
# ============================================================

print("\n========== Example 7 ==========")


def increment(counter):
    return counter + 1


counter = 0

counter = increment(counter)

counter = increment(counter)

counter = increment(counter)

print(counter)

"""
Preferred in production.

No global variables.

No side effects.

Easy to test.
"""

# ============================================================
# Example 8 - ETL Example
# ============================================================

print("\n========== Example 8 ==========")


def clean_customer(customer):
    customer["name"] = customer["name"].strip().title()

    return customer


customer = {
    "name": "   john smith   "
}

clean_customer(customer)

print(customer)

"""
Notice

The original dictionary
was modified.

This is called
a side effect.

We'll improve this later.
"""

# ============================================================
# Example 9 - Better ETL Design
# ============================================================

print("\n========== Example 9 ==========")


def clean_customer(customer):

    cleaned_customer = customer.copy()

    cleaned_customer["name"] = (
        cleaned_customer["name"]
        .strip()
        .title()
    )

    return cleaned_customer


customer = {
    "name": "   john smith   "
}

processed = clean_customer(customer)

print("Original :", customer)

print("Processed:", processed)

"""
The original data
remains unchanged.

This is much safer
for production systems.
"""

# ============================================================
# Example 10 - LEGB Rule
# ============================================================

print("\n========== Example 10 ==========")

name = "Global"


def outer():

    name = "Enclosing"

    def inner():

        name = "Local"

        print(name)

    inner()


outer()

"""
Python searches variables
in this order:

L → Local

E → Enclosing

G → Global

B → Built-in
"""

# ============================================================
# Example 11 - Built-in Scope
# ============================================================

print("\n========== Example 11 ==========")

numbers = [10, 20, 30]

print(len(numbers))

print(max(numbers))

print(min(numbers))

"""
len()

max()

min()

are built-in functions.

They exist even though
we never defined them.
"""

# ============================================================
# Example 12 - Production Configuration
# ============================================================

print("\n========== Example 12 ==========")


def load_data(database):

    print(f"Loading data from {database}")


environment = "production"

load_data(environment)

"""
Good Design

↓

Explicit dependency

Instead of

DATABASE = "production"

as a global variable.
"""

# ============================================================
# END
# ============================================================

print("\nCongratulations!")
print("You completed Variable Scope examples.")
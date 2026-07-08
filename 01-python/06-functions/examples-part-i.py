"""
============================================================
Topic 6 - Functions (Part I)
*args and **kwargs

This file demonstrates:

1. Variable Positional Arguments (*args)
2. Variable Keyword Arguments (**kwargs)
3. Mixing Regular Parameters with *args
4. Mixing *args and **kwargs
5. ETL Examples
6. Configuration Driven Functions
7. Production Best Practices

Author: Sandeep Dass
============================================================
"""

# ============================================================
# Example 1 - *args Basics
# ============================================================

print("\n========== Example 1 ==========")


def add(*numbers):
    print(numbers)
    print(type(numbers))


add(10)
add(10, 20)
add(10, 20, 30)
add(10, 20, 30, 40)

"""
*args is a tuple.

The function can accept any number
of positional arguments.
"""

# ============================================================
# Example 2 - Sum Using *args
# ============================================================

print("\n========== Example 2 ==========")


def total_salary(*salaries):

    total = 0

    for salary in salaries:
        total += salary

    return total


print(total_salary(50000))
print(total_salary(50000, 60000))
print(total_salary(50000, 60000, 70000))

# ============================================================
# Example 3 - **kwargs Basics
# ============================================================

print("\n========== Example 3 ==========")


def create_employee(**employee):

    print(employee)
    print(type(employee))


create_employee(
    name="John",
    salary=100000,
    country="Canada"
)

"""
**kwargs becomes
a dictionary.
"""

# ============================================================
# Example 4 - Reading Keyword Arguments
# ============================================================

print("\n========== Example 4 ==========")


def print_employee(**employee):

    print(employee["name"])
    print(employee["salary"])


print_employee(
    name="Alice",
    salary=120000,
    country="Canada"
)

# ============================================================
# Example 5 - Regular Parameters + *args
# ============================================================

print("\n========== Example 5 ==========")


def greet(country, *names):

    print("Country :", country)

    print("Employees:")

    for name in names:
        print(name)


greet(
    "Canada",
    "John",
    "Mike",
    "Alice"
)

# ============================================================
# Example 6 - *args + **kwargs
# ============================================================

print("\n========== Example 6 ==========")


def process_records(*records, **options):

    print("Records:")

    for record in records:
        print(record)

    print()

    print("Options:")

    for key, value in options.items():
        print(f"{key} : {value}")


process_records(
    {"id": 101},
    {"id": 102},
    {"id": 103},
    validate=True,
    dry_run=False,
    batch_size=100
)

# ============================================================
# Example 7 - Configuration Driven Function
# ============================================================

print("\n========== Example 7 ==========")


def connect_database(**config):

    print("Connecting...")

    for key, value in config.items():
        print(f"{key} = {value}")


connect_database(
    host="localhost",
    port=5432,
    database="employees",
    username="admin",
    timeout=30,
    ssl=True
)

"""
Very common in production.

Configuration changes

without changing

the function signature.
"""

# ============================================================
# Example 8 - ETL Pipeline
# ============================================================

print("\n========== Example 8 ==========")


def process_pipeline(*records, **settings):

    print(f"Processing {len(records)} records")

    print()

    print("Settings")

    for key, value in settings.items():
        print(f"{key}: {value}")


process_pipeline(
    {"id": 101},
    {"id": 102},
    {"id": 103},
    environment="DEV",
    validate=True,
    write_to_s3=False
)

# ============================================================
# Example 9 - Interview Trap
# ============================================================

print("\n========== Example 9 ==========")


def example(*anything, **everything):

    print(anything)
    print(everything)


example(
    10,
    20,
    30,
    country="Canada",
    department="IT"
)

"""
Remember

'args'

and

'kwargs'

are only conventions.

The names

can be anything.

Only * and ** matter.
"""

# ============================================================
# Example 10 - Function Parameter Order
# ============================================================

print("\n========== Example 10 ==========")


def demo(required_parameter,
         *args,
         optional_parameter="Default",
         **kwargs):

    print("Required :", required_parameter)

    print("Args :", args)

    print("Optional :", optional_parameter)

    print("Kwargs :", kwargs)


demo(
    "Employee",
    100,
    200,
    department="IT",
    country="Canada"
)

"""
Correct order:

1. Required parameters

2. *args

3. Optional parameters

4. **kwargs
"""

# ============================================================
# Example 11 - Production Insight
# ============================================================

print("\n========== Example 11 ==========")

"""
Many Python libraries use
*args and **kwargs.

Examples:

print()

dict()

boto3

requests

Flask

FastAPI

Airflow

PySpark

Understanding these concepts
makes reading production code
much easier.
"""

print("Production Insight Complete!")

# ============================================================
# END
# ============================================================

print("\nCongratulations!")
print("You completed *args and **kwargs examples.")
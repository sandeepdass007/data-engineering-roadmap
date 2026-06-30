"""
============================================================
Topic 6 - Functions (Part B)
Function Arguments

This file demonstrates:
1. Positional Arguments
2. Keyword Arguments
3. Default Parameters
4. Mixing Positional and Keyword Arguments
5. Common Interview Traps

Author: Sandeep Dass
============================================================
"""

# ============================================================
# Example 1 - Positional Arguments
# ============================================================

print("\n========== Example 1 ==========")

print("Positional Arguments")


def create_employee(name, salary):
    print(f"Name   : {name}")
    print(f"Salary : {salary}")


create_employee("John", 100000)

"""
Python matches arguments based on position.

Parameter      Argument

name        <- "John"
salary      <- 100000
"""

# ============================================================
# Example 2 - Why Position Matters
# ============================================================

print("\n========== Example 2 ==========")

print("Incorrect Ordering")

create_employee(100000, "John")

"""
Output

Name   : 100000
Salary : John

Python does not know your intention.
It simply maps arguments by position.
"""

# ============================================================
# Example 3 - Keyword Arguments
# ============================================================

print("\n========== Example 3 ==========")

print("Keyword Arguments")

create_employee(
    salary=120000,
    name="Alice"
)

"""
Keyword arguments ignore position.

Instead, Python matches using
the parameter names.
"""

# ============================================================
# Example 4 - Default Parameters
# ============================================================

print("\n========== Example 4 ==========")

print("Default Parameters")


def create_customer(name, country="Canada"):
    print(f"{name} from {country}")


create_customer("John")
create_customer("Mike", "USA")

"""
If no value is supplied,
Python uses the default.
"""

# ============================================================
# Example 5 - Multiple Default Parameters
# ============================================================

print("\n========== Example 5 ==========")


def connect_database(
    host,
    port=5432,
    database="customers",
    ssl=True
):

    print(f"Host      : {host}")
    print(f"Port      : {port}")
    print(f"Database  : {database}")
    print(f"SSL       : {ssl}")


connect_database("db.company.com")

"""
Most production helper functions
look very similar to this.
"""

# ============================================================
# Example 6 - Overriding Defaults
# ============================================================

print("\n========== Example 6 ==========")

connect_database(
    "db.company.com",
    port=3306,
    ssl=False
)

"""
Only override what needs changing.
Everything else keeps its default.
"""

# ============================================================
# Example 7 - Mixing Positional and Keyword Arguments
# ============================================================

print("\n========== Example 7 ==========")


def load_data(table, overwrite=False, retries=3):
    print(f"Table      : {table}")
    print(f"Overwrite  : {overwrite}")
    print(f"Retries    : {retries}")


load_data(
    "customers",
    retries=5
)

"""
Valid

Positional

↓

Keyword
"""

# ============================================================
# Example 8 - Interview Trap
# ============================================================

print("\n========== Example 8 ==========")


def add(a=10, b=20):
    return a + b


print(add())

print(add(100))

print(add(b=100))

"""
Expected

30

120

110
"""

# ============================================================
# Example 9 - Production ETL Example
# ============================================================

print("\n========== Example 9 ==========")


def load_to_snowflake(
    table,
    warehouse="COMPUTE_WH",
    batch_size=5000,
    overwrite=False,
    retries=3
):

    print("Loading...")

    print(f"Table       : {table}")
    print(f"Warehouse   : {warehouse}")
    print(f"Batch Size  : {batch_size}")
    print(f"Overwrite   : {overwrite}")
    print(f"Retries     : {retries}")


load_to_snowflake("customers")

print()

load_to_snowflake(
    table="sales",
    overwrite=True,
    batch_size=10000
)

"""
Notice how keyword arguments make
the function call much easier to read.
"""

# ============================================================
# Example 10 - Data Engineering Helper Function
# ============================================================

print("\n========== Example 10 ==========")


def read_csv(
    file_path,
    delimiter=",",
    encoding="utf-8",
    has_header=True
):

    print(f"Reading : {file_path}")
    print(f"Delimiter : {delimiter}")
    print(f"Encoding : {encoding}")
    print(f"Header : {has_header}")


read_csv("customers.csv")

print()

read_csv(
    "sales.txt",
    delimiter="|",
    encoding="latin-1",
    has_header=False
)

"""
Functions like this appear
everywhere in ETL systems.
"""

# ============================================================
# Example 11 - Common Mistake (DO NOT RUN)
# ============================================================

"""
This code is INVALID.

def employee(country="Canada", name):
    pass

Reason:

Required parameters
must come before
default parameters.
"""

# ============================================================
# Example 12 - Common Mistake (DO NOT RUN)
# ============================================================

"""
This code is INVALID.

create_employee(
    name="John",
    100000
)

Reason:

Keyword arguments
cannot come before
positional arguments.
"""

# ============================================================
# Example 13 - Real Production API Design
# ============================================================

print("\n========== Example 13 ==========")


def process_file(
    file_name,
    validate_schema=True,
    remove_duplicates=True,
    trim_strings=True,
    output_format="parquet"
):

    print("Processing File")
    print("---------------------")
    print(f"File : {file_name}")
    print(f"Validate : {validate_schema}")
    print(f"Remove Duplicates : {remove_duplicates}")
    print(f"Trim Strings : {trim_strings}")
    print(f"Output : {output_format}")


process_file("customers.csv")

print()

process_file(
    "transactions.csv",
    output_format="csv",
    validate_schema=False
)

"""
Notice something?

You only specify
the parameters you wish to change.

This is exactly how
many Python libraries
are designed.
"""

print("\nCongratulations!")
print("You completed Function Arguments examples.")
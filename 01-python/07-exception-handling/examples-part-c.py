"""
============================================================
Topic 7: Exception Handling
Part C: Raising Exceptions (raise)
============================================================

Topics Covered
--------------
1. What is raise?
2. Raising built-in exceptions
3. Business rule validation
4. Validation functions
5. Using raise inside try-except
6. ETL validation example
7. Production best practices

Run one example at a time.
Comment/uncomment sections while practicing.
"""

# ============================================================
# Example 1 - Basic raise
# ============================================================

print("\n===== Example 1: Basic raise =====")

age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")

print("This line will never execute.")

"""
Output:

ValueError: Age cannot be negative.
"""

# ============================================================
# Example 2 - Salary Validation
# ============================================================

print("\n===== Example 2: Salary Validation =====")

salary = -25000

if salary < 0:
    raise ValueError("Salary cannot be negative.")

print("Salary is valid.")

# ============================================================
# Example 3 - Validation Function
# ============================================================

print("\n===== Example 3: Validation Function =====")


def validate_age(age):

    if age < 0:
        raise ValueError("Age cannot be negative.")

    if age > 120:
        raise ValueError("Age cannot be greater than 120.")

    print("Age is valid.")


# Uncomment one at a time

# validate_age(25)

# validate_age(-10)

# validate_age(200)

# ============================================================
# Example 4 - Multiple Business Rules
# ============================================================

print("\n===== Example 4: Multiple Validation Rules =====")


def validate_employee(employee):

    if employee["salary"] < 0:
        raise ValueError("Salary cannot be negative.")

    if employee["age"] < 18:
        raise ValueError("Employee must be at least 18 years old.")

    print("Employee validation successful.")


employee = {
    "name": "John",
    "salary": 80000,
    "age": 30
}

validate_employee(employee)

# ============================================================
# Example 5 - raise inside try
# ============================================================

print("\n===== Example 5: raise inside try =====")

try:

    salary = -100

    if salary < 0:
        raise ValueError("Salary cannot be negative.")

except ValueError as error:

    print(f"Caught Exception: {error}")

# ============================================================
# Example 6 - ETL Validation Example
# ============================================================

print("\n===== Example 6: ETL Validation =====")


def validate_record(record):

    if not record["customer_id"]:
        raise ValueError("Customer ID is mandatory.")

    if record["salary"] < 0:
        raise ValueError("Salary cannot be negative.")

    print("Record is valid.")


record = {
    "customer_id": 101,
    "salary": 75000
}

try:

    validate_record(record)

except ValueError as error:

    print(error)

"""
Try changing:

customer_id = None

salary = -5000
"""

# ============================================================
# Example 7 - AWS Configuration Validation
# ============================================================

print("\n===== Example 7: AWS Configuration Validation =====")


def validate_s3_config(config):

    if not config["bucket"]:
        raise ValueError("S3 bucket name is required.")

    if not config["region"]:
        raise ValueError("AWS region is required.")

    print("Configuration is valid.")


config = {
    "bucket": "customer-data-bucket",
    "region": "ca-central-1"
}

try:

    validate_s3_config(config)

except ValueError as error:

    print(error)

# ============================================================
# Example 8 - Processing Multiple Records
# ============================================================

print("\n===== Example 8: Processing Multiple Records =====")


def validate_salary(record):

    if record["salary"] < 0:
        raise ValueError("Salary cannot be negative.")


records = [
    {"id": 1, "salary": 50000},
    {"id": 2, "salary": -1000},
    {"id": 3, "salary": 75000},
]

for record in records:

    try:

        validate_salary(record)

        print(f"Record {record['id']} processed successfully.")

    except ValueError as error:

        print(f"Record {record['id']} rejected -> {error}")

"""
Notice that one bad record does not stop
processing of the remaining records.
"""

# ============================================================
# Summary
# ============================================================

print("\n===== Summary =====")

print("""
Key Takeaways

1. raise lets developers create exceptions.
2. Use raise to enforce business rules.
3. Raise specific exceptions whenever possible.
4. Validate data as early as possible.
5. Create reusable validation functions.
6. Combine raise with try-except for robust applications.
7. In ETL pipelines, reject bad records while allowing
   valid records to continue processing.
""")
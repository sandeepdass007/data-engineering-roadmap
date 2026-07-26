"""
============================================================
Topic 7: Exception Handling
Part D: Custom Exceptions
============================================================

Topics Covered
--------------
1. Why create custom exceptions?
2. Creating custom exception classes
3. Raising custom exceptions
4. Catching custom exceptions
5. Multiple custom exceptions
6. Data Engineering example
7. Banking example
8. Best practices

Run one example at a time.
Comment/uncomment sections while practicing.
"""

# ============================================================
# Example 1 - Creating Your First Custom Exception
# ============================================================

print("\n===== Example 1: Custom Exception =====")


class InvalidAgeError(Exception):
    """Raised when age validation fails."""
    pass


try:

    age = -5

    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")

except InvalidAgeError as error:

    print(error)


# ============================================================
# Example 2 - Salary Validation
# ============================================================

print("\n===== Example 2: Salary Validation =====")


class InvalidSalaryError(Exception):
    """Raised when salary is invalid."""
    pass


try:

    salary = -1000

    if salary < 0:
        raise InvalidSalaryError(
            "Salary cannot be negative."
        )

except InvalidSalaryError as error:

    print(error)


# ============================================================
# Example 3 - Employee Validation
# ============================================================

print("\n===== Example 3: Employee Validation =====")


class InvalidEmployeeError(Exception):
    """Raised when employee information is invalid."""
    pass


def validate_employee(employee):

    if not employee["employee_id"]:
        raise InvalidEmployeeError(
            "Employee ID is mandatory."
        )

    print("Employee validated successfully.")


employee = {
    "employee_id": 101,
    "name": "John"
}

try:

    validate_employee(employee)

except InvalidEmployeeError as error:

    print(error)


# ============================================================
# Example 4 - Multiple Custom Exceptions
# ============================================================

print("\n===== Example 4: Multiple Custom Exceptions =====")


class InvalidEmailError(Exception):
    pass


class DuplicateEmployeeError(Exception):
    pass


def validate_registration(employee):

    if "@" not in employee["email"]:
        raise InvalidEmailError(
            "Invalid email address."
        )

    if employee["employee_id"] == 101:
        raise DuplicateEmployeeError(
            "Employee already exists."
        )


employee = {
    "employee_id": 101,
    "email": "john@example.com"
}

try:

    validate_registration(employee)

except InvalidEmailError as error:

    print(error)

except DuplicateEmployeeError as error:

    print(error)


# ============================================================
# Example 5 - ETL Validation Example
# ============================================================

print("\n===== Example 5: ETL Validation =====")


class InvalidRecordError(Exception):
    """Raised when a record fails business validation."""
    pass


def validate_record(record):

    if not record["customer_id"]:
        raise InvalidRecordError(
            "Customer ID is missing."
        )

    if record["salary"] < 0:
        raise InvalidRecordError(
            "Salary cannot be negative."
        )


records = [
    {"customer_id": 101, "salary": 60000},
    {"customer_id": None, "salary": 70000},
    {"customer_id": 103, "salary": -500},
]

for record in records:

    try:

        validate_record(record)

        print(
            f"Record {record['customer_id']} processed successfully."
        )

    except InvalidRecordError as error:

        print(
            f"Rejected Record: {record}"
        )

        print(f"Reason: {error}")

        print("-" * 40)


# ============================================================
# Example 6 - Banking Example
# ============================================================

print("\n===== Example 6: Banking Example =====")


class InsufficientBalanceError(Exception):
    """Raised when withdrawal exceeds balance."""
    pass


def withdraw(balance, amount):

    if amount > balance:
        raise InsufficientBalanceError(
            "Insufficient account balance."
        )

    balance -= amount

    return balance


try:

    remaining_balance = withdraw(5000, 6000)

    print(remaining_balance)

except InsufficientBalanceError as error:

    print(error)


# ============================================================
# Example 7 - Exception Hierarchy
# ============================================================

print("\n===== Example 7: Exception Hierarchy =====")


class ValidationError(Exception):
    """Base validation exception."""
    pass


class InvalidCustomerError(ValidationError):
    pass


class InvalidOrderError(ValidationError):
    pass


try:

    raise InvalidCustomerError(
        "Customer does not exist."
    )

except ValidationError as error:

    print(
        f"Caught using parent class: {error}"
    )

"""
Notice:

InvalidCustomerError inherits from ValidationError.

Therefore,

except ValidationError

can catch all validation-related exceptions.
"""

# ============================================================
# Summary
# ============================================================

print("\n===== Summary =====")

print("""
Key Takeaways

1. Create custom exceptions for business-specific errors.

2. Always inherit from Exception.

3. Give exception classes meaningful names.

4. Custom exceptions improve readability
   and maintainability.

5. They help categorize different failure types.

6. Exception hierarchies allow related
   exceptions to be handled together.

7. Custom exceptions are commonly used in
   enterprise applications and ETL pipelines.
""")
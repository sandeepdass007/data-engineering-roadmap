"""
============================================================
Mini Project
Customer Data Validation Pipeline
============================================================

Objective

Validate customer records before loading them into
a simulated database.

Topics Practiced

- try / except
- else
- finally
- raise
- Custom Exceptions
- Logging
- Production-style processing

Complete all TODO sections.
"""

import logging

# ============================================================
# Logging Configuration
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

# ============================================================
# Custom Exceptions
# ============================================================


class InvalidCustomerError(Exception):
    """Raised when a customer record fails validation."""
    pass


class DatabaseConnectionError(Exception):
    """Raised when database loading fails."""
    pass


# ============================================================
# Input Data
# ============================================================

customers = [

    {
        "customer_id": 101,
        "name": "John",
        "age": 30,
        "salary": 75000,
        "email": "john@example.com"
    },
    {
        "name": "Jane",
        "age": 28,
        "salary": 65000,
        "email": "jane@example.com"
    },

    {
        "customer_id": 103,
        "name": "Bob",
        "age": 35,
        "salary": -50000,
        "email": "bob@example.com"
    },

    {
        "customer_id": 104,
        "name": "Alice",
        "age": 29,
        "salary": 80000,
        "email": "alice-invalid-email"
    },

    {
        "customer_id": 105,
        "name": "Charlie",
        "age": -5,
        "salary": 55000,
        "email": "charlie@example.com"
    },

    {
        "customer_id": 106,
        "name": "Diana",
        "age": 0,
        "salary": 70000,
        "email": "diana@example.com"
    },

    {
        "name": "Eve",
        "age": 32,
        "salary": 85000,
        "email": "eve@example.com"
    },

    {
        "customer_id": 108,
        "name": "Frank",
        "age": 40,
        "salary": -15000,
        "email": "frankinvalid.email"
    },

    {
        "customer_id": 109,
        "name": "Grace",
        "age": 27,
        "salary": 60000,
        "email": "grace@example.com"
    },

    {
        "customer_id": 110,
        "name": "Henry",
        "age": 45,
        "salary": 95000,
        "email": "henry@example.com"
    },

]

# ============================================================
# Validation Functions
# ============================================================


def validate_customer_id(customer):
    """
    Raise InvalidCustomerError if customer_id
    is missing.
    """
    customer_id = customer.get("customer_id")
    if not customer_id:
        raise InvalidCustomerError("customer_id not found")


def validate_age(customer):
    """
    Raise InvalidCustomerError if age <= 0.
    """
    age = customer.get("age")
    if not age or age <=0 :
        raise InvalidCustomerError("age does not exist or less than equals to zero")


def validate_salary(customer):
    """
    Raise InvalidCustomerError if salary < 0.
    """
    salary = customer.get("salary")
    if not salary or salary < 0:
        raise InvalidCustomerError("Either Salary does not exist or negative")


def validate_email(customer):
    """
    Raise InvalidCustomerError if email
    does not contain '@'.
    """
    email: str = customer.get("email")
    if not (email or email.contains("@")):
        raise InvalidCustomerError("Either Email nor present or invalid format")

def validate_customer(customer):
    """
    Call all validation functions from here.
    """

    validate_customer_id(customer)
    validate_age(customer)
    validate_salary(customer)
    validate_email(customer)


# ============================================================
# Database Load
# ============================================================


def load_customer(customer):
    """
    Simulate loading a customer into the database.

    Bonus:

    Raise DatabaseConnectionError
    to simulate an infrastructure failure.
    """

    logger.info(
        f"Customer {customer['customer_id']} loaded."
    )


# ============================================================
# Main Processing Logic
# ============================================================

processed = 0
accepted = 0
rejected = 0

rejected_records = []

logger.info("ETL Pipeline Started")

for customer in customers:

    processed += 1

    try:

        validate_customer(customer)

        load_customer(customer)

        accepted += 1

    except InvalidCustomerError as error:

        rejected += 1

        logger.error("Invalid Customer Details.", error)

        rejected_records.append(customer)

    except DatabaseConnectionError as error:

        logger.critical(error)

        logger.critical(
            "Stopping pipeline."
        )

        break

# ============================================================
# Final Summary
# ============================================================

print("\n" + "=" * 55)

print(f"Processed Records : {processed}")

print(f"Accepted Records : {accepted}")

print(f"Rejected Records : {rejected}")

print("=" * 55)

print("\nRejected Records")

for rejected_customer in rejected_records:
    print(rejected_customer)

logger.info("ETL Pipeline Finished")
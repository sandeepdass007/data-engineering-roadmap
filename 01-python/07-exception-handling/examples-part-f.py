"""
============================================================
Topic 7: Exception Handling
Part F: Production ETL Pipeline Example
============================================================

Topics Covered
--------------
1. Data validation
2. Custom exceptions
3. Logging
4. Record processing
5. Continue on business errors
6. Fail fast on system errors
7. Final processing summary

This example combines everything learned in Topic 7.
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


class InvalidRecordError(Exception):
    """Raised when a record violates business rules."""
    pass


class DatabaseConnectionError(Exception):
    """Raised when database operations fail."""
    pass


# ============================================================
# Validation
# ============================================================

def validate_record(record):

    if not record["customer_id"]:
        raise InvalidRecordError(
            "Customer ID is mandatory."
        )

    if record["age"] <= 0:
        raise InvalidRecordError(
            "Age must be greater than zero."
        )

    if record["salary"] < 0:
        raise InvalidRecordError(
            "Salary cannot be negative."
        )

    if "@" not in record["email"]:
        raise InvalidRecordError(
            "Invalid email address."
        )


# ============================================================
# Database Load (Simulation)
# ============================================================

def load_record(record):

    """
    Simulate database load.

    Uncomment the exception below to simulate
    an infrastructure failure.
    """

    # raise DatabaseConnectionError(
    #     "Target database unavailable."
    # )

    logger.info(
        f"Loaded customer {record['customer_id']}"
    )


# ============================================================
# ETL Pipeline
# ============================================================

records = [

    {
        "customer_id": 101,
        "age": 30,
        "salary": 80000,
        "email": "john@example.com"
    },

    {
        "customer_id": None,
        "age": 40,
        "salary": 60000,
        "email": "alice@example.com"
    },

    {
        "customer_id": 103,
        "age": -5,
        "salary": 50000,
        "email": "bob@example.com"
    },

    {
        "customer_id": 104,
        "age": 28,
        "salary": -100,
        "email": "mary@example.com"
    },

    {
        "customer_id": 105,
        "age": 35,
        "salary": 90000,
        "email": "invalid-email"
    },

    {
        "customer_id": 106,
        "age": 32,
        "salary": 75000,
        "email": "david@example.com"
    }

]

processed = 0
accepted = 0
rejected = 0

logger.info("ETL Job Started")

for record in records:

    processed += 1

    try:

        validate_record(record)

        load_record(record)

        accepted += 1

    except InvalidRecordError as error:

        rejected += 1

        logger.warning(
            f"Rejected Record: {record}"
        )

        logger.warning(
            f"Reason: {error}"
        )

    except DatabaseConnectionError as error:

        logger.critical(error)

        logger.critical(
            "Stopping ETL job."
        )

        break

logger.info("=" * 50)

logger.info(f"Processed : {processed}")

logger.info(f"Accepted : {accepted}")

logger.info(f"Rejected : {rejected}")

logger.info("=" * 50)

logger.info("ETL Job Finished")
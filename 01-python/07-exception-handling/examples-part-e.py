"""
============================================================
Topic 7: Exception Handling
Part E: Production Exception Handling Patterns
============================================================

Topics Covered
--------------
1. Logging instead of print()
2. Re-raising exceptions
3. Retry mechanism
4. Business vs System errors
5. Processing multiple records
6. Best practices

Run one example at a time.
"""

import logging
import random
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

# ============================================================
# Example 1 - Logging Instead of print()
# ============================================================

print("\n===== Example 1: Logging =====")


try:
    int("ABC")

except ValueError as error:
    logger.error("Failed to convert input to integer.")
    logger.exception(error)

"""
logger.error() logs a custom message.

logger.exception() logs the complete
stack trace (should only be used inside
an except block).
"""

# ============================================================
# Example 2 - Re-raising Exceptions
# ============================================================

print("\n===== Example 2: Re-raising Exceptions =====")


def validate_age(age):

    try:

        if age < 0:
            raise ValueError("Age cannot be negative.")

    except ValueError:
        logger.error("Age validation failed.")
        raise


try:

    validate_age(-5)

except ValueError as error:

    logger.error(f"Caller received: {error}")

# ============================================================
# Example 3 - Retry Mechanism
# ============================================================

print("\n===== Example 3: Retry Mechanism =====")


def connect_to_database():

    if random.choice([True, False]):
        raise ConnectionError("Database unavailable.")

    return "Connected"


MAX_RETRIES = 3

for attempt in range(1, MAX_RETRIES + 1):

    try:

        connection = connect_to_database()

        logger.info(connection)

        break

    except ConnectionError as error:

        logger.warning(
            f"Attempt {attempt} failed: {error}"
        )

        if attempt == MAX_RETRIES:

            logger.error("Maximum retries reached.")

        else:

            time.sleep(1)

"""
Real systems often use exponential backoff
instead of a fixed delay.
"""

# ============================================================
# Example 4 - Business vs System Errors
# ============================================================

print("\n===== Example 4: Business vs System Errors =====")


class InvalidRecordError(Exception):
    """Business validation error."""
    pass


def process_record(record):

    if record["salary"] < 0:
        raise InvalidRecordError(
            "Salary cannot be negative."
        )

    logger.info("Record processed successfully.")


record = {
    "id": 101,
    "salary": -500
}

try:

    process_record(record)

except InvalidRecordError as error:

    logger.warning(
        f"Rejected record {record['id']}: {error}"
    )

# ============================================================
# Example 5 - Continue Processing Good Records
# ============================================================

print("\n===== Example 5: ETL Processing =====")


records = [
    {"id": 1, "salary": 50000},
    {"id": 2, "salary": -100},
    {"id": 3, "salary": 75000},
    {"id": 4, "salary": -500},
]


for record in records:

    try:

        process_record(record)

    except InvalidRecordError as error:

        logger.warning(
            f"Rejected record {record['id']} -> {error}"
        )

logger.info("ETL processing completed.")

"""
Notice that processing continues even when
individual records fail validation.
"""

# ============================================================
# Example 6 - Fail Fast for System Errors
# ============================================================

print("\n===== Example 6: Fail Fast =====")


def load_to_database():

    raise ConnectionError(
        "Target database unavailable."
    )


try:

    load_to_database()

except ConnectionError as error:

    logger.critical(error)

    logger.critical(
        "Stopping application because the "
        "database is unavailable."
    )

"""
Unlike record validation errors,
system failures should usually stop
the application.
"""

# ============================================================
# Summary
# ============================================================

print("\n===== Summary =====")

print("""
Key Takeaways

1. Prefer logging over print() in production.
2. Use logger.exception() inside except blocks.
3. Re-raise exceptions when higher layers
   should also handle them.
4. Retry only transient failures.
5. Continue processing bad business records.
6. Stop processing for infrastructure failures.
7. Always log enough context to debug issues.
""")
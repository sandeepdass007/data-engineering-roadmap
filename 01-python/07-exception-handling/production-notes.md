# Exception Handling Production Notes

## Purpose

This document explains how exception handling is used in real software systems, ETL pipelines, APIs, and production Data Engineering workflows.

The goal is not just to avoid crashes. The goal is to make failures visible, recoverable when possible, and safe for downstream systems.

---

# 1. Catch Specific Exceptions

Prefer this:

```python
except ValueError:
    ...
```

over this:

```python
except Exception:
    ...
```

Specific exceptions make the code easier to reason about and reduce the chance of hiding unexpected problems.

---

# 2. Do Not Use Bare `except` Lightly

Avoid this:

```python
except:
    pass
```

This can silently hide real problems and make debugging very difficult.

If you genuinely need a fallback, catch a specific exception or log the error explicitly.

---

# 3. Keep `try` Blocks Small

A `try` block should contain only the code that might fail.

Bad:

```python
try:
    read_file()
    transform_data()
    load_database()
    send_email()
except Exception:
    ...
```

Better:

```python
try:
    read_file()
except FileNotFoundError:
    ...

try:
    load_database()
except ConnectionError:
    ...
```

Smaller `try` blocks make it easier to understand which operation failed.

---

# 4. Use `else` for Success-Only Logic

Use `else` when you want code to run only if no exception occurred.

Example:

```python
try:
    value = int(text)
except ValueError:
    ...
else:
    process(value)
```

This keeps the `try` block focused only on risky code.

---

# 5. Use `finally` for Cleanup

Use `finally` for resource cleanup that must happen whether success or failure occurs.

Typical examples:

* closing files
* closing database connections
* deleting temporary files
* releasing locks
* cleaning up sessions

Example:

```python
file = None
try:
    file = open("customers.csv")
    ...
finally:
    if file:
        file.close()
```

---

# 6. Prefer `raise` for Business Validation

Use `raise` when a business rule is violated.

Examples:

* salary cannot be negative
* customer ID is missing
* email is invalid
* duplicate invoice detected

This is different from a system failure such as a network outage or database downtime.

---

# 7. Create Custom Exceptions for Business Concepts

Custom exceptions are useful when your application needs to distinguish between different business errors.

Examples:

* `InvalidCustomerError`
* `DuplicateEmployeeError`
* `InvalidSalaryError`
* `InsufficientBalanceError`

These names make logs and exception handlers much easier to understand.

---

# 8. Log More Than the Error Message

In production, logging only the error text is often not enough.

Good logs include:

* exception message
* record ID
* file name
* job name
* timestamp
* stack trace
* batch number, if relevant

Example:

```python
logger.error(
    f"Failed record customer_id={record['customer_id']}: {error}"
)
```

---

# 9. Separate Business Errors from System Errors

Business errors are data issues.

Examples:

* invalid salary
* missing customer ID
* malformed email

System errors are infrastructure issues.

Examples:

* database unavailable
* file system permission error
* API timeout
* network failure

These should often be handled differently.

Business errors may be rejected and skipped.

System errors may require stopping the job or retrying.

---

# 10. Retry Only Transient Failures

Not every error should be retried.

Good retry candidates:

* temporary network failure
* database timeout
* rate limiting
* short-lived service outage

Bad retry candidates:

* invalid data
* missing required field
* duplicate customer ID
* negative salary

Retrying invalid input does not fix the input.

---

# 11. Fail Fast for Infrastructure Problems

If a critical service is unavailable, it is often better to stop the job quickly than continue in a partially broken state.

Examples:

* target database is down
* S3 bucket is inaccessible
* required credential is missing
* permissions are invalid

Failing fast prevents partial writes and inconsistent data.

---

# 12. Continue for Record-Level Validation Failures

If one record is bad but the rest are valid, the pipeline should usually continue.

Example:

* 1 invalid row in 1,000 records
* 5 malformed emails in a CSV
* one missing optional field in an API response

In ETL systems, this is often handled by rejecting the bad records and moving on.

---

# 13. Never Invent Data to Avoid Exceptions

Do not silently create fake values to keep the pipeline running.

Bad examples:

* generating a random customer ID
* replacing missing salary with a random number
* assuming a default email address for invalid records

This can corrupt downstream reporting and analytics.

---

# 14. Use Exception Hierarchies When Helpful

If your application has related error categories, create a parent custom exception.

Example:

```python
class ValidationError(Exception):
    pass

class InvalidCustomerError(ValidationError):
    pass

class InvalidOrderError(ValidationError):
    pass
```

This allows broad handling when needed and more specific handling when required.

---

# 15. Re-Raise When Higher Layers Need to Know

Sometimes a lower-level function catches an exception only to add context.

Example:

```python
try:
    validate(record)
except ValueError as error:
    logger.error("Validation failed for customer_id=101")
    raise
```

Use bare `raise` to preserve the original traceback.

---

# 16. Exception Handling in ETL Pipelines

Typical ETL flow:

1. Read a record
2. Validate the record
3. If invalid, log and reject it
4. If valid, process it
5. If system fails, stop or retry
6. Produce a summary

This is one of the most common production patterns in Data Engineering.

---

# 17. Exception Handling in AWS Lambda

AWS Lambda functions often receive:

* malformed events
* missing keys
* invalid payloads
* temporary AWS service issues

Best practice:

* validate early
* raise clear business errors
* log enough context
* retry only transient failures
* avoid swallowing exceptions silently

---

# 18. Production Debugging Needs Context

A log entry like this is not enough:

```text
ValueError
```

Better:

```text
Failed processing customer_id=101: Salary cannot be negative.
```

Best logs help answer:

* what failed
* where it failed
* why it failed
* which record or input caused it

---

# 19. Avoid One Huge `try` Block

A large `try` block makes it hard to know which step failed.

Better to isolate risky operations:

* file open
* record parse
* validation
* database write
* external API call

Each step can then be handled differently if needed.

---

# 20. Practical Rule of Thumb

When writing exception handling code, ask:

* Can I recover from this error?
* Should I retry?
* Should I skip the record?
* Should I stop the job?
* Should I log and re-raise?
* Is this a data issue or a system issue?

That mindset is what turns exception handling into good engineering.

---

# Summary

Production exception handling is about control, not just survival.

A strong production design usually does the following:

* catches only the exceptions it expects
* logs helpful context
* separates data problems from system failures
* rejects bad records without stopping good ones
* retries only temporary issues
* fails fast when infrastructure is broken
* preserves tracebacks when re-raising
* uses custom exceptions for business logic

These habits make systems easier to debug, safer to operate, and more reliable in production.

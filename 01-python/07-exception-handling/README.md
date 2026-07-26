# Exception Handling

## Objective

Exception handling allows a program to gracefully handle unexpected situations (exceptions) without crashing.

Instead of terminating the application immediately, exceptions can be caught, logged, handled appropriately, or propagated to higher layers of the application.

Exception handling is one of the most important topics in production software development because real-world applications constantly interact with unreliable systems such as databases, APIs, networks, files, and external services.

---

# Why Exception Handling?

Without exception handling:

- Application crashes
- Remaining work is not completed
- Poor user experience
- Difficult debugging
- Data loss may occur

With proper exception handling:

- Applications become more reliable
- Invalid data can be skipped
- Infrastructure failures can be reported
- Useful logs can be generated
- Processing can continue where appropriate

---

# Exception Handling Flow

```text
Program Starts
      │
      ▼
Execute try block
      │
      │ Exception?
      │
  ┌───┴────┐
  │        │
 No       Yes
  │        │
  ▼        ▼
 else    except
  │        │
  └────┬───┘
       │
       ▼
   finally
       │
       ▼
 Continue Program
```

---

# try

Contains code that may fail.

Example:

```python
try:
    number = int(input("Enter number: "))
```

---

# except

Handles specific exceptions.

```python
try:
    number = int("ABC")

except ValueError:
    print("Invalid number")
```

Always prefer specific exceptions instead of:

```python
except Exception:
```

unless you intentionally want to catch every possible exception.

---

# else

Runs only when no exception occurs.

```python
try:
    number = 10 / 2

except ZeroDivisionError:
    print("Cannot divide")

else:
    print("Calculation successful")
```

---

# finally

Always executes.

Typical uses:

- Close files
- Close database connections
- Release locks
- Remove temporary files
- Cleanup resources

```python
finally:
    connection.close()
```

---

# raise

Used to manually raise exceptions.

```python
if salary < 0:
    raise ValueError(
        "Salary cannot be negative."
    )
```

Use `raise` for business rule validation.

---

# Custom Exceptions

Instead of:

```python
raise ValueError(...)
```

prefer:

```python
class InvalidSalaryError(Exception):
    pass
```

Then:

```python
raise InvalidSalaryError(
    "Salary cannot be negative."
)
```

Benefits:

- Better readability
- Better categorization
- Easier debugging
- Easier exception handling

---

# Production Exception Handling

Good production code should:

- Catch specific exceptions
- Log meaningful information
- Retry transient failures
- Continue processing invalid records where appropriate
- Stop on infrastructure failures

Avoid:

```python
except Exception:
    pass
```

This silently ignores errors.

---

# Business Errors vs System Errors

Business Errors

Examples:

- Negative salary
- Invalid email
- Missing customer ID
- Duplicate customer

Typical action:

- Reject record
- Log reason
- Continue processing

---

System Errors

Examples:

- Database unavailable
- Network timeout
- API unavailable
- Disk full

Typical action:

- Retry (if appropriate)
- Alert
- Stop processing

---

# Retry Strategy

Retry only temporary failures.

Good candidates:

- Network timeout
- Database timeout
- API rate limit

Poor candidates:

- Invalid data
- Missing mandatory field
- Incorrect business rules

A common production approach is:

- Retry
- Exponential backoff
- Maximum retry count
- Raise exception

---

# Logging

Prefer:

```python
logger.error(...)
```

instead of:

```python
print(...)
```

Production logging provides:

- Timestamp
- Log level
- Stack trace
- Monitoring integration
- Easier debugging

---

# Best Practices

- Catch only exceptions you can handle.
- Keep `try` blocks small.
- Use `finally` for cleanup.
- Create custom exceptions for business concepts.
- Never silently ignore exceptions.
- Add context to logs.
- Separate business errors from infrastructure failures.
- Retry only transient failures.
- Fail fast for infrastructure problems.
- Continue processing when business validation fails.

---

# Common Interview Questions

- Difference between syntax errors and exceptions.
- Difference between `raise` and `except`.
- Difference between `print()` and logging.
- Purpose of custom exceptions.
- Difference between business and system errors.
- What should go inside `finally`?
- When should retries be used?
- Why is `except Exception: pass` considered dangerous?

---

# Key Takeaways

- Exception handling makes applications reliable.
- `try` contains risky code.
- `except` handles failures.
- `else` runs when nothing fails.
- `finally` always executes.
- `raise` creates business validation failures.
- Custom exceptions improve readability.
- Logging is preferred over printing.
- Retry only temporary failures.
- Good exception handling is a software design skill, not just a Python feature.
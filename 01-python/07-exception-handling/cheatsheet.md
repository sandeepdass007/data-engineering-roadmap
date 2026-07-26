# Exception Handling Cheat Sheet

## Core Idea

Exception handling allows a program to deal with unexpected errors without crashing immediately.

---

## Basic Structure

```python
try:
    # risky code
except SomeException:
    # handle error
else:
    # runs only if no exception occurs
finally:
    # always runs
```

---

## `try`

Use `try` for code that might fail.

Examples:

* converting input to `int`
* reading files
* database operations
* API calls

---

## `except`

Use `except` to handle exceptions.

Prefer specific exceptions:

```python
except ValueError:
```

Better than:

```python
except Exception:
```

---

## `else`

Runs only if the `try` block succeeds.

Example:

```python
try:
    number = int("25")
except ValueError:
    print("Invalid")
else:
    print("Success")
```

---

## `finally`

Always runs.

Use it for cleanup:

* close files
* close DB connections
* release locks
* delete temp files

---

## `raise`

Use `raise` to create an exception intentionally.

Example:

```python
if salary < 0:
    raise ValueError("Salary cannot be negative.")
```

Use it for business-rule validation.

---

## Custom Exceptions

Create your own exception when you want more meaningful categories.

Example:

```python
class InvalidSalaryError(Exception):
    pass
```

Then:

```python
raise InvalidSalaryError("Salary cannot be negative.")
```

---

## `raise` vs `except`

* `raise` → creates an exception
* `except` → handles an exception

---

## `print()` vs Logging

Use logging in production, not `print()`.

Prefer:

```python
logger.error(...)
logger.exception(...)
```

Logging gives:

* timestamps
* log levels
* stack traces
* production visibility

---

## Business Error vs System Error

### Business Error

Problem with the data or business rule.

Examples:

* negative salary
* missing customer ID
* invalid email

Usually:

* reject record
* log reason
* continue processing

### System Error

Problem with infrastructure or runtime environment.

Examples:

* database down
* network timeout
* file unavailable

Usually:

* retry if transient
* alert
* stop job if needed

---

## Retry Strategy

Retry only temporary failures.

Good retry candidates:

* network timeout
* database timeout
* API rate limit
* temporary service outage

Bad retry candidates:

* missing field
* invalid salary
* duplicate record
* invalid email

---

## Bare `except`

Avoid this:

```python
except:
    pass
```

Why?

* hides errors
* makes debugging difficult
* causes silent failures

---

## `except Exception as error`

Useful when you want to capture and inspect the error.

Example:

```python
except Exception as error:
    logger.error(error)
```

---

## `raise` Inside `except`

Use bare `raise` to re-throw the same exception.

Example:

```python
except ValueError:
    logger.error("Validation failed")
    raise
```

---

## ETL Pattern

A common pattern in Data Engineering:

1. Validate record
2. If invalid, reject it and continue
3. If infrastructure fails, stop or retry
4. Log everything useful

---

## Common Interview One-Liners

* `try` contains risky code.
* `except` handles the error.
* `else` runs if no exception occurs.
* `finally` always runs.
* `raise` creates an exception.
* Custom exceptions improve readability.
* Logging is better than printing in production.
* Retry only transient failures.

---

## Remember

* Catch specific exceptions.
* Keep `try` blocks small.
* Use `finally` for cleanup.
* Separate business errors from system errors.
* Do not silently swallow exceptions.
* Add enough context to logs.

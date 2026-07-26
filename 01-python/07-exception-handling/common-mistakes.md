# Exception Handling Common Mistakes

## Purpose

This document lists common mistakes developers make while working with Python exception handling and explains the better approach.

These are the kinds of mistakes that often appear in interviews, code reviews, and production bugs.

---

# 1. Catching Too Broad an Exception

❌ Bad

```python id="4m1x9a"
try:
    process()
except Exception:
    print("Something failed")
```

This can hide unexpected problems and make debugging difficult.

✅ Better

```python id="8r9j3b"
try:
    process()
except ValueError:
    print("Invalid value")
except ConnectionError:
    print("Connection failed")
```

Catch only the exceptions you expect and know how to handle.

---

# 2. Using a Bare `except`

❌ Bad

```python id="7vh2qk"
try:
    process()
except:
    pass
```

This silently swallows errors and can cause serious production issues.

✅ Better

```python id="1k6r9p"
try:
    process()
except Exception as error:
    logger.error(error)
```

Prefer specific exceptions whenever possible.

---

# 3. Using `pass` After Catching an Exception

❌ Bad

```python id="6n5s2d"
try:
    process()
except Exception:
    pass
```

This makes failures invisible.

✅ Better

```python id="9c3t7m"
try:
    process()
except Exception as error:
    logger.exception(error)
```

If you catch an exception, do something useful with it.

---

# 4. Putting Too Much Code Inside `try`

❌ Bad

```python id="2s8v1n"
try:
    read_file()
    parse_data()
    validate_data()
    transform_data()
    save_data()
except Exception:
    ...
```

A large `try` block makes it hard to know which line failed.

✅ Better

```python id="3h5k8r"
try:
    read_file()
except FileNotFoundError:
    ...

try:
    validate_data()
except ValueError:
    ...
```

Keep `try` blocks small and focused.

---

# 5. Forgetting to Use `finally` for Cleanup

❌ Bad

```python id="5t6n1q"
file = open("customers.csv")
data = file.read()
```

If an exception occurs, the file may remain open.

✅ Better

```python id="7d9m4v"
file = None
try:
    file = open("customers.csv")
    data = file.read()
finally:
    if file:
        file.close()
```

Use `finally` for resource cleanup.

---

# 6. Using `raise` Too Generically

❌ Bad

```python id="1p8k4x"
raise Exception("Invalid data")
```

This is too vague.

✅ Better

```python id="9n2q6d"
raise ValueError("Salary cannot be negative")
```

Even better, use a custom exception when the business concept is important.

---

# 7. Raising the Wrong Exception Type

❌ Bad

```python id="2w7m5c"
if age < 0:
    raise TypeError("Age cannot be negative")
```

This is not a type problem. It is a value problem.

✅ Better

```python id="6p1t8s"
if age < 0:
    raise ValueError("Age cannot be negative")
```

Use the exception class that best matches the problem.

---

# 8. Losing the Original Traceback

❌ Bad

```python id="4q6r1z"
try:
    validate()
except ValueError as error:
    raise error
```

This can make traceback handling less clean than necessary.

✅ Better

```python id="8f3m9b"
try:
    validate()
except ValueError:
    raise
```

Use bare `raise` to re-raise the same exception.

---

# 9. Not Logging Enough Context

❌ Bad

```python id="1c8s2e"
except Exception as error:
    logger.error(error)
```

The error is logged, but you may not know which record caused it.

✅ Better

```python id="9b6m1d"
except Exception as error:
    logger.error(
        f"Failed record customer_id={record['customer_id']}: {error}"
    )
```

Good logs help you debug faster.

---

# 10. Swallowing Business Errors and System Errors the Same Way

❌ Bad

```python id="3v9h4k"
except Exception:
    print("Something failed")
```

This treats everything the same.

✅ Better

```python id="5r2n8p"
except InvalidCustomerError as error:
    logger.warning(error)
    reject_record(record)

except ConnectionError as error:
    logger.critical(error)
    raise
```

Business failures and infrastructure failures often require different actions.

---

# 11. Retrying Invalid Data

❌ Bad

```python id="6d4t2m"
retry_process(invalid_salary_record)
```

Retrying a negative salary will not make it valid.

✅ Better

Retry only transient problems like:

* network failure
* timeout
* temporary service outage

Do not retry bad business data.

---

# 12. Silently Ignoring Invalid Records Without Tracking

❌ Bad

```python id="9x3p7b"
except InvalidRecordError:
    pass
```

This makes it impossible to know how many records failed or why.

✅ Better

```python id="4n8k1q"
except InvalidRecordError as error:
    rejected_records.append(
        {
            "record": record,
            "reason": str(error)
        }
    )
```

Rejected records should usually be tracked.

---

# 13. Inventing Placeholder Values to Avoid Errors

❌ Bad

```python id="5m2r7x"
if not customer_id:
    customer_id = 0
```

This can corrupt data quality.

✅ Better

```python id="1q9v4s"
if not customer_id:
    raise ValueError("Customer ID is mandatory")
```

Never silently invent business data.

---

# 14. Forgetting to Differentiate Validation from Infrastructure

❌ Bad

```python id="8m6p2c"
try:
    validate_record(record)
    load_to_database(record)
except Exception:
    ...
```

This mixes business-rule failures with infrastructure failures.

✅ Better

Handle them separately:

```python id="3r7x1q"
except InvalidRecordError:
    ...
except DatabaseConnectionError:
    ...
```

---

# 15. Writing Exception Messages That Are Too Vague

❌ Bad

```python id="7c4n8d"
raise ValueError("Error")
```

This is not useful.

✅ Better

```python id="2p5q7v"
raise ValueError("Salary cannot be negative.")
```

A good exception message should explain what went wrong.

---

# 16. Creating Custom Exceptions for Every Small Thing

❌ Bad

```python id="1d4v6t"
class TempError(Exception):
    pass
```

Not every scenario needs a custom exception.

✅ Better

Use built-in exceptions for simple validations:

* `ValueError`
* `TypeError`
* `KeyError`

Create custom exceptions when the business concept is meaningful and needs its own category.

---

# 17. Forgetting That `else` Exists

❌ Bad

```python id="4k2m8p"
try:
    number = int(text)
    process(number)
except ValueError:
    print("Invalid")
```

This is fine, but sometimes `process(number)` should only run when conversion succeeds.

✅ Better

```python id="9h7d3r"
try:
    number = int(text)
except ValueError:
    print("Invalid")
else:
    process(number)
```

Use `else` to keep success-only logic separate.

---

# 18. Not Closing Resources

❌ Bad

```python id="5p8n4d"
file = open("customers.csv")
data = file.read()
```

If something fails before closing the file, the resource may be left open.

✅ Better

Use `finally` or a context manager when available.

```python id="6v2m9x"
file = None
try:
    file = open("customers.csv")
    data = file.read()
finally:
    if file:
        file.close()
```

---

# 19. Treating Every Error as Fatal

❌ Bad

Stopping an entire ETL job because one record has an invalid email.

✅ Better

Reject the bad record, log the issue, and continue processing valid records.

Use judgment based on whether the failure is:

* record-level
* batch-level
* system-level

---

# 20. Not Thinking About Operational Impact

❌ Bad

```python id="8c7m1p"
except Exception:
    pass
```

This may cause a silent failure where the pipeline appears successful but produces incomplete results.

✅ Better

Ask:

* Should this error be logged?
* Should it be retried?
* Should the job stop?
* Should the bad record be rejected?

Operational thinking matters as much as syntax.

---

# Summary

Avoid these exception-handling mistakes:

* Catching exceptions too broadly
* Using bare `except`
* Swallowing exceptions with `pass`
* Writing huge `try` blocks
* Forgetting `finally` for cleanup
* Raising overly generic exceptions
* Using the wrong exception type
* Losing traceback information
* Logging too little context
* Retrying invalid data
* Ignoring rejected records
* Inventing placeholder values
* Mixing validation failures with system failures
* Writing vague error messages
* Creating unnecessary custom exceptions
* Forgetting about `else`
* Leaving resources open
* Treating every error as fatal
* Ignoring the operational impact of silent failures

Good exception handling makes applications safer, cleaner, and much easier to support in production.

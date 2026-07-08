# Topic 6 - Functions
## Production Notes

This document summarizes how functions are used in real-world software development, ETL pipelines, cloud applications, and Data Engineering projects.

---

# 1. Keep Functions Small

A function should ideally perform **one logical task**.

❌ Bad

```python
def process_customer():
    validate()
    transform()
    calculate_tax()
    save_database()
    send_email()
    generate_report()
```

This function is doing too much.

---

✅ Better

```python
def validate_customer():
    pass

def transform_customer():
    pass

def calculate_tax():
    pass

def save_customer():
    pass

def send_notification():
    pass
```

Small functions are easier to:

- Read
- Test
- Debug
- Reuse

---

# 2. Follow the Single Responsibility Principle (SRP)

Every function should have **one reason to change**.

Instead of:

```python
process_data()
```

prefer:

```python
read_data()

validate_data()

transform_data()

load_data()
```

This approach naturally maps to ETL pipelines.

---

# 3. Prefer Descriptive Function Names

Avoid names like:

```python
doWork()

process()

calculate()

temp()
```

Prefer names that describe exactly what the function does.

Examples:

```python
calculate_total_salary()

validate_customer_record()

normalize_email()

load_orders_into_redshift()

send_failure_notification()
```

Good function names reduce the need for comments.

---

# 4. Avoid Global Variables

Avoid writing functions that depend on hidden global state.

❌

```python
environment = "DEV"

def load_data():
    print(environment)
```

Prefer:

```python
def load_data(environment):
    print(environment)
```

Benefits:

- Easier testing
- Better reusability
- Fewer side effects
- Easier debugging

---

# 5. Use Keyword Arguments

Instead of:

```python
connect(
    "db.company.com",
    5432,
    True,
    30
)
```

Prefer:

```python
connect(
    host="db.company.com",
    port=5432,
    ssl=True,
    timeout=30
)
```

Benefits:

- Self-documenting
- Less error-prone
- Easier to maintain

---

# 6. Keep Lambda Functions Simple

Good:

```python
lambda x: x.strip().upper()
```

Avoid:

```python
lambda x: ...
```

with long or difficult-to-read expressions.

If the logic requires explanation, create a named function instead.

---

# 7. Prefer Built-in Functions

Instead of:

```python
reduce(lambda a, b: a + b, values)
```

prefer:

```python
sum(values)
```

Similarly:

```python
max(values)

min(values)

any(values)

all(values)
```

Built-in functions are:

- Faster
- Easier to read
- Well optimized

---

# 8. Design Flexible APIs

Instead of changing a function signature every time a new option is introduced:

```python
connect(
    host,
    port,
    timeout,
    ssl,
    retries
)
```

consider:

```python
connect(**config)
```

This keeps APIs extensible and backward-compatible.

---

# 9. Write Pure Functions When Possible

A pure function:

- Depends only on its inputs.
- Produces the same output for the same input.
- Does not modify external state.

Example:

```python
def calculate_discount(price, percentage):
    return price * (1 - percentage / 100)
```

Pure functions are easier to:

- Test
- Reuse
- Parallelize

---

# 10. Keep Business Logic Separate from I/O

Avoid mixing calculations with printing or database operations.

❌

```python
def calculate_total(numbers):
    total = sum(numbers)
    print(total)
```

Prefer:

```python
def calculate_total(numbers):
    return sum(numbers)

total = calculate_total(numbers)
print(total)
```

Returning values makes functions reusable.

---

# 11. Avoid Deep Recursion

Python has a recursion limit.

Recursive solutions are appropriate for:

- Trees
- Nested JSON
- XML
- Directory traversal

Avoid recursion for:

- Large CSV files
- Millions of records
- Flat datasets

Prefer loops in those scenarios.

---

# 12. Make Functions Easy to Test

Good functions:

- Have clear inputs.
- Produce predictable outputs.
- Avoid hidden dependencies.
- Avoid modifying global variables.

Example:

```python
assert calculate_total([10, 20, 30]) == 60
```

Testing becomes straightforward.

---

# 13. Reuse Common Logic

If the same logic appears in multiple places:

❌

```python
# repeated validation logic
```

Extract it into a reusable function.

Example:

```python
validate_customer()

validate_email()

normalize_phone_number()
```

This reduces duplication and improves maintainability.

---

# 14. Functions in Data Engineering

Functions are commonly used for:

- Reading files
- Data validation
- Data transformation
- Schema validation
- API calls
- Database operations
- AWS Lambda handlers
- Airflow tasks
- Spark transformations
- Logging
- Retry mechanisms

A well-designed ETL pipeline is typically composed of many small, focused functions.

---

# Summary

Good production functions are:

- Small
- Reusable
- Easy to test
- Focused on one responsibility
- Independent of global state
- Clearly named
- Flexible through parameters
- Easy to extend
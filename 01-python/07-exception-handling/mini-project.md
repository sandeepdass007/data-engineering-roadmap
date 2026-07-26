# Mini Project - Customer Data Validation Pipeline

## Objective

Build a simple ETL-style customer validation pipeline that demonstrates professional exception handling techniques.

This project combines almost every concept learned in Topic 7:

- try / except
- else
- finally
- raise
- Custom Exceptions
- Logging
- Business vs System Errors
- Production-style record processing

---

# Business Scenario

Your company receives customer records from multiple vendors.

Before loading the records into the target database, each record must be validated.

A single bad record should **not** stop the entire pipeline.

However, if the database becomes unavailable, the application should stop immediately.

---

# Input Data

Create a list of dictionaries similar to:

```python
customers = [
    {
        "customer_id": 101,
        "name": "John",
        "age": 30,
        "salary": 80000,
        "email": "john@example.com"
    },
    ...
]
```

Include at least **10 records**.

Some records should intentionally contain invalid data.

Examples:

- Missing customer_id
- Negative salary
- Invalid email
- Invalid age

---

# Validation Rules

A customer record is valid only if:

- customer_id is present
- age is greater than zero
- salary is zero or greater
- email contains "@"

Create reusable validation functions.

Use **raise** whenever a business rule fails.

---

# Custom Exceptions

Create at least two custom exceptions.

Example:

```python
class InvalidCustomerError(Exception):
    pass

class DatabaseConnectionError(Exception):
    pass
```

---

# Processing Rules

For each customer:

1. Validate the record.

2. If valid:

   Simulate loading into a database.

3. If invalid:

   Log the error.

   Store the rejected record in a separate list.

4. Continue processing the remaining records.

---

# Database Load Simulation

Create a function:

```python
load_customer(customer)
```

Initially, it should simply print or log:

```
Customer loaded successfully.
```

(Optional)

Add a flag that raises:

```python
DatabaseConnectionError
```

to simulate a database outage.

When this happens:

- Stop processing immediately.
- Log the error.
- Display the processing summary.

---

# Final Summary

Display something similar to:

```
=================================

Records Processed : 10

Accepted Records : 7

Rejected Records : 3

=================================
```

Also print all rejected records with the reason for rejection.

---

# Bonus Features (Optional)

If you finish early, try one or more of these:

### Bronze

Add validation for duplicate customer IDs.

---

### Silver

Store rejected records together with the rejection reason.

Example:

```python
{
    "record": customer,
    "reason": "Salary cannot be negative."
}
```

---

### Gold

Create separate validation functions:

- validate_age()
- validate_salary()
- validate_email()
- validate_customer_id()

and call them from a single:

```python
validate_customer()
```

function.

---

### Platinum

Implement a retry mechanism for database connection failures.

Retry up to **3 times** before raising
`DatabaseConnectionError`.

---

# Learning Outcomes

After completing this project, you should be comfortable with:

- Designing robust validation logic
- Creating custom exceptions
- Using raise effectively
- Separating business errors from system errors
- Processing bad records without stopping the pipeline
- Writing production-style exception handling code
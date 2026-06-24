# Python Tuples

## Overview

A Tuple is an ordered, immutable collection of values in Python.

Tuples are similar to Lists, but once created, their contents cannot be modified.

Because of their immutable nature, tuples are commonly used to represent fixed structures, configuration values, database records, coordinates, and function return values.

---

# Why Tuples Matter

Tuples communicate intent.

When another developer sees a tuple, they immediately know:

* The structure is fixed
* The data should not be modified
* The values have a stable meaning

Example:

```python
DATABASE_CONFIG = (
    "prod-server",
    5432,
    "finance_db"
)
```

---

# Key Characteristics

## Ordered

Values maintain insertion order.

```python
employee = ("John", 100000)
```

---

## Immutable

Values cannot be changed after creation.

```python
employee = ("John", 100000)

employee[0] = "Mike"
```

Raises:

```text
TypeError
```

---

## Supports Duplicate Values

```python
numbers = (1, 1, 2, 2, 3)
```

Duplicates are allowed.

---

## Supports Mixed Datatypes

```python
employee = (
    "John",
    100000,
    True
)
```

---

# Creating Tuples

## Standard Tuple

```python
employee = ("John", 100000)
```

---

## Empty Tuple

```python
employee = ()
```

---

## Single Element Tuple

```python
employee = ("John",)
```

Important:

```python
("John")
```

is a string, not a tuple.

The comma creates the tuple.

---

# Accessing Data

## Indexing

```python
employee[0]
```

Output:

```text
John
```

---

## Negative Indexing

```python
employee[-1]
```

Returns the last element.

---

## Slicing

```python
employee = (
    "John",
    "Toronto",
    100000
)

employee[0:2]
```

Output:

```python
("John", "Toronto")
```

---

# Tuple Packing

Python automatically packs values into a tuple.

```python
employee = "John", 100000
```

Equivalent to:

```python
employee = (
    "John",
    100000
)
```

---

# Tuple Unpacking

```python
employee = (
    "John",
    100000
)

name, salary = employee
```

Results:

```python
name = "John"
salary = 100000
```

---

# Star Unpacking

```python
record = (
    "John",
    "Toronto",
    "Canada",
    100000
)

name, *location, salary = record
```

Results:

```python
name = "John"

location = [
    "Toronto",
    "Canada"
]

salary = 100000
```

---

# Returning Multiple Values

A common Python pattern.

```python
def get_metrics():
    return 1000, 25
```

Usage:

```python
processed, failed = get_metrics()
```

Python automatically returns a tuple.

---

# Tuple Methods

Tuples provide only two commonly used methods.

## count()

```python
numbers = (1, 2, 2, 3)

numbers.count(2)
```

Output:

```text
2
```

---

## index()

```python
numbers = (1, 2, 3)

numbers.index(2)
```

Output:

```text
1
```

---

# Hashability

Tuples can be used as dictionary keys because they are immutable.

```python
employee_salary = {
    ("John", "IT"): 100000
}
```

---

## Why Lists Cannot Be Dictionary Keys

This fails:

```python
{
    ["John", "IT"]: 100000
}
```

Error:

```text
TypeError: unhashable type: 'list'
```

Lists are mutable and therefore not hashable.

---

# Composite Keys

A powerful tuple use case.

```python
sales = {
    ("Canada", 2024): 500000,
    ("USA", 2024): 900000
}
```

Lookup:

```python
sales[("Canada", 2024)]
```

Output:

```text
500000
```

---

# Named Tuples

Named tuples provide readable field access while remaining immutable.

```python
from collections import namedtuple

Employee = namedtuple(
    "Employee",
    ["id", "name", "salary"]
)

employee = Employee(
    1001,
    "John",
    100000
)
```

Access:

```python
employee.name
employee.salary
```

Instead of:

```python
employee[1]
employee[2]
```

---

# Data Engineering Usage

Tuples frequently appear in:

## Database Records

```python
(1001, "John", 100000)
```

---

## Function Return Values

```python
return processed_rows, failed_rows
```

---

## ETL Metrics

```python
(
    job_name,
    rows_processed,
    rows_failed
)
```

---

## Composite Keys

```python
(country, year)
```

---

## Configuration Values

```python
DATABASE_CONFIG
```

---

# Production Insights

Use a Tuple when:

* Data should not change
* The structure is fixed
* Returning multiple values
* Creating composite dictionary keys

Use a List when:

* Elements need to be added
* Elements need to be removed
* Ordering changes frequently

---

# Common Pitfalls

## Forgetting the Comma

Wrong:

```python
("John")
```

Correct:

```python
("John",)
```

---

## Unpacking Mismatch

Wrong:

```python
employee = ("John", 100000)

name, salary, city = employee
```

Raises:

```text
ValueError
```

because the number of variables does not match the number of values.

---

## Assuming Immutability Applies Recursively

A tuple is only fully hashable when all contained elements are hashable.

```python
(
    "Canada",
    [2024]
)
```

is not hashable because the list is mutable.

---

# Summary

By completing this topic you should understand:

* Tuple creation
* Immutability
* Packing
* Unpacking
* Star unpacking
* Function return values
* Tuple methods
* Hashability
* Composite keys
* Named tuples
* Data Engineering use cases
* Production design considerations

Tuples are one of the most important immutable data structures in Python and form the foundation for many patterns used throughout Data Engineering and distributed systems.

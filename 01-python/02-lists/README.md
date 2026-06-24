# Python Lists

## Overview

A List is an ordered, mutable collection of elements in Python.

Lists allow storing multiple values in a single variable and support indexing, slicing, iteration, modification, and various utility operations.

Lists are one of the most frequently used data structures in Python and form the foundation for many higher-level data processing concepts used in Data Engineering.

---

## Why Lists Matter in Data Engineering

Lists are commonly used when working with:

* API responses
* JSON arrays
* Configuration files
* ETL transformations
* Batch processing
* Intermediate datasets
* Pandas DataFrames
* PySpark transformations

Example:

```python
employees = [
    "John",
    "Mike",
    "Alice"
]
```

---

## Key Characteristics

### Ordered

Elements maintain insertion order.

```python
employees = ["John", "Mike", "Alice"]
```

---

### Mutable

Lists can be modified after creation.

```python
employees[0] = "David"
```

---

### Dynamic Size

Elements can be added or removed.

```python
employees.append("John")
employees.remove("John")
```

---

### Supports Duplicate Values

```python
employees = ["John", "John", "Mike"]
```

Duplicates are allowed.

---

## Creating Lists

### Empty List

```python
employees = []
```

### List of Strings

```python
employees = ["John", "Mike", "Alice"]
```

### List of Numbers

```python
salaries = [100000, 120000, 90000]
```

---

## Indexing

Python uses zero-based indexing.

```python
employees[0]
```

Output:

```python
John
```

### Negative Indexing

```python
employees[-1]
```

Returns the last element.

---

## Slicing

Retrieve a subset of a list.

```python
employees[1:3]
```

Output:

```python
["Mike", "Alice"]
```

Rules:

* Start index is included
* End index is excluded

---

## Iteration

```python
for employee in employees:
    print(employee)
```

---

## List Comprehensions

Create lists in a concise and Pythonic way.

```python
salaries = [100, 200, 300]

doubled = [salary * 2 for salary in salaries]
```

Output:

```python
[200, 400, 600]
```

### Filtering

```python
high_salary = [
    salary
    for salary in salaries
    if salary > 150
]
```

---

## Nested Lists

Lists can contain other lists.

```python
employees = [
    ["John", 100000],
    ["Mike", 120000]
]
```

Access:

```python
employees[0][1]
```

Output:

```python
100000
```

---

## Reference vs Copy

### Reference Assignment

```python
a = [1, 2, 3]

b = a
```

Both variables point to the same list.

Modifying one affects the other.

---

### Copy

```python
b = a.copy()
```

Creates a new list object.

---

## Shallow Copy vs Deep Copy

### Shallow Copy

```python
copy_employees = employees.copy()
```

Copies only the outer list.

Nested objects remain shared.

### Deep Copy

```python
import copy

copy.deepcopy(employees)
```

Copies all nested objects recursively.

---

## enumerate()

Used when both index and value are needed.

```python
for idx, employee in enumerate(employees):
    print(idx, employee)
```

---

## zip()

Combine multiple iterables.

```python
names = ["John", "Mike"]
salaries = [100, 200]

for name, salary in zip(names, salaries):
    print(name, salary)
```

---

## sort() vs sorted()

### sort()

Modifies the original list.

```python
numbers.sort()
```

### sorted()

Returns a new sorted list.

```python
result = sorted(numbers)
```

---

## any() and all()

### all()

Returns True if all values are True.

```python
all([True, True, True])
```

### any()

Returns True if at least one value is True.

```python
any([False, False, True])
```

---

## Common Production Pitfalls

### Shared References

```python
b = a
```

May unintentionally modify original data.

---

### Shallow Copy on Nested Structures

```python
employees.copy()
```

Does not fully isolate nested objects.

---

### Inefficient List Building

Avoid:

```python
records = records + [row]
```

Prefer:

```python
records.append(row)
```

---

## Data Engineering Examples

### Extract Employee Names

```python
employee_names = [
    emp["name"]
    for emp in employees
]
```

---

### Validation Checks

```python
if all(validation_results):
    load_data()
```

---

### Build Records Dynamically

```python
record = dict(zip(columns, values))
```

---

## Summary

By completing this topic you should understand:

* List creation
* Indexing
* Slicing
* Mutation
* Iteration
* List comprehensions
* Nested lists
* Copy semantics
* enumerate()
* zip()
* Sorting
* Validation helpers
* Real-world Data Engineering usage

Lists are one of the most important Python data structures and are heavily used throughout Pandas, PySpark, ETL pipelines, APIs, and modern Data Engineering workflows.

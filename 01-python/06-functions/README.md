# Topic 6 - Functions

## Overview

Functions are one of the most important building blocks in Python. They help organize code into reusable, modular, and maintainable units. Instead of repeating the same logic multiple times, a function allows us to write it once and use it wherever needed.

In production systems, functions improve readability, simplify testing, reduce duplication, and make applications easier to maintain. Nearly every Python application, ETL pipeline, API, or automation script is built using functions.

---

# Learning Objectives

After completing this topic, you should be able to:

- Create reusable functions
- Pass data using parameters and arguments
- Return values from functions
- Understand local and global scope
- Use lambda functions appropriately
- Apply `map()`, `filter()`, and `reduce()`
- Pass functions as arguments
- Build flexible APIs using `*args` and `**kwargs`
- Understand recursion and identify suitable use cases
- Write production-ready reusable functions

---

# Topics Covered

## Part A - Function Basics

Learned how to:

- Define functions
- Call functions
- Pass parameters
- Return values
- Write reusable code

Example:

```python
def greet(name):
    return f"Hello {name}"
```

---

## Part B - Parameters & Arguments

Covered:

- Positional arguments
- Keyword arguments
- Default arguments

Example:

```python
def connect(host, port=5432):
    pass
```

Production recommendation:

Prefer keyword arguments for readability.

---

## Part C - Variable Scope

Covered:

- Local variables
- Global variables
- Variable shadowing
- `global` keyword

Best practice:

Prefer passing data as parameters instead of relying on global variables.

---

## Part D - Lambda Functions

Lambda functions are anonymous one-line functions.

Example:

```python
square = lambda x: x * x
```

Use lambda when:

- Logic is short
- Reuse is not required

Use a normal function when:

- Logic grows
- Reuse is expected
- Better readability is needed

---

## Part E - map()

Purpose:

Transform every element in an iterable.

Example:

```python
numbers = [1, 2, 3]

result = list(map(lambda x: x * 2, numbers))
```

ETL Example:

- Convert strings to integers
- Standardize names
- Normalize data

---

## Part F - First-Class Functions

Python functions are first-class objects.

This means functions can:

- Be stored in variables
- Be passed as arguments
- Be returned from other functions

Example:

```python
handler = process
```

Production usage:

- ETL pipelines
- Validation pipelines
- Strategy pattern
- Callback functions

---

## Part G - filter()

Purpose:

Keep only records that satisfy a condition.

Example:

```python
valid_records = list(
    filter(
        lambda record: record["active"],
        records
    )
)
```

ETL Example:

- Remove invalid records
- Filter inactive customers
- Validate incoming data

---

## Part H - reduce()

Purpose:

Aggregate multiple values into a single value.

Example:

```python
from functools import reduce

total = reduce(
    lambda a, b: a + b,
    numbers
)
```

Common use cases:

- Sum
- Maximum
- Product
- Custom aggregation

Production note:

Prefer built-in functions like `sum()`, `max()`, and `min()` whenever they solve the problem.

---

## Part I - *args and **kwargs

### *args

Allows a function to accept a variable number of positional arguments.

```python
def add(*numbers):
    pass
```

Internally stored as a tuple.

---

### **kwargs

Allows a function to accept a variable number of keyword arguments.

```python
def connect(**config):
    pass
```

Internally stored as a dictionary.

Production usage:

- Configuration objects
- Logging frameworks
- AWS SDK
- Flask
- FastAPI

---

## Part J - Recursion

Recursion is when a function calls itself.

Every recursive function must contain:

1. Base Case
2. Recursive Case

Common use cases:

- Tree traversal
- Nested JSON
- XML parsing
- Directory traversal

Avoid recursion for:

- Large CSV processing
- Flat datasets
- Millions of records

---

# map() vs filter() vs reduce()

| Function | Purpose | Input | Output |
|----------|---------|-------|--------|
| `map()` | Transform | Many | Many |
| `filter()` | Select | Many | Some |
| `reduce()` | Aggregate | Many | One |

Examples:

```python
map(lambda x: x * 2, numbers)
```

```python
filter(lambda x: x > 10, numbers)
```

```python
reduce(lambda a, b: a + b, numbers)
```

---

# Production Best Practices

- Keep functions focused on one responsibility.
- Prefer meaningful function names.
- Avoid global variables whenever possible.
- Prefer keyword arguments for readability.
- Keep lambda expressions simple.
- Use named functions when logic becomes complex.
- Filter invalid data early in ETL pipelines.
- Prefer built-in aggregation functions over `reduce()` when possible.
- Use `*args` and `**kwargs` for flexible APIs.
- Avoid recursion for deep or large-scale processing.

---

# Common Interview Questions

- Difference between parameters and arguments
- `print()` vs `return`
- Local vs global variables
- Lambda vs normal functions
- Difference between `map()`, `filter()`, and `reduce()`
- Why are functions first-class objects?
- Difference between `*args` and `**kwargs`
- Why is recursion risky in production?
- What is the base case?
- Why are keyword arguments preferred?

---

# Data Engineering Applications

Functions are heavily used in:

- ETL pipelines
- Data validation
- AWS Lambda
- AWS Glue
- Airflow DAGs
- FastAPI
- Flask
- Pandas transformations
- PySpark transformations
- Data quality frameworks

---

# Key Takeaways

- Functions improve code reuse and maintainability.
- Prefer passing data through parameters instead of globals.
- Lambda functions are best for short, simple logic.
- `map()` transforms data.
- `filter()` removes unwanted data.
- `reduce()` aggregates data into a single result.
- `*args` accepts multiple positional arguments.
- `**kwargs` accepts multiple keyword arguments.
- Every recursive function needs a base case.
- Good function design leads to cleaner, more maintainable software.
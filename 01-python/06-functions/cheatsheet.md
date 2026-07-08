# Topic 6 - Functions
## Cheatsheet

---

# Function Syntax

```python
def function_name(parameters):
    # code
    return value
```

Example:

```python
def greet(name):
    return f"Hello {name}"
```

---

# Parameters vs Arguments

| Parameter | Argument |
|------------|----------|
| Variable in function definition | Actual value passed to function |

Example:

```python
def greet(name):   # parameter
    print(name)

greet("John")      # argument
```

---

# Return vs Print

| print() | return |
|----------|---------|
| Displays output | Sends value back to caller |
| Cannot be reused | Can be stored and reused |

---

# Positional Arguments

```python
def greet(name, country):
    pass

greet("John", "Canada")
```

Order matters.

---

# Keyword Arguments

```python
greet(
    country="Canada",
    name="John"
)
```

Order does not matter.

Preferred in production for readability.

---

# Default Parameters

```python
def connect(
    host,
    port=5432
):
    pass
```

Optional parameters should have default values.

---

# Variable Scope

## Local Variable

```python
def example():
    count = 10
```

Accessible only inside the function.

---

## Global Variable

```python
count = 10
```

Accessible throughout the module.

Avoid modifying global variables whenever possible.

---

# Lambda Function

```python
square = lambda x: x * x
```

Use for:

- Short logic
- One-line expressions

Avoid for:

- Complex logic
- Multiple statements
- Reusable code

---

# map()

Purpose:

Transform every element.

```python
numbers = [1, 2, 3]

result = list(
    map(
        lambda x: x * 2,
        numbers
    )
)
```

Result:

```python
[2, 4, 6]
```

---

# filter()

Purpose:

Keep matching elements.

```python
numbers = [1, 2, 3, 4]

result = list(
    filter(
        lambda x: x % 2 == 0,
        numbers
    )
)
```

Result:

```python
[2, 4]
```

---

# reduce()

```python
from functools import reduce
```

Purpose:

Aggregate values.

```python
total = reduce(
    lambda a, b: a + b,
    numbers
)
```

Result:

Single value.

---

# First-Class Functions

Functions can be:

- Stored in variables
- Passed as arguments
- Returned from functions

Example:

```python
handler = process
```

---

# *args

Accepts multiple positional arguments.

```python
def add(*numbers):
    print(numbers)
```

Stored as:

```python
tuple
```

---

# **kwargs

Accepts multiple keyword arguments.

```python
def connect(**config):
    print(config)
```

Stored as:

```python
dict
```

---

# Parameter Order

Correct order:

```python
def example(
    required,
    *args,
    optional=None,
    **kwargs
):
    pass
```

Remember:

```
Required

↓

*args

↓

Optional

↓

**kwargs
```

---

# Recursion

Function calling itself.

Must contain:

1. Base Case
2. Recursive Case

Example:

```python
def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)
```

---

# map() vs filter() vs reduce()

| Function | Purpose | Output |
|----------|----------|--------|
| map() | Transform | Many |
| filter() | Select | Some |
| reduce() | Aggregate | One |

Remember:

```
map()

Many
↓

Many

---------------------

filter()

Many
↓

Some

---------------------

reduce()

Many
↓

One
```

---

# Production Best Practices

- Write small reusable functions.
- Follow the Single Responsibility Principle.
- Prefer keyword arguments.
- Avoid global variables.
- Use descriptive function names.
- Keep lambda expressions short.
- Prefer built-in functions (`sum()`, `max()`, `min()`) over `reduce()` when possible.
- Use `*args` and `**kwargs` for flexible APIs.
- Avoid recursion for large flat datasets.
- Write functions that are easy to test.

---

# Interview One-Liners

**Parameter**

Variable in function definition.

---

**Argument**

Actual value passed to the function.

---

**Lambda**

Anonymous one-line function.

---

**map()**

Transforms every element.

---

**filter()**

Keeps matching elements.

---

**reduce()**

Aggregates values into one.

---

**First-Class Function**

Function treated like any other object.

---

**\*args**

Variable positional arguments (tuple).

---

**\**kwargs**

Variable keyword arguments (dictionary).

---

**Recursion**

A function calling itself until the base case is reached.
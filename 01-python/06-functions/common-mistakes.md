# Topic 6 - Functions
## Common Mistakes

This document highlights common mistakes developers make while working with Python functions and explains the recommended approach.

---

# 1. Confusing Parameters and Arguments

❌ Incorrect understanding

Thinking parameters and arguments are the same thing.

```python
def greet(name):
    print(name)
```

```python
greet("John")
```

✅ Correct

- `name` is a **parameter**.
- `"John"` is an **argument**.

---

# 2. Using print() Instead of return

❌

```python
def add(a, b):
    print(a + b)
```

```python
result = add(10, 20)

print(result)
```

Output:

```
30
None
```

Why?

Because the function does not return anything.

---

✅

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output

```
30
```

---

# 3. Forgetting the return Statement

❌

```python
def square(number):
    number * number
```

Result:

```
None
```

---

✅

```python
def square(number):
    return number * number
```

---

# 4. Writing Functions That Do Too Much

❌

```python
def process_customer():
    read_file()
    validate()
    transform()
    save_database()
    send_email()
```

This violates the **Single Responsibility Principle**.

---

✅

```python
read_customer()

validate_customer()

transform_customer()

save_customer()

send_notification()
```

Small functions are easier to understand and maintain.

---

# 5. Overusing Global Variables

❌

```python
environment = "DEV"

def load():
    print(environment)
```

If another part of the program changes `environment`, the function's behavior changes unexpectedly.

---

✅

```python
def load(environment):
    print(environment)
```

Prefer passing values explicitly.

---

# 6. Making Lambda Functions Too Complex

❌

```python
lambda x: ...
```

with long, difficult-to-read expressions.

---

✅

If the logic is more than a simple expression, write a normal function.

```python
def clean_name(name):
    return name.strip().title()
```

---

# 7. Forgetting That map() and filter() Are Lazy

❌

```python
numbers = map(int, ["1", "2", "3"])

print(numbers)
```

Output

```
<map object at ...>
```

---

✅

```python
numbers = list(map(int, ["1", "2", "3"]))

print(numbers)
```

Output

```
[1, 2, 3]
```

---

# 8. Using reduce() When a Built-in Function Exists

❌

```python
from functools import reduce

reduce(lambda a, b: a + b, numbers)
```

---

✅

```python
sum(numbers)
```

Prefer built-in functions such as:

- `sum()`
- `max()`
- `min()`
- `any()`
- `all()`

They are clearer and often more efficient.

---

# 9. Confusing Function Reference with Function Call

❌

```python
handler = process()
```

This executes the function immediately.

---

✅

```python
handler = process
```

This stores a reference to the function.

---

# 10. Mixing Up *args and **kwargs

Remember:

```python
*args
```

- Variable positional arguments
- Stored as a tuple

---

```python
**kwargs
```

- Variable keyword arguments
- Stored as a dictionary

---

# 11. Using the Wrong Parameter Order

❌

```python
def example(**kwargs, *args):
    pass
```

This raises a `SyntaxError`.

---

✅

```python
def example(required,
            *args,
            optional=None,
            **kwargs):
    pass
```

Correct order:

1. Required parameters
2. `*args`
3. Optional/keyword-only parameters
4. `**kwargs`

---

# 12. Forgetting the Base Case in Recursion

❌

```python
def countdown(n):
    countdown(n - 1)
```

This eventually raises:

```
RecursionError
```

---

✅

```python
def countdown(n):

    if n == 0:
        return

    countdown(n - 1)
```

Every recursive function must have a base case.

---

# 13. Using Recursion for Large Flat Datasets

❌

Using recursion to process millions of CSV records.

Problems:

- High memory usage
- Slower execution
- Recursion limit

---

✅

Use loops for flat datasets.

Reserve recursion for:

- Trees
- Nested JSON
- XML
- Directory traversal

---

# 14. Hardcoding Values Inside Functions

❌

```python
def connect():
    host = "localhost"
    port = 5432
```

This makes the function difficult to reuse.

---

✅

```python
def connect(host, port=5432):
    pass
```

or

```python
def connect(**config):
    pass
```

---

# 15. Poor Function Names

❌

```python
def temp():
    pass

def process():
    pass

def work():
    pass
```

These names do not communicate intent.

---

✅

```python
def validate_customer():
    pass

def calculate_total_salary():
    pass

def load_orders_to_redshift():
    pass
```

Choose names that clearly describe the function's responsibility.

---

# Summary

Avoid these habits:

- Confusing parameters with arguments.
- Using `print()` when `return` is needed.
- Forgetting `return`.
- Creating overly large functions.
- Relying on global variables.
- Writing complex lambda expressions.
- Forgetting that `map()` and `filter()` are lazy.
- Using `reduce()` when a built-in function is available.
- Confusing function references with function calls.
- Mixing up `*args` and `**kwargs`.
- Using the wrong parameter order.
- Forgetting the base case in recursion.
- Using recursion for large flat datasets.
- Hardcoding configuration.
- Choosing vague function names.

Following these practices will result in cleaner, more maintainable, and production-ready Python code.
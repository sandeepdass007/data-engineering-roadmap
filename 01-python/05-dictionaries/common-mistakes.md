# Common Mistakes - Python Dictionaries

## Purpose

This document highlights common mistakes developers make when working with Python Dictionaries.

Understanding these mistakes will help you:

- Write cleaner code
- Avoid production bugs
- Perform better in interviews
- Become a better Data Engineer

---

# Mistake 1 - Using [] for Optional Fields

## ❌ Bad

```python
customer = {
    "name": "John"
}

print(customer["country"])
```

Output:

```
KeyError: 'country'
```

---

## ✅ Better

```python
print(customer.get("country"))
```

Output

```python
None
```

---

## Why?

API fields often change.

Using `get()` makes your code much more robust.

---

# Mistake 2 - Forgetting that `in` Checks Keys

Many beginners think:

```python
employee = {
    "name": "John"
}

print("John" in employee)
```

Output?

Most people answer:

```
True
```

Wrong.

Output:

```
False
```

Why?

Because:

```python
in
```

checks **keys**, not values.

Correct:

```python
"name" in employee
```

---

# Mistake 3 - Duplicate Keys

```python
employee = {
    "name": "John",
    "name": "Mike"
}
```

Output:

```python
{
    "name": "Mike"
}
```

Python silently overwrites the first key.

---

# Mistake 4 - Assuming Dictionaries Are Indexed

Wrong:

```python
employee[0]
```

Dictionary access is done using keys.

Correct:

```python
employee["name"]
```

---

# Mistake 5 - Using Mutable Objects as Keys

Wrong:

```python
employee = {
    ["John"]: 100
}
```

Output:

```
TypeError
```

Lists are mutable.

Dictionary keys must be hashable.

Correct:

```python
employee = {
    ("John",):100
}
```

---

# Mistake 6 - Forgetting `get()` Can Return None

```python
salary = employee.get("salary")

print(salary + 1000)
```

If salary is missing:

```
TypeError
```

Safer:

```python
salary = employee.get("salary", 0)
```

---

# Mistake 7 - Confusing Reference Copy with Actual Copy

```python
employee = {
    "salary":100
}

new_employee = employee

new_employee["salary"] = 200
```

Many expect:

```python
employee["salary"]
```

to remain:

```
100
```

Actual output:

```
200
```

Both variables reference the same Dictionary.

Correct:

```python
new_employee = employee.copy()
```

---

# Mistake 8 - Deleting Keys Without Checking

```python
del employee["country"]
```

If the key doesn't exist:

```
KeyError
```

Safer:

```python
employee.pop("country", None)
```

---

# Mistake 9 - Modifying a Dictionary While Iterating

Wrong:

```python
for key in employee:
    del employee[key]
```

Output:

```
RuntimeError
```

Correct:

```python
for key in list(employee.keys()):
    del employee[key]
```

---

# Mistake 10 - Ignoring Nested Structures

Many APIs return:

```python
customer = {
    "address": {
        "country": {
            "code":"CA"
        }
    }
}
```

Wrong:

```python
customer["address"]["country"]["code"]
```

If any level is missing:

```
KeyError
```

Safer:

```python
customer.get("address", {}) \
        .get("country", {}) \
        .get("code")
```

---

# Mistake 11 - Hardcoding Every Field

Wrong

```python
customer_id = customer["customer_id"]
customer_name = customer["customer_name"]
customer_email = customer["customer_email"]
```

As APIs evolve, maintenance becomes difficult.

Better:

Pass the entire Dictionary to the processing function.

---

# Mistake 12 - Forgetting Dictionaries Preserve Only the Latest Value

```python
counts = {}

counts["Canada"] = 5
counts["Canada"] = 6
```

Output:

```python
{
    "Canada":6
}
```

The previous value is replaced.

---

# Mistake 13 - Reinventing Frequency Counting

Wrong

```python
if country in counts:

    counts[country] += 1

else:

    counts[country] = 1
```

Better

```python
counts[country] = counts.get(country, 0) + 1
```

Shorter.

Cleaner.

Used everywhere.

---

# Mistake 14 - Assuming Every JSON Payload Is Perfect

Real APIs contain:

- Missing fields
- Null values
- Unexpected fields
- Incorrect data types
- Schema changes

Never trust incoming data.

Always validate.

---

# Mistake 15 - Using Dictionaries for Everything

Dictionaries are excellent for:

- JSON
- Metadata
- Configuration
- Records
- Frequency counting

But they are not always the best choice.

Examples:

- Ordered numerical data → List
- Immutable configuration → Tuple
- Unique values → Set
- Tabular data → Pandas DataFrame
- Distributed processing → PySpark DataFrame

Choose the right data structure.

---

# Mistake 16 - Not Thinking About Scale

Python Dictionaries work great for:

- Hundreds
- Thousands
- Millions of records (depending on memory)

They are **not** suitable for processing hundreds of millions or billions of records on a single machine.

At that scale:

- Pandas (medium datasets)
- PySpark (large distributed datasets)

become the better choice.

---

# Interview Traps

Interviewers often ask these intentionally:

### Trap 1

```python
"John" in employee
```

Most candidates answer incorrectly.

---

### Trap 2

Difference between:

```python
get()
```

and

```python
[]
```

Know this extremely well.

---

### Trap 3

Why can't Lists be Dictionary keys?

Expected answer:

Lists are mutable and therefore unhashable.

---

### Trap 4

What happens with duplicate keys?

Only the last value survives.

---

### Trap 5

What happens when a key is missing?

Depends on whether you use:

- `[]`
- `get()`

Know the difference.

---

# Production Best Practices Summary

✔ Prefer `get()` for optional fields.

✔ Validate required fields.

✔ Never trust API responses.

✔ Keep metadata in Dictionaries.

✔ Use frequency counting patterns.

✔ Avoid mutating Dictionaries while iterating.

✔ Understand shallow copies.

✔ Use descriptive keys.

✔ Think about scalability.

✔ Always choose the right data structure.

---

# Final Advice

A Dictionary is much more than a Python data structure.

For a Data Engineer, it represents:

- A JSON document
- An API payload
- A configuration object
- ETL metadata
- A customer record
- An event message
- A log entry

If you can comfortably process Dictionaries, you're already building one of the most important skills required in modern Data Engineering.
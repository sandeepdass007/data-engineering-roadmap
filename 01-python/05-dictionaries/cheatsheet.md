# Python Dictionaries Cheat Sheet

> **Topic 5 Quick Revision**
>
> Read this file in 5–10 minutes before interviews or coding sessions.

---

# What is a Dictionary?

A Dictionary is a mutable collection of **key-value pairs**.

```python
employee = {
    "id": 101,
    "name": "John",
    "salary": 100000
}
```

---

# Characteristics

| Feature | Dictionary |
|----------|------------|
| Mutable | ✅ Yes |
| Ordered (Python 3.7+) | ✅ Yes |
| Duplicate Keys | ❌ No |
| Duplicate Values | ✅ Yes |
| Indexed | ❌ No |
| Lookup | O(1) Average |

---

# Creating Dictionaries

```python
employee = {
    "id": 101,
    "name": "John"
}
```

Empty dictionary

```python
employee = {}

# or

employee = dict()
```

---

# CRUD Operations

## Create

```python
employee["department"] = "Engineering"
```

---

## Read

```python
employee["name"]
```

Safe Read

```python
employee.get("name")
```

Default Value

```python
employee.get("country", "Unknown")
```

---

## Update

```python
employee["salary"] = 120000
```

---

## Delete

```python
del employee["salary"]
```

or

```python
employee.pop("salary")
```

---

# Common Methods

| Method | Purpose |
|---------|----------|
| get() | Safe lookup |
| keys() | All keys |
| values() | All values |
| items() | Key-value pairs |
| pop() | Remove key |
| update() | Merge dictionaries |
| copy() | Shallow copy |
| clear() | Remove everything |

---

# Iteration

Keys

```python
for key in employee:
    print(key)
```

Values

```python
for value in employee.values():
    print(value)
```

Keys + Values

```python
for key, value in employee.items():
    print(key, value)
```

---

# Membership Testing

Checks **keys**, not values.

```python
"name" in employee
```

✅ True

```python
"John" in employee
```

❌ False

---

# Nested Dictionary

```python
customer = {
    "address": {
        "city": "Toronto"
    }
}
```

Access

```python
customer["address"]["city"]
```

Safe Access

```python
customer.get("address", {}).get("city")
```

---

# Dictionary Comprehension

```python
squares = {
    x: x ** 2
    for x in range(1, 6)
}
```

Output

```python
{
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}
```

---

# Time Complexity

| Operation | Complexity |
|------------|------------|
| Lookup | O(1) |
| Insert | O(1) |
| Update | O(1) |
| Delete | O(1) |
| Iterate | O(n) |

---

# Frequency Counting Pattern ⭐

Most common interview question.

```python
counts = {}

for country in countries:

    counts[country] = counts.get(country, 0) + 1
```

Remember this pattern.

---

# Nested JSON Pattern ⭐

```python
customer.get("address", {}) \
        .get("country", {}) \
        .get("code")
```

Avoids `KeyError`.

---

# ETL Metadata Pattern ⭐

```python
metadata = {
    "rows_processed": 100000,
    "rows_failed": 25,
    "execution_time": 32,
    "pipeline": "Customer ETL"
}
```

---

# Configuration Pattern ⭐

```python
config = {
    "database": "Snowflake",
    "warehouse": "COMPUTE_WH",
    "batch_size": 5000
}
```

---

# Dictionary vs Other Collections

| Collection | Best For |
|------------|----------|
| List | Ordered sequence |
| Tuple | Immutable data |
| Set | Unique values |
| Dictionary | Key-value mapping |

---

# Dictionary in Data Engineering

One Dictionary usually represents:

- One customer
- One employee
- One API response
- One JSON document
- One ETL record
- One configuration object
- One event message

---

# Relationship with Other Technologies

## JSON

```python
customer["country"]
```

↓

```json
{
  "country": "Canada"
}
```

---

## Pandas

```python
df.to_dict()

pd.DataFrame(records)
```

---

## PySpark

```python
row.asDict()
```

---

## AWS Lambda

```python
event["Records"]
```

---

## SQL

```sql
SELECT country
FROM customers;
```

Equivalent Python

```python
customer["country"]
```

---

# Production Tips

✅ Use `get()` for optional fields.

✅ Validate required fields.

✅ Never trust API input.

✅ Keep metadata in dictionaries.

✅ Avoid modifying dictionaries while iterating.

✅ Use `.copy()` when you need an independent dictionary.

---

# Common Mistakes

❌ Using `[]` for optional fields.

❌ Assuming `"John" in employee` checks values.

❌ Duplicate keys overwrite previous values.

❌ Using mutable objects as keys.

❌ Forgetting `.get()` can return `None`.

❌ Modifying a dictionary while iterating.

---

# Interview Favourites ⭐

Be ready to answer:

- Difference between `get()` and `[]`
- Why are lookups O(1)?
- What is hashing?
- Why must keys be hashable?
- Difference between `keys()`, `values()`, and `items()`
- Dictionary Comprehensions
- Frequency counting
- Nested JSON processing
- ETL metadata
- Configuration dictionaries

---

# 30-Second Revision

- Dictionary = Key → Value mapping
- Mutable
- Ordered (Python 3.7+)
- Keys must be hashable
- Lookup = O(1)
- Use `get()` for optional fields
- `items()` → Iterate key and value
- Frequency counting = `dict.get(key, 0) + 1`
- One Dictionary often represents one business record
- JSON ↔ Dictionary
- `row.asDict()` in PySpark
- `event["Records"]` in AWS Lambda

---

# Ready for the Next Topic?

Before moving on, make sure you can answer **YES** to all of these:

- ✅ I know when to use a Dictionary.
- ✅ I can perform CRUD operations.
- ✅ I know the difference between `get()` and `[]`.
- ✅ I can iterate using `items()`.
- ✅ I can process nested dictionaries.
- ✅ I can build a frequency counter.
- ✅ I understand how Dictionaries relate to JSON.
- ✅ I understand where Dictionaries appear in Pandas and PySpark.
- ✅ I know common production pitfalls.
- ✅ I can confidently explain Dictionaries in an interview.
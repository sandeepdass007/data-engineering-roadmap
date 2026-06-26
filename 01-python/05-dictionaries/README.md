# Topic 5 - Dictionaries

## Learning Objectives

After completing this topic, you should be able to:

- Understand what a Dictionary is and how it differs from other Python collections.
- Perform CRUD (Create, Read, Update, Delete) operations on dictionaries.
- Safely access dictionary values using `get()`.
- Iterate through keys, values, and key-value pairs efficiently.
- Work with nested dictionaries and JSON-like structures.
- Use dictionary comprehensions.
- Solve real-world Data Engineering problems using dictionaries.
- Understand how dictionaries relate to JSON, Pandas, PySpark, SQL, and AWS.

---

# Why Dictionaries Exist

Imagine storing an employee's information in a List.

```python
employee = [1001, "John", "Toronto", 100000]
```

Accessing the salary:

```python
employee[3]
```

Although it works, it is not very readable.

Now compare it with a Dictionary:

```python
employee = {
    "id": 1001,
    "name": "John",
    "city": "Toronto",
    "salary": 100000
}

print(employee["salary"])
```

The intent is immediately clear.

This readability is one of the main reasons dictionaries are heavily used in production systems.

---

# What is a Dictionary?

A Dictionary is a mutable collection of **key-value pairs**.

Each key uniquely identifies a value.

Example:

```python
employee = {
    "id": 1001,
    "name": "John",
    "salary": 100000
}
```

Here:

| Key | Value |
|------|-------|
| id | 1001 |
| name | John |
| salary | 100000 |

---

# Dictionary Characteristics

| Feature | Dictionary |
|----------|------------|
| Ordered (Python 3.7+) | ✅ Yes |
| Mutable | ✅ Yes |
| Duplicate Keys | ❌ Not Allowed |
| Duplicate Values | ✅ Allowed |
| Indexed | ❌ No |
| Key Lookup | O(1) Average |

---

# Internal Working

Python dictionaries are implemented using **Hash Tables**.

When a key is inserted:

1. Python computes the hash of the key.
2. The hash determines where the value is stored.
3. Future lookups use the same hash.

Because of hashing, dictionary lookups are typically **O(1)**.

Example:

```python
employee["salary"]
```

Python does **not** scan every key one by one.

Instead, it directly computes the hash and retrieves the value.

---

# Creating Dictionaries

## Standard

```python
employee = {
    "id": 1001,
    "name": "John"
}
```

## Empty Dictionary

```python
employee = {}
```

or

```python
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

# Safe Access Using get()

Suppose an API sometimes omits the field:

```python
"middle_name"
```

This fails:

```python
customer["middle_name"]
```

Output:

```
KeyError
```

Safer approach:

```python
customer.get("middle_name")
```

Returns:

```
None
```

You can also specify a default:

```python
customer.get("country", "Unknown")
```

---

# Common Dictionary Methods

| Method | Purpose |
|---------|----------|
| get() | Safe lookup |
| keys() | Returns keys |
| values() | Returns values |
| items() | Returns key-value pairs |
| pop() | Remove and return value |
| update() | Merge dictionaries |
| clear() | Remove all entries |
| copy() | Shallow copy |

---

# Iterating Through Dictionaries

Keys:

```python
for key in employee:
    print(key)
```

Values:

```python
for value in employee.values():
    print(value)
```

Keys and Values:

```python
for key, value in employee.items():
    print(key, value)
```

This is the most common iteration pattern in production code.

---

# Nested Dictionaries

Example:

```python
customer = {
    "id": 101,
    "address": {
        "city": "Toronto",
        "country": "Canada"
    }
}
```

Access:

```python
customer["address"]["city"]
```

Output:

```
Toronto
```

Nested dictionaries commonly represent JSON documents.

---

# Dictionary Comprehension

Example:

```python
squares = {
    number: number ** 2
    for number in range(1, 6)
}
```

Output:

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

# Dictionaries in Data Engineering

## API Responses

```python
response = {
    "customer_id": 101,
    "country": "Canada"
}
```

---

## Configuration Files

```python
config = {
    "database": "Snowflake",
    "warehouse": "COMPUTE_WH"
}
```

---

## ETL Metadata

```python
metadata = {
    "rows_processed": 100000,
    "rows_failed": 15
}
```

---

## Frequency Counting

```python
country_count = {
    "Canada": 500,
    "USA": 300
}
```

---

## Validation

```python
required_fields = [
    "customer_id",
    "country"
]
```

Check:

```python
if "country" not in record:
    ...
```

---

# Relationship with JSON

JSON:

```json
{
    "customer_id":101,
    "country":"Canada"
}
```

Python:

```python
{
    "customer_id":101,
    "country":"Canada"
}
```

Most REST APIs return JSON, which maps directly to Python dictionaries.

---

# Relationship with Pandas

Convert DataFrame to dictionary:

```python
df.to_dict()
```

Create DataFrame from dictionaries:

```python
pd.DataFrame(records)
```

---

# Relationship with PySpark

Spark Row:

```python
row.asDict()
```

Spark DataFrame rows conceptually behave like dictionaries.

---

# Relationship with SQL

Dictionary:

```python
employee["salary"]
```

Equivalent SQL:

```sql
SELECT salary
FROM employee;
```

---

# Relationship with AWS

AWS Lambda receives events as dictionaries.

Example:

```python
def lambda_handler(event, context):

    bucket = event["Records"][0]["s3"]["bucket"]["name"]
```

Understanding dictionaries is essential for AWS serverless development.

---

# Production Notes

### Prefer get() for Optional Fields

APIs evolve over time.

Using `get()` makes your code resilient to missing fields.

---

### Avoid Mutating While Iterating

Bad:

```python
for key in employee:
    del employee[key]
```

Good:

```python
for key in list(employee.keys()):
    del employee[key]
```

---

### Validate Required Fields

Always validate incoming API payloads before processing.

---

### Keep Metadata in Dictionaries

Instead of many variables:

```python
rows_processed
rows_failed
execution_time
```

Use:

```python
metadata = {
    ...
}
```

Cleaner and easier to extend.

---

# Common Mistakes

❌ Assuming membership checks values.

```python
"John" in employee
```

Actually checks keys.

---

❌ Forgetting duplicate keys overwrite previous values.

```python
{
    "name":"John",
    "name":"Mike"
}
```

Result:

```python
{"name":"Mike"}
```

---

❌ Using `[]` for optional API fields.

Prefer:

```python
get()
```

---

# Interview Tips

Expect questions such as:

- Difference between `get()` and `[]`.
- Difference between `keys()`, `values()`, and `items()`.
- Why are dictionary lookups fast?
- Explain hashing.
- How would you count frequencies?
- How would you process nested JSON?

---

# Where You'll Use This Later

Python

↓

JSON APIs

↓

AWS Lambda Events

↓

Pandas DataFrames

↓

PySpark Rows

↓

Kafka Messages

↓

ETL Metadata

↓

Production Data Pipelines

---

# Summary

You should now be comfortable with:

- Creating dictionaries
- CRUD operations
- Safe lookups
- Dictionary methods
- Nested dictionaries
- Dictionary comprehensions
- Frequency counting
- JSON processing
- ETL metadata
- Production best practices

These concepts form the foundation for processing structured data in Data Engineering.

---

# Before Moving On

You are ready for the next topic if you can confidently:

- Explain what a Dictionary is.
- Use `get()` appropriately.
- Iterate using `items()`.
- Process nested dictionaries.
- Build frequency counters.
- Read JSON-like structures.
- Explain how dictionaries relate to Data Engineering.
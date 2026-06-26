# Production Notes - Python Dictionaries

## Purpose

This document covers how Dictionaries are used in real-world Data Engineering projects. While the README explains *what* Dictionaries are, this guide focuses on *how experienced engineers use them in production*.

---

# 1. Prefer `get()` for Optional Fields

## ❌ Bad

```python
customer_name = customer["middle_name"]
```

If `middle_name` is missing, Python raises:

```
KeyError
```

Your ETL pipeline may fail.

---

## ✅ Good

```python
customer_name = customer.get("middle_name")
```

Returns:

```python
None
```

The pipeline continues processing.

---

## Even Better

Provide a default value.

```python
customer_name = customer.get("middle_name", "")
```

---

# 2. Validate Required Fields Before Processing

Never assume incoming data is complete.

## Example

Instead of:

```python
customer_id = record["customer_id"]
country = record["country"]
```

Validate first.

```python
required_fields = [
    "customer_id",
    "country"
]

for field in required_fields:
    if field not in record:
        raise ValueError(f"Missing required field: {field}")
```

---

# 3. Handle Schema Evolution

APIs evolve over time.

Today's payload:

```json
{
    "id":101,
    "name":"John"
}
```

Tomorrow:

```json
{
    "id":101,
    "name":"John",
    "email":"john@gmail.com"
}
```

Well-designed ETL pipelines continue working even when new fields appear.

Avoid hardcoding assumptions about every field.

---

# 4. Avoid Mutating Dictionaries While Iterating

## ❌ Bad

```python
for key in employee:
    del employee[key]
```

Runtime Error.

---

## ✅ Good

```python
for key in list(employee.keys()):
    del employee[key]
```

---

# 5. Store ETL Metadata in Dictionaries

Instead of creating many variables:

```python
rows_processed
rows_failed
execution_time
pipeline_name
```

Group related information together.

```python
metadata = {
    "rows_processed": 100000,
    "rows_failed": 15,
    "execution_time_seconds": 25,
    "pipeline_name": "customer_ingestion"
}
```

Advantages:

- Cleaner code
- Easier logging
- Easier serialization
- Easier monitoring

---

# 6. Frequency Counting

A very common ETL task.

Example:

Count customers by country.

```python
country_count = {}

for customer in customers:
    country = customer["country"]

    country_count[country] = (
        country_count.get(country, 0) + 1
    )
```

Output:

```python
{
    "Canada":520,
    "USA":430,
    "India":190
}
```

This pattern appears frequently in interviews.

---

# 7. Process JSON Instead of Individual Variables

Instead of writing:

```python
customer_id = ...
customer_name = ...
customer_country = ...
customer_email = ...
```

Pass the entire Dictionary through the pipeline.

```python
process_customer(customer)
```

This makes the code more reusable and easier to extend.

---

# 8. Avoid Deeply Nested Access Without Validation

## Risky

```python
customer["address"]["country"]["code"]
```

One missing field causes the pipeline to fail.

---

Safer approach:

```python
address = customer.get("address", {})
country = address.get("country", {})
code = country.get("code")
```

---

# 9. Log Dictionaries as JSON

Instead of:

```python
print(customer)
```

Use structured logging.

Example:

```python
logger.info(customer)
```

or

```python
json.dumps(customer)
```

Structured logs are much easier to search in production systems.

---

# 10. Keep Configuration in Dictionaries

Configuration should not be scattered.

Good:

```python
config = {
    "database":"Snowflake",
    "warehouse":"COMPUTE_WH",
    "schema":"CUSTOMER",
    "batch_size":10000
}
```

---

# 11. Be Careful with Mutable References

Example:

```python
config = {
    "retries":3
}

new_config = config

new_config["retries"] = 5
```

Now:

```python
config["retries"]
```

is also:

```python
5
```

Both variables reference the same Dictionary.

Use:

```python
new_config = config.copy()
```

when appropriate.

---

# 12. Don't Assume Key Order

Although Python 3.7+ preserves insertion order, production logic should never depend on dictionary ordering unless there is a clear business requirement.

Always access data using keys rather than positions.

---

# 13. Think in Terms of Records

A Data Engineer rarely thinks:

> "I have a Dictionary."

Instead, think:

> "I have one customer record."

Example:

```python
customer = {
    "customer_id":101,
    "country":"Canada",
    "email":"abc@gmail.com"
}
```

One Dictionary usually represents one business entity or one record.

---

# 14. Relationship with Pandas

A DataFrame row is conceptually similar to a Dictionary.

```python
{
    "customer_id":101,
    "country":"Canada"
}
```

↓

```python
df.iloc[0]
```

↓

```python
df.to_dict()
```

---

# 15. Relationship with PySpark

A Spark Row can be converted into a Dictionary.

```python
row.asDict()
```

This makes it easy to work with JSON APIs and structured records.

---

# 16. Relationship with AWS Lambda

AWS Lambda events are Dictionaries.

Example:

```python
def lambda_handler(event, context):

    bucket = event["Records"][0]["s3"]["bucket"]["name"]
```

Every AWS Data Engineer works with nested Dictionaries regularly.

---

# 17. Production Checklist

Before deploying code that processes Dictionaries, ask yourself:

- ✅ Am I using `get()` for optional fields?
- ✅ Have I validated required fields?
- ✅ Will my code survive schema evolution?
- ✅ Am I avoiding unnecessary KeyErrors?
- ✅ Am I logging useful metadata?
- ✅ Have I avoided mutating Dictionaries while iterating?
- ✅ Is the code easy to extend when new fields are added?

If the answer to all of these is **Yes**, your code is much closer to production quality.
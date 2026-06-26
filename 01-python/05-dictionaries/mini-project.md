# Mini Project - Customer API Processing Pipeline

## Objective

Build a small ETL pipeline that processes customer records received from an API.

This project simulates a common Data Engineering task where an API returns JSON data that must be validated, analyzed, and summarized before loading into a data warehouse.

---

# Business Scenario

A Customer Management API returns a list of customer records.

Before loading the data into your warehouse, you must:

* Validate mandatory fields
* Handle optional fields safely
* Detect duplicate customer IDs
* Generate processing statistics
* Produce a reconciliation report

---

# Input Data

```python
customers = [
    {
        "customer_id": 101,
        "name": "John",
        "country": "Canada",
        "balance": 1200,
        "active": True
    },
    {
        "customer_id": 102,
        "name": "Alice",
        "country": "USA",
        "balance": 850,
        "active": False
    },
    {
        "customer_id": 103,
        "name": "Mike",
        "country": "Canada",
        "balance": 3000,
        "active": True
    },
    {
        "customer_id": 101,
        "name": "John",
        "country": "Canada",
        "balance": 1200,
        "active": True
    },
    {
        "customer_id": 104,
        "name": "Sara",
        "balance": 500,
        "active": True
    },
    {
        "customer_id": 105,
        "name": "David",
        "country": "India",
        "active": True
    }
]
```

Notice carefully:

* Customer ID **101** appears twice.
* One customer is missing the **country** field.
* One customer is missing the **balance** field.

This is intentional.

---

# Task 1 - Print Every Customer

Print every customer record neatly.

Example:

```text
Customer ID : 101
Name        : John
Country     : Canada
Balance     : 1200
Active      : True
----------------------------------------
```

Use `get()` for optional fields.

---

# Task 2 - Validate Required Fields

Required fields:

```python
required_fields = [
    "customer_id",
    "name",
    "country",
    "balance",
    "active"
]
```

Print all missing fields.

Example:

```text
Customer 104
Missing:
country
```

Do not stop processing after finding one missing field.

---

# Task 3 - Count Customers by Country

Create a dictionary like:

```python
{
    "Canada": 3,
    "USA": 1,
    "India": 1
}
```

For customers with no country, count them under:

```text
Unknown
```

Expected output:

```python
{
    "Canada": 3,
    "USA": 1,
    "India": 1,
    "Unknown": 1
}
```

Use `get()` while counting.

---

# Task 4 - Count Active vs Inactive Customers

Generate:

```python
{
    True: 5,
    False: 1
}
```

---

# Task 5 - Average Balance

Calculate the average balance.

If a customer has no balance:

* Treat it as zero.
* Continue processing.

Print:

```text
Average Balance : XXXX
```

---

# Task 6 - Detect Duplicate Customer IDs

Print:

```python
{
    101
}
```

Use a Set for duplicate detection.

---

# Task 7 - Create Processing Metadata

Create a dictionary named:

```python
processing_metadata
```

Expected structure:

```python
{
    "total_records": 6,
    "valid_records": ?,
    "invalid_records": ?,
    "duplicate_records": ?,
    "countries_found": ?,
    "average_balance": ?
}
```

You decide how to calculate these values.

Think like a Data Engineer.

---

# Task 8 - Function

Create:

```python
def process_customers(customers):
```

Return:

```python
(
    country_counts,
    duplicate_ids,
    processing_metadata
)
```

Use a tuple return value.

---

# Task 9 - Final Report

Produce a report like:

```text
==========================================
CUSTOMER API PROCESSING REPORT
==========================================

Total Records       : 6
Valid Records       : 4
Invalid Records     : 2
Duplicate IDs       : {101}

Country Counts

Canada : 3
USA     : 1
India   : 1
Unknown : 1

Average Balance : 1125

==========================================
```

Formatting doesn't have to match exactly, but it should be clean and readable.

---

# Stretch Goal

Suppose tomorrow the API adds a new field:

```python
"email"
```

or removes the field:

```python
"balance"
```

Answer:

1. Which parts of your code continue to work without changes?
2. Which parts require modification?
3. Why is `dict.get()` valuable for evolving APIs?

Write your answers in:

```text
stretch-goal.md
```

No code is required.

---

# Production Thinking

Imagine this API returns **20 million customers** instead of 6.

Answer the following in a separate file named `production-notes.md`:

1. Would storing all records in a Python list still be appropriate?
2. How might you process the data differently?
3. Which parts of this project could later be replaced by Pandas?
4. Which parts would eventually become PySpark transformations?
5. Which metrics would you expose to monitoring tools such as CloudWatch or Datadog?

Do not worry if you cannot answer everything today. We'll revisit these questions throughout the roadmap.

---

# Learning Outcomes

After completing this project, you should understand:

* Dictionary CRUD operations
* Safe access with `get()`
* Nested data processing
* Frequency counting
* Data validation
* Duplicate detection
* Metadata generation
* Function design
* ETL-style reporting
* Defensive programming for evolving APIs
* Thinking beyond syntax toward production-ready Data Engineering

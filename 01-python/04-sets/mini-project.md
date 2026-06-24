# Mini Project - ETL Data Reconciliation Engine

## Objective

Build a small ETL reconciliation utility using Sets.

This project simulates a common Data Engineering task:

* Compare source and target datasets
* Detect missing records
* Identify duplicate records
* Validate country values
* Generate reconciliation metrics

---

# Business Scenario

A nightly ETL pipeline loads customer records from a source system into a target data warehouse.

The business wants to verify:

1. Which records were not loaded?
2. Which records are common in both systems?
3. Which customer IDs are duplicated in the source file?
4. Are there any invalid country values?
5. What is the reconciliation summary?

---

# Dataset

## Source Customer IDs

```python
source_customer_ids = [
    101,
    102,
    103,
    104,
    105,
    105,
    106,
    106,
    107
]
```

Notice:

```text
105 appears twice
106 appears twice
```

---

## Target Customer IDs

```python
target_customer_ids = [
    101,
    102,
    103,
    107
]
```

---

## Incoming Countries

```python
incoming_countries = [
    "Canada",
    "USA",
    "India",
    "Mars",
    "Canada",
    "Jupiter"
]
```

---

## Valid Countries

```python
valid_countries = {
    "Canada",
    "USA",
    "India"
}
```

---

# Task 1 - Remove Duplicates

Convert the source customer list into a set.

Print:

```text
Unique Customer IDs
```

Expected result:

```python
{101, 102, 103, 104, 105, 106, 107}
```

---

# Task 2 - Find Duplicate Customer IDs

Find which IDs appeared more than once in the source list.

Expected:

```python
{105, 106}
```

Hint:

You may use:

```python
count()
```

or another approach.

---

# Task 3 - Missing Records

Find records present in Source but missing in Target.

Expected:

```python
{104, 105, 106}
```

Use:

```python
source_set - target_set
```

---

# Task 4 - Successfully Loaded Records

Find records present in both systems.

Expected:

```python
{101, 102, 103, 107}
```

Use:

```python
source_set & target_set
```

---

# Task 5 - Invalid Countries

Find invalid country values.

Expected:

```python
{"Mars", "Jupiter"}
```

Convert incoming countries into a set first.

Use:

```python
incoming_country_set - valid_countries
```

---

# Task 6 - Reconciliation Summary Function

Create a function:

```python
def generate_reconciliation_summary(
    source_ids,
    target_ids
):
```

Return:

```python
(
    total_source_records,
    total_target_records,
    missing_record_count
)
```

Example:

```python
(
    7,
    4,
    3
)
```

Use tuple return values.

---

# Task 7 - Stretch Goal

Create a report like:

```text
================================
ETL RECONCILIATION REPORT
================================

Total Source Records : 7
Total Target Records : 4

Missing Records:
{104, 105, 106}

Duplicate IDs:
{105, 106}

Invalid Countries:
{'Mars', 'Jupiter'}

================================
```

---

# Learning Outcomes

After completing this project you should understand:

* Set creation
* Deduplication
* Membership testing
* Difference operations
* Intersection operations
* Data validation
* Reconciliation logic
* Combining Sets and Tuples
* Real-world ETL quality checks

---

# Bonus Challenge (Senior Data Engineer Thinking)

Suppose:

```python
source_ids = 50 million records
target_ids = 48 million records
```

Answer:

1. Why are Sets useful here?
2. What memory concerns might arise?
3. Would this approach still work in Spark?
4. How would Spark solve this problem differently?

Write your answers in a separate section called:

```text
bonus_analysis.md
```

You do not need code for this section.

# Python Sets

## Overview

A Set is an unordered collection of unique elements.

Sets are one of the most useful Python data structures for Data Engineers because they provide:

- Automatic deduplication
- Fast membership testing
- Efficient comparisons
- Data validation capabilities
- Reconciliation operations

---

# Characteristics

## Unique Values

```python
numbers = {1, 2, 2, 3}

print(numbers)
```

Output:

```python
{1, 2, 3}
```

Duplicates are removed automatically.

---

## Unordered

Sets do not guarantee ordering.

```python
employees = {
    "John",
    "Mike",
    "Alice"
}
```

Do not rely on element positions.

---

## Mutable

Sets can be modified.

```python
employees.add("David")
employees.remove("Mike")
```

---

# Creating Sets

## Standard Set

```python
employees = {
    "John",
    "Mike",
    "Alice"
}
```

## Empty Set

```python
employees = set()
```

### Important

```python
{}
```

creates a dictionary, not a set.

---

# Common Operations

## Add

```python
employees.add("David")
```

## Remove

```python
employees.remove("David")
```

Raises:

```text
KeyError
```

if value does not exist.

---

## Discard

```python
employees.discard("David")
```

No error if value does not exist.

---

# Membership Testing

```python
"John" in employees
```

Average complexity:

```text
O(1)
```

---

# Set Operations

## Union

```python
a | b
```

Combine all unique values.

---

## Intersection

```python
a & b
```

Common values only.

---

## Difference

```python
a - b
```

Values present in first set but not second.

---

## Symmetric Difference

```python
a ^ b
```

Values present in only one set.

---

# Hashability

Set elements must be hashable.

Works:

```python
{
    "Canada",
    "USA"
}
```

Fails:

```python
{
    [1, 2]
}
```

Reason:

```text
Lists are mutable and therefore unhashable.
```

---

# Frozensets

Immutable version of a Set.

```python
countries = frozenset(
    ["Canada", "USA"]
)
```

Cannot be modified.

---

# Set Comprehension

```python
squares = {
    n * n
    for n in [1, 2, 3]
}
```

Output:

```python
{1, 4, 9}
```

---

# Data Engineering Use Cases

## Deduplication

```python
unique_ids = set(customer_ids)
```

---

## Data Validation

```python
if country in valid_countries:
```

---

## Detect Invalid Values

```python
invalid_countries = (
    incoming_countries
    - valid_countries
)
```

---

## ETL Reconciliation

```python
missing_records = (
    source_ids
    - target_ids
)
```

---

## Processed File Tracking

```python
processed_files = {
    "customers_20260101.csv"
}
```

---

# Complexity

| Operation | Complexity |
|------------|------------|
| Lookup | O(1) |
| Add | O(1) |
| Remove | O(1) |
| Union | O(n) |
| Intersection | O(min(n,m)) |

---

# Production Considerations

Sets are excellent for:

- Millions of records
- Fast lookups
- Deduplication

But can become memory-intensive for:

- Hundreds of millions of records
- Billions of records

At that scale, distributed frameworks such as PySpark become necessary.

---

# PySpark Connection

Python Set Difference:

```python
source_set - target_set
```

Equivalent Spark Pattern:

```python
source_df.join(
    target_df,
    on="id",
    how="left_anti"
)
```

This is one of the most important conceptual bridges between Python and Spark.

---

# Summary

After completing this topic you should understand:

- Set creation
- Deduplication
- Membership testing
- Union
- Intersection
- Difference
- Symmetric Difference
- Hashability
- Frozensets
- Set Comprehensions
- Data Validation
- ETL Reconciliation
- Distributed Processing Considerations

Sets are one of the most practically useful Python structures for Data Engineering and appear frequently in data quality and reconciliation workflows.
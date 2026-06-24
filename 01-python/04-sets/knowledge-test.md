# Topic 4 - Sets Knowledge Test

## Instructions

- Do not execute the code.
- Predict the output first.
- Explain WHY.
- Think from a Data Engineering perspective whenever possible.

---

# Section A - Fundamentals

## Q1

What is a Set?

List its three most important characteristics.

---

## Q2

What is the output?

```python
numbers = {1, 2, 2, 3, 3}

print(numbers)
```

---

## Q3

What is the datatype?

```python
data = {}
```

---

## Q4

How do you create an empty Set?

---

## Q5

Why does Python automatically remove duplicates from a Set?

---

# Section B - Adding and Removing Values

## Q6

What is the output?

```python
employees = {"John", "Mike"}

employees.add("John")

print(employees)
```

---

## Q7

Difference between:

```python
remove()
```

and

```python
discard()
```

---

## Q8

What happens?

```python
employees = {"John"}

employees.remove("Mike")
```

---

## Q9

What happens?

```python
employees = {"John"}

employees.discard("Mike")
```

---

# Section C - Membership Testing

## Q10

What is the output?

```python
countries = {
    "Canada",
    "USA",
    "India"
}

print("Canada" in countries)
```

---

## Q11

Why is membership testing usually faster in a Set than in a List?

Explain using Big-O notation.

---

# Section D - Set Operations

## Q12

What is the output?

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
```

---

## Q13

What operation is represented by:

```python
a & b
```

---

## Q14

What is the output?

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a & b)
```

---

## Q15

What is the output?

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a - b)
```

---

## Q16

What is the output?

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a ^ b)
```

---

## Q17

Explain the difference between:

```python
a - b
```

and

```python
a ^ b
```

---

# Section E - Data Engineering Scenarios

## Q18

You have:

```python
source_ids = {
    1,
    2,
    3,
    4,
    5
}

target_ids = {
    1,
    2,
    3
}
```

Write the operation that finds records missing from Target.

---

## Q19

What is the output?

```python
source_ids = {
    1,
    2,
    3,
    4,
    5
}

target_ids = {
    3,
    4,
    5,
    6
}

print(source_ids & target_ids)
```

---

## Q20

Why are Sets commonly used for deduplication?

---

## Q21

You receive:

```python
customer_ids = [
    101,
    102,
    101,
    103,
    102
]
```

Write one line of Python that removes duplicates.

---

## Q22

You have:

```python
incoming_countries = {
    "Canada",
    "USA",
    "Mars"
}

valid_countries = {
    "Canada",
    "USA",
    "India"
}
```

Write the operation that identifies invalid countries.

---

# Section F - Hashability

## Q23

Why does this work?

```python
countries = {
    "Canada",
    "USA"
}
```

---

## Q24

Why does this fail?

```python
bad_set = {
    [1, 2]
}
```

---

## Q25

What does "hashable" mean?

---

# Section G - Frozensets

## Q26

What is a frozenset?

---

## Q27

When would you choose a frozenset instead of a normal set?

Provide at least two examples.

---

## Q28

What happens?

```python
countries = frozenset(
    ["Canada", "USA"]
)

countries.add("India")
```

---

# Section H - Production Thinking

## Q29

Suppose:

```text
source_ids = 50 million records
target_ids = 48 million records
```

Why might using Python Sets become problematic?

---

## Q30

How would a distributed framework like PySpark solve large-scale reconciliation differently?

---

# Section I - Advanced

## Q31

What is Set Comprehension?

---

## Q32

What is the output?

```python
numbers = [1, 2, 2, 3]

result = {
    n * n
    for n in numbers
}

print(result)
```

---

## Q33

Explain why Set Comprehension can be useful in ETL pipelines.

---

# Self Evaluation Checklist

You should be comfortable with:

- Set creation
- Empty sets
- Deduplication
- Membership testing
- add()
- remove()
- discard()
- Union
- Intersection
- Difference
- Symmetric Difference
- Subset
- Superset
- Hashability
- Frozensets
- Set Comprehensions
- ETL Reconciliation Patterns
- Data Validation Patterns

before moving to Topic 5.
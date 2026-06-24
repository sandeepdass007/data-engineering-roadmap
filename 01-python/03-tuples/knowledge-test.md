# Topic 3 - Tuples Knowledge Test

## Instructions

* Do not run the code.
* Answer based on reasoning.
* Explain the "why", not just the output.
* Think from a Data Engineering perspective whenever applicable.

---

# Section A - Fundamentals

## Q1

What is the primary difference between a List and a Tuple?

When would you choose one over the other?

---

## Q2

What is the output?

```python
employee = ("John", 100000)

print(employee[1])
```

---

## Q3

What happens here?

```python
employee = ("John", 100000)

employee[0] = "Mike"
```

Explain why.

---

## Q4

What is the datatype?

```python
employee = ("John")
```

---

## Q5

What is the datatype?

```python
employee = ("John",)
```

Explain why the result differs from Q4.

---

# Section B - Tuple Packing & Unpacking

## Q6

What is tuple packing?

Give an example.

---

## Q7

What is the output?

```python
employee = ("John", 100000)

name, salary = employee

print(name)
```

---

## Q8

What happens here?

```python
employee = ("John", 100000)

name, salary, city = employee
```

Will it work? Why or why not?

---

## Q9

What is the output?

```python
a = 10
b = 20

a, b = b, a

print(a, b)
```

Explain what Python is doing behind the scenes.

---

# Section C - Functions & ETL Usage

## Q10

What does this function actually return?

```python
def get_metrics():
    return 1000, 25
```

---

## Q11

What is the output?

```python
def get_metrics():
    return 1000, 25

processed, failed = get_metrics()

print(failed)
```

---

## Q12

Why are tuples commonly used when returning multiple values from a function?

---

# Section D - Production Thinking

## Q13

You have a configuration:

```python
DATABASE_CONFIG = (
    "prod-server",
    5432,
    "finance_db"
)
```

Why might a tuple be a better choice than a list?

---

## Q14

Consider:

```python
employees = (
    "John",
    "Mike"
)
```

Your application needs to:

* add employees
* remove employees
* reorder employees

Would you use a tuple or a list? Why?

---

## Q15

You receive database results like:

```python
rows = [
    (1, "John", 100000),
    (2, "Mike", 120000)
]
```

How does tuple unpacking make processing these records easier compared to using indexes?

---

# Section E - Advanced

## Q16

What is the output?

```python
record = ("John", "Toronto", "Canada", 100000)

name, *location, salary = record

print(location)
```

---

## Q17

What does the `*location` variable capture?

---

## Q18

Why are tuples generally more memory efficient than lists?

(Interview-level explanation only.)

---

## Q19

Name three real-world Data Engineering scenarios where tuples are useful.

---

## Q20

You are designing an ETL framework.

A function returns:

```python
(job_name, rows_processed, rows_failed)
```

Why might returning a tuple be preferable to returning a list?

---

# Self-Evaluation

You should be comfortable with:

* Tuple creation
* Immutability
* Packing
* Unpacking
* Function return values
* Tuple iteration
* Lists of tuples
* ETL use cases
* Production design choices

before moving to the next topic.

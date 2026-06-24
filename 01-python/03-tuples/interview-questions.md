# Python Tuples - Interview Questions

## Junior Level

### Q1

What is a Tuple?

---

### Q2

What is the difference between a List and a Tuple?

---

### Q3

Why are tuples immutable?

---

### Q4

What is the output?

```python
employee = ("John", 100000)

print(employee[0])
```

---

### Q5

What is the output?

```python
employee = ("John")
```

What is its datatype?

---

### Q6

How do you create a single-element tuple?

---

### Q7

What is tuple packing?

---

### Q8

What is tuple unpacking?

---

### Q9

What happens when the number of variables does not match the number of tuple values during unpacking?

---

### Q10

What methods are commonly available on tuples?

---

# Mid-Level

### Q11

Why are tuples commonly used when returning multiple values from functions?

---

### Q12

What is the output?

```python
a = 10
b = 20

a, b = b, a
```

Explain what happens internally.

---

### Q13

What is star unpacking?

Provide an example.

---

### Q14

What is the output?

```python
record = (
    "John",
    "Toronto",
    "Canada",
    100000
)

name, *location, salary = record
```

---

### Q15

What are some Data Engineering use cases for tuples?

---

# Senior Level

### Q16

What does it mean for an object to be hashable?

---

### Q17

Why can tuples be used as dictionary keys while lists cannot?

---

### Q18

Will the following work?

```python
{
    ("Canada", [2024]): 100
}
```

Why or why not?

---

### Q19

What are composite keys and how can tuples help implement them?

---

### Q20

When would you choose a named tuple over a regular tuple?

---

### Q21

What advantages do named tuples provide?

---

### Q22

When would a dataclass be preferable to a named tuple?

---

### Q23

Design a return structure for an ETL job that needs to return:

* rows processed
* rows failed
* execution time

Why would a tuple be a suitable choice?

---

### Q24

How would you explain tuple immutability to a junior developer?

---

### Q25

What are common production bugs related to tuple unpacking?

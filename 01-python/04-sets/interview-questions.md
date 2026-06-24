# Python Sets - Interview Questions

## Junior Level

### Q1
What is a Set in Python?

### Q2
How is a Set different from a List?

### Q3
Can Sets contain duplicate values?

### Q4
Are Sets ordered?

### Q5
How do you create an empty Set?

### Q6
Why does `{}` create a dictionary instead of a Set?

### Q7
What is the difference between:

```python
remove()
```

and

```python
discard()
```

### Q8
What is the output?

```python
numbers = {1, 2, 2, 3}

print(numbers)
```

### Q9
How do you check if an element exists in a Set?

### Q10
Why is membership testing fast in Sets?

---

## Mid-Level

### Q11
Explain:

```python
a | b
```

### Q12
Explain:

```python
a & b
```

### Q13
Explain:

```python
a - b
```

### Q14
Explain:

```python
a ^ b
```

### Q15
Difference between Union and Intersection?

### Q16
Difference between Difference and Symmetric Difference?

### Q17
What is a subset?

### Q18
What is a superset?

### Q19
What is Set Comprehension?

### Q20
Give an example of Set Comprehension.

---

## Data Engineering Level

### Q21
How would you remove duplicate customer IDs from a dataset?

### Q22
How would you find records present in Source but missing in Target?

### Q23
How would you identify invalid country values?

### Q24
Why are Sets useful for data validation?

### Q25
Why are Sets useful for ETL reconciliation?

### Q26
How would you compare two large collections efficiently?

### Q27
What are some real-world examples where Sets are useful?

### Q28
How would you detect duplicate file processing?

---

## Senior Level

### Q29
What does hashable mean?

### Q30
Why can strings exist in Sets but Lists cannot?

### Q31
Why does this fail?

```python
{
    [1, 2]
}
```

### Q32
What is a frozenset?

### Q33
When would you use a frozenset?

### Q34
Can a frozenset be used as a dictionary key?

Why?

### Q35
What memory concerns arise when using Sets on very large datasets?

### Q36
Why might a Python Set approach fail for billions of records?

### Q37
How would Spark solve reconciliation differently?

### Q38
What is a left anti join and how does it relate to:

```python
source_set - target_set
```

### Q39
When would you prefer Spark over native Python Sets?

### Q40
Design a reconciliation framework for:

- 500 million source records
- 480 million target records

What challenges would you consider?
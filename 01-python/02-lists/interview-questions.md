# Python Lists - Interview Questions

## Q1

What is a Python List?

### Answer

A List is an ordered, mutable collection of elements. Lists can store multiple values and support indexing, slicing, iteration, and modification.

---

## Q2

What is the difference between a List and a Tuple?

### Answer

Lists are mutable and can be modified after creation.

Tuples are immutable and cannot be modified after creation.

---

## Q3

What is the output?

```python
employees = ["John", "Mike", "Alice"]

print(employees[1])
```

### Answer

```python
Mike
```

---

## Q4

What is negative indexing?

### Answer

Negative indexing accesses elements from the end of the list.

```python
employees[-1]
```

returns the last element.

---

## Q5

What is slicing?

### Answer

Slicing retrieves a portion of a list.

```python
employees[1:3]
```

returns elements from index 1 up to but excluding index 3.

---

## Q6

What is the output?

```python
numbers = [1,2,3,4,5]

print(numbers[::-1])
```

### Answer

```python
[5,4,3,2,1]
```

---

## Q7

What is a nested list?

### Answer

A list containing other lists.

Example:

```python
employees = [
    ["John",100000],
    ["Mike",120000]
]
```

Often used to represent tabular data.

---

## Q8

What is a List Comprehension?

### Answer

A concise way to create lists.

Example:

```python
salaries = [100,200,300]

result = [salary * 2 for salary in salaries]
```

Output:

```python
[200,400,600]
```

---

## Q9

Why are Lists important in Data Engineering?

### Answer

Lists are heavily used when processing JSON, API responses, file collections, transformation results, and intermediate datasets. Many higher-level structures such as Pandas and Spark collections build upon similar collection concepts.

---

## Q10

What is the time complexity of appending an element to a list?

### Answer

Typically O(1) amortized time.

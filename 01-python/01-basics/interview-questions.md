# Python Basics - Interview Questions

## Q1

What is the difference between:

```python
100
```

and

```python
"100"
```

### Answer

100 is an integer data type.

"100" is a string data type containing characters.

Integers can participate in mathematical operations while strings are treated as text.

---

## Q2

What is dynamic typing?

### Answer

Python is dynamically typed, meaning a variable can reference objects of different types during runtime.

Example:

```python
x = 10
x = "hello"
```

---

## Q3

Why is type conversion important in ETL pipelines?

### Answer

Most source systems provide data as strings.

Before performing aggregations, filtering, joins, analytics, or loading data into databases, values must often be converted to the correct data type.

Incorrect data types can cause calculation errors, schema mismatches, and pipeline failures.

---

## Q4

What is the output?

```python
salary = "100"
print(salary * 3)
```

### Answer

```python
100100100
```

Because string multiplication repeats the string.

---

## Q5

What is the output?

```python
salary = "100"
print(salary + "50")
```

### Answer

```python
10050
```

Because string addition performs concatenation.

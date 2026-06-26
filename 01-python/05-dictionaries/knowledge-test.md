# Topic 5 - Dictionaries Knowledge Test

## Instructions

- Do **not** execute the code initially.
- Predict the output first.
- Explain *why* the output is produced.
- Think about how each concept applies to Data Engineering.

---

# Part A - Fundamentals

## Q1

What is a Dictionary?

---

## Q2

Name three characteristics of a Dictionary.

---

## Q3

Can Dictionary keys be duplicated?

Why?

---

## Q4

Can Dictionary values be duplicated?

Explain.

---

## Q5

What is the difference between:

```python
{}
```

and

```python
dict()
```

---

## Q6

Why are Dictionaries generally faster than Lists for lookups?

---

## Q7

Why must Dictionary keys be hashable?

Give two examples of valid keys and two examples of invalid keys.

---

## Q8

When would you choose a Dictionary over a List?

Give a Data Engineering example.

---

# Part B - CRUD Operations

## Q9

Predict the output.

```python
employee = {
    "name": "John",
    "salary": 100000
}

print(employee["name"])
```

---

## Q10

Predict the output.

```python
employee = {
    "name": "John"
}

print(employee.get("salary"))
```

---

## Q11

Predict the output.

```python
employee = {
    "name": "John"
}

print(employee["salary"])
```

---

## Q12

What is the advantage of:

```python
employee.get("salary", 0)
```

instead of:

```python
employee["salary"]
```

---

## Q13

What is the output?

```python
employee = {
    "name": "John"
}

employee["salary"] = 100000

print(employee)
```

---

## Q14

Predict the output.

```python
employee = {
    "name": "John",
    "salary": 100000
}

employee["salary"] = 120000

print(employee)
```

---

## Q15

Difference between:

```python
del employee["salary"]
```

and

```python
employee.pop("salary")
```

---

# Part C - Dictionary Methods

## Q16

What does:

```python
employee.keys()
```

return?

---

## Q17

What does:

```python
employee.values()
```

return?

---

## Q18

What does:

```python
employee.items()
```

return?

---

## Q19

Why is this preferred?

```python
for key, value in employee.items():
```

instead of

```python
for key in employee:
    print(employee[key])
```

---

## Q20

Explain what `update()` does.

---

# Part D - Predict the Output

## Q21

```python
employee = {
    "name": "John"
}

print("name" in employee)
```

---

## Q22

```python
employee = {
    "name": "John"
}

print("John" in employee)
```

---

## Q23

```python
employee = {
    "name": "John",
    "salary": 100000
}

for key in employee:
    print(key)
```

---

## Q24

```python
employee = {
    "name": "John",
    "salary": 100000
}

for value in employee.values():
    print(value)
```

---

## Q25

```python
employee = {
    "name": "John",
    "salary": 100000
}

for key, value in employee.items():
    print(key, value)
```

---

# Part E - Nested Dictionaries

## Q26

Predict the output.

```python
customer = {
    "address": {
        "city": "Toronto"
    }
}

print(customer["address"]["city"])
```

---

## Q27

Write code to safely retrieve:

```text
customer -> address -> country
```

using `get()`.

---

## Q28

Why are nested dictionaries common in APIs?

---

# Part F - Dictionary Comprehensions

## Q29

Explain what a Dictionary Comprehension is.

---

## Q30

Write a Dictionary Comprehension that creates:

```python
{
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}
```

---

## Q31

How is Dictionary Comprehension better than a traditional loop?

---

# Part G - Data Engineering Thinking

## Q32

You receive this API response:

```python
{
    "customer_id": 101,
    "name": "John"
}
```

Your code needs the customer's country.

Would you use:

```python
response["country"]
```

or

```python
response.get("country")
```

Explain.

---

## Q33

You receive one million customer records.

How would Dictionaries help you count customers by country?

---

## Q34

Why are Dictionaries commonly used for ETL metadata?

---

## Q35

Give three examples of metadata you would store in a Dictionary during an ETL job.

---

## Q36

Suppose a new field:

```text
email
```

is added to the API tomorrow.

Will your code continue working?

Explain.

---

# Part H - Production Thinking

## Q37

Why should production ETL jobs validate required fields before processing?

---

## Q38

Why should you avoid assuming that every API response contains every field?

---

## Q39

Your API processes 20 million JSON records.

Would loading all records into a single Python Dictionary always be a good idea?

Why or why not?

---

## Q40

How would this problem eventually be solved using:

- Pandas?
- PySpark?

(No code required.)

---

# Part I - Interview Challenge

## Q41

Design a frequency counter that counts how many employees belong to each department.

Describe your approach before writing code.

---

## Q42

Suppose you receive customer records with duplicate customer IDs.

Would a Dictionary help?

How?

---

## Q43

What is the time complexity of Dictionary lookup?

Why?

---

## Q44

Explain the difference between these two statements:

```python
employee["salary"]
```

and

```python
employee.get("salary")
```

Which one would you prefer in production?

---

## Q45

Suppose you're writing an AWS Lambda function that processes S3 events.

Why is understanding Dictionaries essential?

---

# Self Assessment Checklist

Before moving to the next topic, ensure you can confidently:

- Explain what a Dictionary is.
- Perform CRUD operations.
- Use `get()` correctly.
- Explain why keys must be hashable.
- Iterate using `keys()`, `values()`, and `items()`.
- Work with nested dictionaries.
- Build Dictionary Comprehensions.
- Process JSON payloads.
- Count frequencies.
- Store ETL metadata.
- Explain production best practices.
- Connect Dictionaries to Pandas, PySpark, SQL, and AWS.
# Topic 5 - Python Dictionaries Interview Questions

## How to Use This File

These questions are arranged by difficulty.

- 🟢 Beginner – Test your understanding of dictionary fundamentals.
- 🟡 Intermediate – Common coding interview questions.
- 🔴 Advanced – Questions that test deeper Python knowledge.
- ⚫ Production – Real-world Data Engineering scenarios.
- 💼 System Design & Architecture – Questions typically asked for senior Data Engineering roles.

Do not memorize answers. Instead, focus on explaining *why* a solution works.

---

# 🟢 Beginner

## Q1
What is a Dictionary in Python?

---

## Q2
How is a Dictionary different from a List?

---

## Q3
How is a Dictionary different from a Tuple?

---

## Q4
Can Dictionary keys be duplicated?

Why?

---

## Q5
Can Dictionary values be duplicated?

---

## Q6
Why must Dictionary keys be hashable?

---

## Q7
Give examples of valid Dictionary keys.

---

## Q8
Why can't Lists be used as Dictionary keys?

---

## Q9
How do you create an empty Dictionary?

---

## Q10
How do you access a value in a Dictionary?

---

## Q11
What happens if the key does not exist?

---

## Q12
What is the difference between:

```python
employee["salary"]
```

and

```python
employee.get("salary")
```

---

## Q13
What does `get()` return when the key is missing?

---

## Q14
How do you provide a default value using `get()`?

---

## Q15
How do you add a new key-value pair?

---

# 🟡 Intermediate

## Q16
How do you update an existing value?

---

## Q17
Difference between:

```python
del
```

and

```python
pop()
```

---

## Q18
What does:

```python
keys()
```

return?

---

## Q19
What does:

```python
values()
```

return?

---

## Q20
What does:

```python
items()
```

return?

---

## Q21
How do you iterate over all keys?

---

## Q22
How do you iterate over all values?

---

## Q23
How do you iterate over keys and values together?

---

## Q24
Explain Dictionary Comprehensions.

---

## Q25
Write a Dictionary Comprehension that stores squares of numbers.

---

## Q26
What is a nested Dictionary?

---

## Q27
How do you access nested values?

---

## Q28
Explain shallow copy vs reference assignment for Dictionaries.

---

## Q29
What does:

```python
update()
```

do?

---

## Q30
When would you use `copy()`?

---

# 🔴 Advanced

## Q31
How are Dictionaries implemented internally?

---

## Q32
Explain hashing.

---

## Q33
Why are Dictionary lookups generally O(1)?

---

## Q34
Can Dictionary ordering be relied upon?

Explain the behavior in Python 3.7+.

---

## Q35
What happens if two keys produce the same hash?

(Hint: Hash Collision)

---

## Q36
Why are mutable objects unsuitable as Dictionary keys?

---

## Q37
How would you merge two Dictionaries?

Discuss multiple approaches.

---

## Q38
How would you invert a Dictionary?

Example:

```python
{
    "A":1,
    "B":2
}
```

↓

```python
{
    1:"A",
    2:"B"
}
```

---

## Q39
What are some limitations of Dictionary Comprehensions?

---

## Q40
How would you count frequencies using a Dictionary?

---

# ⚫ Production (Data Engineering)

## Q41
Why are Dictionaries heavily used in REST APIs?

---

## Q42
Why does JSON map naturally to Dictionaries?

---

## Q43
Why should production code prefer:

```python
get()
```

over

```python
[]
```

for optional fields?

---

## Q44
Suppose an API introduces a new field tomorrow.

How should your code handle it?

---

## Q45
Suppose an API removes a field tomorrow.

How should your code behave?

---

## Q46
How would you validate required fields in an incoming JSON payload?

---

## Q47
How would you detect missing mandatory fields?

---

## Q48
How would you count customers by country?

---

## Q49
How would you count failed ETL records by error type?

Example output:

```text
ValidationError : 120
SchemaError     : 32
DuplicateID     : 11
```

---

## Q50
How would you store ETL job metadata?

What fields would you include?

---

## Q51
Give examples of metadata collected during an ETL pipeline.

---

## Q52
How are Dictionaries used inside AWS Lambda event processing?

---

## Q53
Why are nested Dictionaries common in AWS services?

---

## Q54
How would you safely process deeply nested JSON?

---

## Q55
What problems occur if your ETL assumes every JSON field is present?

---

# 💼 Senior / Architecture

## Q56
Suppose your API returns 20 million customer records.

Would you store everything inside one Python Dictionary?

Why or why not?

---

## Q57
At what scale would you move from native Python to Pandas?

---

## Q58
At what scale would you move from Pandas to PySpark?

Explain your reasoning.

---

## Q59
How would Dictionary-based processing change in a distributed Spark application?

---

## Q60
Suppose your ETL pipeline receives malformed JSON records.

Design a strategy that:

- continues processing valid records,
- captures invalid records,
- records processing statistics,
- produces an audit report.

---

# ⭐ FAANG / Senior Discussion Questions

These questions usually have no single correct answer. Interviewers evaluate your reasoning.

---

## Q61
Design a JSON ingestion framework that can tolerate schema evolution without breaking existing pipelines.

---

## Q62
Suppose customer records contain hundreds of optional fields.

How would you design your processing logic?

---

## Q63
What trade-offs exist between strict schema validation and flexible schema processing?

---

## Q64
Your API response changes every month.

How would you future-proof your ETL jobs?

---

## Q65
How would you design reusable validation logic for multiple APIs?

---

## Q66
How would you collect operational metrics from every ETL job?

---

## Q67
Suppose your manager asks:

"How many customer records failed yesterday?"

How would you answer that question programmatically?

---

## Q68
Design a metadata structure that every ETL job should produce.

---

## Q69
What production mistakes have you seen (or can you imagine) when developers process JSON incorrectly?

---

## Q70
Imagine you're reviewing a teammate's code.

What Dictionary-related best practices would you check before approving the pull request?

---

# Rapid Revision (2 Minutes Before the Interview)

Be able to confidently explain:

- What is a Dictionary?
- Why are lookups O(1)?
- Why must keys be hashable?
- Difference between `get()` and `[]`.
- Difference between `keys()`, `values()`, and `items()`.
- CRUD operations.
- Dictionary Comprehensions.
- Nested Dictionaries.
- Frequency counting.
- JSON processing.
- ETL metadata.
- API validation.
- Production best practices.
- Relationship with Pandas, PySpark, SQL, and AWS.

If you can answer all of the above without referring to notes, you have a strong foundation in Python Dictionaries.
# Exception Handling - Interview Questions

These questions are ordered from beginner to senior-level.

---

# Beginner Level

## Q1. What is an exception in Python?

---

## Q2. What is the difference between a syntax error and an exception?

---

## Q3. Why do we use exception handling?

---

## Q4. Explain the purpose of:

- try
- except
- else
- finally

---

## Q5. What happens if an exception is not handled?

---

## Q6. What is the difference between:

```python
except:
```

and

```python
except Exception:
```

Which one is preferred?

---

## Q7. Why is it considered a bad practice to write:

```python
except Exception:
    pass
```

---

# Intermediate Level

## Q8. What does the `raise` keyword do?

When would you use it?

---

## Q9. Explain the difference between Python-generated exceptions and developer-raised exceptions.

---

## Q10. Why should `try` blocks be kept as small as possible?

---

## Q11. When should code be placed inside a `finally` block?

Give real-world examples.

---

## Q12. Why should you catch specific exceptions instead of using:

```python
except Exception:
```

everywhere?

---

## Q13. What are custom exceptions?

Why are they useful?

---

## Q14. How do you create a custom exception?

---

## Q15. Why should custom exceptions inherit from `Exception`?

---

## Q16. What is the purpose of a bare:

```python
raise
```

inside an `except` block?

---

# Advanced Level

## Q17. What is the difference between a business error and a system error?

Give examples.

---

## Q18. Which errors should be retried?

Which ones should never be retried?

Explain your reasoning.

---

## Q19. Why is logging preferred over `print()` in production applications?

---

## Q20. Describe how you would process one million customer records where a few records are invalid.

Would you stop the pipeline?

Why?

---

## Q21. Suppose the target database becomes unavailable halfway through processing.

How should your application respond?

---

## Q22. Explain the concept of "Fail Fast" and "Fail Safe".

Give practical examples.

---

## Q23. What is exponential backoff?

Why is it commonly used in distributed systems?

---

## Q24. Explain how exception handling improves system reliability.

---

# Scenario-Based Questions

## Q25.

You receive a CSV file from a vendor.

20 out of 1000 records are invalid.

How would you process the file?

---

## Q26.

A customer attempts to withdraw more money than is available in their account.

Would you use:

```python
ValueError
```

or create a custom exception?

Explain your reasoning.

---

## Q27.

Your REST API calls another service.

The service returns HTTP 503.

Would you retry?

If yes, how?

---

## Q28.

You discover this code during a code review:

```python
try:
    process()

except Exception:
    print("Something failed.")
```

What improvements would you suggest?

---

## Q29.

Describe a situation where continuing execution after an exception would be dangerous.

---

## Q30.

Describe a situation where continuing execution after an exception would be the correct design.

---

# Practical Coding Questions

## Q31.

Write a function that raises an exception if age is negative.

---

## Q32.

Create a custom exception named:

```python
DuplicateEmployeeError
```

---

## Q33.

Write a function that validates an email address using `raise`.

---

## Q34.

Write a function that retries a database connection three times before failing.

---

## Q35.

Design an exception hierarchy for an e-commerce application.

Example categories:

- Customer
- Payment
- Inventory
- Order

Explain why you structured it that way.

---

# Senior-Level Discussion

These questions usually have no single correct answer.

## Q36.

Should every exception be logged?

Why or why not?

---

## Q37.

When should an application recover from an exception instead of failing immediately?

---

## Q38.

How would you design exception handling in an ETL pipeline processing hundreds of millions of records?

---

## Q39.

What information should always be included in production logs when an exception occurs?

---

## Q40.

What are the most common exception-handling mistakes you've seen in production systems?

How would you avoid them?
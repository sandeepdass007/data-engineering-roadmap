# Knowledge Test - Exception Handling

Try answering these questions without looking at the examples.

---

# Part A - Basics

## Q1

What is an exception?

---

## Q2

Why do we use exception handling?

---

## Q3

Which block contains the code that might fail?

---

## Q4

Which block handles an exception?

---

## Q5

Predict the output.

```python
try:
    print("Start")
    10 / 0
except ZeroDivisionError:
    print("Division Error")

print("Done")
```

---

## Q6

True or False?

Every exception crashes the application.

---

## Q7

Give three real-world situations where exception handling is useful.

---

# Part B - else and finally

## Q8

When does the `else` block execute?

---

## Q9

When does the `finally` block execute?

---

## Q10

Predict the output.

```python
try:
    print("Hello")
except:
    print("Error")
else:
    print("Success")
finally:
    print("Finished")
```

---

## Q11

Name three resources that should normally be released in a `finally` block.

---

## Q12

Why should a `try` block be kept as small as possible?

---

# Part C - raise

## Q13

What does the `raise` keyword do?

---

## Q14

Who creates the exception when `raise` is used?

---

## Q15

Predict the output.

```python
age = -10

if age < 0:
    raise ValueError("Invalid age")
```

---

## Q16

Why is `raise` useful even when Python code is syntactically correct?

---

## Q17

Give three business validation rules where you would use `raise`.

---

# Part D - Custom Exceptions

## Q18

Why would you create a custom exception instead of always using `ValueError`?

---

## Q19

Which class should every custom exception inherit from?

---

## Q20

Complete the code.

```python
class InvalidCustomerError(________):
    pass
```

---

## Q21

Which exception is more descriptive?

```python
raise ValueError("Duplicate customer")
```

OR

```python
raise DuplicateCustomerError(
    "Customer already exists."
)
```

Explain your answer.

---

## Q22

Give three examples of custom exceptions that might exist in a banking application.

---

# Part E - Production Patterns

## Q23

Why is logging preferred over `print()` in production systems?

---

## Q24

Why is this dangerous?

```python
except Exception:
    pass
```

---

## Q25

What does a bare `raise` do inside an `except` block?

---

## Q26

Which of these should normally be retried?

- Database timeout
- Negative salary
- Temporary network failure
- Missing customer ID

Explain your answer.

---

## Q27

Explain the difference between a business error and a system error.

Give one example of each.

---

## Q28

Your ETL pipeline processes one million records.

One record contains an invalid email address.

Should the job stop?

Why or why not?

---

## Q29

Your ETL pipeline loses the database connection halfway through processing.

Should the job continue?

Explain your reasoning.

---

# Scenario-Based Questions

## Q30

You are processing customer records.

One record contains:

- customer_id = None
- salary = 50000

How would your application handle this?

---

## Q31

A REST API returns HTTP 500 because the database is temporarily unavailable.

Would you retry?

If yes, how?

---

## Q32

Your application receives a file from a vendor.

The file contains 50 invalid records and 950 valid records.

Describe how you would process the file.

---

## Q33

A teammate writes:

```python
except Exception:
    print("Something failed.")
```

What improvements would you suggest?

---

## Q34

Why is separating business validation from infrastructure failures considered a good software design practice?

---

# Self Evaluation

Rate your confidence (1-5):

- I understand try / except.
- I understand else and finally.
- I can use raise confidently.
- I know when to create custom exceptions.
- I can distinguish business errors from system errors.
- I understand retry strategies.
- I can design production-ready exception handling.

If you scored **4 or 5** on most items and answered at least **28 out of 34** questions correctly without referring to notes, you're ready to move on to Object-Oriented Programming.
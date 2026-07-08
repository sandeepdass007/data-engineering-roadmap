# Topic 6 - Functions
## Interview Questions

---

# Level 1 - Fundamentals

## Q1

What is a function?

---

## Q2

Why do we use functions?

---

## Q3

What is the difference between a parameter and an argument?

---

## Q4

What is the difference between `print()` and `return`?

---

## Q5

What happens if a function does not explicitly return anything?

---

## Q6

Can a function return multiple values?

If yes, how?

---

## Q7

What are positional arguments?

---

## Q8

What are keyword arguments?

---

## Q9

What are default parameters?

---

## Q10

Why are default parameters useful?

---

# Level 2 - Intermediate Python

## Q11

Explain local scope and global scope.

---

## Q12

When should the `global` keyword be used?

---

## Q13

Why are global variables generally discouraged?

---

## Q14

What is variable shadowing?

---

## Q15

What is a lambda function?

---

## Q16

When would you choose a normal function instead of a lambda?

---

## Q17

Can a lambda contain multiple statements?

Why?

---

## Q18

What does `map()` do?

---

## Q19

Why does `map()` return a map object instead of a list?

---

## Q20

What does `filter()` do?

---

## Q21

What does `reduce()` do?

---

## Q22

Which module contains `reduce()`?

---

## Q23

Explain the accumulator parameter in `reduce()`.

---

## Q24

What are first-class functions?

---

## Q25

Why can functions be passed to `map()` and `filter()`?

---

# Level 3 - Production-Oriented

## Q26

When would you use `*args`?

Give a production example.

---

## Q27

When would you use `**kwargs`?

Give a production example.

---

## Q28

Why are `**kwargs` common in configuration APIs?

---

## Q29

Explain the difference between:

```python
handler = process
```

and

```python
handler = process()
```

---

## Q30

When would you use `map()` instead of a `for` loop?

---

## Q31

When would you avoid using `map()`?

---

## Q32

When should `sum()` be preferred over `reduce()`?

---

## Q33

Why should lambda expressions usually remain short?

---

## Q34

What is recursion?

---

## Q35

What is the purpose of the base case?

---

## Q36

Why is recursion not recommended for processing very large datasets?

---

## Q37

Name three real-world use cases for recursion.

---

# Level 4 - Senior / Design Thinking

## Q38

You are designing an ETL framework.

Would you choose:

```python
load_data(
    host,
    port,
    username,
    password,
    timeout,
    retries
)
```

or

```python
load_data(**config)
```

Explain your reasoning.

---

## Q39

You have a data-cleaning function that currently performs validation, formatting, logging, and database insertion.

Would you keep it as one function or split it into multiple functions? Why?

---

## Q40

How do functions help implement the Single Responsibility Principle (SRP)?

---

## Q41

Why are reusable functions important in ETL pipelines?

---

## Q42

Suppose your team uses the same customer validation logic in ten different ETL jobs.

How would you design the solution?

---

## Q43

Compare `map()`, `filter()`, and `reduce()`.

When would you choose each?

---

## Q44

A junior developer has written a recursive solution to process five million CSV records.

Would you approve the pull request? Why or why not?

---

## Q45

When reviewing Python code, what signs tell you that a function is doing too much?

---

## Q46

What characteristics make a function production-ready?

---

## Q47

How do keyword arguments improve API readability?

---

## Q48

Why are small reusable functions easier to test?

---

## Q49

How would you design a reusable logging function for multiple ETL pipelines?

---

## Q50

Imagine you're building a Python utility library for your organization.

What principles would you follow when designing its functions?

---

# Bonus Coding Questions

1. Write a function to calculate the factorial of a number using recursion.
2. Write a function that accepts any number of integers and returns their sum using `*args`.
3. Write a function that accepts employee details using `**kwargs` and prints them.
4. Use `map()` to convert a list of strings into integers.
5. Use `filter()` to remove invalid customer IDs from a list.
6. Use `reduce()` to calculate the product of all numbers in a list.
7. Write a recursive function to calculate the sum of all numbers in a list.
8. Write a function that accepts another function as an argument and applies it to a list of values.
9. Write a recursive function to traverse a nested dictionary representing an organization hierarchy.
10. Build a reusable ETL pipeline function that accepts records using `*args` and processing options using `**kwargs`.
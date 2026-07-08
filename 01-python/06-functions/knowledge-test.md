# Topic 6 - Functions
## Knowledge Test

Try answering these questions without executing the code.

---

# Part A - Function Basics

## Q1

Why do we create functions instead of writing everything inside `main`?

---

## Q2

What is the difference between a parameter and an argument?

---

## Q3

What is the difference between `print()` and `return`?

---

## Q4

Can a function return multiple values in Python?

If yes, how?

---

## Q5

What happens if a function has no `return` statement?

---

# Part B - Parameters & Arguments

## Q6

What are positional arguments?

---

## Q7

What are keyword arguments?

---

## Q8

Why are keyword arguments often preferred in production code?

---

## Q9

Predict the output.

```python
def greet(name, country):
    print(name, country)

greet(country="Canada", name="John")
```

---

## Q10

What is a default parameter?

---

## Q11

Why are default parameters useful when APIs evolve?

---

# Part C - Variable Scope

## Q12

What is the difference between local and global variables?

---

## Q13

Which variable has higher priority if both have the same name?

---

## Q14

When is the `global` keyword required?

---

## Q15

Why should global variables generally be avoided?

---

## Q16

Which design is better?

```python
load_data()
```

using global configuration

OR

```python
load_data(config)
```

Why?

---

# Part D - Lambda Functions

## Q17

What is a lambda function?

---

## Q18

When should you choose a normal function instead of a lambda?

---

## Q19

Can a lambda contain multiple statements?

---

## Q20

Write a lambda that squares a number.

---

# Part E - map()

## Q21

What does `map()` do?

---

## Q22

Why does `map()` return a map object instead of a list?

---

## Q23

Predict the output.

```python
numbers = [1,2,3]

result = map(lambda x:x*2, numbers)

print(list(result))
```

---

## Q24

Which is cleaner?

```python
map(int, values)
```

OR

```python
map(lambda x:int(x), values)
```

Why?

---

## Q25

Give one real ETL use case for `map()`.

---

# Part F - First-Class Functions

## Q26

What does it mean that functions are first-class objects?

---

## Q27

What is the difference between:

```python
handler = process
```

and

```python
handler = process()
```

---

## Q28

Why does `map()` accept a function reference?

---

## Q29

Name one production use case for passing functions.

---

## Q30

Why does this make software more extensible?

---

# Part G - filter()

## Q31

What does `filter()` do?

---

## Q32

What type of object does `filter()` return?

---

## Q33

Predict the output.

```python
numbers = [1,2,3,4]

print(
    list(
        filter(
            lambda x:x%2==0,
            numbers
        )
    )
)
```

---

## Q34

Give one ETL use case for `filter()`.

---

## Q35

When should you replace a complex lambda with a named function?

---

# Part H - reduce()

## Q36

What problem does `reduce()` solve?

---

## Q37

Which module contains `reduce()`?

---

## Q38

What is the accumulator?

---

## Q39

Predict the output.

```python
from functools import reduce

print(
    reduce(
        lambda a,b:a+b,
        [1,2,3],
        10
    )
)
```

---

## Q40

When should you use `sum()` instead of `reduce()`?

---

# Part I - *args and **kwargs

## Q41

What problem does `*args` solve?

---

## Q42

Inside a function, what data type is `args`?

---

## Q43

What problem does `**kwargs` solve?

---

## Q44

Inside a function, what data type is `kwargs`?

---

## Q45

Why are `**kwargs` common in configuration APIs?

---

# Part J - Recursion

## Q46

What is recursion?

---

## Q47

What are the two essential parts of every recursive function?

---

## Q48

What happens if the base case is missing?

---

## Q49

Why are loops usually preferred over recursion for large datasets?

---

## Q50

Name two real-world problems where recursion is useful.

---

# Final Revision Question

Explain the difference between:

- map()
- filter()
- reduce()

in one sentence each.
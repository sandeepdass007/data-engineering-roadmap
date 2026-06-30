# Mini Project - Customer Data Processing Pipeline

## Objective

In this project, you will build a small **Customer Data Processing Pipeline** using Python functions.

This project is designed to simulate a simplified ETL (Extract, Transform, Load) workflow and reinforce the concepts learned in this topic.

You will practice:

* Writing reusable functions
* Passing parameters and arguments
* Returning values
* Function composition
* Single Responsibility Principle (SRP)
* Processing lists of dictionaries
* Writing clean, modular Python code

---

# Scenario

You have received customer records from an API.

Unfortunately, the incoming data is inconsistent and needs to be cleaned before it can be loaded into a data warehouse.

Use the following dataset as the input.

```python
customers = [
    {
        "customer_id": 101,
        "name": "  john smith ",
        "country": "canada",
        "salary": 100000
    },
    {
        "customer_id": 102,
        "name": "ALICE",
        "country": "usa",
        "salary": 120000
    },
    {
        "customer_id": 103,
        "name": " mike ",
        "country": "india",
        "salary": 90000
    }
]
```

---

# Project Requirements

## Task 1 - Clean Customer Name

Create a function:

```python
clean_name(name)
```

It should:

* Remove leading and trailing spaces.
* Convert the name to Title Case.

### Example

Input

```text
" john smith "
```

Output

```text
John Smith
```

---

## Task 2 - Clean Country Name

Create a function:

```python
clean_country(country)
```

It should convert the country name to Title Case.

### Example

Input

```text
canada
```

Output

```text
Canada
```

---

## Task 3 - Calculate Bonus

Create a function:

```python
calculate_bonus(salary)
```

Bonus Rules

| Salary           | Bonus |
| ---------------- | ----- |
| Salary >= 100000 | 10%   |
| Salary < 100000  | 5%    |

### Example

Input

```text
100000
```

Output

```text
10000
```

---

## Task 4 - Process a Single Customer

Create a function:

```python
process_customer(customer)
```

This function should:

* Clean the customer's name.
* Clean the customer's country.
* Calculate the customer's bonus.
* Return a **new dictionary** containing the processed customer.

### Expected Output

```python
{
    "customer_id": 101,
    "name": "John Smith",
    "country": "Canada",
    "salary": 100000,
    "bonus": 10000
}
```

> **Important:** Do not modify the original dictionary. Return a new one.

---

## Task 5 - Process All Customers

Create a function:

```python
process_all(customers)
```

This function should:

* Process every customer using `process_customer()`.
* Return a new list containing all processed customers.

---

## Task 6 - Display Customer Report

Print the processed customers in the following format:

```text
----------------------------------------
Customer Report
----------------------------------------

ID       : 101
Name     : John Smith
Country  : Canada
Salary   : 100000
Bonus    : 10000

----------------------------------------
```

Repeat for every customer.

---

# Stretch Goals

## Stretch Goal 1 ⭐

Create a function:

```python
calculate_average_salary(customers)
```

Return the average salary of all customers.

---

## Stretch Goal 2 ⭐⭐

Create a function:

```python
highest_salary(customers)
```

Return the customer with the highest salary.

---

## Stretch Goal 3 ⭐⭐⭐

Create a function:

```python
summary(customers)
```

Return a dictionary like this:

```python
{
    "total_customers": 3,
    "average_salary": 103333.33,
    "highest_salary": 120000,
    "total_bonus": 24000
}
```

---

## Stretch Goal 4 ⭐⭐⭐⭐ (Production Thinking)

Modify your solution so that **no function modifies the original input data**.

Every processing function should return new objects instead of changing existing ones.

Think about why this is considered a good practice in production systems.

---

# Bonus Challenge (Interview Level)

Imagine your manager says:

> "Starting tomorrow, we also need to calculate income tax for every customer."

Before writing any code, answer the following questions:

1. Which functions need to change?
2. How many places in your code should require modification?
3. If you designed your solution well, why is the change easy to implement?

---

# Learning Outcomes

After completing this project, you should be able to:

* Write small, reusable functions.
* Build larger programs by composing multiple functions.
* Apply the Single Responsibility Principle.
* Return dictionaries and lists from functions.
* Avoid modifying input data unnecessarily.
* Build a simple ETL-style processing pipeline.
* Structure code in a way that is easy to maintain and extend.

---

# Real-World Data Engineering Connection

This project represents a simplified ETL pipeline.

```text
Extract
    │
    ▼
Read Customer Records
    │
    ▼
Clean Customer Names
    │
    ▼
Normalize Country Names
    │
    ▼
Calculate Bonus
    │
    ▼
Generate Processed Records
    │
    ▼
Generate Summary Statistics
    │
    ▼
Load to Data Warehouse
```

In future topics, this same project will evolve:

* **Python Functions** → Modular processing
* **Pandas** → DataFrame transformations
* **SQL** → Store and query processed data
* **PySpark** → Distributed processing
* **AWS S3** → Cloud storage
* **AWS Glue** → Managed ETL
* **Apache Airflow** → Workflow orchestration
* **Kafka** → Streaming ingestion
* **Snowflake** → Data warehouse loading

By the end of this roadmap, you'll have built the same business solution using the technologies commonly used in modern Data Engineering.

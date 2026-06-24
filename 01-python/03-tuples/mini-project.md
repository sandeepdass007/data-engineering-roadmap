# Mini Project: ETL Batch Metrics Processor

## Objective

Learn how tuples are used in Data Engineering to represent fixed structures and return multiple values from functions.

---

## Scenario

You are building a lightweight ETL monitoring utility.

Each ETL job returns a tuple in the following format:

```python
(job_name, rows_processed, rows_failed)
```

Example:

```python
("customer_load", 1000, 5)
```

Meaning:

| Field          | Value         |
| -------------- | ------------- |
| Job Name       | customer_load |
| Rows Processed | 1000          |
| Rows Failed    | 5             |

Because the structure is fixed and should not be modified, tuples are a suitable choice.

---

## Dataset

Create the following dataset:

```python
etl_results = [
    ("customer_load", 1000, 5),
    ("employee_load", 1500, 2),
    ("sales_load", 5000, 20),
    ("inventory_load", 2500, 0)
]
```

---

## Task 1

Print all job results using tuple unpacking.

Example output:

```text
Job=customer_load Processed=1000 Failed=5
Job=employee_load Processed=1500 Failed=2
Job=sales_load Processed=5000 Failed=20
Job=inventory_load Processed=2500 Failed=0
```

---

## Task 2

Calculate the total number of processed rows.

Expected result:

```text
10000
```

---

## Task 3

Calculate the total number of failed rows.

Expected result:

```text
27
```

---

## Task 4

Find the job with the highest processed count.

Expected result:

```text
sales_load
```

---

## Task 5

Print only the jobs that had failures.

Expected output:

```text
customer_load
employee_load
sales_load
```

Do not print:

```text
inventory_load
```

because it has zero failed rows.

---

## Task 6

Create a function:

```python
def process_job(job_name):
```

Return a tuple:

```python
(job_name, processed_rows, failed_rows)
```

Example:

```python
("finance_load", 2000, 3)
```

Use tuple unpacking when consuming the returned value.

---

## Stretch Goal

Create a function:

```python
def summarize_jobs(etl_results):
```

Return:

```python
(total_processed, total_failed)
```

Example usage:

```python
processed, failed = summarize_jobs(etl_results)
```

This pattern is frequently used in production ETL code.

---

## Learning Outcomes

After completing this project, you should understand:

* Tuples as immutable structures
* Tuple unpacking
* Returning multiple values from functions
* Iterating through tuples
* Working with lists of tuples
* Real-world ETL monitoring patterns

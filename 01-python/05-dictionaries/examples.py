"""
Topic 5 - Dictionaries

A Dictionary is a collection of key-value pairs.

Data Engineering Usage:
- JSON processing
- API responses
- Configuration management
- ETL metadata
- Event processing
- Frequency counting
"""

# ==========================================================
# 1. Creating Dictionaries
# ==========================================================

employee = {
    "id": 1001,
    "name": "John",
    "salary": 100000
}

print(employee)

# ==========================================================
# 2. Empty Dictionary
# ==========================================================

empty_dict = {}

print(type(empty_dict))

# ==========================================================
# 3. Accessing Values
# ==========================================================

employee = {
    "name": "John",
    "salary": 100000
}

print(employee["name"])

# ==========================================================
# 4. Safe Access Using get()
# ==========================================================

print(employee.get("salary"))

print(employee.get("city"))

# None

# ==========================================================
# 5. Default Value with get()
# ==========================================================

print(employee.get("city", "Unknown"))

# ==========================================================
# 6. Adding New Keys
# ==========================================================

employee["city"] = "Toronto"

print(employee)

# ==========================================================
# 7. Updating Existing Keys
# ==========================================================

employee["salary"] = 120000

print(employee)

# ==========================================================
# 8. Removing Keys Using del
# ==========================================================

employee_copy = employee.copy()

del employee_copy["city"]

print(employee_copy)

# ==========================================================
# 9. Removing Keys Using pop()
# ==========================================================

employee_copy = employee.copy()

city = employee_copy.pop("city")

print(city)

print(employee_copy)

# ==========================================================
# 10. Dictionary Keys Are Unique
# ==========================================================

employee = {
    "name": "John",
    "name": "Mike"
}

print(employee)

# {'name': 'Mike'}

# ==========================================================
# 11. Membership Testing (Keys)
# ==========================================================

employee = {
    "name": "John",
    "salary": 100000
}

print("name" in employee)

print("John" in employee)

# ==========================================================
# 12. Keys View
# ==========================================================

print(employee.keys())

# ==========================================================
# 13. Values View
# ==========================================================

print(employee.values())

# ==========================================================
# 14. Items View
# ==========================================================

print(employee.items())

# ==========================================================
# 15. Iterating Through Keys
# ==========================================================

for key in employee:
    print(key)

# ==========================================================
# 16. Iterating Through Values
# ==========================================================

for value in employee.values():
    print(value)

# ==========================================================
# 17. Iterating Through Keys and Values
# ==========================================================

for key, value in employee.items():
    print(key, value)

# ==========================================================
# 18. Nested Dictionary
# ==========================================================

customer = {
    "id": 101,
    "address": {
        "city": "Toronto",
        "country": "Canada"
    }
}

print(customer["address"]["city"])

# ==========================================================
# 19. Dictionary with Lists
# ==========================================================

customer = {
    "id": 101,
    "orders": [
        1001,
        1002,
        1003
    ]
}

print(customer["orders"])

# ==========================================================
# 20. Dictionary of Dictionaries
# ==========================================================

employees = {
    1001: {
        "name": "John",
        "salary": 100000
    },
    1002: {
        "name": "Mike",
        "salary": 120000
    }
}

print(employees[1001]["name"])

# ==========================================================
# 21. Hashable Keys
# ==========================================================

coordinates = {
    (10, 20): "Point A"
}

print(coordinates)

# ==========================================================
# 22. Frequency Counting (Basic)
# ==========================================================

names = [
    "John",
    "Mike",
    "John",
    "Alice",
    "Mike",
    "John"
]

frequency = {}

for name in names:

    if name in frequency:
        frequency[name] += 1
    else:
        frequency[name] = 1

print(frequency)

# ==========================================================
# 23. Using setdefault()
# ==========================================================

counts = {}

counts.setdefault("John", 0)

counts["John"] += 1

print(counts)

# ==========================================================
# 24. Dictionary Comprehension
# ==========================================================

squares = {
    number: number ** 2
    for number in range(1, 6)
}

print(squares)

# ==========================================================
# 25. Filtered Dictionary Comprehension
# ==========================================================

even_squares = {
    number: number ** 2
    for number in range(1, 11)
    if number % 2 == 0
}

print(even_squares)

# ==========================================================
# 26. JSON-Like API Response
# ==========================================================

api_response = {
    "customer_id": 101,
    "name": "John",
    "country": "Canada",
    "active": True
}

print(api_response["country"])

# ==========================================================
# 27. Data Validation Example
# ==========================================================

required_fields = [
    "customer_id",
    "name",
    "country"
]

record = {
    "customer_id": 101,
    "name": "John"
}

for field in required_fields:

    if field not in record:
        print(
            f"Missing field: {field}"
        )

# ==========================================================
# 28. ETL Metadata Example
# ==========================================================

job_metadata = {
    "job_name": "customer_load",
    "rows_processed": 1000,
    "rows_failed": 5,
    "execution_time": 120
}

print(
    job_metadata["rows_processed"]
)

# ==========================================================
# 29. AWS Lambda Event Example
# ==========================================================

event = {
    "Records": [
        {
            "eventName": "ObjectCreated",
            "bucket": "customer-files"
        }
    ]
}

print(
    event["Records"][0]["eventName"]
)

# ==========================================================
# 30. Merge Dictionaries
# ==========================================================

employee = {
    "name": "John"
}

salary_info = {
    "salary": 100000
}

combined = {
    **employee,
    **salary_info
}

print(combined)

# ==========================================================
# 31. update()
# ==========================================================

employee = {
    "name": "John"
}

employee.update({
    "city": "Toronto",
    "salary": 100000
})

print(employee)

# ==========================================================
# 32. get() vs [] Example
# ==========================================================

employee = {
    "name": "John"
}

print(
    employee.get("city")
)

# Safe

# print(employee["city"])

# KeyError

# ==========================================================
# 33. Real ETL Record
# ==========================================================

customer_record = {
    "customer_id": 101,
    "first_name": "John",
    "last_name": "Smith",
    "country": "Canada",
    "email": "john@example.com",
    "is_active": True
}

for field, value in customer_record.items():
    print(
        f"{field}: {value}"
    )

# ==========================================================
# 34. Dictionary Length
# ==========================================================

print(len(customer_record))

# ==========================================================
# 35. Production Example
# Dynamic Metrics Tracking
# ==========================================================

metrics = {}

for status in [
    "SUCCESS",
    "SUCCESS",
    "FAILED",
    "SUCCESS"
]:

    metrics[status] = (
        metrics.get(status, 0) + 1
    )

print(metrics)

# ==========================================================
# 36. Summary Example
# ==========================================================

job_summary = {
    "job_name": "customer_load",
    "rows_processed": 1000,
    "rows_failed": 5,
    "success_rate": 99.5
}

for key, value in job_summary.items():
    print(
        f"{key}: {value}"
    )
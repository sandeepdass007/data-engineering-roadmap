"""
Topic 4 - Sets
Examples for GitHub Repository

A Set is:
- Unordered
- Mutable
- Contains only unique values

Data Engineering Usage:
- Deduplication
- Fast lookups
- Data validation
- Dataset reconciliation
"""

# ==========================================================
# 1. Creating Sets
# ==========================================================

employees = {"John", "Mike", "Alice"}

print(employees)

# ==========================================================
# 2. Set Removes Duplicates Automatically
# ==========================================================

employees = {
    "John",
    "Mike",
    "John",
    "Alice",
    "Mike"
}

print(employees)

# Expected:
# {'John', 'Mike', 'Alice'}

# ==========================================================
# 3. Creating Set from List
# ==========================================================

employee_list = [
    "John",
    "Mike",
    "John",
    "Alice",
    "Mike"
]

unique_employees = set(employee_list)

print(unique_employees)

# ==========================================================
# 4. Empty Set
# ==========================================================

empty_set = set()

print(type(empty_set))

# ==========================================================
# 5. Empty Dictionary Trap
# ==========================================================

empty_dict = {}

print(type(empty_dict))

# dict

# ==========================================================
# 6. Adding Values
# ==========================================================

employees = {"John", "Mike"}

employees.add("Alice")

print(employees)

# ==========================================================
# 7. Adding Duplicate Values
# ==========================================================

employees = {"John", "Mike"}

employees.add("John")

print(employees)

# No duplicate added

# ==========================================================
# 8. Removing Values
# ==========================================================

employees = {"John", "Mike", "Alice"}

employees.remove("Mike")

print(employees)

# ==========================================================
# 9. remove() Error
# ==========================================================

employees = {"John", "Mike"}

# Uncomment to test

# employees.remove("David")

# KeyError

# ==========================================================
# 10. discard()
# ==========================================================

employees = {"John", "Mike"}

employees.discard("David")

print(employees)

# No error

# ==========================================================
# 11. Membership Testing
# ==========================================================

employees = {
    "John",
    "Mike",
    "Alice"
}

print("John" in employees)

print("David" in employees)

# ==========================================================
# 12. Length
# ==========================================================

employees = {
    "John",
    "Mike",
    "Alice"
}

print(len(employees))

# ==========================================================
# 13. Iterating Through Sets
# ==========================================================

employees = {
    "John",
    "Mike",
    "Alice"
}

for employee in employees:
    print(employee)

# ==========================================================
# 14. Union
# ==========================================================

team_a = {"John", "Mike"}

team_b = {"Mike", "Alice"}

result = team_a | team_b

print(result)

# ==========================================================
# 15. Intersection
# ==========================================================

team_a = {"John", "Mike"}

team_b = {"Mike", "Alice"}

result = team_a & team_b

print(result)

# {'Mike'}

# ==========================================================
# 16. Difference
# ==========================================================

team_a = {"John", "Mike"}

team_b = {"Mike", "Alice"}

result = team_a - team_b

print(result)

# {'John'}

# ==========================================================
# 17. Symmetric Difference
# ==========================================================

team_a = {"John", "Mike"}

team_b = {"Mike", "Alice"}

result = team_a ^ team_b

print(result)

# {'John', 'Alice'}

# ==========================================================
# 18. Subset
# ==========================================================

small = {1, 2}

large = {1, 2, 3, 4}

print(small.issubset(large))

# True

# ==========================================================
# 19. Superset
# ==========================================================

small = {1, 2}

large = {1, 2, 3, 4}

print(large.issuperset(small))

# True

# ==========================================================
# 20. Data Engineering Example
# Deduplication
# ==========================================================

customer_ids = [
    101,
    102,
    101,
    103,
    102,
    104
]

unique_customer_ids = set(customer_ids)

print(unique_customer_ids)

# ==========================================================
# 21. Data Engineering Example
# Country Validation
# ==========================================================

valid_countries = {
    "Canada",
    "USA",
    "India"
}

incoming_country = "Canada"

if incoming_country in valid_countries:
    print("Valid Country")

# ==========================================================
# 22. Data Engineering Example
# Detect Invalid Countries
# ==========================================================

incoming_countries = {
    "Canada",
    "USA",
    "Mars"
}

valid_countries = {
    "Canada",
    "USA",
    "India"
}

invalid_countries = (
    incoming_countries
    - valid_countries
)

print(invalid_countries)

# {'Mars'}

# ==========================================================
# 23. ETL Reconciliation
# ==========================================================

source_ids = {
    1,
    2,
    3,
    4,
    5
}

target_ids = {
    1,
    2,
    3
}

missing_records = (
    source_ids
    - target_ids
)

print(missing_records)

# {4, 5}

# ==========================================================
# 24. Records Present in Both Systems
# ==========================================================

source_ids = {
    1,
    2,
    3,
    4,
    5
}

target_ids = {
    3,
    4,
    5,
    6
}

common_records = (
    source_ids
    & target_ids
)

print(common_records)

# {3, 4, 5}

# ==========================================================
# 25. Hashability Rule
# ==========================================================

valid_values = {
    "Canada",
    "USA"
}

print(valid_values)

# ==========================================================
# 26. Unhashable Example
# ==========================================================

# This fails

# bad_set = {
#     [1, 2]
# }

# TypeError:
# unhashable type: 'list'

# ==========================================================
# 27. Frozenset
# ==========================================================

countries = frozenset(
    [
        "Canada",
        "USA",
        "India"
    ]
)

print(countries)

# ==========================================================
# 28. Frozenset Cannot Be Modified
# ==========================================================

# countries.add("Mexico")

# AttributeError

# ==========================================================
# 29. Performance Thinking
# ==========================================================

customer_ids = {
    101,
    102,
    103,
    104
}

customer_exists = (
    102 in customer_ids
)

print(customer_exists)

# Fast lookup due to hashing

# ==========================================================
# 30. Production Example
# Processed File Tracking
# ==========================================================

processed_files = {
    "customer_20260101.csv",
    "customer_20260102.csv",
    "customer_20260103.csv"
}

new_file = "customer_20260102.csv"

if new_file in processed_files:
    print(
        "Skip processing. "
        "File already processed."
    )

# ==========================================================
# 31. Set Comprehension
# ==========================================================

numbers = [1, 2, 2, 3, 3, 4]

unique_squares = {
    number ** 2
    for number in numbers
}

print(unique_squares)

# {1, 4, 9, 16}

# ==========================================================
# 32. Summary Example
# ==========================================================

customer_ids = [
    101,
    102,
    101,
    103,
    102
]

unique_customers = set(customer_ids)

print(
    f"Original Count: "
    f"{len(customer_ids)}"
)

print(
    f"Unique Count: "
    f"{len(unique_customers)}"
)
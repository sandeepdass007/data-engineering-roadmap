# Reference vs Copy

a = [1,2,3]
b = a

b.append(4)

print(a)  # Output: [1, 2, 3, 4]

# Creating a Real Copy

a = [1,2,3]

b = a.copy() # or b = list(a) or b = a[:]

b.append(4)
print(a)  # Output: [1, 2, 3]
print(b)  # Output: [1, 2, 3, 4]

# Shallow Copy vs Deep Copy

## Shallow Copy

employees = [
    ["John", 100000],
    ["Mike", 120000]
]

copy_employees = employees.copy()  # Shallow Copy

copy_employees[0][1] = 999999

print(employees)  # Output: [['John', 999999], ['Mike', 120000]]

## Deep Copy

import copy

employees = [
    ["John", 100000],
    ["Mike", 120000]
]

copy_employees = copy.deepcopy(employees)  # Deep Copy

copy_employees[0][1] = 888888

print(employees)  # Output: [['John', 100000], ['Mike', 120000]]

# enumerate() function

employees = ["John", "Mike", "Alice"]

for idx, employee in enumerate(employees):
    print(f"{idx}: {employee}")

# zip() function

name = ["John", "Mike", "Alice"]
salary = [100000, 120000, 90000]

for name, salary in zip(name, salary):
    print(f"{name}: {salary}")

# sort() vs sorted() -> sort() mutable while sorted() immutable and creates a new list

numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()  # Sorts the list in place
print(numbers)  # Output: [1, 2, 5, 5, 6, 9]

numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)  # Returns a new sorted list
print(sorted_numbers)  # Output: [1, 2, 5, 5, 6, 9]
print(numbers)  # Output: [5, 2, 9, 1, 5, 6] (original list remains unchanged)

# any() and all() functions
checks = [True, True, False]
print(any(checks))  # Output: True
print(all(checks))  # Output: False
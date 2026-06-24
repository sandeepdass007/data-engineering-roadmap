salaries = [100000, 120000, 90000, 110000]

print(f"Total salary: {sum(salaries)}")
print(f"Max salary: {max(salaries)}")
print(f"Min salary: {min(salaries)}")
print(f"Average salary: {sum(salaries) / len(salaries)}")

print("Second MINI Project.....")

employees = [
    ["John",100000],
    ["Mike",120000],
    ["Alice",90000],
    ["David",150000]
]

# Print all employee names.
names = [employee[0] for employee in employees]
print(f"Employee names: {names}")

salaries = [employee[1] for employee in employees]
print(f"Salary: {salaries}")

total_salary = sum(employee[1] for employee in employees)
print(f"Total salary: {total_salary}")

average_salary = total_salary / len(employees)
print(f"Average salary: {average_salary}")

incremented_salary = [employee[1] + employee[1] * 0.1 for employee in employees]
print(f"Incremented salaries: {incremented_salary}")

filtered_emp = [employee for employee in employees if employee[1] > 100000]
print(f"Employees with salary > 100000: {filtered_emp}")
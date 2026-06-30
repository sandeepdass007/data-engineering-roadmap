customers = [ { "customer_id": 101, "name": " john smith ", "country": "canada", "salary": 100000 }, { "customer_id": 102, "name": "ALICE", "country": "usa", "salary": 120000 }, { "customer_id": 103, "name": " mike ", "country": "india", "salary": 90000 } ]

print("Task 1 - Clean Customer Name")

def clean_name(name : str):
    cleaned_name = name.strip().title()
    return cleaned_name

print(clean_name(" john smith "))

print("Task 2 - Clean Country Name")

def clean_country(country: str):
    return country.title()

print(clean_country("canada"))

print("Task 3 - Calculate Bonus")

def calculate_bonus_100k(salary: int):
    return salary * 0.1;

def calculate_bonus(salary: int):
    if salary >= 100000:
        return calculate_bonus_100k(salary)
    else:
        return salary * 0.05;

print(calculate_bonus(100000))

print("Task 4 - Process a Single Customer")

def process_customer(customer: dict):
    return {
        "customer_id": customer["customer_id"],
        "name": clean_name(customer["name"]),
        "country": clean_country(customer["country"]),
        "salary": customer["salary"],
        "bonus": calculate_bonus(customer["salary"])
    }
customer_data = {
    "customer_id": 101,
    "name": "    john  smith    ",
    "country": "canada",
    "salary": 1000
}
print(f"Original Data - {customer_data}")
print(f"Updated and cleaned data - {process_customer(customer_data)}")

print("Task 5 - Process All Customers")

def process_all(customers: list[dict]) -> None:
    print("----------------------------------------\n" \
    "Customer Report\n" \
    "----------------------------------------\n")
    for customer in customers:
        print(process_customer(customer))
    print("----------------------------------------")

customers_data = [{
    "customer_id": 101,
    "name": "    john  smith    ",
    "country": "canada",
    "salary": 1000
},
{
    "customer_id": 102,
    "name": "    Sam  smith    ",
    "country": "ireland",
    "salary": 100000
}]

process_all(customers_data)

print("Stretch Goal 1")

def calculate_average_salary(customers: list[dict]):
    total_salary = sum(customer_data["salary"] for customer_data in customers)
    return total_salary / len(customers)

print(calculate_average_salary(customers_data))

print("Stretch Goal 2")

def highest_salary(customers: list[dict]):
    return max(customer_data["salary"] for customer_data in customers)

print(highest_salary(customers_data))

print("Stretch Goal 3")

def summary(customers: list[dict]):
    return {
        "total_customers": len(customers),
        "average_salary": calculate_average_salary(customers),
        "highest_salary": highest_salary(customers),
        "total_bonus": sum(calculate_bonus(customer_data["salary"]) for customer_data in customers)
    }

print(summary(customers_data))
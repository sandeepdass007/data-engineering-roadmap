customers = [ { "customer_id": 101, "name": "John", "country": "Canada", "balance": 1200, "active": True }, { "customer_id": 102, "name": "Alice", "country": "USA", "balance": 850, "active": False }, { "customer_id": 103, "name": "Mike", "country": "Canada", "balance": 3000, "active": True }, { "customer_id": 101, "name": "John", "country": "Canada", "balance": 1200, "active": True }, { "customer_id": 104, "name": "Sara", "balance": 500, "active": True }, { "customer_id": 105, "name": "David", "country": "India", "active": True } ]

print("Task 1 - Print Every Customer")

print("========================")

for customer_data in customers:
    print(f"Customer ID : {customer_data.get("customer_id")}")
    print(f"Name : {customer_data.get("name")}")
    print(f"Country : {customer_data.get("country")}")
    print(f"Balance : {customer_data.get("balance")}")
    print(f"Active : {customer_data.get("active")}")
    print("========================")

print("Task 2 - Validate Required Fields")

required_fields = [ "customer_id", "name", "country", "balance", "active" ]

for customer_data in customers:
    for required_field in required_fields:
        print(f"Customer: {customer_data.get("customer_id")}")
        print("Missing:")
        if not required_field in customer_data:
            print(required_field)
        
print("Task 3 - Count Customers by Country")
customers_metrics = {}

for customer_data in customers:
    country = customer_data.get("country", "Unknown")
    if country in customers_metrics:
        customers_metrics[country] += 1
    else:
        customers_metrics[country] = 1

print(customers_metrics)

print("Task 4 - Count Active vs Inactive Customers")

active_customers_metric = {
    True: 0,
    False: 0
}

for customer_data in customers:
    active_customers_metric[customer_data.get("active", False)] += 1

print(active_customers_metric)

comprehensive_dict_metric_valid_customers = {
    val : sum(1 for customer_data in customers if customer_data.get("active") == val)
    for val in [True, False]
}

print(comprehensive_dict_metric_valid_customers)

print("Task 5 - Average Balance")

avg_balance = sum(customer_data.get("balance", 0) for customer_data in customers) / len(customers)
print(avg_balance)

print("Task 6 - Detect Duplicate Customer IDs")

duplication_metric = {}

for customer_data in customers:
    customer_id = customer_data.get("customer_id")

    if customer_id in duplication_metric:
        duplication_metric[customer_id] += 1
    else:
        duplication_metric[customer_id] = 1;

duplicate_ids = {
    customer_id for (customer_id, occurrences) in duplication_metric.items() if occurrences > 1
}

print(duplicate_ids)

print("Task 7 - Create Processing Metadata")

countries_set = set()

countries_set = {customer_data.get("country") for customer_data in customers if customer_data.get("country") != None}

total_records = len(customers)
valid_records = sum(1 for customer_data in customers if customer_data.get("active", False) == True)
invalid_records = total_records - valid_records
duplicate_records = len(duplicate_ids)
countries_found = len(countries_set)

processing_metadata = {
    "total_records" : total_records,
    "valid_records": valid_records,
    "invalid_records": invalid_records,
    "duplicate_records": duplicate_records,
    "countries_found": countries_found,
    "average_balance": avg_balance
}

print(processing_metadata)

print("Task 8 - Function")

def process_customers(customers):
    return len(countries_found), duplicate_ids, processing_metadata

print("Task 9 - Final Report")

print("==========================================\n" \
"CUSTOMER API PROCESSING REPORT\n" \
"==========================================\n")

print(f"Total Records      : {total_records}")
print(f"Valid Records      : {valid_records}")
print(f"Invalid Records    : {invalid_records}")
print(f"Duplicate IDs      : {duplicate_ids}")

print("\nCountry Counts\n")

for country, occurrences in customers_metrics.items():
    print(f"{country} : {occurrences}")

print(f"Average Balance : {avg_balance}")

print("\n==========================================")
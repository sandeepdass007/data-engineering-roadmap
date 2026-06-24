source_customer_ids = [ 101, 102, 103, 104, 105, 105, 106, 106, 107 ]

target_customer_ids = [ 101, 102, 103, 107 ]

incoming_countries = [ "Canada", "USA", "India", "Mars", "Canada", "Jupiter" ]

valid_countries = { "Canada", "USA", "India" }

print("Task 1 - Remove Duplicates")

print(f"Unique Customer IDs : {set(source_customer_ids)}")

print("Task 2 - Find Duplicate Customer IDs")

duplicate_customer_ids_dict = {}
dup_cust_ids = set()

for id in source_customer_ids:
    if(id in duplicate_customer_ids_dict):
        duplicate_customer_ids_dict[id] = duplicate_customer_ids_dict[id] + 1
        dup_cust_ids.add(id)
    else:
        duplicate_customer_ids_dict[id] = 1

print(dup_cust_ids)

print("Task 3 - Missing Records")

print(set(source_customer_ids) - set(target_customer_ids))

print("Task 4 - Successfully Loaded Records")

print(set(source_customer_ids) & set(target_customer_ids))

print("Task 5 - Invalid Countries")

print(set(incoming_countries) - set(valid_countries))

print("Task 6 - Reconciliation Summary Function")

def generate_reconciliation_summary( source_ids, target_ids ):
    total_source_records = set(source_ids)
    total_target_records = set(target_ids)
    return len(total_source_records), len(total_target_records), len(total_source_records - total_target_records)

print(f"Reconciliation Summary: {generate_reconciliation_summary(source_customer_ids, target_customer_ids)}")

print("Task 7 - Stretch Goal")

print("================================")
print("ETL RECONCILIATION REPORT")
print("================================\n")

print(f"Total Source Records : {len(set(source_customer_ids))}")
print(f"Total Target Records : {len(set(target_customer_ids))}\n")

print("Missing Records:")
print(set(source_customer_ids) - set(target_customer_ids))

print("\nDuplicate IDs:")
print(dup_cust_ids)

print("\nInvalid Countries:")
print(set(incoming_countries) - set(valid_countries))

print("\n================================")
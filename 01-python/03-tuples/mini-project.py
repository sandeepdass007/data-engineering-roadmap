etl_results = [ ("customer_load", 1000, 5), ("employee_load", 1500, 2), ("sales_load", 5000, 20), ("inventory_load", 2500, 0) ]

print("Task 1 - Print all job results using tuple unpacking")

for job_name, processed, failed in etl_results:
    print(
        f"Job={job_name}, "
        f"Processed={processed}, "
        f"Failed={failed}"
    )

total_records_processed = sum((processed) for _, processed, _ in etl_results)

print(f"Task 2 - Total Records Processed={total_records_processed}")

total_failed_records = sum((failed_records) for _, _, failed_records in etl_results)

print(f"Task 3 - Total Failed Records={total_failed_records}")

sales_load = max((processed_count) for _, processed_count, _ in etl_results)

print(f"Task 4 - Max Records Processed={sales_load}")

inventory_load = ((job_name) for job_name, _, failed_count in etl_results if failed_count > 0)

print(f"Task 5 - Jobs with Failed Records={list(inventory_load)}")

def process_job(_job_name):
    return ((job_name, processed_rows, failed_rows) for (job_name, processed_rows, failed_rows) in etl_results if job_name == _job_name)

print(f"Task 6 - Process Job Results for 'sales_load'={list(process_job('sales_load'))}")
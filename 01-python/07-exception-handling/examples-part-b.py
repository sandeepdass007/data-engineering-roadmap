"""
============================================================
Topic 7: Exception Handling
Part B: else and finally
============================================================

Topics Covered
--------------
1. else block
2. finally block
3. Resource cleanup
4. File handling example
5. Database connection example
6. Best practices

Run one example at a time.
Comment/uncomment sections while practicing.
"""

# ============================================================
# Example 1 - else Block
# ============================================================

print("\n===== Example 1: else Block =====")

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")

else:
    print(f"You entered: {number}")

"""
Try:

25
ABC

Notice that else executes only when
no exception occurs.
"""

# ============================================================
# Example 2 - finally Block
# ============================================================

print("\n===== Example 2: finally Block =====")

try:
    print("Inside try block.")

finally:
    print("Inside finally block.")

"""
finally always executes.
"""

# ============================================================
# Example 3 - except + finally
# ============================================================

print("\n===== Example 3: except + finally =====")

try:
    result = 100 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Cleanup completed.")

# ============================================================
# Example 4 - else + finally
# ============================================================

print("\n===== Example 4: else + finally =====")

try:
    age = int(input("Enter age: "))

except ValueError:
    print("Invalid age.")

else:
    print("Age accepted.")

finally:
    print("Program finished.")

# ============================================================
# Example 5 - File Cleanup
# ============================================================

print("\n===== Example 5: File Cleanup =====")

file = None

try:
    file = open("sample.txt", "r")

    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    if file:
        file.close()
        print("File closed.")

"""
The file is closed whether reading succeeds
or fails.
"""

# ============================================================
# Example 6 - Database Connection (Simulation)
# ============================================================

print("\n===== Example 6: Database Cleanup =====")


class FakeConnection:

    def close(self):
        print("Database connection closed.")


connection = None

try:
    connection = FakeConnection()

    print("Running database query...")

except Exception as error:
    print(error)

finally:
    if connection:
        connection.close()

# ============================================================
# Example 7 - ETL Cleanup Example
# ============================================================

print("\n===== Example 7: ETL Cleanup =====")

csv_file = None

try:
    csv_file = open("customers.csv")

    print("Reading customer records...")

except FileNotFoundError:
    print("Input file not found.")

finally:
    if csv_file:
        csv_file.close()
        print("CSV file closed.")

"""
Production idea:

Open Resource
      ↓
Process
      ↓
Exception?
      ↓
finally
      ↓
Release Resource
"""

# ============================================================
# Summary
# ============================================================

print("\n===== Summary =====")

print("""
Key Takeaways

1. else executes only when no exception occurs.
2. finally always executes.
3. Use finally for cleanup.
4. Keep try blocks small.
5. Release resources such as files,
   database connections and temporary files.
""")
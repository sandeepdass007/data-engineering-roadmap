"""
=========================================================
Topic 7 - Exception Handling
Part A - Basic Exception Handling
=========================================================

Topics Covered
--------------
1. What is an exception?
2. Basic try-except
3. Handling ValueError
4. Handling Multiple Exceptions
5. Capturing Exception Objects
6. Generic Exception Handling

Run this file section by section.
"""

# =========================================================
# Example 1 - Program Without Exception Handling
# =========================================================

print("=" * 60)
print("Example 1 - Without Exception Handling")
print("=" * 60)

# Uncomment to test.
#
# number = int(input("Enter a number: "))
# print(number)

"""
Try inputs:

10

ABC

Observe what happens.
"""

# =========================================================
# Example 2 - Basic try-except
# =========================================================

print("\n" + "=" * 60)
print("Example 2 - Basic try-except")
print("=" * 60)

try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")

except ValueError:
    print("Invalid integer.")

# =========================================================
# Example 3 - Multiple Exceptions
# =========================================================

print("\n" + "=" * 60)
print("Example 3 - Multiple Exceptions")
print("=" * 60)

try:
    age = int(input("Enter age: "))
    result = 100 / age

    print(result)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Age cannot be zero.")

# Test with:
#
# ABC
#
# 0
#
# 25

# =========================================================
# Example 4 - Capturing Exception Object
# =========================================================

print("\n" + "=" * 60)
print("Example 4 - Exception Object")
print("=" * 60)

try:
    number = int(input("Enter a number: "))

except ValueError as error:
    print("Exception message:")
    print(error)

# =========================================================
# Example 5 - Dictionary Example
# =========================================================

print("\n" + "=" * 60)
print("Example 5 - KeyError")
print("=" * 60)

customer = {
    "id": 101,
    "name": "John"
}

try:
    print(customer["salary"])

except KeyError as error:
    print(f"Missing key: {error}")

# =========================================================
# Example 6 - Generic Exception
# =========================================================

print("\n" + "=" * 60)
print("Example 6 - Generic Exception")
print("=" * 60)

try:
    number = int(input("Enter a number: "))
    print(100 / number)

except Exception as error:
    print("Something went wrong.")
    print(error)

"""
Example Inputs

Input: ABC

Output:
invalid literal for int() ...

----------------------------

Input: 0

Output:
division by zero
"""

# =========================================================
# Example 7 - Why Bare except is Discouraged
# =========================================================

print("\n" + "=" * 60)
print("Example 7 - Bare except")
print("=" * 60)

try:
    number = int("ABC")

except:
    print("Something failed.")

"""
Works...

But gives us no useful debugging information.

Better:

except Exception as error:
    print(error)
"""

# =========================================================
# Summary
# =========================================================

"""
Key Takeaways
-------------

✔ Use try for risky code.

✔ Catch specific exceptions whenever possible.

✔ Use multiple except blocks for different failures.

✔ Capture the exception object using:
      except Exception as error

✔ Avoid bare except.

✔ Good exception handling improves debugging and
   application reliability.
"""
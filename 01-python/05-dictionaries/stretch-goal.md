# Stretch Goal

Suppose tomorrow the API adds a new field:

"email"

or removes the field:

"balance"

Answer:

## 1. Which parts of your code continue to work without changes?
So the code where the the `get()` function is being used should be working fine as long as default value is being passed along.

## 2. Which parts require modification?
So the part of code where the `[]` braces were beign used should be updated to `get()` by providing the default values.

## 3. Why is dict.get() valuable for evolving APIs?
Because it return `None` rather than raising any error or exception. It is safe to use. Also we can provide default values.
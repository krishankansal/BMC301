"""The join() method in Python combines elements from an iterable (like a list or tuple) into a single string using a specified separator. It's the most efficient way to concatenate multiple strings together.

Syntax
The basic syntax is: separator.join(iterable)"""

"""1. Join with space:"""

words = ["Hello", "world", "Python"]
result = " ".join(words)
print(result)
# Output: "Hello world Python"

"""2. Join with comma:"""

fruits = ["apple", "banana", "orange"]
result = ",".join(fruits)
print(result)
# Output: "apple,banana,orange"

"""3. Join with no separator:"""

letters = ["P", "y", "t", "h", "o", "n"]
result = "".join(letters)
print(result)
# Output: "Python"

"""4. Join with custom separator:"""

data = ["name", "age", "city"]
result = " | ".join(data)
print(result)
# Output: "name | age | city"

"""Common Use Cases
Creating CSV data: Building comma-separated values for file output"""

headers = ["Name", "Age", "City"]
csv_line = ",".join(headers)
print(csv_line)
# Output: "Name,Age,City"

"""Email processing:Constructing email addresses from components"""

email_parts = ["username", "domain.com"]
email = "@".join(email_parts)
print(email)

"""Important Notes
   ---------------
All elements in the iterable must be strings - otherwise Python raises a TypeError
For non-string values, convert them first: ",".join(str(x) for x in numbers)"""

lst=[1,2,3,4,5,6,7,8,9]
# result = ",".join(l) --- ERROR ---
result = ",".join([str(x) for x in lst])
print(result)

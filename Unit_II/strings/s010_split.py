"""The split() method in Python divides a string into a list of substrings based on a specified delimiter. It's one of the most commonly used string methods for text processing and data manipulation."""

""" 1. Default splitting (whitespace): """
text = "Hello world Python"
result = text.split()
print(result)
# Output: ['Hello', 'world', 'Python']

""" 2. Custom separator: """
fruits = "apple,banana,orange"
result = fruits.split(",")
print(result)
# Output: ['apple', 'banana', 'orange']

""" 3. With max split: """
data = "one-two-three-four"
result = data.split("-", 2)
print(result)
# Output: ['one', 'two', 'three-four']

"""Common Use Cases
Processing CSV-like data:
Split comma-separated values for data parsing"""

user_info = "John,25,Engineer"
name, age, job = user_info.split(",")
print(name, age, job)

"""File path manipulation:
Separating directory paths or file extensions"""
filepath = "/home/user/document.txt"
parts = filepath.split("/")
print(parts)

"""Email processing:
Extracting username and domain from email addresses"""

email = "user@domain.com"
username, domain = email.split("@")
print(username, domain)





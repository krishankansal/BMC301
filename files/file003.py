""" Reading Files
Python provides several methods to read file content"""

# Method 1: read() - reads entire file
with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)


# Method 2: read(size) - reads specified number of characters
with open('sample.txt', 'r') as file:
    first_10_chars = file.read(10)
    print(first_10_chars)

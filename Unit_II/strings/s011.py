# Searching and validation
text = "  Hello Python World!  "

#index() raises ValueError if substring not found, find() returns -1
print(f"Find 'Python': {text.find('Python')}")
print(f"Index 'World': {text.index('World')}")
print(f"Count 'l': {text.count('l')}")
print(f"Starts with '  H': {text.startswith('  H')}")
print(f"Ends with '!  ': {text.endswith('!  ')}")

# 3. Indexing and Slicing
# Python strings support zero-based indexing with negative indices
# counting from the end, plus slicing operations that extract substrings
# using start:stop:step syntax.[

text = "Python Programming"
print(f"Original: {text}")
print(f"Length: {len(text)}")

# Basic slicing
print(f"First 6 chars: {text[:6]}")
print(f"Last 11 chars: {text[7:]}")
print(f"Middle part: {text[3:10]}")

# Advanced slicing with steps
print(f"Every second char: {text[::2]}")
print(f"Reverse string: {text[::-1]}")
print(f"Every 3rd char backwards: {text[::-3]}")

# Edge cases
print(f"Empty slice: '{text[5:5]}'")
print(f"Beyond bounds: '{text[100:200]}'")
print(f"Negative step slice: {text[10:3:-1]}")


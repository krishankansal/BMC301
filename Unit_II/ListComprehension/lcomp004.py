# Example: Nested IF with List Comprehension

num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

# When we run the above program, the output will be:

# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# Here, list comprehension checks:

# Is y divisible by 2 or not?
# Is y divisible by 5 or not?
# If y satisfies both conditions, y is appended to
num_list = [y for y in range(100) if y % 2 == 0 or y % 5 == 0]
print(num_list)
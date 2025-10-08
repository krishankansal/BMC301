""" Writing Multiple Lines """

# Method 1: Using writelines() with a list
lines_to_write = ['First line\n', 'Second line\n', 'Third line\n']
with open('multiple_lines.txt', 'w') as file:
    file.writelines(lines_to_write)

# Method 2: Using a loop
data = ['Apple', 'Banana', 'Cherry']
with open('fruits.txt', 'w') as file:
    for fruit in data:
        file.write(f"{fruit}\n")

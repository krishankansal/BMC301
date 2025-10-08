""" Read Line by Line """

# Method 1: readline() - reads one line at a time
with open('sample.txt', 'r') as file:
    first_line = file.readline()
    second_line = file.readline()
    print(f"Line 1: {first_line.strip()}")
    print(f"Line 2: {second_line.strip()}")

# Method 2: readlines() - reads all lines into a list
with open('sample.txt', 'r') as file:
    all_lines = file.readlines()
    print(all_lines)

    for line in all_lines:
        print(line)

# Method 3: Iterating over file object
with open('sample.txt', 'r') as file:
    print(file)
    for line in file:
        print(line)

"""
Writing Files
Writing to files involves using the write() method or related functions :
"""

# Writing strings to a file
with open('output.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is a sample file.\n')

    # write() returns the number of characters written
    chars_written = file.write('Python file handling\n')
    print(f"Characters written: {chars_written}")

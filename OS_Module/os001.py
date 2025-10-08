"""The os module in Python is a built-in standard library module that provides a portable way to interact with the operating system."""

"""OS-Module Functions
Some important functions of the Python os module:

1. Handling the Current Working Directory
2. Creating a Directory
3. Listing out Files and Directories with Python
4. Deleting Directory or Files using Python
5. File Permissions and Metadata"""
import os
print(os.name)  # 'nt' for Windows, 'posix' for Unix/Linux/macOS

# Use case: Platform-specific code
if os.name == 'nt':
    print("Running on Windows")
    print("separator = '\\'")
elif os.name == 'posix':
    print("Running on Unix-like system")
    print("separator = '/'")
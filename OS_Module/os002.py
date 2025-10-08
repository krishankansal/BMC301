import os

# Get current directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

"""Change directory"""
os.chdir(r"D:\BMC301\OS_Module\one")
print(f"New directory: {os.getcwd()}")

""" To Create New Direcory"""
# os.mkdir("new_folder")

"""Change back"""
os.chdir(current_dir)

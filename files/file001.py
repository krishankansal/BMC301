"""File I/O (Input/Output) in Python allows programs to read data from files and write data to files"""

"""Opening Files"""
""" SYNTAX
--------------------------------------
file_object = open('filename', 'mode') 
--------------------------------------
"""

# Open a file in read mode (default)
file = open('sample.txt', 'r')
print("File opened:", file.name)
print("Mode:", file.mode)
file.close()

"""
Mode  |  Description      |  File Status              |  Starting Position
------+-------------------+---------------------------+-------------------
'r'   |  Read only        |  File must exist          |  Beginning        
'w'   |  Write only       |  File created or emptied  |  Beginning        
'a'   |  Append only      |  File created or exists   |  End              
'r+'  |  Read and write   |  File must exist          |  Beginning        
'w+'  |  Write and read   |  File created or emptied  |  Beginning        
'b'   |  Binary mode      |  Used with other modes    |  -                
"""

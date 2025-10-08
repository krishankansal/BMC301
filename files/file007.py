""" Appending to Files """

# Append mode adds content without overwriting
with open('log.txt', 'a') as file:
    file.write('New log entry\n')
    file.write('Another entry\n')

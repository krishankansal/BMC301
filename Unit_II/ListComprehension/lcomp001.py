# A list comprehension is a concise way to create lists using a single line of code.
# It combines a for loop, optional if conditions, and an expression.
#
# General syntax:
# [expression for item in iterable if condition]


lst = []
for x in range(1,11):
    lst.append(x)
print(lst)  # Output :[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list of numbers 0 - 10
lst = [x for x in range(1,11)]
print(lst)  # Output :[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#

squares = []
for i in range(10):
    squares.append(i * i)

# print(squares)
# #Output : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#
squares = [i*i for i in range(10)]
print(squares)
# #Output : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]







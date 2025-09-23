# How reduce() works:
# 1. It takes two main arguments: a function (typically a lambda function) and an iterable.
#
# 2. The function is applied to the first two elements of the iterable.
#
# 3. The result of this operation then becomes the first argument for the next application of the function, with the next element from the iterable serving as the second argument.
#
# 4. This process continues until all elements in the iterable have been processed, and a single, final value is returned.

from functools import reduce

numbers = [1, 2, 3, 4, 5,10,34,56]

# Define a lambda function to add two numbers
# x represents the accumulated result, y represents the current element
sum_of_numbers = reduce(lambda x, y: x + y, numbers)

print(f"The sum of the numbers is: {sum_of_numbers}")

#----------------- OR --------------------------------
from functools import reduce
def add(x, y):
    return x + y

a = [1, 2, 3, 4, 5,10,34,56]
res = reduce(add, a)
print(res)
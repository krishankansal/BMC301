# map()
# What it does (short): applies a function to every item of one or more iterables
# and returns an iterator of results.
#
# Signature: map(func, iterable, *more_iterables)
#
# Key points
# -----------
# In Python 3 map() returns a lazy iterator (not a list).
# Use list(...) to see results.
#
# If you pass multiple iterables, func is called with one argument from each;
# iteration stops at the shortest iterable.

nums = [1, 2, 3, 4]

# 1) named function
def double(x):
    return x * 2

print(list(map(double, nums)) ) # -> [2, 4, 6, 8]

# # 2) lambda
print(list(map(lambda x: x * 2, nums)))  # -> [2, 4, 6, 8]

# 3) multiple iterables
a = [1, 2, 3,4,5]
b = [10, 20, 30,40]
print(list(map(lambda x, y: x + y, a, b)))  # -> [11, 22, 33]

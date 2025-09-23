# filter()
#
# keeps items from an iterable for which a predicate function returns True.
# Returns a lazy iterator.
#
# Signature: filter(func, iterable)
from itertools import count

nums = [10, 25, 30, 444, 567, 6,33,78,21,30,56,45,25]

# Keep only even numbers
evens = list(filter(lambda x : x >= 30 and x <=100, nums))
print(evens)
print(len(evens))
print(sum(evens))
# -> [2, 4, 6]

# Use cases
# ----------
# Cleaning datasets (remove missing/falsy values).
# Select rows/records matching a condition (age > 18).

# zip() function takes a number of iterables and then creates a
# tuple containing each of the elements in the iterables.
str = ['a','b','c','d','e']
num = [1,2,3,4,5]
x = list(zip(num, str))
print(x)
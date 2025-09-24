# Combining filter and map

# Sum of squares of even numbers from 0 - 20
def square(x):
    return (x*x)

def iseven(x):
    return(x % 2 == 0)


lst = list(map(square, filter(iseven, range(20))))
print(lst)

# Try using lambda function
lst = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, range(20))))
print(lst)

# Try with list comprehension
lst = [x*x for x in range(20) if x%2 == 0]
print(lst)

# 3. Lambda inside another function

def make_multiplier(n):
    return lambda x: x * n   # closure

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # -> 10
print(triple(5))  # -> 15

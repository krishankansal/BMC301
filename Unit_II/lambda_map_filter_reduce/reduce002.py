from functools import reduce
li = ["if", "for", "while"]
res = reduce(lambda x, y: x + " " + y, li)
print(res)
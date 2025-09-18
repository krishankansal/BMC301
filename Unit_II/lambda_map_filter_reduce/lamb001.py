# What is a Lambda Function?
#
# A lambda function is a small anonymous function (function without a name).

# It can take any number of arguments, but has only one expression.

# Syntax:
# lambda arguments: expression
# 1. Basic lambda
# Normal function
def square(x):
    return x * x

# Lambda function
sq = lambda x: x * x

print(square(5))  # -> 25
print(sq(5))      # -> 25

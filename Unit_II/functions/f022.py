# Lets move one step further and cover the topic
#
# 3. Function can also return a function.
# This is also knows as Closures and Factory Functions.
#
# However, for the case of closures, one must use the nested functions.
#
# The following are the conditions that are required to be met in order to create a closure in Python:
#
# 	1 There must be a nested function
# 	2. The enclosing function has to return the nested function

def outer(text):
    text = text

    def inner():
        print(text)

    return inner  # Note we are returning function WITHOUT parenthesis


funct = outer('Example of closure')
funct()

# **************************************************
# As observed from above code, closures help to invoke function outside their scope.
# The function inner function has its scope only inside the outer Function.
# But with the use of closures we can easily extend its scope to invoke a function outside
# its scope.
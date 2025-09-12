# We have so far studied that
# 1. Function can be assigned to a variable.

# now we will look into

# 2. Function can be declared with in some function(nested function).
# 	or Function inside Function

def outer():

    def inner():
        print("Hi, it's me 'inner'")
        print("Thanks for calling me")

    print("This is the function 'outer'")
    print("I am calling 'inner' now:")
    inner()


outer()

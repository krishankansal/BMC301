def a():
    print("Hi, it's me 'a()'")
    print("Thanks for calling me")


def b(x):
    print("Hi, it's me 'b()'")
    print("I will call 'a()' now")
    x()
    # If we need to know what the 'real' name of func
    print("func's real name is " + x.__name__)
    return x

# b(a)
y = b(a)
y()

def a():
    print("Hi, it's me 'a()'")
    print("Thanks for calling me")


def b(f):
    print("Hi, it's me 'b()'")
    print("I will call 'a()' now")
    f()
    # If we need to know what the 'real' name of func
    print("func's real name is " + f.__name__)

b(a)

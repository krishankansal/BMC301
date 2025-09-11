def outer():

    def inner():
        print("Hi, it's me 'inner'")
        print("Thanks for calling me")

    print("This is the function 'outer'")
    print("I am calling 'inner' now:")
    inner()


outer()

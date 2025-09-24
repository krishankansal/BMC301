def get_loaded(func):
    def inner():
        print("First line added")
        func()
        print("I am loaded")
    return inner


@get_loaded
def rifle():
    print("T-5000 sniper rifle")


rifle()

# # let's decorate this ordinary function
# rifle = get_loaded(rifle)
# rifle()

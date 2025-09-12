# Delete the function call of output() in the last
def outer():  # outer function
    print("Hello from outer function")

    def inner():  # inner function
        print("Hello from inner function")
    inner()

outer()
# Try: all will generate error
# outer.inner
# outer.inner()
# outer().inner
# outer().inner()

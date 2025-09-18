def login_required(func):
    def check():
        print("You are logged in")
        func()
        print("You are logged out")
    return check

@login_required
def view_product():
    print("I am viewing page")

@login_required
def purchase():
    print("I am purchasing page")


view_product()
print("*"*20)
purchase()
def autheticate(func):
    def inner(user):
        if user == 'kkk':
            print('Welcome', user)
            func(user)
        else:
            print('Please Login')
    return inner


@autheticate
def login(user):
    print("You Got an Email")


login('kkk')

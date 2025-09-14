def master_python(func):
    def python():
        func()
        print('Now Expert In Python')
    return python


def master_django(func):
    def django():
        func()
        print('Now Expert In Django')
    return django

# programmer = master_django(programmer)
# programmer = master_python(programmer)
@master_django
@master_python
def programmer():
    print('I know programming concepts')


programmer()

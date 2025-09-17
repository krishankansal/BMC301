
def has_permission(page_url):
    def inner(username):
        if username == 'Admin':
            return f"'{username}' does have access to {page_url}."
        else:
            return f"'{username}' does NOT have access to {page_url}."
    return inner


x = has_permission('http://www.banking.com')
print(x('Admin'))

y = has_permission('http://www.banking.com')
print(y('xyz'))

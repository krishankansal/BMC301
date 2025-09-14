
def has_permission(page):
    def inner(username):
        if username == 'Admin':
            return f"'{username}' does have access to {page}."
        else:
            return f"'{username}' does NOT have access to {page}."
    return inner


current_user = has_permission('Admin Area')
print(current_user('Admin'))

random_user = has_permission('Admin Area')
print(random_user('Not Admin'))

# Extract the domain from an email address using slicing

def extract_domain(email):
    at_index = email.find('@')
    if at_index != -1:
        return email[at_index + 1:]
    return ""

def extract_user(email):
    at_index = email.find('@')
    if at_index != -1:
        return email[:at_index]
    return ""

print(extract_domain("user@example.com"))  # Output: example.com
print(extract_user("user@example.com"))


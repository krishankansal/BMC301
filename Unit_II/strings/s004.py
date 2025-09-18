# Extract the domain from an email address using slicing

def extract_domain(email):
    at_index = email.find('@')
    if at_index != -1:
        return email[at_index + 1:]
    return ""

print(extract_domain("user@example.com"))  # Output: example.com


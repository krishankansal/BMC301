# Implement a function to check if a string is a palindrome using slicing

def is_palindrome(s):
    cleaned = s.lower().replace(' ', '')
    return cleaned == cleaned[::-1]

print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("A man a plan a canal Panama"))  # Output: False (spaces matter)

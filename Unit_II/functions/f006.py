# Function with Default Parameters

def introduce(name, age=25, city="Unknown"):
    print(f"Hi, I'm {name}, {age} years old, from {city}")

introduce("Alice")  # Output: Hi, I'm Alice, 25 years old, from Unknown

introduce("Bob", 30)  # Output: Hi, I'm Bob, 30 years old, from Unknown

introduce("Charlie", 28, "New York")  # Output: Hi, I'm Charlie, 28 years old, from New York


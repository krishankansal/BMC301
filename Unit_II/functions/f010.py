# Function with **kwargs (Keyword Arguments)

def create_profile(**details):
    print("User Profile:")
    for key, value in details.items():
        print(f"  {key.capitalize()}: {value}")

create_profile(name="Alice", age=30, profession="Engineer", city="Mumbai")
# Output:
# User Profile:
#   Name: Alice
#   Age: 30
#   Profession: Engineer
#   City: Mumbai

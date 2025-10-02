import random

lower_bound = 1
upper_bound = 100

# Generate a random number within the specified range
secret_number = random.randint(lower_bound, upper_bound)
print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")

attempts = 0
while True:

        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
   

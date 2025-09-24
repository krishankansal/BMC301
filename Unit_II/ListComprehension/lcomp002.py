letters = []

for letter in 'human':
    letters.append(letter)

print(letters)  # Output : ['h', 'u', 'm', 'a', 'n']

letters = [letter for letter in 'human']
print(letters)  # Output : ['h', 'u', 'm', 'a', 'n']

# even less code
letters = list(map(lambda x: x, 'human'))
print(letters)

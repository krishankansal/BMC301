# Example : if...else With List Comprehension

obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
print(obj)

# When we run the above program, the output will be:
# ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']

# Here, list comprehension will check the 10 numbers from 0 to 9. 
# If i is divisible by 2, then Even is appended to the obj list. 
# If not, Odd is appended.

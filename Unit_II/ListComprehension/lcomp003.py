#Using if with List Comprehension
# even numbers between 0 - 19

even_squares = []
for x in range(1,21):
    if x % 2 == 0:
        even_squares.append(x**2)
print(even_squares)

number_list = [x**2 for x in range(1,21) if x % 2 == 0]
print(number_list)

number_list = list(map(lambda z: z**2,filter(lambda y : y % 2 == 0, range(1,21))))
print(number_list)
# Outout:
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

multiplication_table = [[i * j for j in range(1, 5)] for i in range(1, 6)]
print(multiplication_table)

multiplication_table = [tuple(i * j for j in range(1, 5)) for i in range(1, 6)]
print(multiplication_table)

multiplication_table = [tuple([i * j for j in range(1, 5)]) for i in range(1, 6)]
print(multiplication_table)


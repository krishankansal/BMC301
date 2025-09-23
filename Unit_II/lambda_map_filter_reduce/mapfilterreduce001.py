from functools import reduce

students = [
    {"name": "Asha", "score": 45},
    {"name": "Ravi", "score": 67},
    {"name": "Neha", "score": 82},
    {"name": "Jon",  "score": 40}
]

# Filter passed students -> map to scores -> reduce to total
passed_scores = map(lambda s: s['score'],
                    filter(lambda s: s['score'] >= 50, students))

total_passed = reduce(lambda a, b: a + b, passed_scores, 0)
print(total_passed)  # -> 67 + 82 = 149

# More pythonic: use generator + sum()
total_passed2 = sum(s['score'] for s in students if s['score'] >= 50)
print(total_passed2)  # -> 149 (clearer)

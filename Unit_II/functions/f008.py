# Funtions returning ditionary

def process_grades(grades):
    total = sum(grades)
    average = total / len(grades)
    highest = max(grades)
    lowest = min(grades)

    return {
        'total': total,
        'average': average,
        'highest': highest,
        'lowest': lowest
    }
student_grades = [85, 92, 78, 96, 88]
results = process_grades(student_grades)
print(results)
# Output: {'total': 439, 'average': 87.8, 'highest': 96, 'lowest': 78}

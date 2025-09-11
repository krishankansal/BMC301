# Function Returning Multiple Values

def calculate_circle(radius):
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference

x, y = calculate_circle(5)
print(f"Area: {x:.2f}, Circumference: {y:.2f}")
# Output: Area: 78.54, Circumference: 31.42

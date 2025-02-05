# Create a program to solve a quadratic equation and display the real roots (if any).

import math

# Function to solve the quadratic equation
def solve_quadratic(a, b, c):
    # Calculate the discriminant formula D = b^2 - 4ac
    discriminant = b**2 - 4*a*c
    
    # Check if the discriminant is positive, zero, or negative
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"The equation has two real roots: {root1} and {root2}"
    
    elif discriminant == 0:
        root = -b / (2*a)
        return f"The equation has one real root: {root}"
    
    else:
        return "The equation has no real roots"

# Example usage
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

result = solve_quadratic(a, b, c)
print(result)

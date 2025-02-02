# Develop a function to find the GCD (Greatest Common Divisor)

# Initializing variable for taking input
m = int(input("Enter your first number: "))
n = int(input("Enter your second number: "))
for num in range(1,min(m,n) + 1):
    if m % num == 0 and n % num == 0:
        gcd = num
print(f'{m} and {n} GCD is : {gcd}')


# LCM (Least Common Multiple) of two numbers.

# Initializing lowest Common Multiple as LCM
LCM = (m*n) // gcd
print(f'{m} and {n} LCM is : {LCM}')
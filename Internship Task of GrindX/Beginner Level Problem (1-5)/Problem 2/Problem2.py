# Create a function to calculate the factorial of a given number
# Taking input from user
number = int(input("Enter your number: "))
# Define function for factorial
def factorial(number):
    fact = 1
    while True:
    # Checking if the number is negative or not
     if number < 0:
         print("Invalid Input")
         number = int(input("Enter your number: "))
     else:
            for i in range(1,number+1):
                fact *= i
            return f'Factorial of {number} is {fact}'
    
print(factorial(number))
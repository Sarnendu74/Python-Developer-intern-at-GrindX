# Write a program to check if a number is even or odd

# Define function for checking number even or odd
def evenORodd(number):
    if number % 2 == 0:
        print("Number is Even.")
    else:
        print("Number is Odd.")

# Initialize number
number = int(input("Enter your number: "))
# Calling Function
evenORodd(number)

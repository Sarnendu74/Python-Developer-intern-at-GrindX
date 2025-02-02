# Write a program to print the Fibonacci sequence up to a given number of terms.
n = int(input("Enter your number: "))
# define fibonacci function 
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(n)  

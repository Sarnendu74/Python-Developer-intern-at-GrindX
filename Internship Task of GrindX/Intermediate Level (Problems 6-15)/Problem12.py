# Create a program to calculate the sum of all prime numbers within a given range.
# Function to check if a number is prime
def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count == 2  # Returns True if prime, False otherwise

# Function to calculate the sum of prime numbers in a given range
def sum_of_primes(start, end):
    total = 0
    for num in range(start, end + 1):
        if is_prime(num):
            total += num
    return total

# Taking user input for range
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Calculating and printing the sum of prime numbers in the range
result = sum_of_primes(start, end)
print(f"The sum of prime numbers between {start} and {end} is: {result}")

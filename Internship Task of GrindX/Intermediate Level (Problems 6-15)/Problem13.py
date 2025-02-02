# Write a function to generate a random password of a given length with alphanumeric characters.
import random
import string

def generate_password(length):
    # Define possible characters (uppercase, lowercase, digits)
    characters = string.ascii_letters + string.digits
    
    # Generate password by randomly selecting from characters
    password = ''.join(random.choices(characters, k=length))
    
    return password

# Taking user input for password length
length = int(input("Enter the desired password length: "))
print("Generated Password:", generate_password(length))

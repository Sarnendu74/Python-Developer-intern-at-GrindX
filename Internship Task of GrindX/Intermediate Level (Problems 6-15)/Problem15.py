# Write a program to convert a given decimal number to binary, octal, and hexadecimal formats
def convert_number(decimal):
    binary = bin(decimal)[2:]  # Convert to binary and remove '0b'
    octal = oct(decimal)[2:]   # Convert to octal and remove '0o'
    hexadecimal = hex(decimal)[2:].upper()  # Convert to hexadecimal and remove '0x', uppercase for readability
    
    return binary, octal, hexadecimal

# Input from user
decimal = int(input("Enter a decimal number: "))
binary, octal, hexadecimal = convert_number(decimal)

# Display results
print(f"Binary: {binary}")
print(f"Octal: {octal}")
print(f"Hexadecimal: {hexadecimal}")

# Write a program to reverse a string without using built-in functions
# defining function for reversed 
def reverse_string(s):
    reversed2 = s[::-1]
    return reversed2
# Test the function
s = input("Enter your string: ")
print("Reverse string :",reverse_string(s))
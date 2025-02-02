# Develop a function to check if a given string is a palindrome
st = input("Enter your string: ")
reverse = st[::-1]
if st == reverse:
    print("The string is a palindrome.")
else:
    print("The string is not palindrome.")
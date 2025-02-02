# Write a program to find the largest and smallest elements in a list
# initializing a list
lis =  [12,5,66,89,77]
# Taking first number of list for checking 
largest_element = lis[0]
smallest_element = lis[0]
for num in lis:
    # Checking as largest element in the list
    if num > largest_element:
        largest_element = num
    # Checking as smallest element in the list
    if num < smallest_element:
        smallest_element = num
        
# Displaying element
print(f'Biggest Number is: {largest_element}')
print(f'Smallest Number is: {smallest_element}')       
# Create a function to remove duplicate elements from a list while maintaining the order.
lis = [12, 55 , 98 ,77, 66 , 55,12]
def remove_duplicates(lst):
    seen = set()
    # Using list comprehension method 
    return [x for x in lst if not (x in seen or seen.add(x))]
# Test the function with the provided list
print(remove_duplicates(lis))  

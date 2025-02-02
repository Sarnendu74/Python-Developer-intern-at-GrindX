# Develop a program to find the second largest element in a list.
lis = [12,10,55,88,66]
def largest_second_element(lis):
    lis.sort(reverse = True)
    return lis[1]
largest_second_element(lis)
print(f"Largest second element in {lis} is {largest_second_element(lis)}")
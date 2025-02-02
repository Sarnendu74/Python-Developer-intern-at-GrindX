# Write a program to check if a number is prime or not 
# Initializing num
num = int(input("Enter Your Number: "))
# Assuming counter
count = 0
for i in range(1,num+1):
    if (num % i == 0):
        count += 1
if count == 2 :
    print("Number is Prime.")
else:
    print("Number is not Prime.")
    

# Write a program to find the transpose of a given matrix.
# Our Matrix Print
print("-----------------------------Matrix------------------------------")

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j],end=" ")
    print()
    

print("-----------------------------Transpose Matrix------------------------------")


# Transpose Matrix
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[j][i],end=" ")
    print()
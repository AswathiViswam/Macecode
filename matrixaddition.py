"""Imagine you are helping a student with their mathematics homework which involves a lot of problems based on matrix addition. You decide to write a program to automate the task of adding two matrices, which would make the homework a breeze!

Write a program to add two matrices. The program should:

Prompt the user to enter the dimensions of the matrices (assume both matrices have the same dimensions).

Accept the elements of the two matrices from the user.

Display the two matrices.

Add the two matrices.

Print the resultant matrix.

Kindly check the sample test case for input and output format."""

rows, columns = map(int, input().split())
mata = [[]]
matb = [[]]

mata = [list(map(int,input().split())) for i in range(rows)]


matb= [list(map(int,input().split())) for i in range (rows)]
result = [[0 for _ in range(columns)]for _ in range(rows)]
for i in range (rows):
    for j in range(columns):
        result[i][j] = mata[i][j]+ matb[i][j]
print("first matrix: ")
for row in mata:
    print(*row)
print("second matrix:")
for row in matb:
    print(*row)
print("sum of the two matrices is:")
for row in result:
    print(*row)

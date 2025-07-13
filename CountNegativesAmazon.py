"""Read the following input: an integer n representing the number of rows in the matrix, and an integer m representing the number of columns in the matrix and the values of the matrix (n rows and m columns).
The matrix is sorted such that all elements in any row are sorted in increasing order from left to right, and all elements in any column are sorted in increasing order from top to bottom. You should print the total number of negative numbers present in the matrix.
The input will be provided as follows:
The first line of input contains a single integer n, the number of rows in the matrix.
The second line of input contains a single integer m, the number of columns in the matrix.
The next n lines each contain m integers separated by spaces, representing the elements of the matrix.
Solve this problem with a complexity less than m+n.
Input Format
3
4
-4 -3 -1 1
-2 -2 1 3
-1 1 2 4"""
rows = int(input())
columns = int(input())
c=0
for i in range(rows):
    row = list(map(int,input().split()))
    for v in row:
        if v<0:
            c +=1            
print(c)



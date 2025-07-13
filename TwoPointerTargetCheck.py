"""Given a sorted (in ascending order) integer array nums of n elements and a target value, find if there exists any pair of elements (nums[i], nums[j], i!=j) such that their sum is equal to target.
Solve this problem using the Two-pointers concept. The complexity should not be O(N-square) or more
Input Format
5
-3 -1 0 1 2
-2"""
n = int(input())
lis = list(map(int,input().split()))
target = int(input())
j = len(lis)-1
i = 0
flag = 0
while i < j:
    if lis[i]+lis[j] > target:
        j-=1
    elif lis[i]+lis[j]< target:
        i+=1
    else: 
        print("Yes")
        flag = 1
        break
        
if flag!=1:
    print("No")


    

"""Given an integer array nums, print "true" if any value appears at least twice in the array, and print "false" if every element is distinct.
Read n, the number of values in the first line, followed by the n numbers in the next line.
Input Format
4 1 2 3 1
Constraints
NA
Outp'ut Format
true"""
n = int(input())
s = list(map(int,input().split()))
a = len(s)
b = len(set(s))
if a == b:
    print("false")
else:
    print("true")

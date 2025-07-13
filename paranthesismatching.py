#Given an input of string in combinations of characters '{' and '}', which are parenthesis, you have to find if the input is balanced or not.
#The input is balanced if all the opening curly braces are closed. You can't close a curly brace before it is opened.


a = input()
stack = []
for i in a:
    if i == '{':
        stack.append(i)
    else :
        if stack:
            stack.pop()
        else :
            print("Not Matching")
if not stack:
    print("Matching")
else :
    print("Not Matching")

""""Problem Restatement:
Input: A password string pwd of 0s and 1s.
Requirement:
Divide it into non-overlapping, even-length substrings.
Each substring must consist of only 0s or only 1s.
Task"""

def minflips(pwd):
    flips = 0
    for i in range(0,len(pwd),2):
        block = pwd[i:i+2]
    
        if len(block) == 2:
            if block[0] != block[1] :
                flips +=1
    return flips
passw = "10011100"
print(minflips(passw))
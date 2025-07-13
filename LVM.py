"""You are designing a virtual machine for a new programming language called Lombok. The Lombok Virtual Machine (LVM) runs an assembler-like machine code. It operates on a stack and a single register.
In detail, the instructions work as follows:
PUSH x: This instruction pushes a given integer onto the stack. If the stack for example looks like this: [2, 3] and the machine executes the instruction PUSH -11,the stack looks like this afterwards: [-11, 2, 3]
STORE: This instruction takes the topmost integer from the stack and stores it in the register. If the stack for example looks like this: [3, 9, 4], the register contains any integer, and the machine executes the instruction STORE, the stack looks like this afterwards: [9, 4] and the register contains the integer 3.
LOAD: This instruction copies the content of the register and pushes it onto the stack. If the register for example contains the integer 6, the stack looks like this: [8, 7], and the machine executes the instruction LOAD, the stack looks like this afterwards: [6, 8, 7], and the register still contains the integer 6.
PLUS: This instruction takes the two topmost integers from the stack, adds them, and pushes the resulting integer back onto the stack. If the stack for example looks like this: [2, 3, 4], and the machine executes the instruction PLUS, the stack looks like this afterwards: [5, 4]
TIMES: This instruction takes the two topmost integers from the stack, multiplies them, and pushes the resulting integer back onto the stack. If the stack for example looks like this: [2, 3, 4], and the machine executes the instruction TIMES, the stack looks like this afterwards: [6, 4]
IFZERO n: This instruction removes the topmost integer from the stack, and checks if it is equal to 0. If that is the case, it jumps to the nth instruction (start counting at 0). If not, the machine continues as usual with the next instruction. See example below.
DONE: Finally, the DONE instruction prints out the integer on top of the stack, and terminates the program regardless of the following instructions.
Computation starts with the first instruction. Initially, the stack is empty and the register contains the number 0.
Input Format
14
PUSH 5
STORE
LOAD
LOAD
PUSH -1
PLUS
STORE
LOAD
IFZERO 13
LOAD
TIMES
PUSH 0
IFZERO 3
DONE
"""
n = int(input())
lis = []
reg = 0
commands = []

for _ in range(n):
    commands.append(input().split())
i = 0
while i < n:
    l = commands[i]
    if l[0].upper() == "PUSH":
        lis.insert(0, int(l[1]))
        i += 1
    elif l[0].upper() == "STORE":
        if lis:
            reg = lis.pop(0)
        i += 1
    elif l[0].upper()== "LOAD":
        lis.insert(0, reg)
        i += 1
    elif l[0].upper() == "PLUS":
        if len(lis) >= 2:
            a = lis.pop(0)
            b = lis.pop(0)
            lis.insert(0, a + b)
        i += 1
    elif l[0].upper() == "TIMES":
        if len(lis) >= 2:
            a = lis.pop(0)
            b = lis.pop(0)
            lis.insert(0, a * b)
        i += 1
    elif l[0].upper() =="IFZERO":
        if lis:
            val = lis.pop(0)  
            if val == 0:
                k = int(l[1])
                if 0 <=k < n:
                    i = k
                else:
                    break 
            else:
                i += 1
        else:
            i += 1
    elif l[0].upper() == "DONE":
        if lis:
            print(lis[0])
        break


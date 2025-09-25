"""Takes a number n.
Checks if the sum of digits of n is divisible by 4.
If yes → return n.
If not → add the smallest possible number to n such that the new number’s digit sum is divisible by 4."""

def digit_sum(n):
    return sum(int(d) for d in str(n))

n = 14

while digit_sum(n)%4 != 0:
    n += 1

print(n)

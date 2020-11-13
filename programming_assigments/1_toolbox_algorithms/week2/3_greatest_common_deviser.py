# Uses python3
import sys
import numpy as np

#def gcd_naive(a, b):
#    current_gcd = 1
#    for d in range(2, min(a, b) + 1):
#        if a % d == 0 and b % d == 0:
#            if d > current_gcd:
#                current_gcd = d
#
#    return current_gcd
#
#gcd_naive(12, 8)



def gcd_naive(a, b):
    while (a > 0) & (b > 0):
        b, a = np.sort([a, b])
        a = a - np.floor(a / b) * b
    return int(b)



#gcd_naive(357, 234)
#gcd_naive(17*12, 19*12)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))

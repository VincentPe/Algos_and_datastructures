# Uses python3
import sys
import numpy as np

#def lcm_naive(a, b):
#    for l in range(1, a*b + 1):
#        if l % a == 0 and l % b == 0:
#            return l
#
#    return a*b


def gcd_naive(a, b):
    while (a > 0) & (b > 0):
        b, a = np.sort([a, b])
        a = a - np.floor(a / b) * b
    return int(b)

def lcm_naive(a, b):
    return int(np.abs(a * b) / gcd_naive(a, b))

#lcm_naive(357, 234)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))


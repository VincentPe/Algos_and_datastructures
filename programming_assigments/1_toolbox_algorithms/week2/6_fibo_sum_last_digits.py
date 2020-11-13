# Uses python3
import sys
import numpy as np

# Step 1 remainder after 60 fibos summed
# cumsum n modulo 60 add remainder
# take modulo 10



#def fibonacci_sum_naive(n):
#    if n <= 1:
#        return n
#
#    previous = 0
#    current  = 1
#    sum      = 1
#
#    for _ in range(n - 1):
#        previous, current = current, previous + current
#        sum += current
#
#    return sum % 10


def fibonacci_sum_modulo10(n):
    
    if n > 60:
        n = n % 60
        
    if (n <= 1):
        return n
    
    fibos = [0, 1]
    for i in range(2, n +1):
        fibos.append(fibos[-1] + fibos[-2])
        #fibos = fibos[-2:]
        
    return np.sum(fibos) % 10
    
    
#for n in range(60, 71):
#    print(fibonacci_sum_naive(n) == fibonacci_sum_modulo10(n))



if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_modulo10(n))

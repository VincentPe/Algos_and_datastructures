# Uses python3
from sys import stdin
import numpy as np

#def fibonacci_sum_squares_naive(n):
#    if n <= 1:
#        return n
#
#    previous = 0
#    current  = 1
#    sum      = 1
#
#    for _ in range(n - 1):
#        previous, current = current, previous + current
#        sum += current * current
#
#    return sum % 10


def calc_fib(n):
    if (n <= 1):
        return n
    
    fibos = [0, 1]
    for i in range(2, n +1):
        fibos.append(fibos[-1] + fibos[-2])

    return fibos[-1]


def fibo_cumsum_squared(n):
    if n > 60:
        n = n % 60
        
    if (n <= 1):
        return n
    
    fibos_sq_sum = 1
    for i in range(2, n +1):
        fibos_sq_sum += calc_fib(i)**2

    return fibos_sq_sum % 10



#for n in range(200): 
#    if fibonacci_sum_squares_naive(n) != fibo_cumsum_squared(n):
#        print(n)
    


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibo_cumsum_squared(n))

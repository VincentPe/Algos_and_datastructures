# Uses python3
import sys
import numpy as np

#def fibonacci_partial_sum_naive(from_, to):
#    sum = 0
#
#    current = 0
#    next  = 1
#
#    for i in range(to + 1):
#        if i >= from_:
#            sum += current
#
#        current, next = next, current + next
#
#    return sum % 10


def calc_fib(n):
    if (n <= 1):
        return n
    
    fibos = [0, 1]
    for i in range(2, n +1):
        fibos.append(fibos[-1] + fibos[-2])

    return fibos[-1]


def fibo_partial_sum(from_, to):
    
    if from_ > 60:
        from_ = from_ % 60
    if to > 60:
        to = to % 60
    if from_ > to:
        to += 60
    
    fibos = []
    for i in range(from_, to +1):
        fibos.append(calc_fib(i))
    return np.sum(fibos) % 10


#for i in range(60, 65):
#    for j in range(172, 178):
#        print(fibonacci_partial_sum_naive(i, j) == fibo_partial_sum(i, j))
    






if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibo_partial_sum(from_, to))
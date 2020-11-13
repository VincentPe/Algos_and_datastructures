# Uses python3
#import sys
import datetime

#def get_fibonacci_last_digit_naive(n):
#    if n <= 1:
#        return n
#
#    previous = 0
#    current  = 1
#
#    for _ in range(n - 1):
#        previous, current = current, previous + current
#
#    return current % 10
#
#for i in range(11):
#    print(get_fibonacci_last_digit_naive(i))
    
    
#def get_fibonacci_last_digit_naive(n):
#    if (n <= 1):
#        return n
#    
#    fibos = [0, 1]
#    for i in range(2, n +1):
#        fibos.append(fibos[-1] + fibos[-2])
#        fibos = fibos[-2:]
#
#    return fibos[-1] % 10

def get_fibonacci_last_digit_naive(n):
    
    if n > 60:
        n = n % 60
        
    if (n <= 1):
        return n
    
    fibos = [0, 1]
    for i in range(2, n +1):
        fibos.append(fibos[-1] + fibos[-2])
        fibos = fibos[-2:]

    return fibos[-1] % 10




#for i in [39, 99, 159, 219, 279]:
#    print(get_fibonacci_last_digit_naive(i))
    
    
    
#start = datetime.datetime.now()
#print(get_fibonacci_last_digit_naive(999999))
#print(datetime.datetime.now() - start)


if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))

# Uses python3
import sys

#def get_fibonacci_huge_naive(n, m):
#    if n <= 1:
#        return n
#
#    previous = 0
#    current  = 1
#
#    for _ in range(n - 1):
#        previous, current = current, previous + current
#
#    return current % m
#
#get_fibonacci_huge_naive(6, 3)


def calc_fib(n):
    if (n <= 1):
        return n
    
    fibos = [0, 1]
    for i in range(2, n +1):
        fibos.append(fibos[-1] + fibos[-2])

    return fibos[-1]


def get_pisano_length(m):
    fibo_nr = 3
    fibo_seq = [0, 1, 1]
    modulo_seq = [fibo_seq[i] % m for i in range(3)]
    while ((modulo_seq[-1] == 1) & (modulo_seq[-2] == 0)) == False:
        fibo_seq.append(calc_fib(fibo_nr))
        fibo_nr += 1
        modulo_seq.append(fibo_seq[-1] % m)
    return len(modulo_seq) -2

#get_pisano_length(100, 6)

def get_fibonacci_modulo_huge(n, m):
    return calc_fib(n % get_pisano_length(m)) % m


#get_fibonacci_modulo_huge(2019, 5)
#get_fibonacci_modulo_huge(1548276540, 235)

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_modulo_huge(n, m))

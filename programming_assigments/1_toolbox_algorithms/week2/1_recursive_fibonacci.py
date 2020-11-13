# Uses python3
import datetime


#def calc_fib(n):
#    if (n <= 1):
#        return n
#
#    return calc_fib(n - 1) + calc_fib(n - 2)
#
#for i in range(11):
#    print(calc_fib(i))
#
#
#for i in range(30, 41):
#    start = datetime.datetime.now()
#    print(calc_fib(i))
#    print(datetime.datetime.now() - start)



def calc_fib(n):
    if (n <= 1):
        return n
    
    fibos = [0, 1]
    for i in range(2, n +1):
        fibos.append(fibos[-1] + fibos[-2])

    return fibos[-1]

#for i in range(11):
#    print(calc_fib(i))
#
#
#for i in range(30, 41):
#    start = datetime.datetime.now()
#    print(calc_fib(i))
#    print(datetime.datetime.now() - start)



n = int(input())
print(calc_fib(n))

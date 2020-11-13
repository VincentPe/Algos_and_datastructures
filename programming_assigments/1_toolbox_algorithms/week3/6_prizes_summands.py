# Uses python3
import sys
import numpy as np

def optimal_summands(n):
    summands = []
    counter = 0
    while n > counter:
        counter += 1
        n = n - counter
        if n > counter:
            summands.append(counter)
        else:
            summands.append(counter + n)

    return summands


#optimal_summands(2)




if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

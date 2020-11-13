#Uses python3

import sys
import numpy as np

# n = number of ads to place
# a = sequence of profit per click for each ad
# b = secuence of number of clicks for that slot

# Output is maximum obtainable value

def max_dot_product(a, b):
    dotpr = 0
    for i in range(len(a)):
        pos = max(a) * max(b)
        neg = min(a) * min(b)
        if neg < pos:
            dotpr += pos
            a = np.delete(a, np.argmax(a))
            b = np.delete(b, np.argmax(b))
        else:
            dotpr += neg
            a = np.delete(a, np.argmin(a))
            b = np.delete(b, np.argmin(b))
    return dotpr



#n = 2
#a = [2,3,4]
#b = [3,4,5]
#
#
#max_dot_product(a, b)






if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
    
    

    

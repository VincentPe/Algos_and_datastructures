#Uses python3
import sys
import math
import queue


############################################
## What happens before calling the function
#data = [4, 0, 0, 0, 1, 1, 0, 1, 1]
#data = [5, 0, 0, 0, 2, 1, 1, 3, 0, 3, 2]
#n = data[0]
#x = data[1::2]
#y = data[2::2]
############################################

def euclidian_distance(x1, x2, y1, y2):
    x_diff = x1 - x2
    y_diff = y1 - y2
    return math.sqrt((x_diff**2 + y_diff**2))


def minimum_distance(x, y, n):
    
    result = 0.
    used = {0}
    unused = {i for i in range(1, n)}
    
    Q = queue.PriorityQueue()
    
    for i in unused:
        Q.put((euclidian_distance(x[0], x[i], y[0], y[i]), i))
        
    while len(unused) > 0:
        val, idx = Q.get()
        if idx in unused:
            result += val
            used.add(idx)
            unused.remove(idx)
            
            for i in unused:
                Q.put((euclidian_distance(x[idx], x[i], y[idx], y[i]), i))
    
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y, n)))

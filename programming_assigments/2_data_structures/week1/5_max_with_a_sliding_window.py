# python3

from collections import deque

def max_sliding_window(sequence, m):
    
    maximums = []
    Q = deque(maxlen=m)
    
    Q.append(0)
    for i in range(len(sequence)):
        if (i - m) == Q[0]:
            _ = Q.popleft()
        while True:
            if len(Q) == 0:
                Q.append(i)
                break
            elif sequence[i] > sequence[Q[0]]:
                Q.clear() 
                Q.append(i)
                break
            elif sequence[i] >= sequence[Q[-1]]:
                 _ = Q.pop()
            else:
                Q.append(i)
                break
        if i >= (m-1):
            maximums.append(sequence[Q[0]])

    return maximums

## Example
#n = 8
#sequence = [2, 7, 3, 1, 5, 2, 6, 2]
#m = 4
#
#Output = [7, 7, 5, 6, 6]
#max_sliding_window(sequence, m) == Output
#
## Online example
#sequence = [1, 2, 3, 1, 4, 5, 2, 3, 6]
#m = 3
#
#Output = [3, 3, 4, 5, 5, 5, 6]
#max_sliding_window(sequence, m) == Output




if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))


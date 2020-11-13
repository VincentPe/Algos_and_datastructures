# Uses python3
import sys
import numpy as np

def optimal_weight(W, w):

    matrix = np.zeros([len(w)+1, W+1])
    
    for i in range(1, len(w)+1):
        for j in range(1, W+1):
            if (w[i-1] > j):
                matrix[i,j] = matrix[i-1,j]
            else:
                matrix[i,j] = max(matrix[i-1,j-w[i-1]]+w[i-1], matrix[i-1,j])
    return int(matrix[i,j])



if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

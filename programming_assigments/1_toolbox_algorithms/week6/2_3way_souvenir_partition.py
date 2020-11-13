# Uses python3
import sys
import numpy as np


def fair_3way(A):
    if (sum(A) % 3 != 0) | (len(A) < 3):
        return 0
    else:
        if solution_varible(A, 3, 1) & solution_varible(A, 3, 2):
            return 1
        else:
            return 0

def solution_varible(values, devider, multiplier):
    
    total = sum(values)  
 
    fraction = total // devider * multiplier
    table = np.zeros([fraction + 1, len(values) + 1], dtype=int)
        
    for i in range(1, fraction + 1):  
        for j in range(1, len(values) + 1):
            
            if values[j-1] == i: 
                table[i][j] = True
            elif table[i][j-1]:
                table[i][j] = True
            elif (i-values[j-1] > 0) & (table[i-values[j-1]][j-1]):
                table[i][j] = True
            else:
                pass 
                
    return table[-1][-1]


#A = [17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]
#fair_3way(A)
#
#A = [3, 3, 3, 3]
#fair_3way(A)
#
#A = [1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]
#fair_3way(A)
#    
#A = [4, 1, 3, 2]
#fair_3way(A)



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(fair_3way(A))


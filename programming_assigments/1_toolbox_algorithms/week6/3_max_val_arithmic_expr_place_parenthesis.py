import numpy as np

def get_maximum_value(formula):
    
    digits = formula[::2]
    ops = formula[1:][::2]
    
    n = len(digits)
    m = np.zeros([n+1, n+1], dtype=int)
    M = np.zeros([n+1, n+1], dtype=int)
    
    for i in range(1, n+1):
        m[i,i] = digits[i-1]
        M[i,i] = digits[i-1]
        
    for s in range(1, n+1):
        for i in range(1, n-s+1):
            j = i+s
            m[i,j], M[i,j] = minandmax(i, j, m, M, ops)
            
    return M[1, n]

def minandmax(i, j, m, M, ops):
    
    min_ = float('inf')
    max_ = float('-inf')
    
    for k in range(i, j):
        a = evalt(M[i, k], M[k+1, j], ops[k-1])
        b = evalt(M[i, k], m[k+1, j], ops[k-1])
        c = evalt(m[i, k], M[k+1, j], ops[k-1])
        d = evalt(m[i, k], m[k+1, j], ops[k-1])
        
        min_ = min([min_, a, b, c, d])
        max_ = max([max_, a, b, c, d])
    
    return min_, max_

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


#formula = '5-8+7*4-8+9'
#get_maximum_value(formula)





if __name__ == "__main__":
    print(get_maximum_value(input()))

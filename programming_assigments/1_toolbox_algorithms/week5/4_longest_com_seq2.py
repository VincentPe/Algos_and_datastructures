import sys
import numpy as np
import random


def naive_lcs2(a, b):
    options_a = []
    options_a.append([])
    for j in range(len(a)):
        for i in options_a:
            if len(i) == 0:
                options_a.append([a[j]])
            else:
                if a[j] > i[-1]:
                    options_a.append(i + [a[j]])
                    
    options_b = []
    options_b.append([])
    for j in range(len(b)):
        for i in options_b:
            if len(i) == 0:
                options_b.append([b[j]])
            else:
                if b[j] > i[-1]:
                    options_b.append(i + [b[j]])
                                
    max_len = max([len(x) for x in options_a if x in options_b])
    
    return max_len


def LCS2(s1, s2, n1, n2):
    """ Finds the length of the longest common subsequence of two strings
    (str, str, int, int) -> (int, 2D-array) """

    # Initializing the matrix
    Matrix = np.zeros((n1+1 , n2+1))

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                Matrix[i][j] = Matrix[i-1][j-1] + 1
            if s1[i-1] != s2[j-1]:
                Matrix[i][j] = max(Matrix[i][j-1], Matrix[i-1][j])
    
    return int(Matrix[n1][n2]) #, Matrix



def lcs2(a, b, seq):
    if (len(a) == 0) | (len(b) == 0):
        return seq

#    if len(seq) == 0:
#        last_seq = -10**10
#    else:
#        last_seq = seq[-1]

    if (a[0] not in b): # | (a[0] <= last_seq):
        no_seq = lcs2(a[1:], b, seq)
    else:
        yes_seq = lcs2(a[1:], b[b.index(a[0]) + 1:], seq + [a[0]])
        no_seq = lcs2(a[1:], b, seq)
    if 'yes_seq' in locals():
        if len(no_seq) < len(yes_seq):
            return yes_seq
        else:
            return no_seq
    else:
        return no_seq
    



## Example 1
#a = [2, 7, 5]
#b = [2, 5]
#seq = []
#test = lcs2(a, b, seq)
#print(test)
#print(len(test))
#len(test) == naive_lcs2(a, b)
#
## Example 2
#a = [1]
#b = [4]
#seq = []
#test = lcs2(a, b, seq)
#print(test)
#print(len(test))
#len(test) == naive_lcs2(a, b)
#
#
## Example 3
#a = [2, 7, 5, 3]
#b = [5, 2, 8, 7]
#seq = []
#test = lcs2(a, b, seq)
#print(test)
#print(len(test))
#len(test) == naive_lcs2(a, b)
#
## Made up example
#a = [2, 7, 5, 3, 8, 9]
#b = [1, 2, 6, 3, 9, 8]
#seq = []
#test = lcs2(a, b, seq)
#print(test)
#print(len(test))
#len(test) == naive_lcs2(a, b)
#
#
## Stress testing
#test_completed = 0
#check = True
#while check == True:
#    a = list(np.random.randint(-10, 10, np.random.randint(1, 10)))
#    b = list(np.random.randint(-10, 10, np.random.randint(1, 10)))
#    if  (LCS2(a, b, len(a), len(b)) == len(lcs2(a, b, []))):  #(naive_lcs2(a, b) == len(lcs2(a, b, []))) &
#        test_completed += 1
#    else:
#        check = False
#        print(a, b)
#    if (test_completed > 0) & (test_completed % 100 == 0):
#        print(str(test_completed) + ' tests completed')
#    if test_completed == 1000:
#        break


## Speed test ....


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(LCS2(a, b, n, m))
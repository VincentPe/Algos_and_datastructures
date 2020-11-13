#Uses python3

import sys
import itertools
import random
import numpy as np


def naive_largest_number(a):
    options = []
    for i in range(len(list(itertools.permutations(a)))):
        options.append(int(''.join(list(itertools.permutations(a))[i])))
    return str(max(options))


def largest_number(a):
    a = np.array(a)
    res = ''
    while len(a) > 0:
        best_nr = '0'
        for i in a:
            if int(best_nr + i) <= int(i + best_nr):
                best_nr = i
        for i in a[a == best_nr]:
            res = res + best_nr
        a = a[a != best_nr]
    return res

#
#a = ['9', '4', '6', '1', '9', '0']
#largest_number(a)
#
#
## Simple tests
#a = ['9', '4', '6', '1', '9', '0']
#print(naive_largest_number(a) == largest_number(a))
#
#a = ['23', '39', '42', '46', '441', '4', '44']
#print(naive_largest_number(a) == largest_number(a))
#
#a = ['21', '1', '3', '2']
#print(naive_largest_number(a) == largest_number(a))





# Random stress tests
#test_completed = 0
#check = True
#while check == True:
#    a = list(map(str, random.sample(range(1, 100), random.randint(1, 5))))
#    if naive_largest_number(a) == largest_number(a):
#        test_completed += 1
#    else:
#        check = False
#        print(a)
#    if (test_completed > 0) & (test_completed % 100 == 0):
#        print(str(test_completed) + ' tests completed')
#    if test_completed == 1000:
#        break
        

    



if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    

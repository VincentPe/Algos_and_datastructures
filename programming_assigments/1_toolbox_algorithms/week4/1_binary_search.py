# Uses python3
import sys
#import random
#import numpy as np

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


def binary_search(a, x):
    left, right = 0, len(a)
    mid = int((left + right)/2)
    while left != right:
        mid = int((left + right)/2)
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            if left < mid:
                left = mid
            else:
                left = mid+1
        elif x < a[mid]:
            right = mid
    return -1


# sample test
#a = [1, 5, 8, 12, 13]
#for x in [8, 1, 23, 1, 11]:
#    print(binary_search(a, x))
    
## Random stress tests
#test_completed = 0
#check = True
#while check == True:
#    a = np.sort(np.unique(np.array(random.sample(range(1, 100), random.randint(1, 30)))))
#    x = random.randint(1, 100)
#    if linear_search(a, x) == binary_search(a, x):
#        test_completed += 1
#    else:
#        check = False
#        print(a, x)
#    if (test_completed > 0) & (test_completed % 100 == 0):
#        print(str(test_completed) + ' tests completed')
#    if test_completed == 1000:
#        break



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')

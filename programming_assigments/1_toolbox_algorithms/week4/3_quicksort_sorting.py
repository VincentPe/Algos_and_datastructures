# Uses python3
import sys
import random


def partition2(a, l, r):
    """
    for every number between interval:
        if nr is <= left: put number straight right of number
    finally replace first nr with number of updates, so 
    inbetween the numbers that were lower and higher than it
    return j; the count of numbers higher <= x to the right of l
    This determines the left and right to sort in the recursive call
    """
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def partition3(a, l, r):
    """
    
    """
    x = a[l]
    j = l # <= counter
    s = 0 # same indexes
    for i in range(l + 1, r + 1):
        if a[i] == x:
            j += 1
            s += 1
            a[i], a[j] = a[j], a[i]
        elif a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
            a[j-s], a[j] = a[j], a[j-s]
            
    a[l], a[j-s] = a[j-s], a[l]
    return s, j


def randomized_quick_sort(a, l, r):
    """
    a is sorted recursively and does not stay inside function
    """
    if l >= r:
        return #Like break in while loop. Stops function
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l] #Randomly select one item and put up front
    #use partition3
    s, m = partition3(a, l, r)
    # Now sort to the right and left recursively
    randomized_quick_sort(a, l, m - s - 1)    
    randomized_quick_sort(a, m + 1, r)
    
    
#a = [ 55,  13,  25,   8,  25,  55,  12,  25,   6,  41,  35,  56,  80,
#        61,  80,  78,  99,  88, 55,  81,  11,  44,  85,  55,  21,  60,
#        29,  71,  84,   55,  95,  89,  23,  18,  70,  39,  78,  89,  55,
#        17]
#n = len(a) 
#l = 0
#r = n-1
#
#randomized_quick_sort(a, l, r)
    
    
#n = 10
#a = [2, 3, 2, 3, 2, 3, 4, 2, 3, 2]
#randomized_quick_sort(a, 0, n - 1)
#
#n = 12
#a =[1, 2, 3, 9, 2, 2, 4, 8, 0, 10, 9, 2]
#randomized_quick_sort(a, 0, n - 1)
    
#n = 10
#a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#randomized_quick_sort(a, 0, n - 1)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')


# Uses python3
import sys
#import numpy as np
#import random
#import datetime

#def get_naive_inversions(a):
#    # Self made not provided
#    number_of_inversions = 0
#    new_arr = []
#    while len(a) > 0:
#        idx = np.argmin(a)
#        number_of_inversions += idx
#        new_arr.append(a[idx])
#        del a[idx]
#    return number_of_inversions
    

# Recursively split the sequence in two halfs and sort (arrays of 1 or 2)
# Merge the resulting arrays into one larger arrayby comparing the first element of each array
# Keep track of the number of changes in number_of_inversions

def get_number_of_inversions(a, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        #print('right - left <= 1. left:{}, right:{}, a[left:right]:{}'.format(left, right, a[left:right]))
        #print('number of inv:{}'.format(number_of_inversions))
        return number_of_inversions
    ave = (left + right) // 2
    #print('run first recursive')
    number_of_inversions += get_number_of_inversions(a, left, ave)
    #print('run second recursive')
    number_of_inversions += get_number_of_inversions(a, ave, right)
    
    new_arr = []
    left_arr = a[left:ave]
    right_arr = a[ave:right]
    #print('left_arr:{}. right_arr:{}'.format(left_arr, right_arr))
    
    # mergesort left:right
    while (len(left_arr) > 0) | (len(right_arr) > 0):
        if len(left_arr) == 0:
            for i in range(len(right_arr)):
                new_arr.append(right_arr[i])
            break
        elif len(right_arr) == 0:
            for i in range(len(left_arr)):
                new_arr.append(left_arr[i])
            break
        elif left_arr[0] <= right_arr[0]:
            new_arr.append(left_arr[0])
            left_arr = left_arr[1:]
        else:
             new_arr.append(right_arr[0])
             number_of_inversions += len(left_arr)
             right_arr = right_arr[1:]
    a[left:right] = new_arr
    
    #print('first complete. return num_inv:{} and new_arr:{}'.format(number_of_inversions, new_arr))
    return number_of_inversions



# Provided test. Answer 2    
#a = [2, 3, 9, 2, 9]
#left = 0
#right = len(a)
#
#get_number_of_inversions(a, left, right)
    
# Provided test. Answer 15
#a = [9, 8, 7, 3, 2, 1]
#left = 0
#right = len(a)
#
#get_number_of_inversions(a, left, right)
    

## Random tests
#test_completed = 0
#check = True
#while check == True:
#    a = list(np.array(random.sample(range(1, 100), random.randint(1, 30))))
#    b = a.copy()
#    c = a.copy()
#    if get_naive_inversions(a) == get_number_of_inversions(b, 0, len(b)):
#        test_completed += 1
#    else:
#        check = False
#        print(c)
#    if (test_completed > 0) & (test_completed % 100 == 0):
#        print(str(test_completed) + ' tests completed')
#    if test_completed == 1000:
#        break
#    
## Speed test
#tests_to_run = 1000
#testlist = []
#testlist2 = []
#for i in range(tests_to_run):
#    test = list(np.array(random.sample(range(1, 1000), random.randint(1, 300))))
#    testlist.append(test)
#    testlist2.append(test.copy())
#
#start = datetime.datetime.now()
#for i in testlist:
#    _ = get_naive_inversions(i)
#print('Finished within {}'.format(datetime.datetime.now() - start))
#
#start = datetime.datetime.now()
#for i in testlist2:
#    _ = get_number_of_inversions(i, 0, len(i))
#print('Finished within {}'.format(datetime.datetime.now() - start))

    


    
#new_arr = []
#left_arr = [6, 7, 8]
#right_arr = [1, 2, 3]
#left=0
#right=6
#
#new_arr = []
#left_arr = [1, 3, 5]
#right_arr = [2, 4, 6]
#left=0
#right=6
#
#
#number_of_inversions = 0
#while (len(left_arr) > 0) | (len(right_arr) > 0):
#    if len(left_arr) == 0:
#        for i in range(len(right_arr)):
#            new_arr.append(right_arr[i])
#        break
#    elif len(right_arr) == 0:
#        for i in range(len(left_arr)):
#            new_arr.append(left_arr[i])
#        break
#    elif left_arr[0] <= right_arr[0]:
#        new_arr.append(left_arr[0])
#        left_arr = left_arr[1:]
#    else:
#         new_arr.append(right_arr[0])
#         number_of_inversions += len(left_arr)
#         right_arr = right_arr[1:]
#a[left:right] = new_arr





if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, 0, len(a)))

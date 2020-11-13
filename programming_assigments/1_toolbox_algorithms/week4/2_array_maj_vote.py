# Uses python3
import sys

def get_majority_element(a, left, right):
    
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    
    left_m = get_majority_element(a, left, (left + right - 1)//2 + 1)
    right_m = get_majority_element(a, (left + right - 1)//2 + 1, right)
    left_count = 0
    for i in range(left, right):
        if a[i] == left_m:
            left_count += 1
    if left_count > (right-left)//2:
        return left_m

    right_count = 0
    for i in range(left, right):
        if a[i] == right_m:
            right_count += 1
    if right_count > (right-left)//2:
        return right_m

    return -1


#a = [2, 3, 9, 2, 2]
#left = 0
#right = len(a)
#get_majority_element(a, left, right)
#
#a = [2, 0, 2, 0, 2, 0, 2, 2]
#left = 0
#right = len(a)
#get_majority_element(a, left, right)
#
#
#a = [1, 2, 3, 4, 5, 6, 7, 8]
#left = 0
#right = len(a)
#get_majority_element(a, left, right)



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

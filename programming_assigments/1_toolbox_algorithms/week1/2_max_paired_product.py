# python3
import numpy as np
import datetime

# Example to slow
#def max_pairwise_product(numbers):
#    n = len(numbers)
#    max_product = 0
#    for first in range(n):
#        for second in range(first + 1, n):
#            max_product = max(max_product,
#                numbers[first] * numbers[second])
#
#    return max_product

#
#start = datetime.datetime.now()
#for i in range(1000):
#    numbers = np.random.randint(0, 1000, 100)
#    max_pairwise_product(numbers)
#print(datetime.datetime.now() - start)


def max_pairwise_product(numbers):
    sort_nrs = np.flip(np.sort(numbers))
    return sort_nrs[0] * sort_nrs[1]

    
#start = datetime.datetime.now()
#for i in range(1000):
#    numbers = np.random.randint(0, 1000, 100)
#    max_pairwise_product(numbers)
#print(datetime.datetime.now() - start)




if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))





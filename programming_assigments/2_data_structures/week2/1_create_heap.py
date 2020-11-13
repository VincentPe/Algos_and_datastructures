# python3

import numpy as np

# Implement min heap (min at the top)

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    size = len(data)
    swaps = []
    
    for i in reversed(range(len(data)//2)):
        swaps, data = heapify(i, data, size, swaps)
        
    return swaps


def heapify(i, data, size, swaps):
    
    smallest = i
    left = 2*i+1
    right = 2*i+2
    
    if (left < size) and (data[left] < data[smallest]):
        smallest = left
        
    if (right < size) and (data[right] < data[smallest]):
        smallest = right
        
    # If largest is not root 
    if (smallest != i): 
        swap = data[i]
        data[i] = data[smallest]
        data[smallest] = swap
        
        swaps.append((i, smallest))
  
        # Recursively heapify the affected sub-tree 
        swaps, data = heapify(smallest, data, size, swaps)
        
    return swaps, data
    

#data = [5, 4, 3, 2, 1]
#build_heap(data)
#
#data = [1, 2, 3, 4, 5]
#build_heap(data)


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

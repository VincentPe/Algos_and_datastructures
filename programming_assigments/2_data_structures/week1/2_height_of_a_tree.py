# python3

import os
import queue
import numpy as np
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

# Original function (naive impl)
#def compute_height(self):
#    # Replace this code with a faster implementation
#    maxHeight = 0
#    for vertex in range(self.n):
#        height = 0
#        i = vertex
#        while i != -1:
#                height += 1
#                i = self.parent[i]
#        maxHeight = max(maxHeight, height);
#    return maxHeight;


#testcode
#n = 5
#parent = [4, -1, 4, 1, 1]
#keys = np.unique(parent)
#tree_dict = dict()
#for key in keys:
#    tree_dict[key] = []
#
#for node, parent in enumerate(parent):
#    tree_dict[parent].append(node)
#    
#L = queue.Queue(maxsize=n) 
#for x in tree_dict[-1]:
#    L.put(x) 
#
#maxHeight = 0
#while L.qsize() > 0:
#    for i in range(L.qsize()):
#        x = L.get()
#        if x in tree_dict:
#            for j in tree_dict[x]:
#                L.put(j) 
#    maxHeight += 1
#    
#L.queue


class TreeHeight():
    
    def __init__(self, n, parent):
        self.n = n
        self.parent = parent
        
    def create_dict(self):
        keys = np.unique(self.parent)
        self.tree_dict = dict()
        for key in keys:
            self.tree_dict[key] = []
        for node, parent in enumerate(self.parent):
            self.tree_dict[parent].append(node)

    def compute_height(self):
        self.L = queue.Queue(maxsize=self.n) 
        for x in self.tree_dict[-1]:
            self.L.put(x) 
        
        maxHeight = 0
        while self.L.qsize() > 0:
            for i in range(self.L.qsize()):
                x = self.L.get()
                if x in self.tree_dict:
                    for j in self.tree_dict[x]:
                        self.L.put(j) 
            maxHeight += 1
        return maxHeight
   
    
## run tests
#os.chdir('C:\\Users\\u02vpe\\OneDrive - TRANSAVIA AIRLINES C.V\\Documents\\Data Science training\\algos_and_structures_specialization\\' + 
#         '2_data_structures\\' + 'week1_basic_data_structures\\' + '2_tree_height\\tests')
#
#start = 1
#stop = int(os.listdir()[-2])
#
#for i in range(start, stop+1):
#
#    testfile_name = "{:02d}".format(i)
#    testresult_name = "{:02d}".format(i) + '.a'
#
#    f = open(testfile_name, "r")
#    n = int(f.readline())
#    parent = list(map(int, f.readline().split()))
#    
#    tree = TreeHeight(n, parent)
#    tree.create_dict()
#    dept = tree.compute_height()
#    
#    f = open(testresult_name, "r")
#    answer = int(f.readline())
#    
#    if dept == answer:
#        pass
#    else:
#        print('Answer {} is not the same as dept {} for tree: {}'.format(answer, dept, parent))
#        
#print('Completed running all tests')





def main():
    tree = TreeHeight(n=int(sys.stdin.readline()), 
                      parent=list(map(int, sys.stdin.readline().split())))
    tree.create_dict()
    print(tree.compute_height())

threading.Thread(target=main).start() 

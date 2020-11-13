# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 11:21:00 2020

@author: u02vpe

http://thisthread.blogspot.com/2018/02/2-partition-problem.html
"""

import numpy as np

values = [5, 1, 11, 5]
n = len(values)

  
def solution(values):
    
    total = sum(values)  
    if total % 2:
        return False
 
    half = total // 2
    table = np.zeros([half + 1, len(values) + 1], dtype=int)
        
    for i in range(1, half + 1):  
        
        # can we add the first j elements in the list together
        # to get a total value of i
        
        #print('Fill in the row to try to make {} with the elements we have in the list'.format(i))
        
        for j in range(1, len(values) + 1):
            
            if values[j-1] == i: 
                table[i][j] = True
                #print('Yes, because i is equal to the j-th element in the list (both:{})'.format(i))
            elif table[i][j-1]:
                table[i][j] = True
                #print('Yes, because we could already make it with the shorter list'.format(i))
            elif (i-values[j-1] > 0) & (table[i-values[j-1]][j-1]):
                table[i][j] = True
                #print('Yes, since we could make {} without this element {}'.format(i-values[j-1], i))
            else:
                #print('No, leave False. We can\'t make {} with the list {}'.format(i, values[:j]))
                pass 
                
    return table[-1][-1]
            
            
solution(values)


            
            
            
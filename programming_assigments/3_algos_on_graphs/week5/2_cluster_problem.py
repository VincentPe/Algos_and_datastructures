#Uses python3
import sys
import math

#import matplotlib.pyplot as plt
#import seaborn as sns


#############################################
## What happens before calling the function
#data = [12, 7, 6, 4, 3, 5, 1, 1, 7, 2, 7, 5, 7, 3, 3, 7, 8, 2, 8, 4, 4, 6, 7, 2, 6, 3]
#data = [8, 3, 1, 1, 2, 4, 6, 9, 8, 9, 9, 8, 9, 3, 11, 4, 12, 4]
#n = data[0]
#data = data[1:]
#x = data[0:2 * n:2]
#y = data[1:2 * n:2]
#data = data[2 * n:]
#k = data[0]
## sns.scatterplot(x, y)
#############################################

def distance(v1,v2,x,y):
    return math.sqrt((x[v1]-x[v2])**2 +  (y[v1]-y[v2])**2) 


def clustering(x, y, k):
    #create edge list
    edges = []
    for i in range(len(x)):
        for j in range(i,len(x)):
            if i != j:
                edges.append([i,j, distance(i,j,x,y)])
    
    #sort edges
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    # Create clusters (starting with each in their own cluster)   
    membership = range(n)
    
    #run Kruskal algorithm to join clusters closest to each other
    for i in sorted_edges:
        
        #make sure vertices are not already joined
        if membership[i[0]] != membership[i[1]]:
            
            #stop if number of partitions eqals desired number of clusters
            if len(set(membership)) == k:
                
                # The edge now first in the list is the minimum distance between any two clusters
                next_edge = i
                break
            
            #join groups
            membership = list(map(lambda x: membership[i[0]] if x == membership[i[1]] else x, membership))
            
    return next_edge[2]



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))

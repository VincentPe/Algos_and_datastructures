#Uses python3

import sys

#############################################################
## what happens before calling acyclic?
#data = [5, 7, 1, 2, 2, 3, 1, 3, 3, 4, 1, 4, 2, 5, 3, 5]
#data = [4, 4, 1, 2, 4, 1, 2, 3, 3, 1]
#n, m = data[0:2]
#data = data[2:]
#edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
#adj = [[] for _ in range(n)]
#for (a, b) in edges:
#    adj[a - 1].append(b - 1)
#############################################################
    
def discoverer(adj, start, discovered_nodes=[]):
        
    to_explore = adj[start]
    new_nodes = [i for i in to_explore if i not in discovered_nodes]
    
    #print('New nodes to discover for node {}: {}'.format(start, new_nodes))
    
    for i in new_nodes:
        discovered_nodes.append(i)
        #print('Node {} appended to discovered'.format(i))
        discovered_nodes = discoverer(adj, i, discovered_nodes)

    return discovered_nodes    

def acyclic(adj, n):
    
    found_cycle=0
    start=0
    while True and start < n:
        discovered_nodes = discoverer(adj, start, [])
        if start in discovered_nodes:
            #print('Found cycle, {} can be found from start'.format(start))
            found_cycle = 1
            break
        else:
            start+=1
    
    return found_cycle


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj, n))

#Uses python3

import sys

############################################################
## what happens before calling reach?
#data = [4,2,1,2,3,2]
#n, m = data[0:2] #𝑛 vertices and 𝑚 edges
#data = data[2:]
#edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
## Check which direct neighbors each edge has (adjacency list)
#adj = [[] for _ in range(n)]
#for (a, b) in edges:
#    adj[a - 1].append(b - 1)
#    adj[b - 1].append(a - 1)
############################################################
    
def discoverer(adj, start, discovered_nodes):
    
    discovered_nodes[start] = 1
        
    to_explore = adj[start]
    new_nodes = [i for i in to_explore if discovered_nodes[i] == 0]
    
    for i in new_nodes:
        discovered_nodes = discoverer(adj, i, discovered_nodes)

    return discovered_nodes


def number_of_components(adj, n):
    
    result = 0
    discovered_nodes = [0] * n
    
    while sum(discovered_nodes) < n:
        discovered_nodes = discoverer(adj, discovered_nodes.index(0), discovered_nodes)
        result += 1
    
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj, n))

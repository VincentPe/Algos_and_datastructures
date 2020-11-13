#Uses python3

import sys

############################################################
# # what happens before calling reach?
# data = [4,4,1,2,3,2,4,3,1,4,1,4]
# n, m = data[0:2] #𝑛 vertices and 𝑚 edges
# data = data[2:]
# edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
# x, y = data[2 * m:] # Last two numbers are check to be connected

# x, y = x - 1, y - 1 # zero indexing
# # Check which direct neighbors each edge has (adjacency list)
# adj = [[] for _ in range(n)]
# for (a, b) in edges:
#     adj[a - 1].append(b - 1)
#     adj[b - 1].append(a - 1)
############################################################

def discoverer(adj, start, discovered_nodes=[]):
    
    if start not in discovered_nodes:
        discovered_nodes.append(start)
    to_explore = adj[start]
    new_nodes = [i for i in to_explore if i not in discovered_nodes]
    
    for i in new_nodes:
        discovered_nodes = discoverer(adj, i, discovered_nodes)

    return discovered_nodes


def reach(adj, x, y):
    
    discovered_nodes = discoverer(adj, x)
    
    if y in discovered_nodes:
        return 1
    else:
        return 0



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))

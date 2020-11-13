#Uses python3

import sys
import queue

##############################################
## What happens before calling the function
#data = [4, 4, 1, 2, 4, 1, 2, 3, 3, 1]
#data = [5, 4, 5, 2, 4, 2, 3, 4, 1, 4]
#n, m = data[0:2]
#data = data[2:]
#edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
#adj = [[] for _ in range(n)]
#for (a, b) in edges:
#    adj[a - 1].append(b - 1)
#    adj[b - 1].append(a - 1)
##############################################

def bipartite(adj, n):
    
    if (len(adj) == 0) & (n == 1):
        return 0
    
    bip = 1
    visited = []
    color = len(adj) * [-1]
    Q = queue.Queue()
    
    while len(visited) < n:
        ci = color.index(-1)
        color[ci] = True
        Q.put(ci)
        visited.append(ci)
    
        while not Q.empty():
            u = Q.get()
            for v in adj[u]:
                if color[v] == -1:
                    Q.put(v)
                    color[v] = not color[u]
                    visited.append(v)
                elif color[v] == color[u]:
                    bip = 0
                    break
        if bip == 0:
            break
                
    return bip




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
    print(bipartite(adj, n))

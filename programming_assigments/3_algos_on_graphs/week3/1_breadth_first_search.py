#Uses python3

import sys
import queue

############################################
## What happens before calling the function
#data = [4, 4, 1, 2, 4, 1, 2, 3, 3, 1, 2, 4]
#n, m = data[0:2]
#data = data[2:]
#edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
#adj = [[] for _ in range(n)]
#for (a, b) in edges:
#    adj[a - 1].append(b - 1)
#    adj[b - 1].append(a - 1)
#s, t = data[2 * m] - 1, data[2 * m + 1] - 1
############################################


def distance(adj, s, t):
    
    inf = float('Inf')
    dist = len(adj) * [inf]
    dist[s] = 0
    Q = queue.Queue()
    Q.put(s)
    
    while Q.qsize() > 0:
        u = Q.get()
        for v in adj[u]:
            if dist[v] == inf:
                Q.put(v)
                dist[v] = dist[u] + 1
                
    if dist[t] == inf:
        return -1
    else:
        return dist[t]
    
    
    

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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))

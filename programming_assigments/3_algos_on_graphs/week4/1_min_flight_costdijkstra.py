#Uses python3

import sys
import queue

##############################################
## What happens before calling the function
#data = [4, 4, 1, 2, 1, 4, 1, 2, 2, 3, 2, 1, 3, 5, 1, 3]
#data = [5, 9, 1, 2, 4, 1, 3, 2, 2, 3, 2, 3, 2, 1, 2, 4, 2, 3, 5, 4, 5, 4, 1, 2, 5, 3, 3, 4, 4, 1, 5]
data = [10, 16, 6, 9, 10, 8, 9, 6, 5, 7, 10, 2, 7, 4, 5, 8, 5, 4, 7, 10, 4, 1, 2, 2, 6, 6, 6, 2, 8, 9, 6, 4, 6, 1, 7, 9, 7, 5, 6, 3, 1, 7, 4, 5, 10, 2, 1, 3, 8, 1, 10, 9]
n, m = data[0:2]
data = data[2:]

edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
adj = [[] for _ in range(n)]
cost = [[] for _ in range(n)]
for ((a, b), w) in edges:
    adj[a - 1].append(b - 1)
    cost[a - 1].append(w)
    
data = data[3 * m:]
s, t = data[0] - 1, data[1] - 1
##############################################

#    prev = [float('nan')] * len(adj)
#for idx, x in enumerate(dist):
#    print(str(x) + ': ' + str(idx))
#    Q.put((x, idx))
#prev[v] = u_idx


def distance(adj, cost, s, t):
    
    dist = [float('inf')] * len(adj)
    dist[s] = 0
    
    Q = queue.PriorityQueue()
    Q.put(s)
    
    while not Q.empty():
        u_idx = Q.get()
        
        for v_idx, v in enumerate(adj[u_idx]):
            if dist[v] > dist[u_idx] + cost[u_idx][v_idx]:
                dist[v] = dist[u_idx] + cost[u_idx][v_idx]
                Q.put(v)
    
    if dist[t] == float('inf'):
        return -1
    else:
        return dist[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))

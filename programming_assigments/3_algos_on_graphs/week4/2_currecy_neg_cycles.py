#Uses python3

import sys

##############################################
## What happens before calling the function
data = [4, 4, 1, 2, -5, 4, 1, 2, 2, 3, 2, 3, 1, 1]
n, m = data[0:2]
data = data[2:]
edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
data = data[3 * m:]
adj = [[] for _ in range(n)]
cost = [[] for _ in range(n)]
for ((a, b), w) in edges:
    adj[a - 1].append(b - 1)
    cost[a - 1].append(w)
##############################################


def negative_cycle(adj, cost):
    
    dist = [1000000] * len(adj)
    prev = [float('nan')] * len(adj)
    dist[0] = 0
    
    for i in range(len(adj) -1):
        for j in range(len(adj)):
            for idx_k, k in enumerate(adj[j]):
                if dist[k] > cost[j][idx_k] + dist[j]:
                    dist[k] = cost[j][idx_k] + dist[j]
                    prev[k] = j
    
    neg_cycle = 0
    
    for j in range(len(adj)):
        for idx_k, k in enumerate(adj[j]):
            if dist[k] > cost[j][idx_k] + dist[j]:
                dist[k] = cost[j][idx_k] + dist[j]
                prev[k] = j
                neg_cycle = 1
    
    return neg_cycle


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
    print(negative_cycle(adj, cost))

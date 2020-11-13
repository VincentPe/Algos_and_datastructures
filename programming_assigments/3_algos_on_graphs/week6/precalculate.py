import sys
import queue
import math
import itertools

import matplotlib.pyplot as plt
import seaborn as sns

# Settings
k_hops=2

###############################################################################
# Self made example:
data = [10, 13, # n, m
        0, 0, 1, 1, 1, 3, 2, 2, 3, 1, 2, 4, 4, 4, 5, 2, 6, 4, 6, 6, # x and y
        1, 2, 2, 2, 3, 2, 2, 4, 2, 2, 5, 3, 4, 6, 2, 4, 7, 6, 3, 7, 5, # u, v and l
        5, 8, 3, 7, 9, 2, 8, 9, 3, 9, 10, 3, 7, 10, 6, 6, 7, 2, # more u, v and l
        1, 1, 10] # q, s and t
# Before query starts
n, m = data[0], data[1]
data = data[2:]
x = data[:n*2][::2]
y = data[:n*2][1::2]
data = data[n*2:]
edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
data = data[m*3:]
adj = [[] for _ in range(n)]
R_adj = [[] for _ in range(n)]
cost = [[] for _ in range(n)]
R_cost = [[] for _ in range(n)]
for ((a, b), w) in edges:
    adj[a - 1].append(b - 1)
    R_adj[b - 1].append(a - 1)
    cost[a - 1].append(w)
    R_cost[b - 1].append(w)
q = data[0]
data = data[1:]
s, t = data[0] -1, data[1] -1
###############################################################################
## Plot nodes and edges
#sns.scatterplot(x, y)
#for (i, j), l in edges:
#    sns.lineplot([x[i-1], x[j-1]], [y[i-1], y[j-1]])
###############################################################################

def define_importances():
    shortcuts = [0] * n
    incoming = [len(x) for x in R_adj]
    outgoing = [len(x) for x in adj]
    edge_diff = [s - i - o for s, i, o in zip(shortcuts, incoming, outgoing)]
    contract_neighbors = [0] * n
    shortcut_cover = []
    for v in range(n):
        shortcut_cover.append(count_shortcut_cover(v))
    node_level = [0] * n
    # After contracting node v, for neighbors u of v do L(u) <- max(L(u), L(v) + 1)
    importances = [ed*0.25 + cn*0.25 + sc*0.25 + L*0.25 for ed, cn, sc, L in \
                   zip(edge_diff, contract_neighbors, shortcut_cover, node_level)]
    
    return importances

def count_shortcut_cover(v):
    counter = 0
    for u, w in list(itertools.product(R_adj[v], adj[v])):
        max_shortcut_length = cost[u][adj[u].index(v)] + cost[v][adj[v].index(w)]
        counter += check_withness_path(adj, cost, u, w, v, k_hops, max_shortcut_length)
    return counter

def check_withness_path(adj, cost, s, t, ignore_v, k_hops, max_shortcut_length):
    
    dist = [float('inf')] * len(adj)
    dist[s] = 0
    
    Q = queue.PriorityQueue()
    Q.put((s, 0))
    
    while not Q.empty():
        u_idx, hop = Q.get()
        
        if hop < k_hops:
        
            for v_idx, v in enumerate(adj[u_idx]):
                if v != ignore_v:
                    new_dist = dist[u_idx] + cost[u_idx][v_idx]
                    if (dist[v] > new_dist) & (new_dist < max_shortcut_length):
                        dist[v] = dist[u_idx] + cost[u_idx][v_idx]
                        
                        Q.put((v, hop+1))
                        
                        if v == t:
                            print('Found shortcut for s:{} and t:{} bypassing v:{}'.format(s, t, ignore_v))
    
    if dist[t] == float('inf'):
        return 0
    else:
        return 1





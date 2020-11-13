#Uses python3

import sys

sys.setrecursionlimit(200000)

#############################################################
# what happens before calling SCC?
data = [4, 4, 1, 2, 4, 1, 2, 3, 3, 1]
n, m = data[0:2]
data = data[2:]
edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
adj = [[] for _ in range(n)]
R_adj = [[] for _ in range(n)]
for (a, b) in edges:
    adj[a - 1].append(b - 1)
    R_adj[b - 1].append(a - 1)
#############################################################



def discoverer(adj, start, used, order=[]):
    
    if not used[start]:
        used[start] = 1
        for i in adj[start]:
            order, used = discoverer(adj, i, used, order)
        
        order.append(start)

    return order, used


def toposort(adj):
    
    used = [0] * len(adj)
    order = []
    
    for i in range(len(adj)):
        order, used = discoverer(adj, i, used, order)
    
    return order

def explorer(adj, start, used, discovered=[]):
    
    if (not used[start]) & (start not in discovered):
        used[start] = 1
        discovered.append(start)
        for i in adj[start]:
            used, discovered = explorer(adj, i, used, discovered)
            
    return used, discovered

def number_of_strongly_connected_components(adj, R_adj):
    
    result = 0
    used = [0] * len(adj)
    order = toposort(R_adj)
    
    while len(order) > 0:
        used, discovered = explorer(adj, order[-1], used, [])
        result += 1
        for i in discovered:
            order.remove(i)
    
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    R_adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        R_adj[b - 1].append(a - 1)
    print(number_of_strongly_connected_components(adj, R_adj))

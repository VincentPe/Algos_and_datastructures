#Uses python3

import sys


#############################################################
## what happens before calling acyclic?
#data = [5, 7, 2, 1, 3, 2, 3, 1, 4, 3, 4, 1, 5, 2, 5, 3]
#data = [5, 10, 4, 5,3, 1, 2, 1, 2, 3, 3, 4, 5, 1, 2, 5, 4, 1, 2, 4, 3, 5]
#n, m = data[0:2]
#data = data[2:]
#edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
#adj = [[] for _ in range(n)]
#for (a, b) in edges:
#    adj[a - 1].append(b - 1)
#############################################################
    
    
def discoverer(adj, start, used, order=[]):
    
    if not used[start]:
        for i in adj[start]:
            order = discoverer(adj, i, used, order)
        used[start] = 1
        order.append(start)

    return order


def toposort(adj):
    
    used = [0] * len(adj)
    order = []
    
    for i in range(len(adj)):
        order = discoverer(adj, i, used, order)
    
    return order



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in range(n):
        print(order.pop() + 1, end=' ')


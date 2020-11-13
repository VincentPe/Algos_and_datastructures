import sys
import queue

################################################################################
## What happens before calling the function
#data = [2, 1, 1, 2, 1, 4, 1, 1, 2, 2, 1, 2, 2, 1]
#data = [4, 4, 1, 2, 1, 4, 1, 2, 2, 3, 2, 1, 3, 5, 1, 1, 3]
#data = [5, 9, 1, 2, 4, 1, 3, 2, 2, 3, 2, 3, 2, 1, 2, 4, 2, 3, 5, 4, 5, 4, 1, 2, 5, 3, 3, 4, 4, 1, 1, 5]
#data = [3, 3, 1, 2, 7, 1, 3, 5, 2, 3, 2, 1, 3, 2]
#data = [10, 16, 6, 9, 10, 8, 9, 6, 5, 7, 10, 2, 7, 4, 5, 8, 5, 4, 7, 10, 4, 1, 2, 2, 6, 6, 6, 2, 8, 9, 6, 4, 6, 1, 7, 9, 7, 5, 6, 3, 1, 7, 4, 5, 10, 2, 1, 3, 8, 1, 1, 10, 9]
#
#n, m = data[0], data[1]
#data = data[2:]
#
#edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
#adj = [[] for _ in range(n)]
#R_adj = [[] for _ in range(n)]
#cost = [[] for _ in range(n)]
#R_cost = [[] for _ in range(n)]
#for ((a, b), w) in edges:
#    adj[a - 1].append(b - 1)
#    R_adj[b - 1].append(a - 1)
#    cost[a - 1].append(w)
#    R_cost[b - 1].append(w)
#    
#data = data[m*3:]
#q = data[0]
#data = data[1:]
################################################################################

#for u_idx, u in enumerate(R_adj[R_v]):
#    if R_dist[u] > R_dist[R_v] + R_cost[R_v][u_idx]:
#        R_dist[u] = R_dist[R_v] + R_cost[R_v][u_idx]
#        R_proc.append(u)
#        R_Q.put((R_dist[u], u))
#        print('added: {}, {}'.format(R_dist[u], u))
       

def Process(v, adj, dist, prev, proc, cost, Q, put=True):
    
    for u_idx, u in enumerate(adj[v]):
        if dist[u] == float('inf'):
            proc.append(u)
        if dist[u] > dist[v] + cost[v][u_idx]:
            dist[u] = dist[v] + cost[v][u_idx]
            #prev[u] = v
            if put:
                Q.put((dist[u], u))
                #print('added: {}, {}'.format(dist[u], u))
        
    return dist, prev, proc, Q


def ShortestPath(s, t, dist, prev, proc, R_dist, R_prev, R_proc):
    
    distance = float('inf')
#    u_best = None
#    path = []
    
#    print('Found shortest path')
    #print('processed both:')
    #print(proc)
    
    for u in proc:
        if dist[u] + R_dist[u] < distance:
            distance = dist[u] + R_dist[u]
#            u_best = u
    
#    last = u_best
#    while last != s:
#        path.append(last)
#        last = prev[last]
#    path = list(reversed(path))
#    
#    last = u_best
#    while last != t:
#        path.append(last)
#        last = R_prev[last]
    
    return distance #path


def BidirectionalDijkstra(s, t, adj, R_adj, cost, R_cost):
    
    dist, R_dist = [float('inf')] * len(adj), [float('inf')] * len(adj)
    dist[s], R_dist[t] = 0, 0    
    prev, R_prev = [None] * len(adj), [None] * len(adj)
    proc, R_proc = [s], [t] 
    proc_arr, R_proc_arr = [0] * len(adj), [0] * len(adj)
    proc_arr[s], R_proc_arr[t] = 1, 1
    Q, R_Q = queue.PriorityQueue(), queue.PriorityQueue()
    Q.put((0, s)); R_Q.put((0, t))
    
    while not Q.empty() and not R_Q.empty():
        _, v = Q.get()
        #print(_, v)
        
        if R_proc_arr[v] == 1:
            return ShortestPath(s, t, dist, prev, proc, R_dist, R_prev, R_proc)
        
        dist, prev, proc, Q = Process(v, adj, dist, prev, proc, cost, Q)
        proc_arr[v] = 1
        
            
        _, R_v = R_Q.get()
        #print(_, R_v)
        
        if proc_arr[R_v] == 1:              
            return ShortestPath(s, t, dist, prev, proc, R_dist, R_prev, R_proc)
        
        R_dist, R_prev, R_proc, R_Q = Process(R_v, R_adj, R_dist, R_prev, proc, R_cost, R_Q)
        R_proc_arr[R_v] = 1
        
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0], data[1]
    data = data[2:]
    
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    adj = [[] for _ in range(n)]
    R_adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    R_cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        R_adj[b - 1].append(a - 1)
        cost[a - 1].append(w)
        R_cost[b - 1].append(w)
    
    data = data[m*3:]
    q = data[0]
    data = data[1:]
    for i in range(len(data)//2):
        s, t = data[i*2] - 1, data[i*2+1] - 1
        print(BidirectionalDijkstra(s, t, adj, R_adj, cost, R_cost))
    